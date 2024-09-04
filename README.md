# Santa Cruz Mountain Biking

## Goals
In Santa Cruz, most mountain bike trails aren't public and therefore data on ridership is not available. This project is my opportunity to get more experience with APIs and GIS while satisfying my own curiosity. Additionally, I might find some interesting patterns in the process!

## Skills/Tools Used

- Strava API through Python

## Steps
1. Get my [list of trails](datasets/trail_list.csv)
   - Done manually with segment search, mostly based on personal knowledge of the trails.
2. For each trail in the list query the API for segment stats
   - Count of unique athletes is saved to [athlete_count.csv](datasets/athlete_count.csv)
   - Ridership volume by ebikers is saved to [ebike_attempts.csv](datasets/ebike_attempts.csv)
   - Ridership volume by pedal bikes is saved to [pedal_attempts.csv](datasets/pedal_attempts.csv)
3. I'm still working on data collection, but the next steps are to:
   - convert these all-time counts into day-to-day change
   - map the data in ArcGIS

