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

print "letöltés: ", url


print "fájlméret lekérdezése..."

response = urllib.urlopen(url)

if response.getcode() != 200:
    print "nem található"
    exit(1)

meta = response.info()

size = meta.getheaders("Content-Length")[0]

print "méret = ", size


# méret beolvasás fájlból
psize = 0
if os.path.isfile(datafilename):
    with open(datafilename, "r") as thefile:
        psize = thefile.read()

print "tárolt méret = ", psize

if size != psize:
    urllib.urlretrieve(url, zipfilename)

    print "letöltve"

    print "kicsomagolás..."

    zip_ref = zipfile.ZipFile(zipfilename, 'r')
    zip_ref.extractall('.')
    zip_ref.close()

    #fájl méret mentése fájlba
    thefile = open(datafilename, "w")
    thefile.write(size)

    # letöltött fájl törlése
    os.remove(zipfilename)

else:
    print "nincs válzotás"

print "indítás..."

# létezik az exe fájl?
if not os.path.isfile(exefilename):
    print "nem találom a fájlt: ", exefilename
    exit(0)

# paraméter lekérdezés
arg = ""
if len(sys.argv) > 1:
    arg = sys.argv[1]
    print "arg = ", arg

print "platform = ", platform.system()

if platform.system() == 'Linux':

    # wine telepítésének ellenőrzése

    wineerror = subprocess.call(["which", "wine"])

    if wineerror == 0:
        # telepítve van
        subprocess.call(["wine", exefilename, arg])
        exit(0)
    else:
        print "nincs telepítve a wine"
        print "Ubuntu vagy Debian Linuxon használd a 'sudo apt install wine' parancsot"
        exit(2)

elif platform.system() == 'Windows':
    subprocess.call([exefilename, arg])
    exit(0)

else:
    print "nem támogatott operációs rendszer"
    exit(3)
