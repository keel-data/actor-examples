"""Pull remote engineering jobs from five boards and print them."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("loamy_barista/remote-jobs-aggregator").call(run_input={
    "keywords": ["engineer"],
    "maxAgeDays": 14,
    "maxItems": 40,
})
for job in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(job["source"], "|", job["company"], "|", job["title"], "|", job["applyUrl"])
