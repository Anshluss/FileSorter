print("start")
import os, shutil
path = r"C:/Users/User/OneDrive/Documents/"
file_name = os.listdir(path)
folder_names = ['docx folder', 'xlsx folder', 'pdf folder', 'pptx folder']
for loop in range(0,4):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))
for file in file_name:
    if ".docx" in file and not os.path.exists(path + "docx folder/" + file):
        shutil.move(path + file, path + "docx folder/" + file)
    elif ".xlsx" in file and not os.path.exists(path + "xlsx folder/" + file):
        shutil.move(path + file, path + "xlsx folder/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf folder/" + file):
        shutil.move(path + file, path + "pdf folder/" + file)
    elif ".pptx" in file and not os.path.exists(path + "pptx folder/" + file):
        shutil.move(path + file, path + "pptx folder/" + file)