"""Split the returned Markdown on headings so each chunk fits an embedding model."""
import os
import re
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("loamy_barista/url-to-markdown").call(run_input={
    "urls": ["https://en.wikipedia.org/wiki/Markdown"],
})
for page in client.dataset(run["defaultDatasetId"]).iterate_items():
    chunks = re.split(r"\n(?=#{1,3} )", page["markdown"])
    print(page["url"], len(chunks), "chunks")
