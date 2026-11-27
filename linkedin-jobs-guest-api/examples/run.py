import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("loamy_barista/linkedin-jobs-guest-api").call(run_input={
    "keywords": "python developer",
    "location": "Germany",
    "datePosted": "pastWeek",
    "workplaceType": ["remote", "hybrid"],
    "maxItems": 15,
})
for job in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(job["postedDate"], job["title"], "|", job["companyName"], "|", job["location"])
