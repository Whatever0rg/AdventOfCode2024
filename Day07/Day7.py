import re

input_file = 'Day07/input.txt'

def add(num1 : int, num2 : int):
    result = num1 + num2
    return result

def mul(num1 : int, num2 : int):
    result = num1 * num2
    return result

def mush(num1 : int, num2 : int):
    result = int(str(num1) + str(num2))
    return result

def extract_equations(input_file: str):
    result = []
    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            
            if len(parts) != 2:
                print(f"Skipping invalid line: {line}")
                continue
            
            try:
                left = int(parts[0].strip())
            except ValueError:
                print(f"Skipping invalid line (non-numeric left part): {line}")
                continue
            
            right = list(map(int, re.split(r'[ ,\s]+', parts[1].strip()))) 
            
            result.append([left] + right)
    
    return result

def next_inline(current_result : int, remaining_elem : list, solution : int, mode : int):
    if len(remaining_elem) == 1:
        Sum = add(remaining_elem[0],current_result)
        Product = mul(remaining_elem[0],current_result)
        Mush = mush(remaining_elem[0],current_result)
        if Sum == solution:
            return True           
        elif Product == solution:
            return True
        elif Mush == solution:
            return True
        else:
            return False
    else:
        if mode == 1:
            current_result = mul(remaining_elem[0],current_result)
        elif mode == 2:
            current_result = add(remaining_elem[0],current_result)
        elif mode == 3:
            current_result = mush(current_result,remaining_elem[0])
        if next_inline(current_result,remaining_elem[1:],solution,1) == False:
            if next_inline(current_result,remaining_elem[1:],solution,2) == False:
                return next_inline(current_result,remaining_elem[1:],solution, 3)
            else: 
                return True
        else:
            return True
        
def matching_solution(eq_list):
    solution : int
    is_right : bool
    solution_list = []
    
    for eq_sublist in eq_list:
        solution = eq_sublist[0]
        
        if len(eq_sublist[1:]) == 2:
            Sum = add(eq_sublist[1],eq_sublist[2])
            Product = mul(eq_sublist[1],eq_sublist[2])
            Mush = mush(eq_sublist[1],eq_sublist[2])
            if Sum == solution:
                is_right = True
            elif Product == solution:
                is_right = True
            elif Mush == solution:
                is_right = True
            else:
                is_right = False
        elif len(eq_sublist[1:]) == 1 and eq_sublist[1] == solution:
            print('one element right')
        else:
            if next_inline(eq_sublist[1],eq_sublist[2:],solution,1) == False:
                if(next_inline(eq_sublist[1],eq_sublist[2:],solution,2)) == False:
                    is_right = next_inline(eq_sublist[1],eq_sublist[2:],solution,3)
                else:
                    is_right = True
            else: 
                is_right = True
        if is_right == True:
            solution_list.append(solution)
        print(is_right,' | ',eq_sublist)
    return sum(solution_list)

print(matching_solution(extract_equations(input_file)))