from config import START_INDEX
from utils.renamer import copy_renamed_images

if __name__ == "__main__":
    prefix = input("Enter filename prefix: ").strip()
    if not prefix:
        raise ValueError("Filename prefix cannot be empty.")

    copy_renamed_images("input_images", "renamed_images", prefix, START_INDEX)
