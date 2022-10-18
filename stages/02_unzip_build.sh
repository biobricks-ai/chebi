#!/usr/bin/env bash

# Script to unzip files

# Get local path
localpath=$(pwd)
echo "Local path: $localpath"

# Set download path
downloadpath="$localpath/download"
echo "Download path: $downloadpath"

# move in the download folder
cd $downloadpath

# Set list path
gzfile=(*)
echo "gz path: $gzfile"

# Unzip file
gunzip $downloadpath/$gzfile
echo "Unzip done"
cd ..

# convert to parquet
python sdf2parquet.py $downloadpath/ ./brick/chebi.parquet