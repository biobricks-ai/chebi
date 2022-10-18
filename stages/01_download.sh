#!/usr/bin/env bash

# Script to download files

# Get local [ath]
localpath=$(pwd)
echo "Local path: $localpath"

# Create the list directory to save list of remote files and directories
downloadpath="$localpath/download"
echo "Download path: $downloadpath"
mkdir -p $downloadpath
cd $downloadpath;

# Define the FTP base address
ftplink="https://ftp.ebi.ac.uk/pub/databases/chebi/SDF/ChEBI_complete.sdf.gz"

# Create the download directory
downloadpath="$localpath/download"
echo "Download path: $downloadpath"
mkdir -p "$downloadpath"
cd $downloadpath;

# Download file
wget -P $downloadpath $ftplink

echo "Download done."
