<img src="img/jetbrains_logo.png" width="100">

# Jetbrains Academy

these python code files are my own solution to pass the task of each project from the study program.

## Project <img src="https://image.flaticon.com/icons/png/512/148/148953.png" width="25">

 - ### Simple Tic Tac Toe 🎖️(Done)
	#### 📌 About
	Everybody remembers this paper-and-pencil game from childhood: Tic-Tac-Toe, also known as Noughts 
	and crosses or Xs and Os.A single mistake usually costs you the game, but thankfully it is simple 
	enough that most players discover the best strategy quickly. Let’s program Tic-Tac-Toe and get playing!
	
	#### 📌 Learning outcomes
	
	After finishing this project, you'll get to know a lot about planning and developing a complex program from scratch, using functions, handling errors, and processing user input.
	
	#### 📌 Description
	
	Our game is almost ready! Now let's combine what we’ve learned in the previous stages to make a game of tic-tac-toe that two players can play from the beginning (with an empty grid) through to the end (until there is a draw, or one of the players wins).
	The first player has to play as X and their opponent plays as O.
	
	#### 📌 Example
	[enter link description here](https://drive.google.com/file/d/1y8qSghGngbYYUMFfF4vXtcANvOLTUnKj/view?usp=sharing)
	
---
 - ### Simple Banking System 💳 (Done)
	#### 📌 About
	
	Everything goes digital these days, and so does money.Today, most people have credit cards, which save us time, 
	energy and nerves.From not having to carry a wallet full of cash to consumer protection, cards make our lives 
	easier in many ways. In this project, you will develop a simple banking system with database.
	
	#### 📌 Learning outcomes
	
	In this project, you will find out how the banking system works and learn about SQL. We'll also see how Luhn algorithm can help us avoid mistakes when entering the card number. As an overall result, you'll get new experience in Python.
	
	#### 📌 Description
	
	You have created the foundation of our banking system. Now let's take the opportunity to deposit money into an account, make transfers and close an account if necessary.
	Now your menu should look like this:
	```
	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	```
	if the user asks for "Balance", you should read the balance of the account from the database and output it into the console.
	
	"Add income" item should allow us to deposit money to the account.
	
	"Do transfer" item should allow transferring money to another account. 
	
	You should handle the following errors:
	
		- If the user tries to transfer more money than he/she has, output: "Not enough money!"
		- If the user tries to transfer money to the same account, output the following message: "You can't transfer money to the same account!"
		- If the receiver's card number doesn’t pass the Luhn algorithm, you should output: "Probably you made a mistake in the card number. Please try again!"
		- If the receiver's card number doesn’t exist, you should output: "Such a card does not exist."
		- If there is no error, ask the user how much money they want to transfer and make the transaction.
		- If the user chooses the "Close account" item, you should delete that account from the database.
	
	#### 📌 Example
	The symbol > represents the user input. Notice that it's not a part of the input.
	
	```code
	1. Create an account
	2. Log into account
	0. Exit
	>1

	Your card has been created
	Your card number:
	4000009455296122
	Your card PIN:
	1961

	1. Create an account
	2. Log into account
	0. Exit
	>1

	Your card has been created
	Your card number:
	4000003305160034
	Your card PIN:
	5639

	1. Create an account
	2. Log into account
	0. Exit
	>2

	Enter your card number:
	>4000009455296122
	Enter your PIN:
	>1961

	You have successfully logged in!

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>2

	Enter income:
	>10000
	Income was added!

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>1

	Balance: 10000

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>3

	Transfer
	Enter card number:
	>4000003305160035
	Probably you made a mistake in the card number. Please try again!

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>3

	Transfer
	Enter card number:
	>4000003305061034
	Such a card does not exist.

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>3

	Transfer
	Enter card number:
	>4000003305160034
	Enter how much money you want to transfer:
	>15000
	Not enough money!

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>3

	Transfer
	Enter card number:
	>4000003305160034
	Enter how much money you want to transfer:
	>5000
	Success!

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>1

	Balance: 5000

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit

	>0
	Bye!
	```
	
	
---
 - ### Food Blog Backend 📄 (Done)
	#### 📌 About
	
	Your great-grandmother asked you to copy "to these computers" all the recipes that she had been collecting 
	in her notebook for several decades. You don't like the easy ways, so you decide to build a recipe database. 
	You will need to refresh your SQL knowledge to build a simple backend.
	
	#### 📌 Learning outcomes
	
	You will create a simple backend that will allow you to populate an SQLite3 database. You will know how to deal with the primary key auto-increment and how to use foreign keys to create relationships between the tables. Learn how to deal with many-to-many relations. Work with SQL queries and database cursor methods.
	
	#### 📌 Description
	
	You decided to build a simple database query interface. The search results will be displayed on the screen, but 
	in the future, you may want to create JSON files, load them in the frontend and show them in a browser... Stop! 
	For now, the screen should suffice.Today you want to eat a dish that will contain strawberries and milk, so you 
	decide to build a query to the database which will return all dishes that contain both ingredients. 
	Thanks to this, you will learn what else you need to buy for selected recipes. And since you're not interested 
	in dinner dishes, you 	decide to add a second condition to find dishes that are appropriate for the time of day.
	Next week you have an appointment with your great-grandmother, so you can ask about a few unreadable recipes, 
	and maybe also show her what you have done.
	
	#### 📌 Example
	The symbol > represents the user input. Notice that it's not a part of the input.
	##### Example 1
	
	```code
	> python food_blog.py food_blog.db
	Pass the empty recipe name to exit.
	Recipe name: > Milkshake
	Recipe description: > Blend all ingredients and put in the fridge.
	1) breakfast  2) brunch  3) lunch  4) supper
	Enter proposed meals separated by a space: > 1 3 4
	Input quantity of ingredient <press enter to stop>: > 500 ml milk
	Input quantity of ingredient <press enter to stop>: > 1 cup strawberry
	Input quantity of ingredient <press enter to stop>: > 1 tbsp sugar
	Input quantity of ingredient <press enter to stop>: >
	Pass the empty recipe name to exit.
	Recipe name: > Hot cacao
	Recipe description: > Pour the ingredients into the hot milk. Mix it up.
	1) breakfast  2) brunch  3) lunch  4) supper
	Enter proposed meals separated by a space: > 1 2
	Input quantity of ingredient <press enter to stop>: > 250 ml milk
	Input quantity of ingredient <press enter to stop>: > 2 tbsp cacao
	Input quantity of ingredient <press enter to stop>: >
	Pass the empty recipe name to exit.
	Recipe name: > Hot cacao
	Recipe description: > Pour the ingredients into the hot milk. Mix it up.
	1) breakfast  2) brunch  3) lunch  4) supper
	Enter proposed meals separated by a space: > 1 4
	Input quantity of ingredient <press enter to stop>: > 250 ml milk
	Input quantity of ingredient <press enter to stop>: > 2 tbsp cacao
	Input quantity of ingredient <press enter to stop>: > 1 tsp sugar
	Input quantity of ingredient <press enter to stop>: >
	Pass the empty recipe name to exit.
	Recipe name: > Fruit salad
	Recipe description: > Cut strawberries and mix with other fruits. you can sprinkle everything with sugar.
	1) breakfast  2) brunch  3) lunch  4) supper
	Enter proposed meals separated by a space: > 3 4
	Input quantity of ingredient <press enter to stop>: > 10 strawberry
	Input quantity of ingredient <press enter to stop>: > 50 g black
	Input quantity of ingredient <press enter to stop>: > 1 cup blue
	Input quantity of ingredient <press enter to stop>: > 1 tsp sugar
	Input quantity of ingredient <press enter to stop>: >
	Pass the empty recipe name to exit.
	Recipe name: > 
	```
	##### Example 2:
	
	```
	> python food_blog.py food_blog.db --ingredients="sugar,milk" --meals="breakfast,brunch"
	Recipes selected for you: Hot cacao, Milkshake
	```
	##### Example 3:
	
	```
	> python food_blog.py food_blog.db --ingredients="sugar,milk,strawberry" --meals="brunch"
	There are no such recipes in the database.
	```
	
---
 - ### THE NEXT PROJECT WILL COMING SOON !!!

