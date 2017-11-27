#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib
import zipfile
import platform
import subprocess
import os.path
import sys


baseurl = "http://freetr.hu/download-freetr/"
zipfilename = "freetr-project-2016.zip"
exefilename = "FreeTR.exe"
datafilename = "freetr_start.data"

url = baseurl + zipfilename

print u"ellenőrzés: ", url

print u"fájlméret lekérdezése..."

response = urllib.urlopen(url)

if response.getcode() != 200:
    print u"nem található"
    exit(1)

meta = response.info()

size = meta.getheaders("Content-Length")[0]

print u"méret = ", size


# méret beolvasás fájlból
psize = 0
if os.path.isfile(datafilename):
    with open(datafilename, "r") as thefile:
        psize = thefile.read()

print u"tárolt méret = ", psize

if size != psize:
    urllib.urlretrieve(url, zipfilename)

    print u"letöltve"

    print u"kicsomagolás..."

    zip_ref = zipfile.ZipFile(zipfilename, 'r')
    zip_ref.extractall('.')
    zip_ref.close()

    #fájl méret mentése fájlba
    thefile = open(datafilename, "w")
    thefile.write(size)

    # letöltött fájl törlése
    os.remove(zipfilename)

else:
    print u"nincs válzotás"

print u"indítás..."

# létezik az exe fájl?
if not os.path.isfile(exefilename):
    print u"nem találom a fájlt: ", exefilename
    exit(0)

# paraméter lekérdezés
arg = ""
if len(sys.argv) > 1:
    arg = sys.argv[1]
    print u"arg = ", arg

print u"platform = ", platform.system()

if platform.system() == 'Linux':

    # wine telepítésének ellenőrzése

    wineerror = subprocess.call(["which", "wine"])

    if wineerror == 0:
        # telepítve van
        subprocess.call(["wine", exefilename, arg])
        exit(0)
    else:
        print u"nincs telepítve a wine"
        print u"Ubuntu vagy Debian Linuxon használd a 'sudo apt install wine' parancsot"
        exit(2)

elif platform.system() == 'Windows':
    subprocess.call([exefilename, arg])
    exit(0)

else:
    print u"nem támogatott operációs rendszer"
    exit(3)
