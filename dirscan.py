import os
import sys
from pathlib import Path

def recursive_scan(dirpath):
	for entry in os.scandir(dirpath):
		if entry.is_file():
			yield entry.path
		else:
			for file in recursive_scan(entry.path):
				yield file

def get_dirpath(dirpath):
    p = Path(dirpath)
    if not p.is_dir():
        raise Exception("No such directory.")
    return p

def main():
    if len(sys.argv) != 2:
        print("Usage: dirscan.py <dirname>")
        sys.exit(1)

    try:
        dirpath = get_dirpath(sys.argv[1])
    except Exception as e:
        print(f"Error locating directory: {e}\n")
        sys.exit(1)

    for file in recursive_scan(dirpath):
        print(file)
	
if __name__=="__main__":
	main()
