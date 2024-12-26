# This script provides utility methods for performing train-test split operations.

import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from src.core.exception import HotelBookingException



# split data into three datasets train, test and validation datasets
@staticmethod
def split_into_train_test_val(dataframe: pd.DataFrame) -> tuple:
    """
    Method Name: split_data
    Description :   Splits the given DataFrame into three datasets: train, test, and validation.
    
    Input       :   dataframe      -> The input DataFrame (train/test).
    
    Output      :   tuple         -> A tuple containing the training DataFrame, the testing DataFrame, and the validation DataFrame.
    """ 
    try:
        # Split into train and remaining (test + validation)
        train_data, temp_data = train_test_split(
            dataframe, 
            test_size=0.30,  # 30% for test + validation
            random_state=42, 
            shuffle=True
        )

        # Split remaining into test and validation
        test_data, validation_data = train_test_split(
            temp_data, 
            test_size=0.50,  # Split 30% into 50% test and 50% validation
            random_state=42, 
            shuffle=True
        )

        return train_data, test_data, validation_data
    
    except Exception as e:
        raise HotelBookingException(f"Error in split_data: {str(e)}", sys) from e


# Funcion for Separating Target feature from Dataset
@staticmethod
def separate_features_and_target(dataframe: pd.DataFrame, target_column: str) -> tuple:
    """
    Method Name :   separate_features_and_target
    Description :   Separates independent features and dependent (target) feature from the DataFrame.
    
    Input       :   df            -> The input DataFrame (train/test).
                target_column  -> The name of the target column in the DataFrame.
    
    Output      :   tuple         -> A tuple containing the independent features DataFrame and the target feature series.
    """
    try:        
        # Separating independent features (X) and target feature (y)
        X = dataframe.drop(columns=[target_column], axis=1)
        y = dataframe[target_column]
        
        return X, y

    except Exception as e:
        raise HotelBookingException(f"Error in separate_features_and_target: {str(e)}", sys) from e


@staticmethod
def train_test_split_for_data_validation(dataframe: pd.DataFrame, test_size: float) -> tuple:
    """
    Perform train-test split on the given DataFrame for data validation.

    :param dataframe: The DataFrame to split.
    :param test_size: The proportion of the dataset to include in the test split.
    :return: A tuple containing the training set and the testing set.
    """
    try:
        train_set, test_set = train_test_split(dataframe, test_size=test_size, random_state=42)
        return train_set, test_set
    except Exception as e:
        raise HotelBookingException(e, sys) from e


@staticmethod
def train_test_split_for_model_building(dataframe: pd.DataFrame, test_size: float, target_column: str) -> tuple:
    """
    Perform train-test split on the given DataFrame with stratification for model training.

    :param dataframe: The DataFrame to split.
    :param test_size: The proportion of the dataset to include in the test split.
    :param target_column: The name of the target column to stratify on.
    :return: A tuple containing the training set and the testing set.
    """
    try:
        # Separate the features and the target column
        X = dataframe.drop(columns=[target_column])
        y = dataframe[target_column]

        # Perform train-test split with stratification
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, stratify=y)

        # # Combine the features and target columns back into DataFrames
        # train_set = pd.concat([X_train, y_train], axis=1)
        # test_set = pd.concat([X_test, y_test], axis=1)

        return X_train, X_test, y_train, y_test 
    except Exception as e:
        raise HotelBookingException(e, sys) from e


@staticmethod
def train_test_split_for_tuning(X_train: pd.DataFrame, y_train: pd.Series, test_size: float) -> tuple:
    """
    Perform train-test split on the given training data for hyperparameter tuning.

    :param X_train: The training features DataFrame.
    :param y_train: The training target Series.
    :param test_size: The proportion of the dataset to include in the test split.
    :return: A tuple containing the tuning set features and target.
    """
    try:
        # Perform train-test split for hyperparameter tuning
        X_tune, _, y_tune, _ = train_test_split(X_train, y_train, test_size=test_size)
        return X_tune, y_tune
    except Exception as e:
        raise HotelBookingException(e, sys) from e
