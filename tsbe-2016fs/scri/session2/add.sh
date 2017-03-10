#!/bin/bash

read -p "Zahl 1: " n1
read -p "Zahl 2: " n2

summe=$(($n1 + $n2))

echo "Die Summe der Zahlen $n1 und $n2 ist $summe"
