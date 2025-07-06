"""
This example run script shows how to run the Aliexpress.com scraper defined in ./aliexpress.py
It scrapes product data and product search and saves it to ./results/

To run this script set the env variable $SCRAPFLY_KEY with your scrapfly API key:
$ export $SCRAPFLY_KEY="your key from https://scrapfly.io/dashboard"
"""
import asyncio
from datetime import datetime
import json
from pathlib import Path
import realtorcom

output = Path(__file__).parent / "results"
output.mkdir(exist_ok=True)


async def run():
    # enable scrapfly cache for basic use
    realtorcom.BASE_CONFIG["cache"] = True
    realtorcom.BASE_CONFIG["country"] = "US"

    print("running Realtor.com scrape and saving results to ./results directory")

    # url = "https://www.realtor.com/realestateandhomes-detail/12355-Attlee-Dr_Houston_TX_77077_M70330-35605"
    # result_property = await realtorcom.scrape_property(url)
    # output.joinpath("property.json").write_text(json.dumps(result_property, indent=2))

    result_search = await realtorcom.scrape_search("https://www.realtor.com/realestateandhomes-search/Middlesex-County_NJ/type-single-family-home/beds-3/baths-2/pnd-hide/price-na-600000/commute-100-Business-Park-Dr_Skillman_NJ-08558,40.40472,-74.669176,40m,drive,traffic/pg-1", "NJ", "Middlesex County")
    output.joinpath("search.json").write_text(json.dumps(result_search, indent=2))

    # url = "https://cdn.realtor.ca/sitemap/realtorsitemap/sitemap.xml"
    # result_feed = await realtorcom.scrape_feed(url)
    # output.joinpath("feed.json").write_text(json.dumps(result_feed, indent=2, cls=DateTimeEncoder))


class DateTimeEncoder(json.JSONEncoder):
    """Custom JSONEncoder subclass that knows how to encode datetime values."""

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()  # Convert datetime objects to ISO-8601 string format

        return super(DateTimeEncoder, self).default(o)  # Default behaviour for other types


if __name__ == "__main__":
    asyncio.run(run())
