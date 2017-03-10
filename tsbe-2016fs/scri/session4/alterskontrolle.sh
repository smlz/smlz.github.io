#!/bin/bash

read -p "Wie alt sind sie? " alter
read -p "Was möchten sie kaufen? (1: Kaugummi, 2: Zigaretten) " wahl

if [ "$alter" -lt 18 ] && [ "$wahl" = 2 ]; then
    echo "Nicht OK"
else
    echo "OK"
fi
