import time
import random

# python and dsa questions list
questions = [
    {"q": "What is the correct file extension for Python files?", "op": ["A. .pt", "B. .pyt", "C. .py", "D. .txt"], "ans": "C"},
    {"q": "Which data structure follows the LIFO (Last In, First Out) principle?", "op": ["A. Queue", "B. Array", "C. Linked List", "D. Stack"], "ans": "D"},
    {"q": "Which keyword is used to define a function in Python?", "op": ["A. def", "B. func", "C. define", "D. function"], "ans": "A"},
    {"q": "What is the time complexity of accessing an element in an array by its index?", "op": ["A. O(1)", "B. O(n)", "C. O(log n)", "D. O(n^2)"], "ans": "A"},
    {"q": "Which of these data types is mutable in Python?", "op": ["A. Tuple", "B. String", "C. List", "D. Integer"], "ans": "C"},
    {"q": "Which data structure follows the FIFO (First In, First Out) principle?", "op": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"], "ans": "B"},
    {"q": "What does the '//' operator do in Python?", "op": ["A. Exponentiation", "B. Floor Division", "C. Modulus", "D. Commenting"], "ans": "B"},
    {"q": "Which sorting algorithm is known to have a worst-case time complexity of O(n^2)?", "op": ["A. Merge Sort", "B. Heap Sort", "C. Bubble Sort", "D. Radix Sort"], "ans": "C"},
    {"q": "How do you add an element to the end of a list in Python?", "op": ["A. list.add()", "B. list.insert()", "C. list.push()", "D. list.append()"], "ans": "D"},
    {"q": "Which data structure is best suited for representing hierarchical relationships?", "op": ["A. Array", "B. Stack", "C. Tree", "D. Queue"], "ans": "C"},
    {"q": "What is the average time complexity of searching for a key in a Python dictionary?", "op": ["A. O(1)", "B. O(n)", "C. O(log n)", "D. O(n log n)"], "ans": "A"},
    {"q": "Which of the following is NOT a built-in data structure in Python?", "op": ["A. Dictionary", "B. Tuple", "C. Set", "D. Linked List"], "ans": "D"}
]

# Shuffle the questions so every game is different
random.shuffle(questions)

prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
print("               ")
print("Welcome to KBC")
print("_______________")

level = 0
question_index = 0  # We need a separate index to track our place in the question list
money_won = 0
used_50 = False
used_skip = False

# main game loop
while level < 10:
    current_q = questions[question_index]
    prize_money = prizes[level]
    
    print(f"\nQuestion {level + 1} for Rs. {prize_money}")
    print(current_q["q"])
    
    # print options using a loop
    for opt in current_q["op"]:
        print(opt)
    
    start_time = time.time()
    ans = input("Enter A, B, C, D or 50 or SKIP: ").upper()
    end_time = time.time()
    
    # check time
    if end_time - start_time > 30:
        print("Time is up!")
        break

    # 50-50 lifeline
    if ans == "50":
        if not used_50:
            used_50 = True
            print("\n50-50 Lifeline used! Two options left:")
            
            # Find the correct option and gather the wrong ones
            correct_opt_str = ""
            wrong_opts = []
            
            for o in current_q["op"]:
                if o.startswith(current_q["ans"]):
                    correct_opt_str = o
                else:
                    wrong_opts.append(o)
            
            # Randomly pick one wrong option
            random_wrong = random.choice(wrong_opts)
            
            # Sort them alphabetically (A, B, C, D order) before printing
            remaining_options = sorted([correct_opt_str, random_wrong])
            for ro in remaining_options:
                print(ro)
                
            ans = input("Enter answer again: ").upper()
        else:
            print("\nYou already used 50-50!")
            ans = input("Enter answer again: ").upper()

    # skip lifeline
    if ans == "SKIP":
        if not used_skip:
            used_skip = True
            print("\nQuestion skipped! Here is your new question:")
            
            # Move to the next question in the list, but keep the level (prize money) the same
            question_index += 1
            current_q = questions[question_index]
            
            print(current_q["q"])
            for opt in current_q["op"]:
                print(opt)
                
            ans = input("Enter answer: ").upper()
        else:
            print("\nYou already used skip!")
            ans = input("Enter answer again: ").upper()

    # check if answer is right
    if ans == current_q["ans"]:
        print("Correct Answer!")
        money_won = prize_money
        level += 1
        question_index += 1
    else:
        print(f"Wrong Answer! The correct answer was {current_q['ans']}")
        break

print("\nGAME OVER")
print(f"Total money won: Rs. {money_won}")