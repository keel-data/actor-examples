// Call the Greenhouse / Lever / Ashby jobs Actor through the Apify API.
// Set APIFY_TOKEN in your environment first.  npm install apify-client
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('loamy_barista/ats-job-board-scraper').call({
  companies: ['greenhouse:airbnb', 'lever:palantir', 'ashby:ramp'],
  keywords: ['engineer'],
  maxItems: 50,
  descriptionMaxLength: 0,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const job of items) console.log(`${job.company} | ${job.title} | ${job.location} | ${job.applyUrl}`);
