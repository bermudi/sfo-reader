#!/usr/bin/python

import argparse
import os
import logging
from dir_ops import process_game_root, process_library_root, organize_games, generate_text_file

def parse_args():
    parser = argparse.ArgumentParser(description="Process and organize game directories.")
    parser.add_argument('--organize', action='store_true', help='Organize games into folders named after their STITLE.')
    parser.add_argument('--debug', action='store_true', help='Print debugg messages')
    parser.add_argument('--txt-paramsfo', action='store_true', help='Generate a text file with the contents of param.sfo at the game directory level.')
    parser.add_argument('path', nargs='?', default=None, help='Root directory of the game library or game directory.')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        
    if args.path:
        if args.organize:
            organize_games(args.path, args.txt_paramsfo)
        else:
            process_library_root(args.path, args.txt_paramsfo)
    else:
        process_game_root('.', args.txt_paramsfo)

if __name__ == '__main__':
    main()
