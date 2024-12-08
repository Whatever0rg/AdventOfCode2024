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

def extract_equations(input_file : str):
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

def next_inline(result : int, rest : list):
    if len(rest) == 1:
        return rest[0] == result

    last = rest[-1]

    if result % last == 0:
        possible_mul = next_inline(result // last, rest[:-1])
    else:
        possible_mul = False
    next_power_of_10 = 1
    while next_power_of_10 <= last:
        next_power_of_10 *= 10
    if (result - last) % next_power_of_10 == 0:
        possible_concat = next_inline((result - last) // next_power_of_10, rest[:-1])
    else:
        possible_concat = False

    possible_add = next_inline(result - last, rest[:-1])
    return possible_mul or possible_add or possible_concat


def matching_solution(eq_list : list):
    solution = 0  
    for eq_sublist in eq_list:
        result = eq_sublist[0]
        rest = eq_sublist[1:]
        if  next_inline(result,rest):
            solution += result
            print('True | ',eq_sublist)
        else: 
            print('False | ',eq_sublist)
    return solution

print(matching_solution(extract_equations(input_file)))