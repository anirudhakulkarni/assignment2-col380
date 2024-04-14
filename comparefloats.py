def read_file_to_floats(file_name):
    """Read a file and convert each number in it to a float with specified precision."""
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            float_line = [round(float(num), 4) for num in line.split()]
            data.append(float_line)
    return data

def compare_two_files(path1,path2):
    # Compare the two datasets and count differences
    data1 = read_file_to_floats(path1)
    data2 = read_file_to_floats(path2)
    
    difference_count = 0
    for row1, row2 in zip(data1, data2):
        for num1, num2 in zip(row1, row2):
            if num1 != num2:
                difference_count += 1
    return difference_count
    # print(f'Number of different values: {difference_count}')
