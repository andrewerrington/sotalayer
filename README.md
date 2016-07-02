# sotalayer
Make a POI layer for OsmAnd using SOTA summit data.

You will need Python 3, and a copy of the SOTA summit data, which can
be downloaded from here:

http://www.sotadata.org.uk/summitslist.csv

To run the program, specify the region you want to extract.  For
example:

sotalayer.py G/

This will extract all the England summits.  The program does a very
simple character match to the beginning of the SOTA ref., so 'G' will
match England ('G'), Isle of Man ('GD'), Northern Ireland ('GI'),
Scotland ('GM') and Wales (GW).  'G/' will match only England, and
'G/CE' will match Central England, and so on.

The output is an OSM XML file, which is written to 'sotalayer.osm'.
If this file exists it will be overwritten, so please move or rename
it after each extraction.

To make the OsmAnd POI layer you will need OsmAnd Map Creator, which
is described here:

http://wiki.openstreetmap.org/wiki/OsmAndMapCreator

Run OsmAnd Map Creator and select only 'Build POI index'. Choose 'Create
.obf file from osm file...' from the 'File' menu and open the .osm
file you created above. OsmAnd Map Creator will make a file called
'Sotalayer.obf' (or similar, if you renamed the .osm file). Copy this
file to the OsmAnd 'files' directory on your phone.
