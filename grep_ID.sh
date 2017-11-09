#!/bin/bash
while read yyy
do
  grep -o '[0-9]*' > ID.txt
done < origin.csv
