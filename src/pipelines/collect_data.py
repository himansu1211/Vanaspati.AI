"""
CLI Pipeline: Web scraping and data enrichment orchestrator
Usage:
    python -m src.pipelines.collect_data [--weather-cities "Mumbai,Delhi,Bengaluru"] [--sample-leaves]
"""

import argparse
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.data.scraper import AgriculturalDataScraper
from src.data.image_collector import PlantImageCollector

def main():
    parser = argparse.ArgumentParser(description="Agricultural Data Collection & Scraping Pipeline")
    parser.add_argument("--scrape-profiles", action="store_true", default=True, help="Scrape standard crop profiles")
    parser.add_argument("--weather-cities", type=str, default="Mumbai,Delhi,Bengaluru,Pune,Nagpur,Ludhiana", help="Comma-separated cities for agro-weather")
    parser.add_argument("--sample-leaves", action="store_true", default=True, help="Generate sample testing leaf imagery")
    args = parser.parse_args()

    print("=" * 60)
    print("Vanaspati.AI - Agricultural Data Collection & Enrichment")
    print("=" * 60)

    # 1. Scraper
    scraper = AgriculturalDataScraper()
    if args.scrape_profiles:
        print("\n1. Scraping agronomic crop benchmarks & fertilizer guidelines...")
        df_benchmarks = scraper.scrape_curated_crop_profiles()
        scraper.scrape_fertilizer_recommendations()
        print(f"   Collected {len(df_benchmarks)} crop agronomy profiles.")

    cities = [c.strip() for c in args.weather_cities.split(",") if c.strip()]
    if cities:
        print(f"\n2. Collecting agro-climatic readings for {len(cities)} cities...")
        df_weather = scraper.batch_collect_district_weather(cities)
        print(f"   Collected {len(df_weather)} live weather readings.")

    # 2. Image Collector
    if args.sample_leaves:
        print("\n3. Verifying image dataset folders & generating sample test leaves...")
        collector = PlantImageCollector()
        collector.prepare_directory_structure()
        samples = collector.generate_sample_test_leaves()
        print(f"   Created {len(samples)} sample leaf test images for web UI verification.")

    print("\nData enrichment pipeline completed successfully!")

if __name__ == "__main__":
    main()
