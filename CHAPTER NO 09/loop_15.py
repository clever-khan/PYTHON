my_list: list = [1, 2, 3, 4]
for number in my_list:
    if number == 4:
        print("Number 4 Found")
        break
    print(number)
else:
    print("Number 4 Not Found")
