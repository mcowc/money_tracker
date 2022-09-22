import json

# Check money
def check_money():
    # Vars
    money = 0
    expenses = dict()

    # Assigning vars from .txt file    
    with open('Money.txt', 'r') as file:
        for ln, line in enumerate(file):
            if ln == 0:
                money = int(line)
            else:
                x = line.split(" ", 1)
                dict_key = int(x[0])
                dict_value = x[1].split(', ')
                dict_value = [float(dict_value[0]), dict_value[1]]
                expenses.update({dict_key:dict_value})

    # Display our balance and expenses
    current_money = money
    print ("You started with: $" + str(money))
    print ("You have spent:")
    for i in range(len(expenses)):
        j = i+1
        print((str(j)) + ".  $" + str(expenses[j][0]))
        current_money = current_money - expenses[j][0]
    print("You have $" + str(current_money) + " left")

    # Viewing expenses
    print("Please choose a number from 1 - " + str(len(expenses)) + " to see what the money was spent on, or type q to quit.\n")
    while True:
        uinput = input()
        if uinput == 'q':
                exit()
        else:
            try:
                uinput = int(uinput)
            except:
                print("That is not a number. Please choose a number.")
            else:
                gnum = False
                for i in range(len(expenses)):
                    if int(uinput)-1 == i:
                        print(expenses[i+1][1])
                        gnum = True
                if gnum == False:
                    print("Please choose a number within the range of 1 - " + str(len(expenses)))


# Run function
check_money()
