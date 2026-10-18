from pathlib import Path
import shutil

def copy_renamed_images(input_folder, output_folder, prefix, start_index=1):
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    files = sorted(
        f for f in input_path.iterdir()
        if f.is_file() and f.suffix.lower() in [".jpg", ".jpeg", ".png"]
    )
    for i, file_path in enumerate(files, start=start_index):
        new_name = f"{prefix}_{i:03d}{file_path.suffix.lower()}"
        shutil.copy2(file_path, output_path / new_name)
        print(f"Copied: {new_name}")
