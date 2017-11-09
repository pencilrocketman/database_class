#!/bin/bash
touch shots.csv 
while read yyy
do
python sc_from_nba.py $yyy 
cat add.csv >> shots.csv
done < ID.txt
