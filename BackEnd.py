import os
import shutil
import glob


# Copying Files
def copy(newpath,file): #Define the method "copy"
    if not os.path.exists(newpath): #Checks if the folder exists
        os.makedirs(newpath) #Recursive directory creation function
    shutil.copy(file, newpath) #Copies the existing file to the the new directory
    os.remove(file) #Removes the original file

#The program doesn't actually "move" the file, instead it duplicates it and deletes the old file

# Creating Folders
def folder(extension,foldername): #Define the method "folder" and create parameters extension and foldername
    lists=glob.glob(extension) #Recursively lists out the file names
    for name in lists: 
        copy(foldername,name)

#Sorting Files

folder("*.py","Python Scripts")
folder("*.java","Java Codes")
folder("*.c","C Codes")
folder("*.html","HTML")
folder("*.cpp","C++ Files")
folder("*.mp3","Music")
folder("*.mp4","Videos")
folder("*.txt","Documents/Text Files")
folder("*.docx","Documents/Word Files")
folder("*.xlsx","Documents/Excel Sheets")
folder("*.pptx","Documents/PowerPoint Presentations")
folder("*.pdf","Documents/PDF Files")
images=["*.jp*","*.png","*.psd","*.bmp"]
for img in images:
    folder(img,"Images")



'''
DIRECTORIES = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
}

FILE_FORMATS = {file_format: directory 
                for directory, file_formats in DIRECTORIES.items() 
                for file_format in file_formats} 
  
def organize_junk(): 
    for entry in os.scandir(): 
        if entry.is_dir(): 
            continue
        file_path = Path(entry) 
        file_format = file_path.suffix.lower() 
        if file_format in FILE_FORMATS: 
            directory_path = Path(FILE_FORMATS[file_format]) 
            directory_path.mkdir(exist_ok=True) 
            file_path.rename(directory_path.joinpath(file_path)) 
  
        for dir in os.scandir(): 
            try: 
                os.rmdir(dir) 
            except: 
                pass
  
if __name__ == "__main__": 
    organize_junk()
'''


