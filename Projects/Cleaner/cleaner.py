import os
import shutil

def create_subfolder_if_needed(folder_path:str, subfolder_name:str) -> str:
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path


def clean_folder(folder_path:str, destination_path: str) -> None:
    
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder_if_needed(destination_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                shutil.move(file_path, subfolder_path)
                print(f"Moved: {filename} -> {subfolder_name}")



def main() -> None:
    print("Cleaner script")
    choice:int = int(input('Choose what to clean:\n1. Desktop\n2. Downloads folder\n'))
    if choice == 1:
        folder_path = "C:/Users/gabri/Desktop"
    elif choice == 2:
        folder_path = "C:/Users/gabri/Downloads"
    else:
        print("Invalid choice")
        return
    
    if os.path.isdir(folder_path):
        destination_path = "D:/docs/CLEANER"
        clean_folder(folder_path, destination_path)
        print("All clean !")
    else:
        print("Invalid path")
    x = input('')


if __name__ == "__main__":
    main()
    