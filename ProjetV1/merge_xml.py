# Les importations --------------
try:
    import os
except ImportError:
    "Please install the os library : type ->pip install os<-"
try:
    import requests
except ImportError:
    "Please install the requests library : type ->pip install requests<-"
print("If you haven't install requests library yet, please install it : type ->pip install requests<-")
print("/!\ WARNING : This will only add the selected filesnames ! If they are already in the file they will be duplicated")
print("What OFFLINE files do you want to add ? (enter the paths separated by a \",\") :")
filenames = input(str("->")).split(",")
hasOfflineFiles = True
if filenames[0] == "":
    hasOfflineFiles = False
print("What ONLINE files do you want to add ? (enter the urls separated by a \",\") :")
online = input(str("->")).split(",")
hasOnlineFiles = True
if online[0] == "":
    hasOnlineFiles = False

# Les entrées ------------------
if not(hasOfflineFiles):
    filenames = []
if hasOnlineFiles:
    for onlineFile in online:
        response = requests.get(onlineFile)
        with open(("online.xml"), 'wb') as xmlTVfile:
            xmlTVfile.write(response.content)
    filenames.extend(["online.xml"])

# filenames = ['guide.xml', 'guide_1.xml', 'xmltvfr.xml',
#             'special_qc.xml', 'xmltv-complet.xml']

# Les sorties ----------------
# file = 'merged.xml'
file = 'mergedTest.xml'

# Le code --------------------
outfile = file

if (hasOnlineFiles or hasOfflineFiles):
    for fname in filenames:
        print(filenames)
        with open(file, 'a', encoding="utf8") as outfile:
            with open(fname, encoding="utf8") as infile:
                for line in infile:
                    outfile.write(line)

# On nettoie les fichiers en trop --
os.remove("online.xml")
