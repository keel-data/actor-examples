"""Run on a daily schedule: with onlyNew, each run returns only jobs not seen by this monitorId before."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("loamy_barista/remote-jobs-aggregator").call(run_input={
    "keywords": ["python"],
    "onlyNew": True,
    "monitorId": "python-remote-daily",
})
new_jobs = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(f"{len(new_jobs)} new or changed jobs")
for job in new_jobs:
    print(job["company"], "-", job["title"], "-", job["applyUrl"])
