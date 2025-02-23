import sys

import importlib
import pandas as pd

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (accuracy_score, 
                             f1_score, 
                             precision_score, 
                             recall_score, 
                             roc_auc_score)

from src.model.predictor import HotelBookingModel

from src.core.logger import logging
from src.core.exception import HotelBookingException

from src.core.entities.config_entity import ModelTrainerConfig
from src.core.entities.artifact_entity import (DataPreprocessingArtifact,
                                               DataSplitArtifact,
                                               ModelTrainerArtifact)

from src.core.utils.data_utils import read_data 
from src.core.utils.yaml_utils import read_yaml
from src.core.utils.object_utils import save_object
from src.core.utils.json_utils import (read_json, write_json)
from src.core.utils.train_test_split_utils import (train_test_split_for_tuning,
                                                   separate_features_and_target)

from src.core.constants.common_constant import (TARGET_COLUMN,
                                                MODEL_PARAMS_FILE_PATH)




class ModelTrainer:
    """
    Class Name: ModelTrainer
    Description: Trains a model using neuro_mf and returns trained model object and classification metrics
    """
    def __init__(self, 
                 data_preprocessing_artifact: DataPreprocessingArtifact,
                 data_split_artifact: DataSplitArtifact,
                 model_trainer_config: ModelTrainerConfig):
        """
        :param data_ingestion_artifact: Output reference of data ingestion artifact stage
        :param data_preprocessing_config: Configuration for data preprocessing
        """
        try:
            logging.info("")
            logging.info("- - - Started Model Training Stage: - - -")
            logging.info("- "*50)

            self.data_preprocessing_artifact = data_preprocessing_artifact
            self.data_split_artifact = data_split_artifact
            self.model_trainer_config = model_trainer_config
            # Load the full model parameters from YAML
            self.model_config = read_yaml(MODEL_PARAMS_FILE_PATH)


        except Exception as e:
            logging.error(f"Error in ModelTrainer initialization: {str(e)}")
            raise HotelBookingException(f"Error during ModelTrainer initialization: {str(e)}", sys) from e
                


    def metrics_calculator(self, clf, X_test: pd.DataFrame, y_test: pd.Series, model_name: str) -> pd.DataFrame:
        '''
        This function calculates all desired performance metrics for a given model on test data.
        The metrics are calculated specifically for class 1.
        '''
        try:
            logging.info(f"Calculating performance metrics for model: {model_name}")
            y_pred = clf.predict(X_test)

            result = pd.DataFrame(data=[accuracy_score(y_test, y_pred),
                                         precision_score(y_test, y_pred, pos_label=1),
                                         recall_score(y_test, y_pred, pos_label=1),
                                         f1_score(y_test, y_pred, pos_label=1),
                                         roc_auc_score(y_test, clf.predict_proba(X_test)[:, 1])],
                                   index=['Accuracy', 'Precision (Class 1)', 'Recall (Class 1)', 'F1-score (Class 1)', 'AUC (Class 1)'],
                                   columns=[model_name])


            result = (result * 100).round(2).astype(str) + '%'
            logging.info(f"Metrics for {model_name}: {result.to_dict()}")

            return result

        except Exception as e:
            raise HotelBookingException(e, sys) from e



    def tune_hyperparameters(self, X_train: pd.DataFrame, y_train: pd.Series) -> dict:
        logging.info("Starting hyperparameter tuning...")
        try:

            # Use 30% of the dataset for hyperparameter tuning
            X_tune, y_tune = train_test_split_for_tuning(X_train, y_train, test_size=0.7)
            logging.info(f"Tuning dataset size: {X_tune.shape}, {y_tune.shape}")


            # Load model parameters
            models = self.model_config['model_selection']
            grid_search_params = self.model_config['grid_search']['params']
            logging.info("Model parameters and hyperparameter grids loaded successfully")


            # Dictionary to store best models after tuning
            best_models = {}
            best_params_dict = {}

            # Loop through each model and its parameters for tuning
            for model_name, model_info in models.items():
                logging.info(f"Tuning hyperparameters for model: {model_name}")

                print(f"Tuning hyperparameters for {model_name}...")
                model_class = getattr(importlib.import_module(model_info['module']), model_info['class'])
                model = model_class(**model_info['params'])
                params = model_info['search_param_grid']

                # Use GridSearchCV for tuning
                search = GridSearchCV(
                    model,
                    params,
                    **grid_search_params
                )
                logging.info(f"GridSearchCV initialized for {model_name} with parameters: {params}")

                # Fit the model using the subset of data
                search.fit(X_tune, y_tune)
                logging.info(f"Hyperparameter tuning completed for {model_name}")

                # Save the best model
                best_models[model_name] = search.best_estimator_
                best_params_dict[model_name] = search.best_params_

                # Print best parameters and best score
                print(f"Best parameters for {model_name}: {search.best_params_}")
                print(f"Best cross-validation score for {model_name}: {search.best_score_}\n")
                logging.info(f"Best parameters for {model_name}: {search.best_params_}")
                logging.info(f"Best cross-validation score for {model_name}: {search.best_score_}\n")

            logging.info("Hyperparameter tuning completed successfully")

            return best_models, best_params_dict

        except Exception as e:
            raise HotelBookingException(e, sys) from e



    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Starting model training process...")
        try:
            # Load training data
            train_df = read_data(self.data_split_artifact.train_data_file_path)
            logging.info(f"Loaded preprocessed training data from: {self.data_split_artifact.train_data_file_path}")
            logging.info(f"Training Data shape: {train_df.shape}")

            # Separate training data into X and y
            X_train, y_train = separate_features_and_target(train_df, TARGET_COLUMN)
            logging.info("Seperate Training data into X and y completed successfully")
            logging.info(f"X_train set size: {X_train.shape}, y_train set size: {y_train.shape}")


            # Load test data
            test_df = read_data(self.data_split_artifact.test_data_file_path)
            logging.info(f"Loaded preprocessed Test data from: {self.data_split_artifact.test_data_file_path}")
            logging.info(f"Test Data shape: {test_df.shape}")

            # Separate test data into X and y
            X_test, y_test = separate_features_and_target(test_df, TARGET_COLUMN)
            logging.info("Seperate Validaton data into X and y completed successfully")
            logging.info(f"X_test set size: {X_test.shape}, y_test set size: {y_test.shape}")


            # Check if best model parameters exists in best_model.json
            try:
                best_model_params = read_json(self.model_trainer_config.best_model_params_file_path)  # NEW: Try loading best_model.json
                logging.info(f"Loaded best model parameters from {self.model_trainer_config.best_model_params_file_path}: {best_model_params}")
            except Exception as e:
                logging.info(f"Best model parameters not found in {self.model_trainer_config.best_model_params_file_path}: {str(e)}")
                best_model_params = None
                
            
            if best_model_params:
                
                best_model_name = best_model_params["name"]
                best_params = best_model_params["params"]
                
                # Convert class_weight keys from strings to integers if present
                if "class_weight" in best_params:
                    best_params["class_weight"] = {int(k): v for k, v in best_params["class_weight"].items()}

                logging.info(f"Using pre-tuned best model: {best_model_name} with parameters: {best_params}")

                
                # Determine the model class based on best_model_name (extend logic as needed)
                if best_model_name.lower() == "rfc":
                    model_module = importlib.import_module("sklearn.ensemble")
                    model_class = getattr(model_module, "RandomForestClassifier")
                
                elif best_model_name.lower() == "dtc":
                    model_module = importlib.import_module("sklearn.tree")
                    model_class = getattr(model_module, "DecisionTreeClassifier")
                
                elif best_model_name.lower() == "gb":
                    model_module = importlib.import_module("sklearn.ensemble")
                    model_class = getattr(model_module, "GradientBoostingClassifier")
                
                elif best_model_name.lower() == "xgb":
                    model_module = importlib.import_module("xgboost")
                    model_class = getattr(model_module, "XGBClassifier")
                
                else:
                    raise HotelBookingException(f"Best model {best_model_name} not supported.", sys)

                
                best_model = model_class(**best_params)
                logging.info("Training model using fixed best model parameters...")
                best_model.fit(X_train, y_train)


                # Calculate metrics for the chosen model and convert it to dict format
                logging.info("Calculating final evaluation metrics for the selected model...")
                final_best_metrics = self.metrics_calculator(best_model, X_test, y_test, best_model_name).to_dict()


                # Save the best model metrics in json format
                best_model_metrics = {
                    "name": best_model_name,
                    "params": final_best_metrics
                }

                write_json(self.model_trainer_config.best_model_metrics_file_path, best_model_metrics)
                logging.info(f"Saved best model parameters to {self.model_trainer_config.best_model_metrics_file_path}:\n {best_model_metrics}")
                print(f"Best Model Metrics for {best_model_name}:\n{best_model_metrics}")

            else:
                
                logging.info("No best model parameters found; proceeding with hyperparameter tuning.")
                best_models, best_params_dict = self.tune_hyperparameters(X_train, y_train)
                

                best_model = None
                best_recall = 0
                final_best_model_name = None
                final_best_params = None
                

                # Evaluate the best model
                logging.info("Evaluating tuned models on the validation set")
                for model_name, model in best_models.items():
                    logging.info(f"Evaluating model: {model_name}")
                    
                    result = self.metrics_calculator(model, X_test, y_test, model_name)
                    recall = float(result.loc['Recall (Class 1)'].values[0].replace('%', ''))
                    
                    if recall > best_recall:
                        logging.info(f"Model {model_name} has recall: {recall}%")
                        
                        best_recall = recall
                        best_model = model
                        final_best_model_name = model_name
                        final_best_params = best_params_dict[model_name]


                if best_model is None:
                    raise HotelBookingException("No suitable model found.", sys)


                # Save the best parameters in json format
                best_model_params = {
                    "name": final_best_model_name,
                    "params": final_best_params
                }
                write_json(self.model_trainer_config.best_model_params_file_path, best_model_params)
                logging.info(f"Saved best model parameters to {self.model_trainer_config.best_model_params_file_path}: {best_model_params}")


            # Wrap the trained model in a HotelBookingModel and save it
            hotel_booking_model = HotelBookingModel(trained_model_object=best_model)
            save_object(file_path=self.model_trainer_config.model_object_file_path, obj=hotel_booking_model)
            logging.info("Best model saved successfully")


            model_trainer_artifact = ModelTrainerArtifact(
                model_object_file_path=self.model_trainer_config.model_object_file_path,
                best_model_params_file_path=self.model_trainer_config.best_model_params_file_path,
                best_model_metrics_file_path=self.model_trainer_config.best_model_metrics_file_path
            )
            logging.info(f"Model trainer artifact created: {model_trainer_artifact}")
            
            return model_trainer_artifact

        except Exception as e:
            raise HotelBookingException(e, sys) from e
