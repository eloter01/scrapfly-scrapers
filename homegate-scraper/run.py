"""
This example run script shows how to run the homegate.ch scraper defined in ./homegate.py
It scrapes ads data and saves it to ./results/

To run this script set the env variable $SCRAPFLY_KEY with your scrapfly API key:
$ export $SCRAPFLY_KEY="your key from https://scrapfly.io/dashboard"
"""
import asyncio
import json
from pathlib import Path
import homegate

output = Path(__file__).parent / "results"
output.mkdir(exist_ok=True)


async def run():
    # enable scrapfly cache for basic use
    homegate.BASE_CONFIG["cache"] = True

    print("running Homegate scrape and saving results to ./results directory")

    properties_data = await homegate.scrape_properties(
        urls=[
            "https://www.homegate.ch/rent/4002086534",
            "https://www.homegate.ch/rent/4002244507",
            "https://www.homegate.ch/rent/4002268715"
        ]
    )
    with open(output.joinpath("properties.json"), "w", encoding="utf-8") as file:
        json.dump(properties_data, file, indent=2, ensure_ascii=False)

    search_data = await homegate.scrape_search(
        url="https://www.homegate.ch/rent/real-estate/city-bern/matching-list",
        scrape_all_pages=False,
        max_scrape_pages=2,
    )
    with open(output.joinpath("search.json"), "w", encoding="utf-8") as file:
        json.dump(search_data, file, indent=2)


if __name__ == "__main__":
    asyncio.run(run())
