
# BE AWARE!! 
# This program is slow af

import re

input_file = 'Day05/sampleinput.txt'


def extract_patterns(file_path):
    pipe_list = []
    comma_list = []
    
    pipe_pattern = r'\d+\|\d+'  
    comma_pattern = r'\d+(?:,\d+)+' 
    
    with open(file_path, 'r') as file:
        content = file.read()

    pipe_matches = re.findall(pipe_pattern, content)
    comma_matches = re.findall(comma_pattern, content)
    
    for match in pipe_matches:
        pipe_list.append(match.split('|'))  
    
    for match in comma_matches:
        comma_list.append(match.split(','))  
    
    return pipe_list, comma_list

pipe_list, comma_list = extract_patterns(input_file)


def Middle_correct_list(List):
    n = len(List)
    middle = List[n//2]
    middle = int(middle)
    return middle


def Swap(pipe_list,comma_sublist):
    for pipe_sublist in pipe_list:
        trigger = False 
        place_wrong_result = None 

        for counter, comma_elem in enumerate(comma_sublist):
            
            for pipe_elem in pipe_sublist:
                if comma_elem == pipe_elem and trigger and pipe_sublist[0] == pipe_elem: 

                    comma_sublist[place_wrong_result], comma_sublist[counter] = comma_sublist[counter], comma_sublist[place_wrong_result]
                    comma_sublist = Swap(pipe_list,comma_sublist)

                
                elif comma_elem == pipe_elem and not trigger:
                    trigger = True
                    place_wrong_result = counter
    return comma_sublist


def Check_comma_list(pipe_list, comma_list):
    pn = len(pipe_list)
    cn = len(comma_list)
    task_one_result_list = []
    task_two_result_list = []

    for comma_sublist in comma_list:
        first_rule_first = True
        for pipe_sublist in pipe_list:
            trigger = False 
            place_wrong_result = None  

            for counter, comma_elem in enumerate(comma_sublist):     
                for pipe_elem in pipe_sublist:
                    if comma_elem == pipe_elem and trigger and pipe_sublist[0] == pipe_elem: 
                        comma_sublist[place_wrong_result], comma_sublist[counter] = comma_sublist[counter], comma_sublist[place_wrong_result]
                        comma_sublist = Swap(pipe_list,comma_sublist)
                        first_rule_first = False
                        
                    elif comma_elem == pipe_elem and not trigger:
                        trigger = True
                        place_wrong_result = counter
 
                        
        if first_rule_first:
            task_one_result_list.append(Middle_correct_list(comma_sublist))
        else:
            task_two_result_list.append(Middle_correct_list(comma_sublist))


    one_result = sum(task_one_result_list)
    two_result = sum(task_two_result_list)

    return one_result, two_result



result1,result2 = Check_comma_list(pipe_list,comma_list)
print('Result Task One:', result1, '| Result Task Two:', result2 )