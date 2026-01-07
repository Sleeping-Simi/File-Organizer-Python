import os 
import shutil

path =r"C:\Users\SOVANGI\Downloads"

folder_path=os.path.join(path,"Images")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("Created Images folder")
files=os.listdir(path)
ext=[".jpg",".png",".jpeg", ".gif",".jfif",".tiff",".bmp"]
count=0
for file in files:
    filename,extension=os.path.splitext(file)
    if extension in ext:
        original_file_path=os.path.join(path,file)
        new_file_path=os.path.join(folder_path,file)
        if os.path.exists(new_file_path): 
            print("Skip")
        else:
            shutil.move(original_file_path,new_file_path)
            print(f"Moved: {file} to Images folder")
            count+=1
print("Total number of files moved =",count)
