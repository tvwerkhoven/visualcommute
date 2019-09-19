# visualcommute

Visualise gpx tracks of commuting data to find optimal route & departure time

# Output

1. Time spent per segment, per weekday, per departure time as boxcar plot
2. Time spent on different routes for segments (e.g. in Veldhoven) as comparison of histograms
3. Visual plot of GPS tracks, color coding for time spent

# Todo

- Filter tracks on starting point close to ASML or Home. If this fails, try to recover duration/departure time from track name and tag track as 'partial'
- Get carpool state from GPS data directly

# Segments

waypoints_gps = {'ASML': (51.403432, 5.416201),
	'N2onramp': (51.419101, 5.429392),
	'A2Best': (51.501797, 5.419135),
	'Vught': (51.670612,5.319057),
	'Empel': (51.73085, 5.31379),
	'Maas': (51.73878, 5.30435),
	'Waal': (51.81856, 5.26004),
	'Deil': (51.85703, 5.22841),
	'Everdingen': (51.97013, 5.10905),
	'LunettenA12': (52.05557, 5.13639),
	'PapendorpA12' (),
	'Thuis1': (52, 5),
	'Thuis2': (52, 5)}

carpoolpts_gps = {'NieuwegeinA2zuid': (52.00207, 5.07815, 30),
	'HoutenA27': (52.02764, 5.12832, 30),
	'EverdingenA2': (51.94329, 5.1471, 30),
	'NovotelN2': (51.45882, 5.40704, 10)}

# Pseudo code

Loop over GPS tracks:
  Check if start at home or at work
  if not: mark and skip, else use
  construct vector of all x,y trackpoints (±3000 data points)
  compute difference of all trackpoints to each waypoint and carpoolpoint (14 points) --> 3000x14x2 matrix
  for waypoints: mark time at closest encouter
  for carpoolpoints: measure duration while in vicinity

# Sources

- https://everydayanalytics.ca/2012/11/the-hour-of-hell-of-every-morning-commute-analysis-april-to-october-2012.html
- https://matplotlib.org/basemap/users/examples.html
- https://stevendkay.wordpress.com/2010/01/14/creating-a-pinboard-map-of-geotagged-photos-in-a-flickr-pool/
- https://stevendkay.wordpress.com/tag/basemap/
