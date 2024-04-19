import os
import shutil
import logging
from file_ops import read_sfo_data


def process_game_root(directory, create_txt=False):
    """ Process a single game directory to print the contents of param.sfo. """
    is_valid, dir_type, sfo_data = is_valid_game_directory(directory)
    if is_valid:
        for key, value in sfo_data.items():
            print(f"{key}: {value}")
        stitle = sfo_data.get('STITLE', 'Unknown').replace('/', '_')
        print(f"\n\nTitle: {stitle}")
        print(f"Detected as: {dir_type}")
        if create_txt:
                txt_path = os.path.join(directory, f"{stitle}.txt")
                generate_text_file(txt_path, sfo_data)
    else:
        print("Error: 'sce_sys/param.sfo' and 'eboot.bin' not found in the current directory.")

def process_library_root(directory, create_txt=False):
    """ Process the library root to find all games and summarize them. """
    is_valid = False
    game_titles = []
    homebrew_titles = []
    # game_count = 0
    # homebrew_count = 0
    for root, dirs, files in os.walk(directory):
        is_valid, dir_type, sfo_data = is_valid_game_directory(root)
        if is_valid:
            stitle = sfo_data.get('STITLE')
            # logging.debug(f"Found {dir_type} {stitle} at {root}")
            if dir_type == 'game':
                game_titles.append(stitle)
                # game_count += 1
            elif dir_type == 'homebrew':
                homebrew_titles.append(stitle)
                # homebrew_count += 1
            if create_txt:
                txt_path = os.path.join(root, f"{stitle}.txt")
                generate_text_file(txt_path, sfo_data)
    sep = '\n'
    if len(game_titles) >= 1:
        print("Games found:\n")
        print(f"{sep.join(game_titles)}")
    print()
    if len(homebrew_titles) >= 1:
        print("Homebrews found:\n")
        print(f"{sep.join(homebrew_titles)}")
    print("\nSummary:")
    print(f"Games: {len(game_titles)}, Homebrews: {len(homebrew_titles)}")

def is_valid_game_directory(root):
    """ Check if the directory contains valid game or homebrew structure.
    And return `game` for game structure and `homebrew` for homebrew """
    logging.debug(f"Checking {os.path.abspath(root)} directory...")
    is_valid = False
    dir_type = False
    sfo_path = os.path.join(root, 'sce_sys',  'param.sfo')
    logging.debug(f"checking sfo_path: {sfo_path}")
    eboot_path = os.path.join(root, 'eboot.bin')
    logging.debug(f"checking eboot_path: {eboot_path}")
    if os.path.exists(sfo_path) and os.path.exists(eboot_path):
        is_valid = True
        sfo_data = read_sfo_data(sfo_path)
        stitle = sfo_data.get('STITLE')
        logging.debug(f"Found {stitle} in {root}")
        if os.path.exists(os.path.join(root,'sce_pfs')) and 'PUBTOOLINFO' in sfo_data:
            dir_type = 'game'
            logging.debug(f"{root} detected as `game`")
        elif not os.path.exists(os.path.join(root,'sce_pfs')) and 'PUBTOOLINFO' not in sfo_data:
            dir_type = 'homebrew'
            logging.debug(f"{root} detected as `homebrew`")
        else:
            raise ValueError(f"What is this? {root}")
        logging.debug(f"{root} is {is_valid}, {dir_type}, {sfo_data}")
        return is_valid, dir_type, sfo_data
    logging.debug(f"{os.path.abspath(root)} doesn't seem to be a valid game directory.")
    return False, False, False

def organize_games(directory, create_txt=False):
    # Predefine paths for games and homebrew
    games_dir = os.path.join(directory, "Games")
    logging.debug(f"games_dir: {games_dir}")
    homebrew_dir = os.path.join(directory, "Homebrew")
    logging.debug(f"homebrew_dir: {homebrew_dir}")

    if not os.path.exists(games_dir):
        logging.debug(f"Creating games_dir: {games_dir}")
        os.makedirs(games_dir)
    if not os.path.exists(homebrew_dir):
        logging.debug(f"Creating homebrew_dir: {homebrew_dir}")
        os.makedirs(homebrew_dir)

    # Walk through each directory in the library root
    for root, dirs, files in os.walk(directory, topdown=False):
        is_valid, dir_type, sfo_data = is_valid_game_directory(root)
        if is_valid:
                stitle = sfo_data.get('STITLE', 'Unknown').replace('/', '_')
                if dir_type == 'game':
                    target_dir = os.path.join(games_dir, stitle)
                    logging.debug(f"New Target Directory: {target_dir}")
                elif dir_type == 'homebrew':
                    target_dir = os.path.join(homebrew_dir, stitle)
                    logging.debug(f"New Target Directory: {target_dir}")
                # Ensure the target directory exists
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                    logging.debug(f"Created Target Directory: {target_dir}")
                
                # Move the entire game directory to the new location
                new_game_dir = os.path.join(target_dir, os.path.basename(root))
                logging.debug(f"new_game_dir: {new_game_dir}")
                if os.path.exists(new_game_dir):
                    raise FileExistsError("There is something at the target directory")
                shutil.move(root, target_dir)
                logging.debug(f"Moved: {root} to new location: {target_dir}")

                # Create a text file summarizing param.sfo contents if required
                if create_txt:
                    txt_path = os.path.join(new_game_dir, f"{stitle}.txt")
                    generate_text_file(txt_path, sfo_data)
                

def generate_text_file(txt_path, sfo_data):
    """ Generates a text file with 'param.sfo' contents at the game directory level. """
    with open(txt_path, 'w') as txt_file:
        for key, value in sfo_data.items():
            txt_file.write(f"{key}: {value}\n")
    logging.debug(f"Generated text file at {txt_path}")
