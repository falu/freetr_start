# FreeTR Start

Segéd alkalmazás a [FreeTR](http://freetr.hu/) programhoz.

A **freetr_start** ellenőrzi, hogy van-e könyvtárban lévőnél újabb kiadás a FreeTR honlapján. Ha igen, akkor indítás előtt automatikusan letölti.

## Használat

A program használatához [python](https://www.python.org/) 2.7 szükséges.

A program Linuxon is használható, ilyenkor a [wine](https://www.winehq.org/) segítségével futtatja a FreeTR-t.

Telepítést nem igényel, egyszerűen csak be kell másolni a letöltött FreeTR mappájába.

Linuxon futtathatóvá kell tenni:

`chmod +x freetr_start.py`

A program a FreeTR indításakor átadja a FreeTR számára az argumentumként kapott első fájlnevet, így megnyitható vele egy tetszőleges *.ftr fájl.
   