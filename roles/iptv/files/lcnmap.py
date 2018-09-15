#!/usr/bin/env python3
import xml.etree.ElementTree as xml
import json
import argparse

parser = argparse.ArgumentParser(prog="lcnmap", description="Small program to add an <LCN> tag to an IPTV EPG XML file so Plex correctly parses the channel numbers. Uses map.json to map the channels")

#-i INPUT_XMLTV_FILE -o OUTPUT_XMLTV_FILE
parser.add_argument("-i", "--input", dest = "input", metavar="input.xml", help="source XMLTV EPG file", required=True)
parser.add_argument("-o", "--output", dest = "output", metavar="output.xml", help="output XMLTV EPG file with mapped channels", required=True)
parser.add_argument("-m", "--map", dest = "map", metavar="map.json", help="map file of TVG-ID channel names and their mapped channel numbers", required=True)

args = parser.parse_args()

# Load our EPG XML
tree = xml.parse(args.input)
xmlRoot = tree.getroot()

# Load our channel map json
with open(args.map) as f:
	map = json.load(f)
	
# Initialize counter for non-mapped channels
c=700

for child in xmlRoot:
    for channel in child.iter("channel"):
    	id = channel.attrib.get('id')
    	if id in map:
    		lcn = xml.SubElement(channel, "lcn")
    		lcn.text = "{0}".format(map[id])
    	else:
    		c += 1
    		lcn = xml.SubElement(channel, "lcn")
    		lcn.text = "{0}".format(c)    		
        
# Write out our new epg
tree.write(args.output)