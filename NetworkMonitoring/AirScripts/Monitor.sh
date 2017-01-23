#!/bin/bash
#Conner Jackson DARQ

echo "Starting Monitor Script"
echo "Input Network Interface you would like to use for monitoring:"
#airmon-ng will list wireless interfaces
airmon-ng

read Interface

echo "You have chosen Interface: $Interface"
#if there is already a monitor interface you can use airmon-ng stop mon0
#may need to restart network manager
echo "Creating Monitor Interface with $Interface"
airmonOutput="$(airmon-ng start $Interface)"
echo "${airmonOutput}"
