"""Run this daily (cron or an Apify schedule). With onlyNew, only pages whose Markdown changed come back."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("loamy_barista/url-to-markdown").call(run_input={
    "urls": ["https://docs.python.org/3/whatsnew/index.html"],
    "onlyNew": True,
    "monitorId": "python-whatsnew",
})
for page in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(page["changeType"], page["url"])
