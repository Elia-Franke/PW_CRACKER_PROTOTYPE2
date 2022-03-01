while True:
            print("Hallo, ich bin Robo, dein Schere-Stein-Papier Roboter. Ich werde mit dir Schere-Stein-Papier spielen!")
            choices = ["schere", "stein", "papier"]
            computer = choice(choices)
            player = None
            while player not in choices:
                player = input("Schere, Stein oder Papier? ").lower()
            if player == computer:
                os.system('color 4')
                print("Robo: ", computer)
                print("Du :", player)
                print("Robo: GLEICHSTAND!")

            elif player.lower() == "stein":
                if computer.lower() == "papier":
                    os.system('color 4')
                    print("Robo: ", computer)
                    print("Du :", player)
                    print("Robo: ICH habe gewonnen, YUHU!")

            elif player.lower() == "schere":
                if computer.lower() == "stein":
                    os.system('color 4')
                    print("Robo: ", computer)
                    print("Du :", player)
                    print("Robo: ICH habe gewonnen, YUHU!")

            elif player.lower() == "stein":
                if computer.lower() == "schere":
                    os.system('color 4')
                    print("Robo: ", computer)
                    print("Du :", player)
                    print("Robo: DU hast gewonnen :(")

            elif player.lower() == "papier":
                if computer.lower() == "stein":
                    os.system('color 4')
                    print("Robo: ", computer)
                    print("Du :", player)
                    print("Robo: DU hast gewonnen :(")

            elif player.lower() == "papier":
                if computer.lower() == "schere":
                    os.system('color 4')
                    print("Robo: ", computer)
                    print("Du :", player)
                    print("Robo: DU hast gewonnen :(")

            elif player.lower() == "schere":
                if computer.lower() == "papier":
                    os.system('color 4')
                    print("Robo: ", computer)
                    print("Du :", player)
                    print("Robo: ICH habe gewonnen, YUHU!")

            play_again = input("Nochmal? (ja/nein): ").lower()

            if play_again != 'ja':
                break
