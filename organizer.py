import os 
import shutil

path =r"C:\Users\SOVANGI\Downloads"
folders={
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx"],
    "Applications": [".exe", ".msi"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music":[".mp3"]
}

files=os.listdir(path)
count=0
for file in files:
    filename,extension=os.path.splitext(file)
    extension=extension.lower()
    for folder in folders:
        if extension in folders[folder]:
            folder_paths=os.path.join(path,folder)
            if not os.path.exists(folder_paths):
                os.makedirs(folder_paths)
                print(f"Created {folder} folder")
            original_file_path=os.path.join(path,file)
            new_file_path=os.path.join(folder_paths,file) 
            if os.path.exists(new_file_path): 
                print("Skipped:",file,"(file already exists in",folder,"folder)")
            else:
                shutil.move(original_file_path,new_file_path)
                print(f"Moved: {file} to {folder} folder")
                count+=1
            break 
print("Total number of files moved =",count)
