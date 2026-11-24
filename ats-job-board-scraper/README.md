# Greenhouse, Lever and Ashby jobs API (Apify Actor examples)

Get every open job from any company's Greenhouse, Lever or Ashby job board as flat JSON: title, department, location,
remote flag, salary range (where published), posted date and apply URL. It reads the official public job board APIs, so no
proxies and no login.

Built by Keel Data. Store page: https://apify.com/loamy_barista/ats-job-board-scraper

## Sample output
Real output from a platform run on 2026-11-24 (60 jobs from 3 boards, descriptions shortened here).
Full sample: [sample-output.json](sample-output.json).

```json
{
  "jobId": "greenhouse:airbnb:8413908",
  "title": "Operations Associate, Guest Services",
  "company": "Airbnb",
  "atsProvider": "greenhouse",
  "department": "Community Support",
  "team": null,
  "location": "Ireland",
  "isRemote": true,
  "workplaceType": "Remote",
  "employmentType": null,
  "salaryMin": null,
  "salaryMax": null,
  "salaryCurrency": null,
  "salaryPeriod": null,
  "postedAt": "2026-11-24T09:26:43-05:00",
  "updatedAt": "2026-11-24T09:26:43-05:00",
  "applyUrl": "https://careers.airbnb.com/positions/8413908?gh_jid=8413908",
  "jobUrl": "https://careers.airbnb.com/positions/8413908?gh_jid=8413908",
  "descriptionText": "Airbnb was born in 2007 when two hosts welcomed three guests to their San Francisco home, and has since grown to over 5 ",
  "changeType": null,
  "scrapedAt": "2026-11-24T18:31:48.755530Z"
}
```

## Python
```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("loamy_barista/ats-job-board-scraper").call(run_input={
    "companies": ["greenhouse:airbnb", "lever:palantir", "ashby:ramp"],
    "keywords": ["engineer"],
    "maxItems": 50,
})
for job in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(job["company"], job["title"], job["applyUrl"])
```

## JavaScript
```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('loamy_barista/ats-job-board-scraper').call({
  companies: ['greenhouse:airbnb', 'lever:palantir', 'ashby:ramp'],
  keywords: ['engineer'],
  maxItems: 50,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items.length);
```

More scripts: [examples/](examples/) (`run.py`, `run.js`, `monitor_daily.py`).

## Input (main fields)
- `companies`: board URLs, `provider:slug` (`greenhouse:airbnb`), bare slugs, or plain company names.
- `keywords`, `excludeKeywords`, `departments`, `locations`, `remoteOnly`, `maxAgeDays`: optional filters.
- `maxItems`: spend cap; jobs are taken from each board in turn.
- `onlyNew` and `monitorId`: monitor mode, only new or changed jobs.
- `descriptionMaxLength`: 0 to skip descriptions.

## Pricing example
Pay per result: $0.0014 per job. 1,000 jobs cost $1.40. The run above (60 jobs) costs $0.084. Set `maxItems` to cap spend.

## Use from AI agents
The Actor works through Apify's hosted MCP server (https://mcp.apify.com). Minimal call:
`{"companies": ["stripe", "lever:netflix"], "keywords": ["engineer"]}`.

## Related
- [Remote Jobs Aggregator](https://apify.com/loamy_barista/remote-jobs-aggregator)
- [Shopify Products JSON Scraper](https://apify.com/loamy_barista/shopify-store-products)

Sample data on Hugging Face: https://huggingface.co/datasets/Keel-data/ats-job-postings-sample
