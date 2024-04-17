import argparse
import logging
from file_ops import read_sfo_data
from dir_ops import organize_games

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    parser = argparse.ArgumentParser(description="Organize game folders based on game titles extracted from param.sfo and include SFO data in a text file.")
    parser.add_argument('library_root', type=str, help='Path to the root directory of the game library')
    args = parser.parse_args()
    
    organize_games(args.library_root, read_sfo_data)

if __name__ == '__main__':
    main()

