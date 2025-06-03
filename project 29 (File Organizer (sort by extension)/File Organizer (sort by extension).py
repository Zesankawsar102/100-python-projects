import os
import shutil

def organize_files_by_extension(folder_path):
    if not os.path.isdir(folder_path):
        print("❌ Invalid folder path.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext[1:].upper()  # Remove dot and make uppercase like 'PDF'

            if ext:  # Only proceed if there's an extension
                folder_name = os.path.join(folder_path, ext)

                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)

                shutil.move(file_path, os.path.join(folder_name, filename))
                print(f"✅ Moved: {filename} ➜ {ext}/")
            else:
                print(f"⚠️ Skipped (no extension): {filename}")

if __name__ == "__main__":
    path = input("Enter the folder path to organize: ").strip()
    organize_files_by_extension(path)
