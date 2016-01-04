import csv
import sys
import os
import json
# command line argument
number = int(sys.argv[1])
name=sys.argv[2]
outputfile=sys.argv[3]
csvfile = open(name, 'rU')
jsonfile = open(outputfile, 'w')
reader = csv.DictReader( csvfile, delimiter=',',dialect=csv.excel_tab)
out = json.dumps( [ row for row in reader ] , indent=4 )
o = json.loads(out)  
jsonfile.write(out)
for i in range(number):
	print(o[i])
	
