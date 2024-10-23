# src/alerting.py
import pandas as pd
from config import TEMP_THRESHOLD, ALERT_THRESHOLD

def check_thresholds(df, threshold=TEMP_THRESHOLD):
    """Check if any city exceeds the temperature threshold."""
    breach_count = (df["Temperature"] > threshold).sum()

    if breach_count >= ALERT_THRESHOLD:
        print(f"Alert: Temperature exceeded {TEMP_THRESHOLD}°C in {breach_count} cities!")
        # Optionally, send an email or console alert here
