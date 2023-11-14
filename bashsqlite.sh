#!/bin/bash
source varsondes.sh
python3 pythonsqlite.py
sqlite3 maBD.db "insert into 'info' values ('$util','$espace',$ram,$cpu,'$dateactuel')"
