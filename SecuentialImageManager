import os
import shutil
from pathlib import Path

# Path
ROOT_FOLDER = "C:\MyImageFolder"
OUTPUT_FOLDER = "output"
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp') # tried with these extensions

def its_an_image(a_file):
    return a_file.lower().endswith(IMAGE_EXTENSIONS)

def begin_image_process(root_folder, output_path):
    os.makedirs(output_path, exist_ok=True)
    counter = 1

    for sub_folder in os.listdir(root_folder):
        sub_folde_route = os.path.join(root_folder, sub_folder)
        if sub_folder == OUTPUT_FOLDER or not os.path.isdir(sub_folde_route):
            continue  # evade output folder

        for a_file in os.listdir(sub_folde_route):
            if its_an_image(a_file):
                origin_route = os.path.join(sub_folde_route, a_file)
                new_file_name = f"{counter:04d}{Path(a_file).suffix}"
                destination_route = os.path.join(output_path, new_file_name)

                shutil.copy2(origin_route, destination_route)
                print(f"Copied: {origin_route} to -> {destination_route}")
                counter += 1

    if counter == 1:
        print("No images.")

if __name__ == "__main__":
    begin_image_process(ROOT_FOLDER, OUTPUT_FOLDER)
