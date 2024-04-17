import os
import shutil
import logging

def is_valid_game_directory(path):
    necessary_paths = {
        'eboot_bin': os.path.join(path, 'eboot.bin'),
        'sce_sys': os.path.join(path, 'sce_sys'),
        'param_sfo': os.path.join(path, 'sce_sys', 'param.sfo'),
        'sce_pfs': os.path.join(path, 'sce_pfs')
    }
    valid = all(os.path.exists(necessary_paths[key]) for key in necessary_paths)
    if not valid:
        missing_components = [key for key in necessary_paths if not os.path.exists(necessary_paths[key])]
        logging.warning(f"Invalid game directory: {path}, missing components: {missing_components}")
    return valid

def organize_games(library_root, sfo_data_reader):
    logging.info(f"Organizing games in {library_root}")
    for game_id in os.listdir(library_root):
        game_path = os.path.join(library_root, game_id)
        if os.path.isdir(game_path) and is_valid_game_directory(game_path):
            sfo_path = os.path.join(game_path, 'sce_sys', 'param.sfo')
            try:
                sfo_data = sfo_data_reader(sfo_path)
                title = sfo_data.get('TITLE', 'Unknown Title').replace('/', '_')
                title_dir = os.path.join(library_root, title)
                if not os.path.exists(title_dir):
                    os.makedirs(title_dir)
                new_game_path = os.path.join(title_dir, game_id)
                shutil.move(game_path, new_game_path)
                logging.info(f"Moved {game_id} to {title}")

                # Create and write the SFO data to a text file named after the game title
                filename = f"{title}.txt"
                txt_path = os.path.join(new_game_path, filename)
                with open(txt_path, 'w') as txt_file:
                    for key, value in sfo_data.items():
                        txt_file.write(f"{key}: {value}\n")
                logging.info(f"SFO data written to {txt_path}")

            except Exception as e:
                logging.error(f"Error processing {game_id}: {e}")


