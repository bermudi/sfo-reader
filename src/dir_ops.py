import os
import shutil
from file_ops import read_sfo_data

def process_game_root(directory):
    """ Process a single game directory to print the contents of param.sfo. """
    sfo_path = os.path.join(directory, 'sce_sys', 'param.sfo')
    if os.path.exists(sfo_path):
        sfo_data = read_sfo_data(sfo_path)
        for key, value in sfo_data.items():
            print(f"{key}: {value}")
        stitle = sfo_data.get('STITLE', 'Unknown').replace('/', '_')
        print(f"\n\nTitle: {stitle}")
    else:
        print("Error: 'sce_sys/param.sfo' not found in the current directory.")

def process_library_root(directory):
    """ Process the library root to find all games and summarize them. """
    stitles = []
    game_count = 0
    homebrew_count = 0
    for root, dirs, files in os.walk(directory):
        if 'param.sfo' in files:
            #sfo_path = os.path.join(root, 'sce_sys', 'param.sfo')
            sfo_path = os.path.join(root, 'param.sfo')
            sfo_data = read_sfo_data(sfo_path)
            if sfo_data:
                stitle = sfo_data.get('STITLE', 'Unknown')
                stitles.append(stitle)
                if 'PUBTOOLINFO' in sfo_data:
                    game_count += 1
                else:
                    homebrew_count += 1
    sep = '\n'
    print("TITLEs found:\n")
    print(f"{sep.join(stitles)}")
    print()
    print(f"Games: {game_count}, Homebrews: {homebrew_count}")

def is_valid_game_directory(root):
    """ Check if the directory contains valid game or homebrew structure. """
    required_files = ['eboot.bin']
    required_dirs = ['sce_sys']
    if all(os.path.exists(os.path.join(root, f)) for f in required_files) and \
       all(os.path.exists(os.path.join(root, d)) for d in required_dirs):
        sfo_path = os.path.join(root, 'sce_sys', 'param.sfo')
        return os.path.exists(sfo_path)
    return False

def organize_games(directory, organize=False, create_txt=False):
    """ Organize games and homebrew by STITLE and optionally generate a text file. """
    if organize:
        games_dir = os.path.join(directory, "Games")
        homebrew_dir = os.path.join(directory, "Homebrew")
        if not os.path.exists(games_dir):
            os.makedirs(games_dir)
        if not os.path.exists(homebrew_dir):
            os.makedirs(homebrew_dir)

    for root, dirs, files in os.walk(directory):
        if is_valid_game_directory(root):
            sfo_path = os.path.join(root, 'sce_sys', 'param.sfo')
            sfo_data = read_sfo_data(sfo_path)
            if sfo_data:
                stitle = sfo_data.get('STITLE', 'Unknown').replace('/', '_')
                if 'PUBTOOLINFO' in sfo_data:
                    new_path = os.path.join(games_dir, stitle)
                else:
                    new_path = os.path.join(homebrew_dir, stitle)

                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                
                # Move all contents of the current game directory to the new directory
                for item in os.listdir(root):
                    shutil.move(os.path.join(root, item), os.path.join(new_path, item))

                if create_txt:
                    generate_text_file(new_path, sfo_data)

def generate_text_file(root, sfo_data):
    """ Generates a text file with 'param.sfo' contents at the game directory level. """
    filename = sfo_data.get('STITLE', 'Unknown').replace('/', '_') + '.txt'
    txt_path = os.path.join(root, filename)
    with open(txt_path, 'w') as txt_file:
        for key, value in sfo_data.items():
            txt_file.write(f"{key}: {value}\n")
    print(f"Generated text file at {txt_path}")
