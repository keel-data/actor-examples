# Remote jobs API: Himalayas, Remote OK, We Work Remotely, Jobicy and Arbeitnow (Apify Actor examples)

One call returns remote job postings from five public job boards as one flat, de-duplicated JSON list: title, company,
source, location restrictions, salary where published, posted date and apply URL. It reads each board's public API or
feed, so no proxies and no login. Every row carries the source name and a link back to the board, as the boards ask.

Built by Keel Data. Store page: https://apify.com/loamy_barista/remote-jobs-aggregator

## Sample output
Real output from a platform run on 2026-11-25 (input: keywords "engineer", maxAgeDays 14, maxItems 40; descriptions
shortened here). The run returned 40 jobs: Jobicy 15, Himalayas 13, Remote OK 5, Arbeitnow 4, We Work Remotely 3.
Full sample: [sample-output.json](sample-output.json).

```json
{
  "jobId": "himalayas:https://himalayas.app/companies/niki-digital-engineering/jobs/engineer-management-of-weight-data-in-vehicle-development",
  "title": "Engineer - Management of Weight Data in Vehicle Development",
  "company": "NIKI Digital Engineering",
  "source": "Himalayas",
  "sourceUrl": "https://himalayas.app/companies/niki-digital-engineering/jobs/engineer-management-of-weight-data-in-vehicle-development?utm_source=api",
  "applyUrl": "https://himalayas.app/companies/niki-digital-engineering/jobs/engineer-management-of-weight-data-in-vehicle-development?utm_source=api",
  "category": "Weight-Data-Engineer, Vehicle-Development-Engineer, Automotive-Engineer, Mechanical-Engineer, Electrical-Engineer",
  "tags": null,
  "employmentType": "Full Time",
  "seniority": "Mid-level",
  "locationRestrictions": "Greece",
  "salaryMin": null,
  "salaryMax": null,
  "salaryCurrency": null,
  "postedAt": "2026-11-20T02:02:00Z",
  "companyLogo": "https://cdn-images.himalayas.app/4za9ut22z63copri77i80tw1xmkr",
  "descriptionText": "NIKI is looking for Electrical/Mechanical Engineers, Physicists, and Mathematicians holding a Ph.D., M.Sc, or similar di",
  "dedupKey": "niki-digital-engineering-engineer-management-of-weight-data-in-vehicle-development",
  "scrapedAt": "2026-11-25T23:10:24.334285Z"
}
```

## Python
```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("loamy_barista/remote-jobs-aggregator").call(run_input={
    "keywords": ["engineer"],
    "maxAgeDays": 14,
    "maxItems": 40,
})
for job in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(job["source"], job["company"], job["title"], job["applyUrl"])
```

## JavaScript
```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('loamy_barista/remote-jobs-aggregator').call({
  keywords: ['engineer'],
  maxAgeDays: 14,
  maxItems: 40,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items.length);
```

More scripts: [examples/](examples/) (`run.py`, `run.js`, `monitor_daily.py`).

## Input (main fields)
- `keywords`, `excludeKeywords`: keep or drop jobs by words in the title, category or tags.
- `sources`: any of himalayas, remoteok, weworkremotely, jobicy, arbeitnow (default all five).
- `maxAgeDays`: drop jobs older than this.
- `onlyNew` and `monitorId`: monitor mode, only new or changed jobs on each scheduled run.
- `dedupe`: remove cross-source duplicates (on by default).
- `maxItems`: spend cap; sources are read round-robin so a capped run still covers every board.

## Pricing example
Pay per result: $0.0014 per job. 1,000 jobs cost $1.40. The run above (40 jobs) costs $0.056. Set `maxItems` to cap spend.

## Use from AI agents
The Actor works through Apify's hosted MCP server (https://mcp.apify.com). Minimal call:
`{"keywords": ["python"], "maxItems": 20}`.

## Sources and attribution
Himalayas, Remote OK, We Work Remotely, Jobicy and Arbeitnow are credited in every row (`source`, `sourceUrl`). Apply
links go to the original posting.

## Related
- [Greenhouse, Lever and Ashby Jobs API](https://apify.com/loamy_barista/ats-job-board-scraper)
- [Shopify Products JSON Scraper](https://apify.com/loamy_barista/shopify-store-products)

If this saved you time, a short review on the Store page helps others find it.
