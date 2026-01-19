# Smart_Organizer for the Downloads Folder (macOS)
from pathlib import Path


def smart_organizer():
    # 1. Define the path to the directory we want to organize
    folder_to_track = Path.home() / "Downloads"

    # 2. Map of file extensions to their corresponding folder names
    extension_map = {
        ".jpg": "Images", ".png": "Images", ".jpeg": "Images",
        ".doc": "Word Files", ".docx": "Word Files",
        ".pdf": "PDFs",
        ".txt": "Text",
        ".ppt": "Presentations", ".pptx": "Presentations", ".pptm": "Presentations",
        ".xlsx": "Excel", ".xlsm": "Excel",
        ".zip": "ZIP",
        ".py": "Scripts"  # Added .py so the script can organize other scripts too
    }

    # 3. Iterate through every item in the folder
    for item in folder_to_track.iterdir():

        # Process only files, ignore directories
        if item.is_file():
            # Skip hidden macOS files like .DS_Store
            if item.name.startswith('.'):
                continue

            # Get the file extension in lowercase
            ext = item.suffix.lower()

            # Identify target folder or default to "Others"
            target_folder = extension_map.get(ext, "Others")

            # Prepare the destination directory
            target_dir = folder_to_track / target_folder
            target_dir.mkdir(exist_ok=True)

            # Define the final destination path
            new_path = target_dir / item.name

            # Move the file
            item.rename(new_path)

            # Log the action
            print(f"Success: {item.name} moved to {target_folder}")


if __name__ == "__main__":
    smart_organizer()
    print("--- Sorting Completed ---")