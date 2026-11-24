"""Monitor mode: schedule this daily and only new or changed jobs come back (and are billed)."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("loamy_barista/ats-job-board-scraper").call(run_input={
    "companies": ["stripe", "ramp", "palantir"],
    "onlyNew": True,
    "monitorId": "eng-watch",
    "descriptionMaxLength": 0,
})
for job in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(job["changeType"], job["company"], job["title"], job["jobUrl"])
