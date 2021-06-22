# Weather forecast project

Project objective:


## Data

Historical data from: [Inmet historical weather data](https://portal.inmet.gov.br/dadoshistoricos)

Directory structure based on [hitchhikers-guide](https://github.com/dssg/hitchhikers-guide/tree/master/sources/curriculum/0_before_you_start/pipelines-and-project-workflow#models)

--- 
## Folder Structure
    ├── site:
    │
    ├── notebooks:
    │    ├── n01_data_cleaning
    │    ├── n02_eda
    │    └── n03_models
    │
    ├── services:
    │    └── database
    │    └── api
    │
    ├── data:
    │    ├── 01_raw
    │    ├── 02_preprocessed
    │    ├── 03_processed
    │    ├── 04_datasets
    │    ├── 05_models
    │    ├── 06_model_output
    │    └── 07_reporting
    │
    └── src:
         ├── d00_modules:
         ├── d01_data
         ├── d02_modeling
         ├── d03_model_evaluation
         ├── d04_reporting
         └── d05_collector

---
## Database Structure

    ├── cleaning
    │    ├── raw
    │    ├── preprocessed
    │    └── processed
    │
    ├── datasets:
    │    ├── metadata
    │    ├── dataset_0
    │    ├── dataset_1
    │    ├── dataset_2
    │    ├── dataset_3
    │    ├── dataset_4
    │    └── dataset_5
    │
    └── models:
         ├── models_metadata
         ├── stations
         └── forecast

Tables
- models:
  - name:string
  - type:string
  - dataset:string
  - info:string
  - time_granularity:array
  - parameters:json
  
- forecast
  - model:string
  - first_date:date
  - last_date:date
  - values:array
  - evaluation:json

- stations
  - first date
  - last date
  - lat
  - long
  - city

---
## Model Structure to be reproduces or analyzed

>       "model_0" :{
>          "info":"univariate",
>          "time_granularity":["00","03","06","09","12","15","18","21","24"],
>          "model_type":"lstm",
>          "dataset":"dataset_0",
>          "training_parameters":{
>             "epochs":100,
>             "n_steps_in": 42,
>             "n_steps_out": 42,
>             "first_layer": 16,
>             "hidden_layers": [32], 
>             "optimizer": "adam", 
>             "loss": "mse"
>          }
>       }