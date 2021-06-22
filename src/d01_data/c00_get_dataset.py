import os
from c01_raw_to_preprocessed import clean_raw_data
from c02_preprocessed_to_processed import process_data
from c03_final_datasets import make_datasets

def main():
    print('00 - Cleaning started')

    # ? raw to preprocessed
    clean_raw_data()
    print('01 - dataset preprocessed created')
    
    # ? preprocessed to processed
    process_data()
    print('02 - dataset processed created')

    # ? processed to datasets
    make_datasets()
    print('03 - datasets made')


if __name__ == "__main__":
    main()