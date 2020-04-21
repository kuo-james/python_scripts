# PCO2A Merger
The PCO2A Merger filters out data from pco2a.log files and consolidates the data into a single file named `data_only.log` Once the script is done reading the pco2a.log file, it will move the pco2a.log file into an archive folder.

### Setup
Create a folde with pco2a.log files.

Modify the variable `folder_path` to the folder that contains the pco2a.log files.

Run the script.

### Double Checking the data
The PCO2A Merger also creates a file named `merged_files.log` with the pco2a.log files merged together. This file is created for user to compare it with `data_only.log` as a final check.
