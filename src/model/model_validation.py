from src.core.exception import HotelBookingException

def validate_model(report_path="artifacts/reports/metrics/report.json"):
    with open(report_path, "r") as f:
        report = json.load(f)
    
    # Example: Check if accuracy is above 80%
    if report["accuracy"] < 0.8:
        raise HotelBookingException("Model accuracy below 80% threshold.")