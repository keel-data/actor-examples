import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('loamy_barista/url-to-markdown').call({
  urls: ['https://docs.python.org/3/tutorial/introduction.html'],
  formats: ['markdown'],
  maxCharsPerPage: 20000,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const page of items) console.log(page.title, page.wordCount, 'words');
