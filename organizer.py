from pathlib import Path
import shutil

# Folder to organize
SOURCE_FOLDER = Path("/workspaces/File-Organizer/downloads")

# File categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css"]
}


def move_file(file_path, destination_folder):

    try:
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / file_path.name

        # Handle duplicate filenames
        counter = 1

        while destination.exists():
            destination = (
                destination_folder /
                f"{file_path.stem}_{counter}{file_path.suffix}"
            )
            counter += 1

        shutil.move(str(file_path), str(destination))

        print(f" Moved: {file_path.name} -> {destination_folder.name}")

    except Exception as error:
        print(f" Error moving {file_path.name}: {error}")


def organize_files():

    for file in SOURCE_FOLDER.iterdir():

        # Skip folders
        if file.is_dir():
            continue

        extension = file.suffix.lower()

        moved = False

        for category, extensions in FILE_CATEGORIES.items():

            if extension in extensions:

                destination_folder = SOURCE_FOLDER / category

                move_file(file, destination_folder)

                moved = True
                break

        # Uncategorized files
        if not moved:

            others_folder = SOURCE_FOLDER / "Others"

            move_file(file, others_folder)


if __name__ == "__main__":
    organize_files()