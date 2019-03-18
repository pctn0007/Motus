#!/bin/bash
# This script handles saving images on the device and removal of bad images.

imagefile="$(date).jpg"

cp /SECURITYIMAGE.jpg /MOTUSCaptures/$imagefile
rm SECURITYIMAGE.jpg

# Return to Primary Program