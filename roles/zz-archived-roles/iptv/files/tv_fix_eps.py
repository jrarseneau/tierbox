#!/usr/bin/env python3
import re
import argparse

parser = argparse.ArgumentParser(prog="tv_fix_eps", description="Small program which parses an XMLTV file and converts S#E# episode numbers into valid xmltv_ns episode numbers (example: \"S1E10\" becomes \"0 . 9 . \")")

#-i INPUT_XMLTV_FILE -o OUTPUT_XMLTV_FILE
parser.add_argument("-i", "--input", dest = "input", metavar="input.xml", help="source XMLTV file", required=True)
parser.add_argument("-o", "--output", dest = "output", metavar="output.xml", help="output XMLTV file with fixed episode numbers", required=True)

args = parser.parse_args()

with open(args.input) as in_file, open(args.output, 'w') as out_file:
	for line in in_file:
		m = re.search("^(\s+)<episode-num system=\"xmltv_ns\">S([0-9]+)E([0-9]+)</episode-num>", line)
		
		if m:
			season = int(m.group(2))
			episode = int(m.group(3))
			line1 = "%s<episode-num system=\"onscreen\">S%dE%d</episode-num>" % (m.group(1), season, episode)
			line2 = "%s<episode-num system=\"xmltv_ns\">%d . %d . </episode-num>" % (m.group(1), season - 1, episode - 1)
			out_file.write("%s\n%s\n" % (line1, line2))
		else:
			out_file.write("%s" % line)
