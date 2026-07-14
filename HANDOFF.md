# Van Dispatch Board — handoff

This is a complete, working copy of the Van Dispatch Board. It's yours to change however you like — it is fully independent of the original. Nothing you do here affects the other copy, and nothing they do affects yours.

## To keep building it with Claude

Start a new conversation on your own Claude account, **upload `index.html`**, and say something like:

> This is a single-file HTML app (a van dispatch board for rail crew transport). All the HTML, CSS, and JavaScript are in this one file. Read it, then help me change [whatever you want]. Keep it a single self-contained file with no frameworks.

Claude can read the whole file and edit it directly. A few things worth telling it up front, because they're easy to break:

- **Keep it one file.** No build step, no npm, no frameworks. Open the file, it runs.
- **The schedule lives in `BUILTIN_JOBS`**, near the top of the `<script>` — one job per line. Each job has a `days` pattern (`Mon-Fri`, `Sat-Sun`, `Fri`, etc.) and a list of van `moves` with start/end times in minutes past midnight.
- **`ALIAS`** maps the railway's short location codes (`WB`, `WRMF`) to display names (`WILLOWBROOK`, `WHITBY RAIL`).
- **The scheduling model** simulates each day independently with maximum van reuse: a van that drops a crew is reused for the next trip leaving that location. `locNeeds()` figures out the fewest vans that must start at each location, by netting arrivals from other crews against departures.

## Running it

Open `index.html` in any browser. That's it. To put it online, upload to GitHub and turn on Pages (Settings → Pages → Deploy from branch → main / root).

## Loading a new job package

The **⟳ Job package** button in the header reads a job-book PDF in the browser and rebuilds the schedule from it. It understands these day patterns: `Mon-Fri`, `Mon-Thu`, `Mon-Wed`, `Mon-Tue`, `Wed-Fri`, `Thu-Fri`, `Fri`, `Sat`, `Sun`, `Sat-Sun`. **Reset** puts the built-in schedule back.

## Where your data is saved

Right now: **only in your own browser.** The original's cloud database has been disconnected, so your fleet, staging, and dispatch changes are private to you and stored locally.

If you later want your data to sync across devices, create a free [Supabase](https://supabase.com) project and paste your own URL and publishable key into the two blank constants near the top of the `<script>` (search for `SUPA_URL`). Claude can walk you through it, including creating the table.

## What's in the app

| Tab | Purpose |
|---|---|
| **Home** | Alerts: where a van is needed and by when, returns due, service due, out-of-service vans |
| **Positions** | Live board: departures within the hour, vans on the road, vans by location |
| **Daily Schedule** | Every van move for a day; add extra jobs (Route / Hotel / DOB Van / Shuttle Van) |
| **Fleet** | Fleet size, van status, winter tires, service dates, symbol legend |
| **Spare Van Request** | Find a spare van, see what pulling it costs, track its return |
| **Maintenance** | Service history |
| **Locations** | Per-location staging plan |
