"""Run once a day (cron or an Apify schedule) and print only jobs not returned before."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("loamy_barista/linkedin-jobs-guest-api").call(run_input={
    "keywords": "data engineer",
    "location": "United States",
    "onlyNew": True,
    "monitorId": "my-daily-data-engineer",
    "maxItems": 100,
})
new_jobs = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(len(new_jobs), "new jobs")
for job in new_jobs:
    print(job["jobUrl"], job["title"], job["companyName"])
