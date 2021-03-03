import json
import sys
import random

if len(sys.argv) != 2:
	print("Usage: {} <exp>".format(sys.argv[0]))
	exit(1)

try:
	exp = int(sys.argv[1])
except ValueError:
	print("Usage: {} <exp>".format(sys.argv[0]))
	exit(1)

count = 10**exp

LON_MIN = 48
LON_MAX = 51
LAT_MIN = 12
LAT_MAX = 19
NAME_MIN = 3
NAME_MAX = 20


with open("random_geojson_{}.geojson".format(exp),"w") as f:
	f.write('{"type": "FeatureCollection", "features":[\n')
	for i in range(count):
		if i%10000 == 0:
			print(f"{i:_} of {count:_}")
		pos_lon = random.uniform(LON_MIN,LON_MAX)
		pos_lat = random.uniform(LAT_MIN,LAT_MAX)
		name = "".join([ chr(random.randint(ord('a'),ord('z'))) for _ in range(random.randint(NAME_MIN, NAME_MAX))])
		feat = {"type": "Feature", 
			"geometry": {"type": "Point", "coordinates": [pos_lat,pos_lon]},
			"properties": {
				"id": i,
				"name": name}
			}
		json.dump(feat,f)
		if i != count-1:
			f.write(",\n")
	f.write("]}")
