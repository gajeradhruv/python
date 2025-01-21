import pdb

def get_directory_size(directory):
    total = 0
    for entry in directory.iterdir():
        if entry.is_file():
            total += entry.stat().st_size
        else:
            total += get_directory_size(entry)
    return total