import random

play_again = "yes"

while play_again == "yes":

    print("\nEND-OF-MONTH SURVIVAL(HOSTEL EDITION)")
    
    print("Starting Balance: ₹5000\n")

    week = 1
    money = 5000

    # Once-a-month event flags
    recharge_done = False
    friend_money_done = False

    while week <= 4:
        print("\n===================================")
        print("WEEK", week, "OF 4")
        print("Balance at start of week: ₹", money)
        print("===================================")

        
        event = random.randint(1, 10)

        # using boolean cause they are once a month events
        if event == 2 and recharge_done == False:
            print("EVENT: Phone recharge + data pack (-₹399)")
            money -= 399
            recharge_done = True

        elif event == 5 and friend_money_done == False:
            print("EVENT: Friend returned borrowed money (+₹700)")
            money += 700
            friend_money_done = True

        # REPEATABLE EVENTS
        elif event == 7:
            print("EVENT: Late-night snacks (-₹300)")
            money -= 300

        elif event == 8:
            print("EVENT: Extra laundry this week (-₹250)")
            money -= 250

        elif event == 9:
            print("EVENT: Auto ride because you were late (-₹200)")
            money -= 200

        else:
            print("EVENT: Normal hostel week.")

        print("\nHow many actions do you want to take this week?")
        print("(Choose between 1 and 5)")

        actions = int(input("Enter number of actions: "))

        if actions < 1:
            actions = 1
        elif actions > 5:
            actions = 5

        count = 1

        while count <= actions:
            print("\nAction", count)
            print("1️.Eat mess food (₹500)")
            print("2️.Eat outside / canteen (₹1000)")
            print("3️.Late-night snacks (₹300)")
            print("4️.Auto / cab when late (₹400)")
            print("5️.Movie / outing (₹600)")
            print("6️.Printing & stationery (₹200)")

            choice = input("Choose action (1-6): ")

            if choice == "1":
                money -= 500
                print("You ate mess food.")
            elif choice == "2":
                money -= 1000
                print("You ate outside.")
            elif choice == "3":
                money -= 300
                print("Late-night cravings satisfied.")
            elif choice == "4":
                money -= 400
                print("Used auto to save time.")
            elif choice == "5":
                money -= 600
                print("Went out with friends.")
            elif choice == "6":
                money -= 200
                print("Paid for printing & stationery.")
            else:
                money -= 300
                print("Unplanned expense occurred.")

            print("Balance now: ₹", money)

            count += 1

        print("\nEnd of Week", week)
        print("Balance: ₹", money)

        if money < 0:
            print("WARNING: You are in deficit!")

        week += 1

    # Game ending
    print("\n===== GAME OVER =====")

    if money > 2000:
        print("EXCELLENT!")
        print("You managed hostel life very well.")
        print("Final Balance: ₹", money)

    elif money > 0:
        print("YOU SURVIVED THE MONTH")
        print("Final Balance: ₹", money)

    elif money == 0:
        print("BROKE EVEN")
        print("Final Balance: ₹0")

    else:
        print("BANKRUPT")
        print("Deficit: ₹", -money)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

print("\nThanks for playing Hostel life is tough")
