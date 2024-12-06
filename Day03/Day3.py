import re

pattern = r"mul\(\d{1,3},\d{1,3}\)|do(?:n't)?\(\)"

input_file = 'DayThree/sampleinput.txt'

def mul(x,y):
    return x * y

def find(text):
    found = re.findall(pattern, text)
    return list(found)

def extract_mul_expression(file_path):
    product = 0

    with open(file_path) as file:
        last_seen_do = True

        for line in file.readlines():

            for n in find(line):
                
                if n == "do()":
                    last_seen_do = True

                elif n == "don't()":
                    last_seen_do = False  

                else:
                    if last_seen_do:
                        product += eval(n)

    print(product)

result = extract_mul_expression(input_file)
