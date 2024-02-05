# Database

## Start postgresql using docker
        docker-compose up -d   

## Init DB
This step will be the longest in time. This step requires running *c01_raw_to_preprocessed.py* with success. Innmet give us the 01_raw data. We need to append the files and clean.

        python db_init.py

## Add metadata tables

This step will just add Stations and Datasets table.  
This tables will keep metadata and the information of what stations we are collecting data

        python add_metadata.py