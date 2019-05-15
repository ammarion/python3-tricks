# coding: utf-8
get_ipython().run_line_magic('clear', '')
import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=1487&route=22')
u
data = u.read()
data
from xml.etree.ElementTree import XML
doc = XML(data)
doc
for pt in doc.findall('.//pt')
for pt in doc.findall('.//pt'):
    print(pt.text)
    
