import csv
import sys
import json
# command line argument
number = int(sys.argv[1])
csvfile = open('erosnow.csv', 'r')
jsonfile = open('file.json', 'w')
reader = csv.DictReader( csvfile, delimiter=',')
out = json.dumps( [ row for row in reader ] , indent=4 )
o = json.loads(out)  
jsonfile.write(out)
for i in range(number):
	print(o[i])
