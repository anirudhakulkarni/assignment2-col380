import os 
import shutil
import making_playground
import comparefloats

list_of_submissions = ['2019CS50129_2019CS10363_2019CS50506', 'cs1210557_cs1210548_cs1210075', 'cs1210081_cs1210070_cs1210559']
params_subtask1_subtask2 = [
    "1 25 3 0 ",
    "1 25 7 0 ",
    "1 50 3 0 ",
    "1 50 7 0 ",
    "1 100 3 0 ",
    "1 100 7 0 ",
    "2 0 10 10",
    "2 1 50 50",
    "2 0 100 100",
    "3 0 2 10",
    "3 1 4 50",
    "3 0 5 100",
    "4 0 10",
    "4 1 50",
    "4 0 100",
]
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


def run_grading(): 
    global list_of_submissions
    scores = [{each:{"marks":0,}} for each in list_of_submissions]
    print(scores)
    # make_for_each_subtask()

run_grading()