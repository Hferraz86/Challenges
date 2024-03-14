#!/bin/bash

# Script: Challenge 02
# Purpose: Append, Data & Time
# Why: Knowing the data & timing of events is fundamental

year= $(date +%y)

echo $year

month= $(month +%m)

echo $month

hours= $(date +%H)

echo $hours

echo "Reading this message at $hours on $month $year"
