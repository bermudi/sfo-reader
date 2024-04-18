import logging

def read_sfo_data(filename):
    logging.debug(f"Reading data from {filename}")
    with open(filename, 'rb') as file:
        magic = file.read(4)
        if magic != b'\x00PSF':
            logging.error("File is not a valid SFO file.")
            raise ValueError("Not a valid SFO file.")
        version = int.from_bytes(file.read(4), 'little')
        key_table_start = int.from_bytes(file.read(4), 'little')
        data_table_start = int.from_bytes(file.read(4), 'little')
        num_entries = int.from_bytes(file.read(4), 'little')
        
        entries = []
        for _ in range(num_entries):
            key_offset = int.from_bytes(file.read(2), 'little')
            data_fmt = int.from_bytes(file.read(2), 'little')
            data_len = int.from_bytes(file.read(4), 'little')
            data_max_len = int.from_bytes(file.read(4), 'little')
            data_offset = int.from_bytes(file.read(4), 'little')
            entries.append((key_offset, data_fmt, data_len, data_max_len, data_offset))
        
        file.seek(key_table_start)
        key_table = file.read(data_table_start - key_table_start).decode()
        keys = key_table.split('\x00')
        
        sfo_data = {}
        for key, (key_offset, data_fmt, data_len, data_max_len, data_offset) in zip(keys, entries):
            file.seek(data_table_start + data_offset)
            if data_fmt == 0x0204:  # Assume UTF-8 encoded text
                data_value = file.read(data_len).decode('utf-8').rstrip('\x00')
            else:
                data_value = file.read(data_len)
            sfo_data[key] = data_value
            logging.debug(f"Extracted {key}: {data_value}")
        
        return sfo_data
