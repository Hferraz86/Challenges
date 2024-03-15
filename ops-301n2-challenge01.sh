#!/bin/bash

# Script: Challenge 02
# Purpose: Append, Data & Time
# Why: Knowing the data & timing of events is fundamental

datetime=$(date +%Y-%m-%d\ %H:%M:%S)

echo "$datetime"

#Copy file to current directory

for file in /Users/hugoferraz/Desktop/Challenge01/*.sh; do

    cp "$file" "$file.$datetime"

    echo "$datetime" >> "$file.$datatime"

done

