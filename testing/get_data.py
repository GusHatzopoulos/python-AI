import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

today = datetime.now().date()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Your city coordinates (from latlong.net)
LATITUDE = 40.640064
LONGITUDE = 22.944420
TIMEZONE = "Europe%2FAthens"  # Europe/Athens (URL-encoded)

url = (
    "https://archive-api.open-meteo.com/v1/archive"
    f"?latitude={LATITUDE}&longitude={LONGITUDE}"
    f"&start_date={start_date}&end_date={end_date}"
    "&daily=temperature_2m_max,temperature_2m_min"
    f"&timezone={TIMEZONE}"
)

response = requests.get(url, timeout=30)
response.raise_for_status()
data = response.json()

# Defensive checks
if data.get("error"):
    raise RuntimeError(f"Open-Meteo error: {data.get('reason')}")

daily = data.get("daily")
if not daily or "time" not in daily:
    raise RuntimeError(f"No daily data returned. Response keys: {list(data.keys())}")

df = pd.DataFrame(
    {
        "date": pd.to_datetime(daily["time"]),
        "max_temp": daily["temperature_2m_max"],
        "min_temp": daily["temperature_2m_min"],
    }
).sort_values("date")

plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["max_temp"], marker="o", label="Max Temp")
plt.plot(df["date"], df["min_temp"], marker="o", label="Min Temp")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("My City Weather - Past 7 Days")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Save to CSV
df.to_csv("data/my_city_weather.csv", index=False)
print("Data saved to data/my_city_weather.csv")