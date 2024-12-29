# Santa Cruz Mountain Biking

## Goals
In Santa Cruz, most mountain bike trails aren't public and therefore data on ridership is not available. This project is my attempt to gather and visualize data on which trails are the most popular, and get better knowledge of APIs and GIS tools in the process.

## Skills/Tools Used

- Strava API through Python
- ArcGIS Pro

## Steps
### API Data Collection
1. Get my [list of trails](datasets/trail_list.csv)
   - Done manually with segment search, mostly based on personal knowledge of the trails.
2. For each trail in the list query the API for segment stats
   - Count of unique athletes is saved to [athlete_count.csv](datasets/athlete_count.csv)
   - Ridership volume by ebikers is saved to [ebike_attempts.csv](datasets/ebike_attempts.csv)
   - Ridership volume by pedal bikes is saved to [pedal_attempts.csv](datasets/pedal_attempts.csv)
3. In order to be able to map each trail, the segment [polyline](https://developers.google.com/maps/documentation/utilities/polylinealgorithm) is decoded into a csv of XY coordinates.
   This is done for every trail in the list. This data can be found [here](trail_coords).
### Data Cleaning and Mapping
In order to import this data into ArcGIS, the process needs to be automated and the data has to be formatted such that the first XY point in each .csv file also has the attribute data for the trail. This is done by [gis_preprocess.py](code/gis_preprocess.py) to make a [modified list of trail coordinates](arcgis_ready_trails). From here, the trails can be loaded in using the model builder set up as shown below

![image](https://github.com/user-attachments/assets/1e2b6fbc-0cbc-4bc8-8f7a-83bb9ebec8f8)

From there, some of the trail paths need to be extended manually in the case that the official segment only covered a portion. Symbology and layouts are completed and shown below.

![Full](https://github.com/user-attachments/assets/42c11a6f-3dd3-4539-ae63-734b83059137)
![UCSC](https://github.com/user-attachments/assets/24dab4e5-8ccd-4007-a35f-b10fd4b160f8)
![Nisene](https://github.com/user-attachments/assets/ff97d121-46ec-46d4-9d59-5bfe0c1d0fb8)




