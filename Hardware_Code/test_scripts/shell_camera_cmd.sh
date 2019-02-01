#!/bin/sh

echo Input name of jpg to save / overwrite:
read filename

// the time is 1500 milliseconds or 1.5 seconds
raspistill -t 1500 -o test.jpg
