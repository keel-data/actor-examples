"""Call the Greenhouse / Lever / Ashby jobs Actor through the Apify API.
Set APIFY_TOKEN in your environment first."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("loamy_barista/ats-job-board-scraper").call(run_input={
    "companies": ["greenhouse:airbnb", "lever:palantir", "ashby:ramp"],
    "keywords": ["engineer"],
    "maxItems": 50,
    "descriptionMaxLength": 0,
})
for job in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(job["company"], "|", job["title"], "|", job["location"], "|", job["applyUrl"])
