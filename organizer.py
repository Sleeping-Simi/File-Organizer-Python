import os 
import shutil
import logging

def logging_setup():
     logging.basicConfig(
        filename="organizer_log.txt", 
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s --> %(message)s'
    )

def create_folder(folder, folder_paths):
    if not os.path.exists(folder_paths):
        os.makedirs(folder_paths)
        logging.info(f"Created {folder} folder")
    
path =r"C:\Users\SOVANGI\Downloads"
folders={
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx"],
    "Applications": [".exe", ".msi"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music":[".mp3"]
}

logging_setup()
 
logging.info("***********New Scanning Started***********")

files=os.listdir(path)
count=0
for file in files:
    filename,extension=os.path.splitext(file)
    extension=extension.lower()
    for folder in folders:
        if extension in folders[folder]:
            folder_paths=os.path.join(path,folder)
            create_folder(folder,folder_paths)
            original_file_path=os.path.join(path,file)
            new_file_path=os.path.join(folder_paths,file) 
            if os.path.exists(new_file_path): 
                logging.warning(f"Skipped: {file} (file already exists in {folder} folder)")
            else:
                try:
                    shutil.move(original_file_path,new_file_path)
                    print(f"Moved: {file} to {folder} folder")
                    count+=1
                except Exception as e:
                    logging.error(f"Error in {file} moving  as :{e}")
            break 
if count == 0:
    summary = "Checking done! \nYour folder is already organized nothing to change! \nFor more details may refer to the LOG file"
    
else:
    summary = f"Checking done✅! Total number of files moved = {count}"
    
logging.info(summary)
print(f"✅{summary}")
logging.info("***********Scanning Completed***********")