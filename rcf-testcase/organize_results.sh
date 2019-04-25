#!/bin/bash
mkdir results
for file in output-*
do
echo $file
j=`echo $file | cut -d _ -f 4-5`
echo $j
cp $file/statistics results/statistics-$j
cp $file/depth_average.txt results/depth_average-$j.txt
done
