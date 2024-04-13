import os
import shutil
import zipfile
import tarfile

def function_to_unzip_files_in_submissions():
    # Paths to the directories
    source_dir = 'submissions'
    destination_dir = 'submission_unziped'

    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Move all files from submissions to solution
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)
        
        # Move the file
        shutil.copy(source_path, destination_path)
        print(f"Moved {filename} to {destination_dir}")

        # Check if the file is a zip file and unzip it
        if filename.endswith('.zip'):
            try:
                with zipfile.ZipFile(destination_path, 'r') as zip_ref:
                    # Extract all the contents into destination directory
                    zip_ref.extractall(destination_dir)
                    print(f"Unzipped {filename}")
                    os.remove(destination_path)
            except zipfile.BadZipFile:
                print(f"Failed to unzip {filename}, it may be corrupted.")
          
        if filename.endswith('.tar') or filename.endswith('.tar.gz') or filename.endswith('.tar.bz2'):
            try:
                with tarfile.open(destination_path, 'r:*') as tar:
                    tar.extractall(path=destination_dir)
                    print(f"Extracted {filename}")
                    os.remove(destination_path)
            except tarfile.TarError:
                print(f"Failed to extract {filename}, it may be corrupted.")
    # Final message
    print("All files have been moved and unzipped if applicable.")

def make_folders_like_template():
    os.system("rm -rf submission_unziped/__MACOSX")
    source_folder = 'submission_unziped/'
    destination_folder = "playground/"
    filename_contains = ["subtask1","subtask2","subtask3","subtask4"]
    new_filename = ["assignment2_subtask1","assignment2_subtask2","assignment2_subtask3","assignment2_subtask4"]
    # Iterate over all files in the source folder
    for i in range(0,4): 
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if filename_contains[i] in file:
                    # Construct source and destination paths
                    folder_path = destination_folder + root.split('/')[-1]
                    if not os.path.exists(folder_path):
                        os.system("cp -r playground/template " + folder_path)
                    source_file = os.path.join(root, file)
                    os.system("cp ")
                    destination_file = destination_folder + root.split('/')[-1]+ "/src/" + new_filename[i] +"." + file.split('.')[-1]
                    print(destination_file)
                    # Rename the file
                    shutil.copy(source_file, destination_file)
                    print(f"'{file}' renamed to '{new_filename[i]}'")

    # If no file containing the specified text is found
    print(f"No file containing '{filename_contains}' found in '{source_folder}'")


def make_for_each_subtask():
    solution_folder = 'submission_unziped'
    for filename in os.listdir(solution_folder):
        
        source_path = os.path.join(solution_folder, filename)
        print(source_path)
        os.chdir(source_path)
        resultcode1 = os.system("make subtask1")
        resultcode2 = os.system("make subtask2")
        resultcode3 = os.system("make subtask3")
        resultcode4 = os.system("make subtask4")
        print(resultcode1,resultcode2,resultcode3,resultcode4)
        os.chdir("../../")
    
# function_to_unzip_files_in_submissions()
make_folders_like_template()
# make_for_each_subtask()