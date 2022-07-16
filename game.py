#import libraries and database class
from time import sleep
from db import Database

class Game:
    def __init__(self):
        self.rock = [" /ooo\\", "|ooooo|", " \\ooo/"]
        self.paper = [" ----","|    |","|    |"," ----"]
        self.scissors = ["\  /", " \/", " 00"]
        self.row1 = [" /ooo\\", " ----",  "  \  /"]
        self.row2 = ["|ooooo|", "|    |", "   \/"]
        self.row3 = [" \\ooo/", "|    |", "   00"]
        self.row4 = [" ",  " ----", " "]
        self.player1 = ""
        self.player2 = ""
        self.numrounds = None
        self.score1 = 0
        self.score2 = 0
        self.p1_firstName = ""
        self.p1_lastName = ""
        self.p2_firstName = ""
        self.p2_lastName = ""
        self.win = 0
        self.db = Database()
        self.db_name = r"c:\sqlite\scoreboard.db"


    def printRock(self):
        for i in self.rock:
            print(i)

    def printPaper(self):
        for i in self.paper:
            print(i)

    def printScissors(self):
        for i in self.scissors:
            print(i)

    def printOptions(self):
        """
        print options in columns
        """
        print(f"{' 1. Rock':<20}  {' 2. Paper':<20} {'3. Scissors':<20}")
        print(f"{' ':<20}  {' ':<20} {' ':<20}")
        print(f"{self.row1[0]:<20}  {self.row1[1]:<20} {self.row1[2]:<20}")
        print(f"{self.row2[0]:<20}  {self.row2[1]:<20} {self.row2[2]:<20}")
        print(f"{self.row3[0]:<20}  {self.row3[1]:<20} {self.row3[2]:<20}")
        print(f"{self.row4[0]:<20}  {self.row4[1]:<20} {self.row4[2]:<20}")

    
    def clear(self):
        """
        clears the screen so player can't see other player's choice
        """
        clear = "\n" * 200
        print(clear)

    
    def chooseWeapon(self):
        self.printOptions()
        choice = int(input('Enter your choice > '))
        return choice
    
    def declareWinnerRound(self):
        print(f'{self.p1_firstName}')
        print('-----------------')
        if self.player1 == 1:
            self.printRock()
        elif self.player1 == 2:
            self.printPaper()
        elif self.player1 == 3:
            self.printScissors()

        print(f'\n{self.p2_firstName}')
        print('-----------------')
        if self.player2 == 1:
            self.printRock()
        elif self.player2 == 2:
            self.printPaper()
        elif self.player2 == 3:
            self.printScissors()

        # rock = 1, paper = 2, scissors = 3
        print()
        if self.player1 == 1 and self.player2 == 1:
            print('It\'s tied!')
        elif self.player1 == 2 and self.player2 == 1:
            print(f'{self.p1_firstName} won this round...')
            self.score1 +=1
        elif self.player1 == 3 and self.player2 == 1:
            print(f'{self.p2_firstName} takes it home!')
            self.score2 +=1

        elif self.player1 == 1 and self.player2 == 2:
            print(f'{self.p2_firstName} won this round...')
            self.score2 +=1
        elif self.player1 == 2 and self.player2 == 2:
            print('Tie')
        elif self.player1 == 3 and self.player2 == 2:
            print(f'{self.p1_firstName} wins!') 
            sleep(5)
            print('jk..just this round...')
            self.score1 +=1

        elif self.player1 == 1 and self.player2 == 3:
            print(f'{self.p1_firstName} takes it home...')
            self.score1 +=1
        elif self.player1 == 2 and self.player2 == 3:
            print(f'{self.p2_firstName} won this round!')
            self.score2 +=1
        elif self.player1 == 3 and self.player2 == 3:
            print('Tied!')


    def rounds(self):
        self.numrounds = int(input('How many rounds do you want to play > '))
        
    def intro(self):
        print('\nWelcome to Rock-Paper-Scissors!\n')
        self.rounds()
        self.getName()

    def getName(self):
        print('\nPlayer One')
        print('----------')
        self.p1_firstName = input('First Name: ')
        self.p1_lastName = input('Last Name: ')
        print('\nPlayer Two')
        print('----------')
        self.p2_firstName = input('First Name: ')
        self.p2_lastName = input('Last Name: ')


    def declareWinner(self):
        """
        Declare winner for the game
        """
        if self.score1 > self.score2:
            print(f'{self.p1_firstName} wins the game!')
            self.win = 1
        elif self.score2 > self.score1:
            print(f'{self.p2_firstName} wins the game!')
            self.win = 2
        else:
            print('Nobody won this game. It\'s a tie!')
            self.win = 0

    def print_topfive(self, topfive):
        """
        print top five scores in columns and give the average score and number of players in our database
        """
        print()
        print(f"{'TOP FIVE SCORES':^31}")
        print("-------------------------------")
        print(f"{'1':^3}  {topfive['name1']:<20} {topfive['score1']:<7}")
        print(f"{'2':^3}  {topfive['name2']:<20} {topfive['score2']:<7}")
        print(f"{'3':^3}  {topfive['name3']:<20} {topfive['score3']:<7}")
        print(f"{'4':^3}  {topfive['name4']:<20} {topfive['score4']:<7}")
        print(f"{'5':^3}  {topfive['name5']:<20} {topfive['score5']:<7}")
        print()
        print(f"{'Average Score:':<20}  {round(topfive['AVG'], 2):<20}")
        print(f"{'Number of Players:':<20}  {topfive['CNT']:<20}")
        print()


    def gameover(self):
        if self.win != 0:
            if self.win == 1:
                lastName = self.p1_lastName
                firstName = self.p1_firstName
            else:
                lastName = self.p2_lastName
                firstName = self.p2_firstName

            #create table in database
            self.db.create_table(self.db_name)

            #add or update score
            self.db.add_score(firstName, lastName, self.db_name)

        #get top five from database and plug it into columns
        top_five = self.db.get_scoreboard(self.db_name)
        self.print_topfive(top_five)

        print("1. Play again")
        print("2. Delete account")
        print("3. Quit.")
        
        choice = int(input("> "))
        if choice == 1:
            self.score1 = 0
            self.score2 = 0
            self.win = 0
            self.main()
            
        elif choice ==2:
            print('Please enter your information to delete your account.')
            firstName = input('First Name: ')
            lastName = input('Last Name: ')
            self.db.delete_user(self.db_name, firstName, lastName)
            print(f'{firstName} has been removed from our records.')
        else:
            print('Ending game...')
            exit()



    def main(self):
        self.intro()
        print()
        print()

        #This will run rock paper scissors for how many rounds the player chose
        for i in range(self.numrounds):
            print(f'{self.p1_firstName}: ')
            self.player1 = self.chooseWeapon()
            self.clear()
            print(f'{self.p2_firstName}: ')
            self.player2 = self.chooseWeapon()
            self.clear()
            self.declareWinnerRound()
            print()
            if i == (self.numrounds - 1):
                print()
            else:
                print('\nNext Round...\n')
        print()

        #after the rounds are finished, declare winner and go to gameover screen for top five scores.
        self.declareWinner()
        self.gameover()