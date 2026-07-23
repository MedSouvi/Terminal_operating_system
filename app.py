if __name__ == '__main__':
    import json
    from os import system
    import time
    json_path = r"C:\Users\PC\Desktop\python\Histoire\Programmation_avancée\Terminal_Operating_System\users.json"
    class User:
        def __init__(self, name, age, gender, passWord):
            self.name = name
            self.age = age
            self.gender = gender
            self.passWord = passWord

        def add_user(self):

            try:
                with open(json_path, "r") as file:
                    users = json.load(file)
    
            except (FileNotFoundError, json.JSONDecodeError):
                users = []

            users.append(self.__dict__)

            print("After append:", users)

            with open(json_path, "w") as file:
                json.dump(users, file, indent=4)
                


    def help_menu():
        print("|welcome to the Terminal_Operating_System|\n")
        print("       informations of the app")
        print("        ","-"*17)
        print("         Terminal OS v1.0")
        print("        Developer: Ballahi")
        print("   Use the menu numbers to navigate.")
        print("-"*39);print("")

            
    def new_user():
        name = input("Enter your name: ")

        while True: #chiqing for age...
            try:
                age = int(input("Enter your age: "))
            except ValueError:
                print("this is not age, Try again.")
                continue
            else:
                if 5 > age or age > 170:
                    print("invalid age......")
                else:
                    break

        gender = input("Enter your gender: ")
        passWord = input("Enter a pass word: ")
        if gender.lower() in ("male", "homme", "garcon", "man", " boy", "men"):
            gender = "man"
        elif gender.lower() in ("femme", "femel", "fille", "weman"):
            gender = "weman"
        else:
            gender = 'unoune'
        return User(name, str(age), gender, passWord)
            

    def main_menu():
        print("------------<main menu>------------")
        print("1. Sign in : Create or login to an account")
        print("2. Help : Show this help menu")
        print("3. Calculator : Perform calculations")
        print("4. Games : Play available games")
        print("5. Timer : Start a timer")
        print("6. Exit : Close the program")
        print("------------------------------------")



    system('cls')
    while True:
        main_menu()
        choice = input("shoose one of this menu(1 - 6): ")
        if choice == "1":
            time.sleep(3)
            system('cls')
            user = new_user()
            user.add_user()

        elif choice == "2":
            time.sleep(3)
            system('cls')
            help_menu()
            
        elif choice == "3":
            time.sleep(3)
            system('cls')
            import Calculator
            time.sleep(3)
            system('cls')

        
        elif choice == "4":
            while True:
                time.sleep(3)
                system('cls')
                print("you have only two games....")
                print('1. Guess Game')
                print('2. Ping Pong Game')
                print('3. Return of main menu')
                choice_Game = input("Enter your choice of this menu(1 - 3): ")
                if choice_Game == '1':
                    time.sleep(3)
                    system('cls')
                    from Games import guess_game
                    time.sleep(3)
                    system('cls')
                    break
                
                elif choice_Game == '2':
                    time.sleep(3)
                    system('cls')
                    from Games import ping_pang_game
                    time.sleep(3)
                    system('cls')
                    break

                elif choice_Game == '3':
                    break

                else:
                    print("invalid choice.....")

        elif choice == '5':
            time.sleep(3)
            system('cls')
            import clock
            time.sleep(3)
            system('cls')


        elif choice == '6':
            system('cls')
            print("BY...........")
            time.sleep(3)
            break
            


        else:
            print("invalid choice......")

        
else:
    print("you cann't runing this fil....")