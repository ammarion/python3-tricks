# coding: utf-8
import sys
from xml.etree.ElementTree import XML
import urllib.request
if len(sys.argv) != 3:
    raise SystemExit('Usage: bus.py route stopid')
route = sys.argv[1]
stopid = sys.argv[2]

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={}&route={}'.format(route, stopid))
u
data = u.read()
doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)
    
