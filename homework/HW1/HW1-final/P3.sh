#!/bin/bash
grep [0-9] apollo13.txt | wc -l > apollo_out.txt
grep --help | grep "\--count"
ls *.py | wc
find . -type f ! -perm -o=rw | wc -l
find . -maxdepth 1 ! -perm -o=rw | wc -l