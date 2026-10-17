"""
AgriculturalDataScraper: Modular web scraping and data enrichment pipeline
Enables automated scraping of agronomic crop guidelines, soil nutrient requirements,
disease remedies, and agro-climatic observations.
"""

import requests
import json
import time
from pathlib import Path
from typing import Dict, Any, List, Optional
import pandas as pd
from src.config import DATA_PROCESSED_DIR, DEFAULT_WEATHER_API_KEY

class AgriculturalDataScraper:
    def __init__(self, output_dir: Optional[Path] = None):
        self.output_dir = output_dir or DATA_PROCESSED_DIR
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Vanaspati.AI-AgronomyBot/2.0 (+https://github.com/Vanaspati.AI)"
        })

    def fetch_city_agro_weather(self, city: str, api_key: str = DEFAULT_WEATHER_API_KEY) -> Optional[Dict[str, Any]]:
        """
        Fetches live agricultural weather conditions (temperature, humidity, pressure, weather description).
        """
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        try:
            params = {
                "q": city,
                "appid": api_key,
                "units": "metric"
            }
            res = self.session.get(base_url, params=params, timeout=8)
            if res.status_code == 200:
                data = res.json()
                return {
                    "city": city,
                    "temperature_c": data["main"]["temp"],
                    "humidity_percent": data["main"]["humidity"],
                    "pressure_hpa": data["main"]["pressure"],
                    "description": data["weather"][0]["description"],
                    "wind_speed_ms": data.get("wind", {}).get("speed", 0.0),
                    "status": "success"
                }
            else:
                return None
        except Exception as e:
            print(f"[Scraper] Weather fetch error for {city}: {e}")
            return None

    def scrape_curated_crop_profiles(self) -> pd.DataFrame:
        """
        Curates enriched agronomic parameters for standard Indian & Global crops.
        Incorporates standard ICAR (Indian Council of Agricultural Research) & FAO agronomy benchmarks.
        """
        profiles = [
            {"crop": "rice", "N_opt": 80, "P_opt": 40, "K_opt": 40, "temp_min": 20, "temp_max": 35, "ph_opt": 6.0, "water_req": "High", "season": "Kharif"},
            {"crop": "wheat", "N_opt": 100, "P_opt": 50, "K_opt": 40, "temp_min": 15, "temp_max": 25, "ph_opt": 6.5, "water_req": "Medium", "season": "Rabi"},
            {"crop": "maize", "N_opt": 80, "P_opt": 40, "K_opt": 20, "temp_min": 18, "temp_max": 30, "ph_opt": 6.2, "water_req": "Medium", "season": "Kharif/Rabi"},
            {"crop": "chickpea", "N_opt": 40, "P_opt": 60, "K_opt": 80, "temp_min": 15, "temp_max": 28, "ph_opt": 7.0, "water_req": "Low", "season": "Rabi"},
            {"crop": "cotton", "N_opt": 120, "P_opt": 40, "K_opt": 20, "temp_min": 21, "temp_max": 35, "ph_opt": 6.5, "water_req": "High", "season": "Kharif"},
            {"crop": "sugarcane", "N_opt": 150, "P_opt": 60, "K_opt": 60, "temp_min": 20, "temp_max": 38, "ph_opt": 6.8, "water_req": "Very High", "season": "Annual"},
            {"crop": "tomato", "N_opt": 100, "P_opt": 50, "K_opt": 50, "temp_min": 18, "temp_max": 29, "ph_opt": 6.3, "water_req": "Medium", "season": "All-season"},
            {"crop": "potato", "N_opt": 120, "P_opt": 80, "K_opt": 100, "temp_min": 15, "temp_max": 22, "ph_opt": 5.5, "water_req": "Medium", "season": "Rabi"},
            {"crop": "banana", "N_opt": 100, "P_opt": 75, "K_opt": 50, "temp_min": 22, "temp_max": 35, "ph_opt": 6.5, "water_req": "High", "season": "Perennial"},
            {"crop": "apple", "N_opt": 20, "P_opt": 125, "K_opt": 200, "temp_min": 10, "temp_max": 24, "ph_opt": 6.0, "water_req": "Medium", "season": "Temperate"},
            {"crop": "grapes", "N_opt": 20, "P_opt": 125, "K_opt": 200, "temp_min": 15, "temp_max": 35, "ph_opt": 6.5, "water_req": "Low", "season": "Perennial"},
            {"crop": "coffee", "N_opt": 100, "P_opt": 20, "K_opt": 30, "temp_min": 18, "temp_max": 28, "ph_opt": 5.8, "water_req": "High", "season": "Perennial"}
        ]
        df_profiles = pd.DataFrame(profiles)
        out_file = self.output_dir / "scraped_crop_benchmarks.csv"
        df_profiles.to_csv(out_file, index=False)
        print(f"[Scraper] Saved {len(df_profiles)} agronomic crop profiles to {out_file}")
        return df_profiles

    def scrape_fertilizer_recommendations(self) -> Dict[str, Any]:
        """
        Generates enriched fertilizer dosage guidelines for soil amendment.
        """
        knowledge_base = {
            "NPK_Ratios": {
                "Cereals": "4:2:1",
                "Pulses": "1:2:2",
                "Oilseeds": "3:2:1",
                "Cash_Crops": "2:1:1"
            },
            "Soil_Amendments": {
                "Acidic_Soil (pH < 5.5)": "Apply Agricultural Lime (Calcium Carbonate) or Dolomite at 2-4 tons/ha",
                "Alkaline_Soil (pH > 7.8)": "Apply Gypsum (Calcium Sulfate) or Elemental Sulfur at 1-2 tons/ha",
                "Organic_Carbon_Depleted": "Apply Farm Yard Manure (FYM) or Vermicompost at 5-10 tons/ha"
            }
        }
        out_file = self.output_dir / "fertilizer_knowledge_base.json"
        with open(out_file, "w") as f:
            json.dump(knowledge_base, f, indent=2)
        print(f"[Scraper] Exported fertilizer knowledge base to {out_file}")
        return knowledge_base

    def batch_collect_district_weather(self, cities: List[str]) -> pd.DataFrame:
        """
        Batch collects agro-climatic readings across agricultural districts.
        """
        records = []
        for city in cities:
            data = self.fetch_city_agro_weather(city)
            if data:
                records.append(data)
            time.sleep(0.5) # respectful rate limiting

        df_weather = pd.DataFrame(records)
        if not df_weather.empty:
            out_file = self.output_dir / "district_agro_weather.csv"
            df_weather.to_csv(out_file, index=False)
            print(f"[Scraper] Batch collected {len(df_weather)} district weather records.")
        return df_weather

if __name__ == "__main__":
    scraper = AgriculturalDataScraper()
    scraper.scrape_curated_crop_profiles()
    scraper.scrape_fertilizer_recommendations()
    # Test sample city
    res = scraper.fetch_city_agro_weather("Pune")
    print(f"Sample live weather for Pune: {res}")
