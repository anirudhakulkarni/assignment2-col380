import os 

def make_for_each_subtask():
    solution_folder = 'playground'
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

def fduy():
    source_folder = "playground"
    for root, dirs, files in os.walk(source_folder):
        print(root,dirs,files)

fduy()