'''PYCODE'''

# ? 2. Quiz App
# ? Features: Multiple-choice questions, score calculation.

# * Source Code
questions = [
    ['What is the output of print(2 ** 3)?', '6', '8', '9', 'None', 2],
    ['Which of these is a valid variable name?', '1variable', 'variable-1', 'variable_one', 'variable.1', 3],
    ['What is the correct syntax to output "Hello World" in Python?', 'echo "Hello World"', 'printf("Hello World")', 'print("Hello World")', 'cout << "Hello World"', 3],
    ['What keyword is used to create a function in Python?', 'define', 'fun', 'function', 'def', 4],
    ['Which of the following is an immutable data type in Python?', 'List', 'Set', 'Dictionary', 'Tuple', 4],
    ['What is the correct file extension for Python files?', '.py', '.python', '.pyth', '.pt', 1],
    ['How do you create a single-line comment in Python?', '| Comment', '/* Comment */', '# Comment', '// Comment', 3],
    ['Which of the following is used to declare a loop in Python?', 'for', 'while', 'both', 'none', 3],
    ['Which of these is not a valid Python keyword?', 'pass', 'eval', 'assert', 'execute', 4],
    ['What is the data type of the expression 10/2 in Python 3?', 'int', 'float', 'complex', 'decimal', 2],
    ['How do you add an element to a list in Python?', 'list.add()', 'list.append()', 'list.push()', 'list.insert()', 2],
    ['Which of the following is not a Python built-in data type?', 'List', 'Dictionary', 'Tree', 'Set', 3],
    ['How do you handle exceptions in Python?', 'try-expect', 'try-catch', 'try-except', 'catch-try', 3],
    ['What is the result of len([1, 2, 3, 4])?', '3', '4', '5', 'None', 2],
    ['Which library is commonly used for data manipulation in Python?', 'numpy', 'matplotlib', 'pandas', 'seaborn', 3]
]

score = 0
for i in range(len(questions)):
    print(f"Question. {questions[i][0]}")
    print(f"1. {questions[i][1]}")
    print(f"2. {questions[i][2]}")
    print(f"3. {questions[i][3]}")
    print(f"4. {questions[i][4]}")
    
    ans = int(input("Enter the Correct Option (1, 2, 3, 4): "))
    
    if ans == questions[i][-1]:
        score += 1
        print("Correct\nScore: {}".format(score))
    else:
        print(f"Wrong: {questions[i][-1]}")
        
    print("-"*50)
    
print("Great Work\nYour Score is {}/{}".format(score, len(questions)))
