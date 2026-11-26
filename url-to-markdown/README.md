# URL to Markdown API: web page to clean Markdown for LLMs and RAG (Apify Actor examples)

Give it public URLs, get back clean Markdown (or plain text, cleaned HTML, links) plus title, language, canonical URL,
word count and robots.txt status. Plain HTTP fetch, no browser, so runs are fast and cheap. Batch many URLs in one call,
cap characters per page to fit a context window, and use monitor mode to get only pages whose content changed.

Built by Keel Data. Store page: https://apify.com/loamy_barista/url-to-markdown

## Sample output
Real output from a platform run on 2026-11-26 (3 pages, `maxCharsPerPage` 1500, so `truncated` is true; the markdown
field is shortened again below). Full sample: [sample-output.json](sample-output.json).

| Page | Words | Markdown chars (before cut) | robots.txt |
|---|---|---|---|
| https://en.wikipedia.org/wiki/Markdown | 3595 | 47434 | allowed |
| https://docs.python.org/3/tutorial/introduction.html | 3224 | 19341 | allowed |
| https://www.rfc-editor.org/rfc/rfc9110.html | 69514 | 744910 | allowed |

```json
{
  "inputUrl": "https://docs.python.org/3/tutorial/introduction.html",
  "url": "https://docs.python.org/3/tutorial/introduction.html",
  "domain": "docs.python.org",
  "status": "ok",
  "error": null,
  "httpStatus": 200,
  "contentType": "text/html",
  "title": "3. An Informal Introduction to Python \u2014 Python 3.15.2 documentation",
  "description": "In the following examples, input and output are distinguished by the presence or absence of prompts (>>> and \u2026): to repeat the example, you must type everything after the prompt, when the ...",
  "language": "en",
  "canonicalUrl": "https://docs.python.org/3/tutorial/introduction.html",
  "publishedAt": null,
  "markdown": "# 3. An Informal Introduction to Python\n\nIn the following examples, input and output are distinguished by the presence or\nabsence of prompts ([>>>](https://docs.python.org/3/glossary.html#term-0) and [\u2026](https://docs.python.org/3/glossary.html#term-...)): to repeat the example, you must type\neverything after the prompt, when the prompt appears; lin...",
  "text": null,
  "html": null,
  "raw": null,
  "links": null,
  "linkCount": 27,
  "wordCount": 3224,
  "markdownChars": 19341,
  "truncated": true,
  "robotsTxt": "allowed",
  "responseTimeMs": 28,
  "contentHash": "0e806a20ed1fe241",
  "changeType": null,
  "fetchedAt": "2026-11-26T23:09:44.227956Z"
}
```

## Python
```python
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
```

## JavaScript
```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('loamy_barista/url-to-markdown').call({
  urls: ['https://docs.python.org/3/tutorial/introduction.html'],
  formats: ['markdown'],
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items[0].markdown.slice(0, 200));
```

More scripts: [examples/](examples/) (`run.py`, `run.js`, `monitor_docs.py`, `chunk_for_rag.py`).

## Input (main fields)
- `urls`: public pages to convert. `url` (single string) and `startUrls` are also accepted, so inputs written for
  apify/web-fetch work unchanged.
- `formats`: any of markdown, text, html, links, raw.
- `onlyMainContent`: drop navigation, footers and banners (on by default).
- `maxCharsPerPage`: cut each field to fit a context window; `truncated` shows when it applied.
- `onlyNew` and `monitorId`: monitor mode, only new or changed pages on each scheduled run.
- `maxItems`: spend cap.

## Pricing example
Pay per event: $0.001 per page fetched, plus a small start fee of $0.00005 per GB of memory. Failed, blocked and
unchanged pages are free. The run above (3 pages) cost $0.0003 in platform usage; 1,000 pages cost about $1.00.

## Use from AI agents
The Actor works through Apify's hosted MCP server (https://mcp.apify.com). Minimal call:
`{"urls": ["https://example.com/docs"], "maxCharsPerPage": 20000}`.

## Notes
Fetches public pages only, with no login and no browser. Pages that need JavaScript to render return what the server
sends. Each row reports `robotsTxt` so you can see the page's robots.txt status.

## Related
- [Website Tech Stack Detector](https://apify.com/loamy_barista/website-tech-stack-detector)
- [PDF Text Extractor](https://apify.com/loamy_barista/pdf-text-extractor)
- [Shopify Products JSON Scraper](https://apify.com/loamy_barista/shopify-store-products)

If this saved you time, a short review on the Store page helps others find it.
