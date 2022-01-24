import os
import re
import

file = 'merged.xml'

link = "https://xmltvfr.fr/xmltv/xmltv.xml"
url_response = urllib.request.urlopen(link)
url_contents = url_response.read()

filenames = ['guide.xml', 'guide_1.xml', url_contents,
             'special_qc.xml', 'xmltv-complet.xml']

outputfile = file

for fname in filenames:
    with open(file, 'a', encoding="utf8") as outfile:
        with open(fname, encoding="utf8") as infile:
            for line in infile:
                outfile.write(line)
