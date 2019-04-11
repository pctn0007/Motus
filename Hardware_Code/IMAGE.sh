#!/bin/bash
# This script handles saving images on the device and removal of bad images.

imagefile=`date '+%d/%m/%Y_%H:%M:%S'`

cp SECURITYIMAGE.jpg MOTUSCaptures
rm SECURITYIMAGE.jpg

# Return to Primary Program