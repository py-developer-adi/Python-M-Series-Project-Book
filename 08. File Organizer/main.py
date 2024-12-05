'''PYCODE | @_py.code'''

# ? 8. File Organizer
# ? Features: Organize files into folders based on type.

import os
import shutil

# Define file type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".html", ".css", ".js"],
    "Others": []  # For files that don't match any category
}

def create_folders(base_path, categories):
    """Create folders for each file category."""
    for folder_name in categories:
        folder_path = os.path.join(base_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def get_file_category(file_extension):
    """Find the category for a given file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    return "Others"

def organize_files(directory):
    """Organize files in the given directory into categorized folders."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    print(f"Organizing files in directory: {directory}")

    # Create categorized folders
    create_folders(directory, FILE_CATEGORIES.keys())

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1].lower()
            category = get_file_category(file_extension)
            destination_folder = os.path.join(directory, category)
            try:
                shutil.move(item_path, destination_folder)
                print(f"Moved: {item} -> {category}")
            except Exception as e:
                print(f"Error moving {item}: {e}")

def main():
    directory = input("Enter the path of the directory to organize: ").strip()
    organize_files(directory)
    print("File organization complete.")

if __name__ == "__main__":
    main()
