# Overview

I wrote a program for Rock-Paper-Scissors. I wanted the game to simple enough so I could focus on implimenting a database with it. 

This game is a two person game. The players will choose how many rounds they want and then each player will enter their first and last name. It will then run through the rounds allowing the players to choose rock, paper, or scissors and keep track of the score for each round.
At the end of the game is where the database comes into play. It'll record the winning player in our database, and then display our scoreboard. The scoreboard will hold the top five scores, the average score across all players, and the number of players in our database. 

The purpose for this project was to learn how to work with a SQLite database. It was great learning how to work with result sets in Python! By writing this program, I'm more prepared in the future to work more in depth with databases.

[Software Demo Video](https://youtu.be/YroMP9v9O1k)

# Relational Database

I used a SQLite Database to hold the data from my game.
This database had just one table that held each player's first and last names, score, and an ID column.


# Development Environment

Tools
* SQLite Database
* Visual Studio Code

Language
* Python

Libraries
* sqlite3 library

# Useful Websites

* [SQL Tutorial W3Schools](https://www.w3schools.com/sql/default.asp)
* [SQLite Tutorial](https://www.sqlitetutorial.net/)

# Future Work

* Utilize unique pins to let users create accounts.
* Expand the database to two tables. One table would keep track of the players ID, PIN, and full name. The ID would serve as a foreign key to the second table. This table would keep track of the data from each game. Who played and who won. 
* Let users see their individual history/scores.
