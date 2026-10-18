total=0
count=0
min_numb= None
max_numb= None
while True:
    user_input = input("Enter a number (or 'stop' to finish): ")
    if user_input.lower() == "stop":
        break
    try:
        number = float(user_input)
        total += number
        count += 1
        if min_numb is None or number < min_numb:
            min_numb = number
        if max_numb is None or number > max_numb:
            max_numb = number
    except ValueError:
        print("Invalid input. please enter a valid number.")

print(f"total: {total}, Count: {count}, Min: {min_numb}, Max: {max_numb}")

