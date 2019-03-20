#!/bin/bash
# This script handles saving images on the device and removal of bad images.

imagefile="$(date).jpg"

cp /MOTUSCaptures/$imagefile /SECURITYIMAGE.jpg
rm SECURITYIMAGE.jpg

# Return to Primary Program