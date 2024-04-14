import os
import shutil
import zipfile
import tarfile

list_of_submissions = []
def function_to_unzip_files_in_submissions():
    # Paths to the directories
    source_dir = 'submissions'
    destination_dir = 'submission_unziped'
    global list_of_submissions
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Move all files from submissions to solution
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)

        # Move the file
        shutil.copy(source_path, destination_path)
        print(f"Moved {filename} to {destination_dir}")
        dir_path = destination_path.split('.')[0]
        print(dir_path.split("/")[1])
        list_of_submissions.append(dir_path.split("/")[1])
        # Check if the file is a zip file and unzip it
        if filename.endswith('.zip'):
            try:
                with zipfile.ZipFile(destination_path, 'r') as zip_ref:
                    # Extract all the contents into destination directory
                    zip_ref.extractall(dir_path)
                    print(f"Unzipped {filename}")
                    os.remove(destination_path)
            except zipfile.BadZipFile:
                print(f"Failed to unzip {filename}, it may be corrupted.")
          
        if filename.endswith('.tar') or filename.endswith('.tar.gz') or filename.endswith('.tar.bz2'):
            try:
                with tarfile.open(destination_path, 'r:*') as tar:
                    tar.extractall(path=dir_path)
                    print(f"Extracted {filename}")
                    os.remove(destination_path)
            except tarfile.TarError:
                print(f"Failed to extract {filename}, it may be corrupted.")
    # Final message
    print("All files have been moved and unzipped if applicable.")
def make_folders_like_template():
    os.system('find submission_unziped -name "__MACOSX" -type d -exec rm -rf {} +')
    source_folder = 'submission_unziped/'
    destination_folder = "playground/"
    filename_contains = ["subtask1", "subtask2", "subtask3", "subtask4"]
    new_filename = ["assignment2_subtask1","assignment2_subtask2","assignment2_subtask3","assignment2_subtask4"]
    # Iterate over all files in the source folder
    for i in range(0,4): 
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if filename_contains[i] in file:
                    # Construct source and destination paths
                    folder_path = destination_folder + root.split('/')[1]
                    if not os.path.exists(folder_path):
                        os.system("cp -r playground/TEMPLATE " + folder_path)
                    source_file = os.path.join(root, file)

                    destination_file = destination_folder + root.split('/')[1]+ "/src/" + new_filename[i] +"." + file.split('.')[-1]
                    # Rename the file
                    shutil.copy(source_file, destination_file)
                    print(f"'{source_file}' renamed to '{destination_file}'")

    # If no file containing the specified text is found
    print(f"No file containing '{filename_contains}' found in '{source_folder}'")
def search_for_preprocess_and_makefile():
    os.system('find submission_unziped -name "__MACOSX" -type d -exec rm -rf {} +')

    source_folder = 'submission_unziped/'
    destination_folder = "playground/"
    filename_contains = ["preprocess.py", "Makefile"]
    for i in range(2):
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if filename_contains[i] in file:
                    source_file = os.path.join(root, file)
                    destination_file = destination_folder + root.split('/')[1] +"/"+ filename_contains[i]
                    shutil.copy(source_file, destination_file)
                    print(f"'{source_file}' copied to '{destination_file}'")
            print(root)
def make_like_template():
    os.system('find submission_unziped -name "__MACOSX" -type d -exec rm -rf {} +')
    global list_of_submissions
    for each in list_of_submissions: 
        # making folder same as given template
        os.system("cp -r static_files/TEMPLATE playground/"+each)
        # copying the student root folder files
        cmd = "find submission_unziped/"+ each +"/ -maxdepth 2 -type f -exec cp -p {} playground/"+ each +"/ \;"
        os.system(cmd)
        # copying the source files if not in root 
        cmd = "find submission_unziped/"+ each +"/*/src -maxdepth 1 -type f -exec cp -p {} playground/"+ each +"/src \; "
        os.system(cmd)
    return list_of_submissions

if __name__ == "__main__":
    function_to_unzip_files_in_submissions()
    # list_of_submissions = ['2019CS50129_2019CS10363_2019CS50506', 'cs1210557_cs1210548_cs1210075', 'cs1210081_cs1210070_cs1210559']
    make_like_template()
    
    pass