from os import walk
import os
import sys
import json

input_path = 'input'
keywords = 'thời gian'
f = []


def create_folder_if_not_exist(path):
    temp_path = path.split('/')
    if temp_path[-1].find('.') > -1:
        path = '/'.join(temp_path[:-1])
    if not os.path.exists(path):
        os.makedirs(path)


def let_extract(content, position_input):
    start = 0
    end = 0
    position = position_input
    while position > 1:
        position -= 1
        if (content[position] == " " and content[position-1] == " ") or (content[position] == "\n") or (content[position] == "\t") or (content[position] == " " and content[position-1] == ".") or (content[position] == "." and content[position-1] == "."):
            start = position

            break
    position = position_input
    while position < len(content)-1:
        position += 1
        # print(position)
        if (content[position] == " " and content[position+1] == " ") or (content[position] == "." and content[position+1] == " ") or (content[position] == "\n") or (content[position] == " " and content[position+1] == ".") or (content[position] == "\t"):
            end = position
            break
    return start + 1, end +1


for (dirpath, dirnames, filenames) in walk(input_path):
    for single_file in filenames:
        sentenses = []
        file_path = '/'.join([input_path, single_file])
        create_folder_if_not_exist(file_path)
        file_stream = open(file_path, mode='r', encoding='utf-8')
        file_content = file_stream.read()
        flag_search = flag_start_str = 0
        prevent_infinity_loop = 0
        while True:
            flag_search = file_content.find(keywords)

            if flag_search == -1:
                break
            start_s, end_s = let_extract(file_content, flag_search)
            sentenses.append(file_content[start_s: end_s].rstrip())
            file_content = file_content[end_s:]
            prevent_infinity_loop += 1
            if prevent_infinity_loop > 10000:
                break
        output_folder = '/'.join([input_path+'_output', single_file+'.json'])
        create_folder_if_not_exist(output_folder)
        with open(output_folder, "w", encoding='utf-8') as outfile:
            json.dump(sentenses, outfile, ensure_ascii=False, indent=4)


