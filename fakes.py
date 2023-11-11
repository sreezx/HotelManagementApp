import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import numpy as np

# Weather data for Monaco
monaco_weather = {
    'temperature': 25,
    'humidity': 60,
    'wind_speed': 10,
    'UV_index': 5,
}

# Weather data for Maldives
maldives_weather = {
    'temperature': 30,
    'humidity': 75,
    'wind_speed': 12,
    'UV_index': 8,
}

# Create a DataFrame for visualization
weather_df = pd.DataFrame({
    'Metrics': list(monaco_weather.keys()),
    'Monaco': list(monaco_weather.values()),
    'Maldives': list(maldives_weather.values())
})

# Set Metrics as the index
weather_df.set_index('Metrics', inplace=True)


# Create a DataFrame
mon_df = pd.DataFrame(np.random.randn(20, 3), columns=["2020", "2021", "2022"])

# Create a DataFrame
mal_df = pd.DataFrame(pd.DataFrame(np.random.randn(10, 3), columns=["2020", "2021", "2022"]))
