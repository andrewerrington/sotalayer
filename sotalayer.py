id = -1

print("<?xml version='1.0' encoding='UTF-8'?>")
print("<osm version='0.5' generator='sotalayer.py'>")

with open("summitslist.csv", encoding='utf-8') as f:
    for line in f:
        if line[:5] == 'HL/GN':  # Filter the association and region here

            fields = line.split(',')

            name = fields[0] + ' ' + fields[3] + ' [' + fields[10] + ']'
            
            activations = fields[14] + (' activation.' if int(fields[14])==1 else ' activations.')
            if int(fields[14]) > 0:
                activations += ' Last ' + fields[16] + ' (' + fields[15] + ')'
                
            print("<node id='%s' visible='true' lat='%s' lon='%s'>"%(id,fields[9],fields[8]))
            print("<tag k='name' v='%s'/>"%(name))
            print("<tag k='note' v='%s'/>"%(activations))
            print("<tag k='ele' v='%s'/>"%(fields[4]))
            print("<tag k='natural' v='peak'/>")
            print("</node>")

            id -= 1

print("</osm>")
