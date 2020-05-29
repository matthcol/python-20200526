# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:43:33 2020

@author: Matthias
"""

from pathlib import Path
import sys

def listingDir(myDir):
    if myDir.is_dir():
        for f in myDir.iterdir():
            print(f.name, ':', f.stat().st_size//1024, 'Ko')

# traitement des arguments en ligne de commande
if len(sys.argv)==1:
    listingDir(Path('.'))
elif len(sys.argv)==2:
    listingDir(Path(sys.argv[1]))
else:
    for dirName in sys.argv[1:]:
        myDir = Path(dirName)
        print()
        print("Contenu de ", myDir)
        print("-----------")
        listingDir(myDir)
        
        
