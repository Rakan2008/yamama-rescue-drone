"""
weather_for_drone_real.py
Get real-time weather data from Open-Meteo (no API key needed)
and decide realistic drone flight status: SAFE / CAUTION / NO-FLY
"""

import requests
from datetime import datetime, timezone
from colorama import Fore, Style, init
import time

# Enable colored text in terminal
init(autoreset=True)

# ⚙️ Realistic thresholds for coastal / Jeddah-like environment
THRESHOLDS = {
    "no_fly_wind": 17.0,      # m/s - very strong wind
    "no_fly_gust": 23.0,      # m/s - dangerous gusts
    "caution_wind": 10.0,     # m/s - moderate wind, caution
    "caution_gust": 15.0,     # m/s - moderate gusts
    "low_visibility_m": 2000  # meters - poor visibility
}

# 📡 Fetch data from Open-Meteo API (no key required)
def fetch_weather(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        "&current=temperature_2m,wind_speed_10m,wind_gusts_10m,precipitation,cloud_cover"
    )
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()

# 🔍 Analyze weather data and determine flight decision
def analyze_weather(data):
    c = data["current"]
    report = {
        "timestamp_utc": c.get("time"),
        "temp_c": c.get("temperature_2m"),
        "wind_speed_m_s": c.get("wind_speed_10m"),
        "wind_gust_m_s": c.get("wind_gusts_10m"),
        "precipitation_mm": c.get("precipitation"),
        "clouds_pct": c.get("cloud_cover"),
    }

    wind = report["wind_speed_m_s"] or 0
    gust = report["wind_gust_m_s"] or 0
    rain = report["precipitation_mm"] or 0

    decision = "SAFE"
    reasons = []

    # Decision logic
    if wind >= THRESHOLDS["no_fly_wind"] or gust >= THRESHOLDS["no_fly_gust"]:
        decision = "NO-FLY"
        reasons.append("Very strong wind or gusts")
    elif wind >= THRESHOLDS["caution_wind"] or gust >= THRESHOLDS["caution_gust"]:
        decision = "CAUTION"
        reasons.append("Moderate wind/gusts")

    if rain > 2.5:
        decision = "NO-FLY"
        reasons.append("Heavy rain")

    report["decision"] = decision
    report["reasons"] = reasons
    return report

# 🎨 Nicely formatted color output
def pretty_print(r, lat, lon):
    print("=" * 45)
    print(f"🌍 Location: lat={lat}, lon={lon}")
    print(f"🕓 Time (UTC): {r['timestamp_utc']}")
    print(f"🌡️ Temperature: {r['temp_c']}°C")
    print(f"💨 Wind: {r['wind_speed_m_s']} m/s | Gusts: {r['wind_gust_m_s']} m/s")
    print(f"🌧️ Precipitation: {r['precipitation_mm']} mm | ☁️ Clouds: {r['clouds_pct']}%")
    print("-" * 45)

    if r["decision"] == "SAFE":
        print(Fore.GREEN + "✅ Decision: SAFE – Weather is excellent for flight.")
    elif r["decision"] == "CAUTION":
        print(Fore.YELLOW + "⚠️ Decision: CAUTION – Fly with caution.")
    else:
        print(Fore.RED + "🚫 Decision: NO-FLY – Unsafe flying conditions.")

    if r["reasons"]:
        print(Style.BRIGHT + "📝 Reasons:", "; ".join(r["reasons"]))
    print("=" * 45 + "\n")

# 🚀 Main loop: check weather every 10 minutes
def main():
    lat, lon = 21.4858, 39.1925  # Jeddah coordinates
    print(Fore.CYAN + "🔄 Starting continuous weather monitoring for drone...\n")

    while True:
        try:
            data = fetch_weather(lat, lon)
            rep = analyze_weather(data)
            pretty_print(rep, lat, lon)
        except Exception as e:
            print(Fore.RED + f"⚠️ Error fetching data: {e}")
        time.sleep(600)  # refresh every 10 minutes

if __name__ == "__main__":
    main()
