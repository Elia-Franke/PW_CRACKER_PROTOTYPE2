while True:
            choices = ["schere", "stein", "papier"]
            computer = choice(choices)
            player = None
            while player not in choices:
                player = input("Schere, Stein oder Papier? ").lower()
            if player == computer:
                os.system('color 4')
                print("Computer: ", computer)
                print("Du :", player)
                print("Gleichstand")

            elif player.lower() == "stein":
                if computer.lower() == "papier":
                    os.system('color 4')
                    print("Computer: ", computer)
                    print("Du :", player)
                    print("Der Computer hat gewonnen")

            elif player.lower() == "schere":
                if computer.lower() == "stein":
                    os.system('color 4')
                    print("Computer: ", computer)
                    print("Du :", player)
                    print("Der Computer hat gewonnen")

            elif player.lower() == "stein":
                if computer.lower() == "schere":
                    os.system('color 4')
                    print("Computer: ", computer)
                    print("Du :", player)
                    print("Du hast gewonnen")

            elif player.lower() == "papier":
                if computer.lower() == "stein":
                    os.system('color 4')
                    print("Computer: ", computer)
                    print("Du :", player)
                    print("Du hast gewonnen")

            elif player.lower() == "papier":
                if computer.lower() == "schere":
                    os.system('color 4')
                    print("Computer: ", computer)
                    print("Du :", player)
                    print("Du hast gewonnen")

            elif player.lower() == "schere":
                if computer.lower() == "papier":
                    os.system('color 4')
                    print("Computer: ", computer)
                    print("Du :", player)
                    print("Der Computer hat gewonnen")

            play_again = input("Nochmal? (ja/nein): ").lower()

            if play_again != 'ja':
                break
