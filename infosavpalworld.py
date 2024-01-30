import subprocess
import os
import zlib
import sys
import json

def convert_sav_to_json(uesave_path, sav_file, json_file):

    if not os.path.isfile(uesave_path):
        raise FileNotFoundError(f"uesave.exe not found at {uesave_path}")
    
    with open(sav_file, 'rb') as file:
        data = file.read()
    
    magic_bytes = data[8:11]
    save_type = data[11]

    if magic_bytes != b'PlZ' or save_type not in [0x31, 0x32]:
        raise ValueError("Invalid file format or save type")
    
    # Decompress if necessary
    uncompressed_data = zlib.decompress(data[12:]) if save_type in [0x31, 0x32] else data

    # Convert to json using uesave
    uesave_run = subprocess.run(
        [uesave_path, 'to-json'],
        input=uncompressed_data,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Check for successful conversion
    if uesave_run.returncode != 0:
        raise RuntimeError(f"uesave.exe conversion failed: {uesave_run.stderr.decode()}")

    # Write the output to a JSON file
    with open(json_file, 'w') as file:
        file.write(uesave_run.stdout.decode())

def print_last_ten_unlocked_recipe_names(json_file):

    with open(json_file, 'r') as file:
        data = json.load(file)

    # Navigate to the 'UnlockedRecipeTechnologyNames' section
    recipe_names = data.get("root", {}).get("properties", {}).get("SaveData", {}).get("Struct", {}).get("value", {}).get("Struct", {}).get("UnlockedRecipeTechnologyNames", {}).get("Array", {}).get("value", {}).get("Base", {}).get("Name", [])

    last_ten_names_reversed = recipe_names[-10:][::-1]

    # Print the last 10 names found (in reverse order to get the last unlocked first)
    print("Last 10 unlocked recipe names:")
    for name in last_ten_names_reversed[-10:]:
        print("- " + name)
    
def print_pal_capture_counts(json_file):

    with open(json_file, 'r') as file:
        data = json.load(file)

    pal_capture_counts = data.get("root", {}).get("properties", {}).get("SaveData", {}).get("Struct", {}).get("value", {}).get("Struct", {}).get("RecordData", {}).get("Struct", {}).get("value", {}).get("Struct", {}).get("PalCaptureCount", {}).get("Map", {}).get("value", [])

    print("Pal capture counts (names in the game files, not the ones in game):")
    for entry in pal_capture_counts:
        name = entry.get("key", {}).get("Name")
        count = entry.get("value", {}).get("Int")
        if name and count is not None:
            print(f"{name} : {count}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_uesave.exe> <path_to_file.sav>")
        sys.exit(1)

    uesave_path = sys.argv[1]
    sav_file = sys.argv[2]
    json_file = "temp5434158431.json"

    convert_sav_to_json(uesave_path, sav_file, json_file)
    sav_file_name = os.path.basename(sav_file)
    print()
    print("Info about the save file: " + sav_file_name)
    print()
    print_last_ten_unlocked_recipe_names(json_file)
    print()
    print_pal_capture_counts(json_file)
    os.remove(json_file)

if __name__ == "__main__":
    main()
