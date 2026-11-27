# LinkedIn Jobs Scraper and API: public job postings as JSON (Apify Actor examples)

Search public LinkedIn job postings by keyword and location and get clean JSON: title, company, location, posting date,
salary when listed, applicant count, seniority, employment type, industries and the full description. It reads only the
job pages LinkedIn shows to logged-out visitors: no account, no cookies, no browser. Monitor mode returns only jobs you
have not seen before.

Built by Keel Data. Store page: https://apify.com/loamy_barista/linkedin-jobs-guest-api

## Sample output
Real output from a platform run on 2026-11-27 (run NWfPUYyfgf15qifkM): `python developer` in `Germany`, past week,
remote or hybrid, 15 jobs. Full details on, so every row has its description. The run took 135 seconds and cost
$0.0019 in platform usage. Five of the rows are in [sample-output.json](sample-output.json) with descriptions cut to 300
characters.

| Title | Company | Location | Posted | Applicants |
|---|---|---|---|---|
| Senior Python Entwickler* | Haeger Consulting GmbH | Bonn, North Rhine-Westphalia,  | 2026-11-24 | 25 |
| (Senior) Software Engineer (m/w/d) mit Schwerpunkt | Cornelsen Verlag GmbH | Berlin, Berlin, Germany | 2026-11-23 | 38 |
| Senior Backend Developer (Python) | Hornetsecurity | Hannover, Lower Saxony, German | 2026-11-26 | 200 |
| Senior Software Engineer | Rise Technical | Hamburg, Germany | 2026-11-27 | 26 |
| Backend-Entwickler Python (m/w/d) | tprime IT GmbH | Augsburg, Bavaria, Germany | 2026-11-25 | 61 |
| Senior Software Engineer (m/w/d) – Python | ZABEL | Berlin, Germany | 2026-11-23 | 44 |
| Software Engineer - Python, AI, R&D - Heidelberg - | Findr | Heidelberg, Baden-Württemberg, | 2026-11-26 | 30 |
| Senior Python Entwickler (w/m/d) | Instaffo | Ratingen, North Rhine-Westphal | 2026-11-26 | 25 |

First row (description shortened):

```json
{
 "jobId": "4492684415",
 "jobUrl": "https://www.linkedin.com/jobs/view/4492684415/",
 "title": "Senior Python Entwickler*",
 "companyName": "Haeger Consulting GmbH",
 "companyUrl": "https://www.linkedin.com/company/haeger-consulting",
 "companyLogoUrl": "https://media.licdn.com/dms/image/v2/C4E0BAQH_d8N7IIcv-A/com...",
 "location": "Bonn, North Rhine-Westphalia, Germany",
 "postedDate": "2026-11-24",
 "postedTimeAgo": "3 days ago",
 "badge": "Be an early applicant",
 "salaryText": null,
 "salaryMin": null,
 "salaryMax": null,
 "salaryCurrency": null,
 "salaryPeriod": null,
 "applicantsCount": 25,
 "applicantsText": "Be among the first 25 applicants",
 "seniorityLevel": "Associate",
 "employmentType": "Full-time",
 "jobFunction": null,
 "industries": "Software Development",
 "description": "Was dich erwartet\n\n- Du konzipierst, entwickelst und optimierst anspruchsvolle Softwarelösungen im Enterprise-Umfeld.\n- Du übernimmst die technische Verantwortung für Projekte und unterstützt Teams bei Architektur- und Technologieentscheidungen.\n- Du entwickelst leistungsfähige Backend-Lösungen mit ...",
 "descriptionChars": 6050,
 "applyUrl": null,
 "detailStatus": "ok",
 "searchKeywords": "python developer",
 "searchLocation": "Germany",
 "searchRank": 1,
 "scrapedAt": "2026-11-27T23:09:52Z"
}
```

## Python
```python
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
    print(job["postedDate"], job["title"], "|", job["companyName"])
```

## JavaScript
```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('loamy_barista/linkedin-jobs-guest-api').call({
  keywords: 'python developer', location: 'Germany', datePosted: 'pastWeek', maxItems: 15,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items.length, 'jobs');
```

More scripts: [examples/](examples/) (`run.py`, `run.js`, `daily_new_jobs.py`).

## Input (main fields)
- `keywords`, `location`: as typed in LinkedIn's job search box. Defaults: `data engineer`, `United States`.
- `datePosted`: `pastHour`, `past24h`, `pastWeek`, `pastMonth`.
- `workplaceType`, `jobType`, `experienceLevel`: lists of filters.
- `maxItems`: spend cap (default 10).
- `fetchDetails`: on by default (description, applicants, salary); off gives faster card-only rows.
- `onlyNew` and `monitorId`: monitor mode, only new jobs on each scheduled run.
- `searchUrls`: paste LinkedIn job search URLs and their filters are used.

## Pricing example
Pay per event: $0.0012 per job posting plus a $0.00005 run-start event. 1,000 jobs cost about $1.20. The 15-job run
above was charged 15 job events and 1 start event. Jobs already seen in monitor mode are free.

## Use from AI agents
The Actor works through Apify's hosted MCP server (https://mcp.apify.com). Minimal call:
`{"keywords": "python developer", "location": "Germany", "maxItems": 10}`.

## Notes
Public job postings only. People are never part of the output: no recruiter or poster names, no member profiles.
Emails and phone numbers inside descriptions are replaced with `[email removed]` and `[phone removed]`. Fetching with
details runs at a polite pace, so allow about 9 seconds per job; turn `fetchDetails` off for speed.

## Related
- [ATS Job Board Scraper](https://apify.com/loamy_barista/ats-job-board-scraper)
- [Career Site Jobs API](https://apify.com/loamy_barista/career-site-jobs-api)
- [Remote Jobs Aggregator](https://apify.com/loamy_barista/remote-jobs-aggregator)

If this saved you time, a short review on the Store page helps others find it.
