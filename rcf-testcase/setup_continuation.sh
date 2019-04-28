#!/bin/bash
for i in output-*spinup*
do
j=`echo $i | sed 's/spinup/continue/g'`
echo $i $j
mkdir $j
cp $i/restart* $j
done
