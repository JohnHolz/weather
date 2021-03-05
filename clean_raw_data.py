from modules.transform_data.raw_to_preprocessed import clean_raw_data
from modules.transform_data.preprocessed_to_processed import process_data
from modules.transform_data.final_datasets import make_datasets
import os

def main():
    clean_raw_data()
    print('dataset preprocessed created')
    process_data()
    print('dataset processed created')
    make_datasets()
    print('datasets made')


if __name__ == "__main__":
    main()