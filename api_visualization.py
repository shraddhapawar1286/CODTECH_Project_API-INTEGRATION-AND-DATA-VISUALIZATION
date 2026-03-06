import requests
import matplotlib.pyplot as plt
from datetime import datetime

# -----------------------------
# CONFIGURATION
# -----------------------------
API_KEY = "3219db8c749ec7f5b5d924615b34c4d2"
CITY = "Barshi"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={"Barshi"}&appid={'3219db8c749ec7f5b5d924615b34c4d2'}&units=metric"

# -----------------------------
# FETCH DATA FROM API
# -----------------------------
response = requests.get(URL)
data = response.json()

if response.status_code != 200:
    print("Error fetching data:", data)
    exit()

# -----------------------------
# EXTRACT REQUIRED DATA
# -----------------------------
dates = []
temperatures = []
humidity = []
wind_speed = []

for item in data["list"][:8]:   # Next 24 hours (3-hour interval data)
    dates.append(datetime.fromtimestamp(item["dt"]))
    temperatures.append(item["main"]["temp"])
    humidity.append(item["main"]["humidity"])
    wind_speed.append(item["wind"]["speed"])

# -----------------------------
# CREATE VISUALIZATION DASHBOARD
# -----------------------------

plt.figure(figsize=(12, 8))

# Temperature Plot
plt.subplot(3, 1, 1)
plt.plot(dates, temperatures)
plt.title(f"Temperature Forecast for {CITY}")
plt.ylabel("Temperature (°C)")

# Humidity Plot
plt.subplot(3, 1, 2)
plt.plot(dates, humidity)
plt.title("Humidity Levels")
plt.ylabel("Humidity (%)")

# Wind Speed Plot
plt.subplot(3, 1, 3)
plt.plot(dates, wind_speed)
plt.title("Wind Speed")
plt.ylabel("Wind Speed (m/s)")
plt.xlabel("Date & Time")

plt.tight_layout()
plt.show()