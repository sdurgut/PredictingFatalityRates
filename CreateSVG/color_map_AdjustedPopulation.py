import csv
from BeautifulSoup import BeautifulSoup

data = {}
# reader = csv.reader(open('FatalityActualData_2011_2015.csv'), delimiter=",")
reader = csv.reader(open('FatalityPredictionData_2011_2015.csv'), delimiter=",")
for row in reader:
	# print row
	tmp = ''
	if len(row[0])<5:
		tmp = "0"+row[0]
	else: tmp = row[0]
	if row[3]!= "" : data[tmp] = float(row[3].strip())


# Load the SVG map
svg = open('USA_Counties_with_FIPS_and_names.svg', 'r').read()

# Load into Beautiful Soup
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])
# Find counties
paths = soup.findAll('path')

# Map colors
colors = ["#f7f4f9", "#e7e1ef", "#d4b9da", "#c994c7", "#df65b0", "#e7298a", "#ce1256", "#980043", "#67001f"]


# County style
path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'



# Color the counties based on unemployment rate
for p in paths:
	 
	if p['id'] not in ["State_Lines", "separator"]:
		# pass
		try:
			rate = data[p['id']]
		except:
			continue
			 
		if rate > 40:
			color_class = 8
		elif rate > 20:
			color_class = 7
		elif rate > 10:
			color_class = 6
		elif rate > 8:
			color_class = 5
		elif rate > 6:
			color_class = 4
		elif rate > 4:
			color_class = 3
		elif rate > 2:
			color_class = 2
		elif rate > 1:
			color_class = 1
		else:
			color_class = 0
 
		color = colors[color_class]
		p['style'] = path_style + color



# Output map
print soup.prettify()

