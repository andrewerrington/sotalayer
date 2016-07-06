#!/usr/bin/env python3

# Python program to extract country-specific SOTA peaks from "summitslist.csv"
# and write out an OSM file, "sotapoi_XX.osm", where XX is the region that
# was specified on the command line.  This .osm file can be processed by
# OsmAnd Map Creator to produce an .obf file for use with OsmAnd, showing
# SOTA peaks as POIs.

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('region',
                    nargs='?',
                    help='SOTA region to extract, e.g. G/ or G/CE')

args = parser.parse_args()

if args.region is None:
    print("Region must be specified.")
    sys.exit()

key = args.region       # First part of SOTA ref. to match (can be as long as you like)
print("Extracting '%s'."%key)

# Output filename is sotapoi_XX.osm, but we can't have a slash in the filename
outfile = "sotapoi_%s.osm"%key.replace('/','') 

id = 0     # Internal counter for node IDs

with open(outfile, 'w', encoding='utf-8') as o:

    o.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    o.write("<osm version='0.5' generator='sotalayer.py'>\n")

    with open("summitslist.csv", encoding='utf-8') as f:
        for line in f:
            if line[:len(key)] == key:
                
                id -= 1

                fields = line.split(',')

                # Name is "SOTA ref. Name [Points]"
                name = "%s %s [%s]"%(fields[0], fields[3], fields[10])

                # Activations go in the note.
                activations = fields[14] + ' activation' + ('.' if int(fields[14])==1 else 's.')
                if int(fields[14]) > 0:
                    activations += ' Last ' + fields[16] + ' (' + fields[15] + ')'

		# URL on SOTA's webpage
                website = "http://www.sota.org.uk/Summit/%s"%fields[0]
                    
                o.write('  <node id="%s" visible="true" lat="%s" lon="%s">\n'%(id,fields[9],fields[8]))
                o.write('    <tag k="name" v="%s"/>\n'%(name))
                o.write('    <tag k="note" v="%s"/>\n'%(activations))
                o.write('    <tag k="website" v="%s"/>\n'%(website))
                o.write('    <tag k="ele" v="%s"/>\n'%(fields[4]))
                o.write('    <tag k="natural" v="peak"/>\n')
                o.write('  </node>\n')

    o.write("</osm>\n")

print("%s POIs extracted."%abs(id))
