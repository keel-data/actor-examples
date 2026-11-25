// Pull remote engineering jobs from five boards and print them.
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('loamy_barista/remote-jobs-aggregator').call({
  keywords: ['engineer'],
  maxAgeDays: 14,
  maxItems: 40,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const job of items) console.log(job.source, '|', job.company, '|', job.title, '|', job.applyUrl);
