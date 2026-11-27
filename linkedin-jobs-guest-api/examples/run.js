import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('loamy_barista/linkedin-jobs-guest-api').call({
  keywords: 'python developer',
  location: 'Germany',
  datePosted: 'pastWeek',
  workplaceType: ['remote', 'hybrid'],
  maxItems: 15,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const job of items) console.log(job.postedDate, job.title, '|', job.companyName);
