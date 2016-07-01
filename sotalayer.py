# Python program to extract country-specific SOTA peaks from "summitslist.csv"
# and write out an OSM file, "sotalayer.osm".  This can be processed by
# OsmAnd Map Creator to produce an .obf file for use with OsmAnd, showing
# SOTA peaks as POIs.

key = 'HL/'  # First part of SOTA ref. to match (can be as long as you like)

id = -1     # Internal counter for node IDs

with open('sotalayer.osm', 'w', encoding='utf-8') as o:

    o.write("<?xml version='1.0' encoding='UTF-8'?>")
    o.write("<osm version='0.5' generator='sotalayer.py'>")

    with open("summitslist.csv", encoding='utf-8') as f:
        for line in f:
            if line[:len(key)] == key:

                fields = line.split(',')

                # Name is "SOTA ref. Name [Points]"
                name = fields[0] + ' ' + fields[3] + ' [' + fields[10] + ']'

                # Activations go in the note.
                activations = fields[14] + ' activation' + ('.' if int(fields[14])==1 else 's.')
                if int(fields[14]) > 0:
                    activations += ' Last ' + fields[16] + ' (' + fields[15] + ')'
                    
                o.write('<node id="%s" visible="true" lat="%s" lon="%s">'%(id,fields[9],fields[8]))
                o.write('<tag k="name" v="%s"/>'%(name))
                o.write('<tag k="note" v="%s"/>'%(activations))
                o.write('<tag k="ele" v="%s"/>'%(fields[4]))
                o.write('<tag k="natural" v="peak"/>')
                o.write('</node>')

                id -= 1

    o.write("</osm>")



    
