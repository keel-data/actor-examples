import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("loamy_barista/url-to-markdown").call(run_input={
    "urls": ["https://docs.python.org/3/tutorial/introduction.html"],
    "formats": ["markdown"],
    "maxCharsPerPage": 20000,
})
for page in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(page["title"], page["wordCount"], "words")
    print(page["markdown"][:300])
