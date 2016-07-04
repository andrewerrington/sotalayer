# sotalayer
Make a POI layer for OsmAnd using SOTA summit data.

There are two versions of this software:

###sotalayer.py  
makes a .osm XML file which can be processed by OsmAnd Map Creator
to produce a .obf file.

###sotagpx.py
makes a favourites.gpx file which can be directly read by OsmAnd

In either case, the file contains POI nodes for SOTA summits, which
can be viewed on the OsmAnd mapping screen.

##Requirements
You will need Python 3, and a copy of the SOTA summit data, which can
be downloaded from [here](http://www.sotadata.org.uk/summitslist.csv) (13Mb CSV file)

##Using the program
To run the program, specify the region you want to extract.  For
example:

`sotalayer.py G/`

or

`sotagpx.py G/`

This will extract all the England summits.  The program does a very
simple character match to the beginning of the SOTA ref., so 'G' will
match England ('G'), Isle of Man ('GD'), Northern Ireland ('GI'),
Scotland ('GM') and Wales (GW).  'G/' will match only England, and
'G/CE' will match Central England, and so on.

In the case of `sotalayer.py` the output is an OSM XML file, which is
written to _sotalayer.osm_. If this file exists it will be overwritten,
so please move or rename it after each extraction.

In the case of `sotagpx.py` the output is an GPX XML file, which is
written to _favourites.gpx_. If this file exists it will be overwritten,
so please move or rename it after each extraction.

##Further processing
No further processing is needed for _favourites.gpx_, however to make the
OsmAnd POI layer from _sotalayer.osm_ you will need OsmAnd Map Creator,
which is described [here](http://wiki.openstreetmap.org/wiki/OsmAndMapCreator)

Run OsmAnd Map Creator and select only _Build POI index_. Choose _Create
.obf file from osm file..._ from the _File_ menu and open the .osm
file you created above. OsmAnd Map Creator will make a file called
_Sotalayer.obf_ (or similar, if you renamed the .osm file). Copy this
file to the OsmAnd 'files' directory on your phone.
