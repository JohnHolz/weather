from modules.get_raw_data import clean_raw_data
from modules.process_data import process_data
import os

def main():
    clean_raw_data()
    print('dataset preprocessed created')
    process_data()
    print('dataset processed created')


if __name__ == "__main__":
    main()