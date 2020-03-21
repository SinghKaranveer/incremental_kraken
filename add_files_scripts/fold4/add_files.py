#!/usr/local/bin/python3

import sys
import subprocess
import os

if len(sys.argv) < 3:
    print("Please enter DB path followed by the requested years")
    sys.exit()

years = sys.argv[2:]
db = sys.argv[1]
kraken_build = "/mnt/HA/groups/rosenclassGrp/Kraken_tutorial/kraken2/kraken2-build"
for year in years:
    path = "/scratch/djd378/training_data/" + year
    for subdir, dirs, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if 'fold5' not in subdir:
                if ext == '.fna':
                    subprocess.run([kraken_build, "--add-to-library", os.path.join(subdir, file), "--db", db, "--no-masking"])
