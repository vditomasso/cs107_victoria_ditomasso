#!/bin/bash
FILEVAR=$(find . -maxdepth 1 -type f)
for f in $FILEVAR
do
        echo $f $(cat $f | wc -l)
done