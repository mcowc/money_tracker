# Check money
def check_money():
    # Vars
    money = 0
    expenses = dict()

    # Assigning vars from .txt file    
    with open('Money.txt', 'r') as file:
        for n, line in enumerate(file):
            if n == 0:
                money = int(line)
            else:
                x = line.split(", ", 1)
                expenses.update({n:[float((x)[0]), x[1]]})

    # Display our balance and expenses
    current_money = money
    
    print ("You started with: $" + str(money) + "\nYou have spent:")
    for i in range(len(expenses)):
        expense_n = i+1
        print(str(expense_n) + ".  $" + str(expenses[expense_n][0]))
        current_money = current_money - expenses[expense_n][0]
    print("You have $" + str(current_money) + " left")

    # Viewing expenses
    print("Please choose a number from 1 - " + str(len(expenses)) + " to see what the money was spent on, or type q to quit.\n")
    
    while True:
        uinput = input()
        if uinput == 'q':
                main_menu()
        else:
            try:
                uinput = int(uinput)
            except:
                print("That is not a number. Please choose a number.")
            else:
                got_num = False
                for i in range(len(expenses)):
                    if int(uinput)-1 == i:
                        print(expenses[i+1][1])
                        got_num = True
                if got_num == False:
                    print("Please choose a number within the range of 1 - " + str(len(expenses)))

# Main Menu
def main_menu():
    uinput = input("Would you like to view your balance and expenses (v) or quit (q)?\n")
    if uinput == "v":
        check_money()
    elif uinput == "q":
        exit()
    else:
        print("That is not a valid input")
        main_menu()


# Run function
main_menu()
