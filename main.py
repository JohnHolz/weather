from modules.get_raw_data import clean_raw_data
from modules.process_data import process_data

def main():
    clean_raw_data()
    process_data()

if __name__ == "__main__":
    main()