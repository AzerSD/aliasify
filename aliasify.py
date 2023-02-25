import os
import sys

if len(sys.argv) < 3:
    print("Usage: python create_alias.py [alias name] [file]")
    sys.exit(1)

alias_name = sys.argv[1]
file_name = sys.argv[2]

if not os.path.exists(file_name):
    print(f"Error: file '{file_name}' does not exist")
    sys.exit(1)

os.system(f"alias {alias_name}='open \"{os.path.abspath(file_name)}\"'")
print(f"Alias '{alias_name}' created for file '{file_name}'")

