# src/visualization.py
import matplotlib.pyplot as plt

def plot_weather_summary(df):
    """Plot weather summary for a given dataframe."""
    df.plot(x="City", y=["avg_temp", "max_temp", "min_temp"], kind="bar")
    plt.title("Daily Weather Summary")
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.show()
