# Van Dispatch Board

Crew-transport van scheduling board for CN rail crews. Single-file HTML app — no build step, no frameworks, no dependencies.

Schedule effective **July 5, 2026** (263 job variants, 201 van moves).

## Run it

### Streamlit app

```bash
pip install -r requirements.txt
streamlit run app.py
```

The Streamlit app wraps the original single-file board so the dispatch UI still runs in the browser, but it can now be launched and hosted like a normal Streamlit project.

### Original static HTML

You can still open `index.html` directly in a browser. To host the static version on GitHub Pages: push this repo, then **Settings → Pages → Deploy from branch → main / root**. It'll be live at `https://<user>.github.io/<repo>/`.

## Tabs

| Tab | What it does |
|---|---|
| **Home** | Alerts only: where a van is needed and by when, returns due, service due, out-of-service vans |
| **Positions** | Live board — clock, departures within the hour, vans on the road (moving icon on a start→finish line), and vans by location |
| **Daily Schedule** | Every van move for the selected day, plus manually added extra jobs (Route / Hotel / DOB Van / Shuttle Van) |
| **Fleet** | Fleet size, per-van status, winter tires, service dates, symbol legend |
| **Spare Van Request** | Find a spare van, see what it costs the origin, accept the move and track its return |
| **Maintenance** | Service history log |
| **Locations** | Per-location staging plan and time scrubber |

## How the scheduling model works

Each day is simulated independently, with **maximum reuse**: a van that drops a crew is reused for the next trip departing that location. For each location it nets *arrivals from other crews* against *departures* over the day, and only asks you to pre-stage the leftover peak shortfall — so a location is allowed to run thin whenever a van is due to arrive.

Minimum fleet by day:

| Day | Vans |
|---|---|
| Mon–Wed | 42 |
| Thu | 43 |
| Fri | 47 |
| Sat | 15 |
| Sun | 15 |

Friday is the binding constraint: a Willowbrook outbound wave around 15:35 means ~11–12 vans must start the day there. Assumes vans are positioned overnight into their start-of-day locations.

## Loading a new job package

**⟳ Job package** in the header → pick the PDF. It parses in-browser (pdf.js) and previews the counts before you apply. **Reset** restores the built-in schedule.

The parser reads van moves from labeled job blocks, handles multi-van lines (`2 VANS`), and knows these day patterns: `Mon-Fri`, `Mon-Thu`, `Mon-Wed`, `Mon-Tue`, `Wed-Fri`, `Thu-Fri`, `Fri`, `Sat`, `Sun`, `Sat-Sun`.

## Persistence

State (fleet, staging, manual dispatches, extra jobs) is saved **in your own browser only**. No backend is configured in this copy.

To sync across devices, create a free Supabase project and fill in `SUPA_URL` and `SUPA_KEY` near the top of the `<script>`. Until then the app runs fully offline and your data stays local.

## Editing

All CSS, markup, and JS live in `index.html`. The schedule itself is the `BUILTIN_JOBS` array near the top of the `<script>`; `JOBSVER` below it version-stamps the baseline so a new schedule supersedes anything previously saved.
