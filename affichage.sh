#!/bin/bash

sqlite3 maBD.db -header -column "select * from info;"
