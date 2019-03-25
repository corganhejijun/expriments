#!/bin/bash
num1=1
num2=1
count=0
while [ $1 -gt $count ]
do
    num3=`expr $num1 + $num2`
    num1=$num2
    num2=$num3
    echo $num3
    count=`expr $count + 1`
done
