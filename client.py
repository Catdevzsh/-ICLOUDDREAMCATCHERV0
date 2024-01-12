#!/bin/bash

# Clear the screen
clear

# Set colors
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Print the BIOS-like startup screen
echo -e "${GREEN}C Flames LABS 20XX BIOS v1.0.0"
echo "*******************************"
echo "ICLOUD DREAM CATCHER Initializing..."
echo "*******************************"
sleep 2

# Path to your iCloud Drive
iCloudDrive=~/Library/Mobile\ Documents/com~apple~CloudDocs/

# Directory to link (example: Documents)
localDir=~/Documents

# Check if the local directory exists
if [ -d "$localDir" ]; then
    # Create a symbolic link
    echo "Linking $localDir to iCloud Drive..."
    ln -s "$iCloudDrive" "$localDir"
    echo "Linked $localDir to iCloud Drive"
else
    echo "Local directory $localDir does not exist. Link not created."
fi

echo -e "Operation completed.${NC}"

# Your additional script logic (if any) goes here

