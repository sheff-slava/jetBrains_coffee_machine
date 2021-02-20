def print_supplies():
    print(f'''\nThe coffee machine has:
{supplies[0]} of water
{supplies[1]} of milk
{supplies[2]} of coffee beans
{supplies[3]} of disposable cups
${supplies[4]} of money\n''')


def buy():
    global supplies
    espresso = [250, 16, 4]
    latte = [350, 75, 20, 7]
    cappuccino = [200, 100, 12, 6]
    coffee = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
    if coffee != 'back':
        if supplies[3] < 1:
            print("Sorry, not enough disposable cups!\n")
        else:
            coffee = int(coffee)
            if coffee == 1:
                if supplies[0] >= espresso[0] and supplies[2] >= espresso[1]:
                    supplies[0] -= espresso[0]
                    supplies[2] -= espresso[1]
                    supplies[3] -= 1
                    supplies[4] += espresso[2]
                    print("I have enough resources, making you a coffee!\n")
                else:
                    if supplies[0] < espresso[0]:
                        print("Sorry, not enough water!\n")
                    elif supplies[2] < espresso[1]:
                        print("Sorry, not enough coffee beans!\n")
            elif coffee == 2:
                if supplies[0] >= latte[0] and supplies[1] >= latte[1] and supplies[2] >= latte[2]:
                    supplies[0] -= latte[0]
                    supplies[1] -= latte[1]
                    supplies[2] -= latte[2]
                    supplies[3] -= 1
                    supplies[4] += latte[3]
                    print("I have enough resources, making you a coffee!\n")
                else:
                    if supplies[0] < latte[0]:
                        print("Sorry, not enough water!\n")
                    elif supplies[1] < latte[1]:
                        print("Sorry, not enough milk!\n")
                    elif supplies[2] < latte[2]:
                        print("Sorry, not enough coffee beans!\n")
            elif coffee == 3:
                if supplies[0] >= cappuccino[0] and supplies[1] >= cappuccino[1] and supplies[2] >= cappuccino[2]:
                    supplies[0] -= cappuccino[0]
                    supplies[1] -= cappuccino[1]
                    supplies[2] -= cappuccino[2]
                    supplies[3] -= 1
                    supplies[4] += cappuccino[3]
                    print("I have enough resources, making you a coffee!\n")
                else:
                    if supplies[0] < cappuccino[0]:
                        print("Sorry, not enough water!\n")
                    elif supplies[1] < cappuccino[1]:
                        print("Sorry, not enough milk!\n")
                    elif supplies[2] < cappuccino[2]:
                        print("Sorry, not enough coffee beans!\n")


def fill():
    global supplies
    water = int(input("\nWrite how many ml of water do you want to add: \n"))
    milk = int(input("Write how many ml of milk do you want to add: \n"))
    coffee_beans = int(input("Write how many grams of coffee beans do you want to add: \n"))
    disposable_cups = int(input("Write how many disposable cups of coffee do you want to add: \n"))
    supplies[0] += water
    supplies[1] += milk
    supplies[2] += coffee_beans
    supplies[3] += disposable_cups


def take():
    global supplies
    print(f"\nI gave you ${supplies[4]}\n")
    supplies[4] = 0


actions = ["buy", "fill", "take", "remaining", "exit"]
supplies = [400, 540, 120, 9, 550]
action = input(f"Write action ({actions[0]}, {actions[1]}, {actions[2]}, {actions[3]}, {actions[4]}): \n")
while action != actions[4]:
    if action == actions[0]:
        buy()
    elif action == actions[1]:
        fill()
    elif action == actions[2]:
        take()
    elif action == actions[3]:
        print_supplies()
    action = input(f"Write action ({actions[0]}, {actions[1]}, {actions[2]}, {actions[3]}, {actions[4]}): \n")
