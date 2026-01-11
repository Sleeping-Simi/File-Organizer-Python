import os 
import shutil
import logging
import json

def logging_setup():
     logging.basicConfig(
        filename="organizer_log.txt", 
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s --> %(message)s'
    )

logging_setup()

def create_folder(folder, folder_paths):
    if not os.path.exists(folder_paths):
        os.makedirs(folder_paths)
        logging.info(f"Created {folder} folder")

def load_config():
    try:
        with open ("config.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("Config file not found!")
        return {}

def if_path_exists(target_path, purpose="directory"):
    if os.path.exists(target_path):
        return True
    else:
        logging.error(f"Missing {purpose}: {target_path}")
        print(f"Error ❌⚠️: The specified path does not exist: {target_path}")  
        return False
    

config= load_config()
 
logging.info("***********New Scanning Started***********")

folders=config.get("folders",{})
path=config.get("target_path","")

if not if_path_exists(path, "default target directory"):
    new_path=input("Please enter a valid path to organize files: ")
    new_path=new_path.strip('"')
    path=new_path
    if not if_path_exists(path, f"{path}"):
        print("Error ❌⚠️: Your provided path is still invalid. Exiting the program.")
        exit()
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