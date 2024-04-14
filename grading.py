import os 
import shutil
import making_playground
import comparefloats
import time

list_of_submissions = ['2019CS50129_2019CS10363_2019CS50506', 'cs1210557_cs1210548_cs1210075', 'cs1210081_cs1210070_cs1210559']
params_subtask1_subtask2 = [
    "",
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
# def make_for_each_subtask():
#     solution_folder = 'playground'
#     for filename in os.listdir(solution_folder):
#         source_path = os.path.join(solution_folder, filename)
#         print(source_path)
#         os.chdir(source_path)
#         resultcode1 = os.system("make subtask1")
#         resultcode2 = os.system("make subtask2")
#         resultcode3 = os.system("make subtask3")
#         resultcode4 = os.system("make subtask4")
#         print(resultcode1,resultcode2,resultcode3,resultcode4)
#         os.chdir("../../")


def run_grading_s1_s2(): 
    global list_of_submissions
    scores = {each:{"marks":0,"subtask1":0,"subtask2":0,"time_subtask1":0,"time_subtask2":0,"time_subtask3":0,"time_subtask4":0} for each in list_of_submissions}
    solution_folder = 'playground'
    tasks = ["subtask1","subtask2","subtask3","subtask4"]
    tasks = ["subtask2"]
    for submission in list_of_submissions: 
        for task in tasks: 
            os.chdir(solution_folder + "/" + submission)        
            resultcode = os.system("make "+task)
            if resultcode != 0: 
                scores[submission][task] = -1
                scores[submission]["time_"+task] = -1

                os.chdir("../../")
                continue
            os.system("pwd")
            for i in range(1,7):
                with open('../../correct_answers/subtask12/case'+str(i)+"/input/kernel.txt", 'r') as file:
                    kernel = file.read()
                    with open('../../correct_answers/subtask12/case'+str(i)+"/input/matrix.txt", 'r') as file:
                        matrix = file.read()
                        cmd = "./" + task + " " + params_subtask1_subtask2[i] + matrix + " " + kernel + "> output" + str(i)
                        start_time = time.time()
                        os.system(cmd)
                        end_time = time.time()
                        diff = comparefloats.compare_two_files("output" + str(i), '../../correct_answers/subtask12/case'+str(i)+"/output/output.txt")
                        print(submission,diff)
                        if diff == 0 :
                            execution_time = end_time - start_time
                            scores[submission]["time_"+task] += execution_time
                            scores[submission][task] += 1
                            
            # for i in range(6,9):
            
            os.chdir("../../")
    print(scores)
    # make_for_each_subtask()

run_grading_s1_s2()