# Battleships Python Game
(Developer: Brian Dolan)

![Mockup image](./assets/images/am_i_responsive.png)

# Battleships
Battleships is a two-player guessing game that is typically played on a square grid. Each player has their own grid on which they place a number of "ships" throughout the grid for the opponent to guess location, without the other player being able to see where they are placed.

The objective of the game is to guess the location of the other player's ships and "sink" them all before they can sink your own ships. Players take turns calling out coordinates on the opponent's grid, such as "4A" or "6F", to try to hit a ship.

If a player's guess hits an opponent's ship, the opponent must say "hit" or "you hit my battleship" and mark that spot on their own grid to indicate the hit. If a player's guess misses, the opponent must say "miss" and mark that spot on their own grid to indicate the miss.

Once a ship has been hit on all of its squares, the player who hit the ship announces that they have "sunk" the ship. The game continues until one player has sunk all of their opponent's ships and declared the winner.

[Live webpage](https://bdolan55.github.io/CI_PP2_rock_paper_scissors/)


## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requrements and Expectations](#user-requrements-and-expectations)
    3. [User Stories](#user-stories)
3. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [Manual Testing](#Manual-Testing)
    2. [CI Python Linter](#CI-python-linter)
    3. [Performing tests on various devices](#performing-tests-on-various-devices)
    4. [Browser compatibility](#browser-compatability)
    5. [Testing User Goals](#testing-user-goals)
8. [Bugs and Future Works](#Bugs-and-Future-Works)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgement](#acknowledgement)

## Project Goals 

### User Goals
- I want to enter name to give the game a personal experience.
- I want to play the game.
- I want to read the rules of the game and how to play.
- I want to see the current leaderboard of winners.
- I want to see the current score after every guess.
- I want to see at the end of the game the final score and the ships that I have not hit.

### Site Owner Goals
- Give the player a more personal experience by allowing name entry.
- Provide the visiting user a good understanding of the game and rules.
- Provide user the ability to see the leaderboard of players.
- Prompt player on what to do next to provide a user friendly enviornment to encourage 
the visitor to return to play again.
- Show the player if there guess has hit or miss the computers ship.
- Show the player the computers guess and prompt if the computer has a hit or miss.
- Provide the player the current score at the end of every turn.
- Provide the player the score at the end of the game to see if they have won or lost the game.

## User Experience

### Target Audience
- This game would be aimed at casual gamers who enjoy a quick and easy game to pass the time.

### User Requrements and Expectations

- The ability to make a selection on the Opening Menu on what I want to do be it Play Game, Read Rules or see the leaderboard.
- The ability to make a selection on the User Guess grid and have it register with the game.
- The site visitor should be able to see the outcome of a guess in the game and understand if it is a hit or miss.
- The site visitor should be able to see the outcome of a computers guess in the game and understand if it is a hit or miss.
- The site visitor should be able to see the score after every turn to see if they are winning or losing.
- The site visitor should be able to see the outcome of the game and understand who has won or lost.
- The site visitor should be able to see the the grid at end of game to show them the locations of the missed ships.

### User Stories

#### First-time User 
1. As a first time user, I want to add my name into game to make it a more personal experience.
2. As a first time user, I want to find understand the rules to the Game.
3. As a first time user, I want to find the leaderboard.
4. As a first time user, I want to prompted on what to do next after every turn or Input error.
5. As a first time user, I want to be able to see the current score in the match.
6. As a first time user, I want to be notified when I win, lose or draw the game at the end.



#### Returning User
7. As a returning user, I want a reminder on the game rules.
8. As a returning user, I want to enjoy the game like the first time I visited ther site.
 

#### Site Owner 
9. As the site owner, Provide clear details on how to play the game.
10. As the site owner, Provide the ability to insert your name into the game to make it more interactive to the player.
11. As the site owner, Provide a user frindly interface and enjoyable experience.
12. As the site owner, Provide the ability to see the score in the current match after every turn.
13. As the site owner, Provide clear indication if the player has hit or miss the computers ship.
14. As the site owner, Provide clear indication if the computer has hit or miss the players ship.
15. As the site owner, Provide clear indication on who wins or losses the match.
16. As the site owner, Provide the player the a map of locations of the computer ships they missed in the game.
---

### Structure
The Battleships has been presented in a User friendly and easily navigated way. On running of the Balleship programs you will be met with visual que of a ship and also be prompted to enter your name. When the name is entered you will be guided to the "Main Menu" of the game. At the Main Menu, the player will be prompted to make a selection from the 3 options. The 3 options available are Play Game, Read Rules or See leaderboard. When you enter the Play Game section of the game, there is a 8x8 Grid broken into 2 selections 1-8 for Row and A-H for column, The player will then be prompted to make there row and column selection ex. A1,C5,E6,G8 etc.. The players guess will be then cross referenced with the Computers random generated ship locations and prompt the Player if they have hit or miss the Computers ship. The outcome of the guess will be then shown back to player. The computer will make a gues on the players random generated ship and the result of the computers guess will also be prompted to the player. After each round a score board will be appear and show how many ship hits the player and the computer have so far. The Player and Computer will have 10 guesses to hit all eachothers ships. After 10 turns the player will be prompted with a note saying that they have 0 turns remaining and it is Game Over. The Final scores of the Player and Computer will be shown to detrmine the winner. At the very end of the game, The computers board will be shown to the player to show the locations of the remaing ships that the player has not hit. The objective of the game is to sink all of your opponents ships. When either the Player or the Computer hit all the opponents ships they will be prompted that they have won as they have hit all ships.

---

## Technologies Used

### Languages
- Python - Used for Game functionality and interactivness of the Battleship Game.

### Frameworks & Tools
- <a href="https://github.com/">Github</a> - Storing the pushed code and Version Control of the website.
- <a href="https://www.gitpod.io/">Gitpod</a> - Online IDE.
- <a href="https://pythontutor.com/python-debugger.html#mode=edit">Python Tutor</a> - Online Python Code Exectution checker.
- <a href="https://pep8ci.herokuapp.com/">Code Institute Python Linter</a> - Online Python error checker.
- <a href="https://asciiart.website/index.php?art=transportation/nautical">ASCII Art</a> - Welcome Page Ship Art
- <a href="https://openai.com/blog/chatgpt">Chat GPT</a> Assist with checking Python Code functionality.


## Features
The website consists of a main home page hosting the Battleships game.

### Welcome Screen and Name Input
- The header appears with the welcome to Battleships Message.
- The player will be greeted with a text based image of a ship in water
- The "Enter name here" text is displayed prompting the player to enter name of player when the player presses enter they will move to the menu page.
- User Stories Covered: 1, 4, 9, and 10
<br>
<details>
<summary>Welcome Screen</summary>
<img src="/workspace/CI_PP3_battleships/assets/features_screenshots/home_screen_name.png" alt='Welcome Screen with Boat text image'>
</details>
<br>

### Main Menu
- When the player enters there name a main menu will pop up with choices on how you would like to proceed.
- The Player will be shown 3 choices of Play Game, Read Rules or Look up Leaderboard.
- The player will be prompted to enter there choice on which option they would like to do.
- If choice is Invalid they will be prompted to try "invalid Choice Enter 1,2 or 3".
- If the Player picks 2 they will be brought to the rules page and when finished reading will be prompted to press enter to go back to the Main Menu.
- If the Player picks 3 they will be shown the current leaderboard and when finished reading will be prompted to press enter to go back to the Main Menu.
- User Stories Covered: 2, 3, 4, 7 and 11
<br>
<details>
<summary>Main Menu</summary>
<img src="/workspace/CI_PP3_battleships/assets/features_screenshots/main_menu.png" alt='Main Menu'>
</details>
<br>
<details>
<summary>Menu Invalid Choice Error</summary>
<img src="/workspace/CI_PP3_battleships/assets/features_screenshots/menu_invalid_choice.png" alt='Main Menu inavlid choice error'>
</details>
<br>
<details>
<summary>Rules Page</summary>
<img src="/workspace/CI_PP3_battleships/assets/features_screenshots/game_rules_page.png" alt='Rules Page'>
</details>
<br>
<details>
<summary>Leaderboard</summary>
<img src="/workspace/CI_PP3_battleships/assets/features_screenshots/leaderboard_page.png" alt='Leaderboard printed to terminal'>
</details>
<br>

### Game Area
- The player will be met with a blank grid and a prompt for them to pick ship row 1-8 and ship column A-H.
- When the player guesses a row and column they are prompted with message telling them if they have hit or miss a ship. The players grid will be marked with either an "X" for hit or a "-" for miss. The player will be prompted with message saying you have already guessed here if they try to pick same position twice.
- The Computer then will make a guess and the player will be prompted with the outcome of the computers guess. 
- When the Player and Computer both have guessed they will be notified of the current scores.
- When both Players have used up all shots the Gam Over message will prompt and show the final score of the game.
- When the game is over the computer grid will be shown to show the positions of the ships the player missed.
- User Stories Covered: 4, 5, 6, 12, 13 14, 15 and 16
<br>
<details>
<summary>Players grid</summary>
<img src="/workspace/CI_PP3_battleships/assets/features_screenshots/player_first_blank_grid.png" alt='Player grid blank ready for guess'>
</details>
<br>
<details>
<summary>Players Guess</summary>
<img src="/workspace/CI_PP3_battleships/assets/features_screenshots/player_guess_hit.png" alt='Player Guess Hit'>
</details>
<br>
<details>
<summary>Duplicate Guess</summary>
<img src="/workspace/CI_PP3_battleships/assets/features_screenshots/duplicate_guess.png" alt='error message saying i already guessed this position'>
</details>
<br>
<details>
<summary>Players Hit on Grid</summary>
<img src="/workspace/CI_PP3_battleships/assets/features_screenshots/hit_on_grid.png" alt='Player Guess Hit on Grid'>
</details>
<br>
<details>
<summary>Computer Guess and Current Scores</summary>
<img src="/workspace/CI_PP3_battleships/assets/features_screenshots/comp_guess_with_scores.png" alt='Comp Guess and results of the match so far'>
</details>
<br>
<details>
<summary>Game Over and Final Score</summary>
<img src="/workspace/CI_PP3_battleships/assets/features_screenshots/game_over_final_score.png" alt='Game over message and final score of match'>
</details>
<br>
<details>
<summary>Players missed ships</summary>
<img src="/workspace/CI_PP3_battleships/assets/features_screenshots/player_missed_ships.png" alt='Positions of the ships the player missed'>
</details>
<br>

---

## Validation
<br>

### Manual Testing

To test my Battleships game, I first checked that all the game's features were working correctly. I made sure that the user interface was user-friendly and intuitive, and that the computer placed the ships randomly. I also verified that the game's logic was working correctly, such as ensuring that the player could only hit the opponent's ships once.

Next, I tested the game's scoring system to ensure that it accurately updated the player's score and displayed the correct message when the player won or lost.

To check for bugs and errors, I deliberately inputted incorrect data to try and break the game. For example, I tried to place a ship outside of the game board or hit the same spot twice. I also tested whether the game handled unexpected inputs and displayed helpful error messages.

Overall, by following these steps, I was able to ensure that my Battleships game was reliable, easy to use, and provided an enjoyable experience for players playing against the computer.


<br>

### CI Python Linter
The Battleships Game website was tested for Python errors using CI Python Linter.The Battleships Game Python code has passed CI Python Linter testing with no errors recorded.

<details><summary>CI Python Linter Result</summary>
<img src="/workspace/CI_PP3_battleships/assets/testing_screenshots/ci_python_linter_test.png">
</details>

<br>

### Performing tests on various devices 
The website was tested on the following devices:
- Redmi Note 11 Pro 5G
- Lenovo Ideapad Flex 5


### Browser compatability
The website was tested on the following browsers:
- Google Chrome
- Mozilla Firefox
- Microsoft Egde

---

### Testing User Goals 

#### First-time User 
1. As a first time user, I want to add my name into game to make it a more personal experience.
    * On initial loading of the page, The user will be met with a text based image of a sail ship with color utilising the colorama import. The player will then be prompted to insert there name.
2. As a first time user, I want to find understand the rules to the Game.
    * After the Player inserts there name a Main Menu will appear with 3 options to choose, The rules section is Option 2 on the Menu. 
3. As a first time user, I want to find the leaderboard.
    * After the Player inserts there name a Main Menu will appear with 3 options to choose, The Leaderboard section is Option 3 on the Menu. 
4. As a first time user, I want to prompted on what to do next after every turn.
    * When the user is playing the game and a text promp will state firstly which Row they would like to choose 1-8 and when decision made they will be prompted to choose which column they would like to choose A-H. When the choice has been made they will be notified if they have hit any of the computer ships or if they have missed. They will then be met with a "Computers Turn" text and the computer will make a random guess. The result of hit or miss will be shown to the player then asell. Then the sequnce will repeat until all ships are hitbby either the Player or Computer or until the players turns are all used. This will be end of the game.   
5. As a first time user, I want to be able to see the current score in the match. 
    * When the user and the computer have both guessed there Row and Column, The Players Score and Computer score will be shown to let the player know if they are winning or losing so far in the game. 
6. As a first time user, I want to be notified when I win, lose or draw the game at the end.
    * When the user and the computer have both used up all 10 turns, The Players Score and Computer score will be shown to let the player know if they have won or lost the game.If the Player or computer sink all there opponents ships first before turns run out, The game will also end and result prompted. 
<br>

#### Returning User
7. As a returning user, I want a reminder on the game rules.
    * Similar to the first time the user has visited, The user will be met with a "Main Menu" to navigate them to the How to Play Section with the rules of the game and how to play. 
8. As a returning user, I want to enjoy the game like the first time I visited ther site.
    * Battleships is fun and exciting game to play. The game encourages playing with its User friendly experience and is for people of all ability and ages.The user will be able to navigate the game easily and understand the interface and allow the player to enjoy the game.

#### Site Owner 
9.  As the site owner, Provide the ability to insert your name into the game to make it more interactive to the player.
    * On initial loading of the page, The player will be met with a text image of a ship. When the ship loads below there will be a prompt for the Player to enter their name.
10. As the site owner, Provide clear details on how to play the game..
    * The player enters their name and press Enter, A menu will then be loaded and will have 3 options to choose. 1. Play Game, 2. Rules and 3. Leaderboard. The player will be prompted to enter their prefered choice. The Player will press 2 to see the rules of the game and how to play.
11. As the site owner, Provide a user frindly interface and enjoyable experience.
    * The game is set up with instructions at every step to navigate the player through the Battleship Game. The player will be prompted for name and choice, will be told when the selection is invalid and guide them on how get to the next step. This makes the experience of playing the game easy and fun. The prompts throughout the game will also keep the player update on the score and how many turns are remaining. 
12. As the site owner, Provide the ability to see the score in the current match after every turn.
    * When the player makes there move, The computer will automatically go next and the player and computer scpre will be shown after every turn to keep the player updated on the score and if they are winning or losing.
13. As the site owner, Provide clear indication if the player has hit or miss the computers ship.
    * When the player decides on there Row selection 1-8 and also there column selection A-H the shot will be taken, below the Players selection they will be prompted if the guess is a hit, miss or a notification to guess again as they have already chosen that position already.  
14. As the site owner, Provide clear indication if the computer has hit or miss the players ship.
    * When the Computer auto generates the guess on there Row selection 1-8 and also there column selection A-H the shot will be taken, below the Computers selection the player will be prompted if the Computers guess is a hit or miss. The computer will not get a notification to guess again as the python code is set up to re-run the computer guess until a selection not chosen before is made.  
15. As the site owner, Provide clear indication on who wins or losses the match. 
    * When the Player and Computer have used up all turns the game will end. At the end of the game the player will be notified of the player and Computers final score and can determine who the winner is. 
16. As the site owner, Provide the player the a map of locations of the computer ships they missed in the game.
    * When the game ends and the final scores are shown to the player, they will also be shown the computers ship locations to see the locations of their guesses and also the positions of the ships the player has missed.
---

## Bugs and Future Works

- I had an issue with adding of the Welcome message screen. I had original planned to have all menu choice within the 1 main welcome screen class on the welcome screen. I was recieving run errors and unable to proceed when choice made. I found if i broke the steps up into small functions within the main Welcome screen classes the program worked. I created a handle choice function that work on if, elif and else methods to progress through the welcome screen class. The choice handle menu decision would then run the corresponding fuction to bring the user to the requested location ie. Play Game, Rules or Leaderboard.

- I had an issue with the player and computer hit counts as I was originally planning to have a view of both the player and computers boards throughout the game. The Problem was that once I had the hit count set to 5 the game would end as the function was awaiting for either the Player or computer to reach 5 on there opponents board to state who won but both were already starting with 5 "X" markers on there board at as I had the ships for both the computer and the player ships set to "X". To counter this i changed the Players Ships to "." and the computers ships set to "O". When i changed these symbols the player ship guess is looking for an "O" and the Computer guess is looking for a ".". If the either of the player hit there corresponding symbol it would count as a hit and plot a "X" on that board.  

- I had an issue that when I was in the game section the ship guess symbol "." was showing up on my user board. When i went to run a guess on that grid spot it would come back to me as you already guessed this position or the game ran into an error and would end. To fix this problem I created a third board which was included with the user guess board if else statment and will be viewable to the player as a full blank board and not show either the computer ship locations or the user ship locations. Now the player has a full clean board at the start of the game and the "-" missed ship symbol and "X" Hit symbols will only show up on the grid as it is part of the user_guess board if else statement. 

- I had an error messages on the num to char function and the get computer guess input function. The error message stated Method has no arguement. I added in a staticmethod python built in function as an object was not required for each of the functions. This removed the errors.

- In a future update I would like the leaderboard external gsheet to update automatically with a most hits in least guesses and in the quickest time. Currently the leaderboard is static and does not update. The leaderboard option on the main menu does bring you to external gsheet currently and prints the manually entered scores to terminal.

- In a future update I would like to add the option of placing your ships on the board and also add in 2,3 and 4 grid spot ships. The different type of ships could have differnt points scores and be added up at end of turns to give you a score recieved total.

---

## Deployment
The website was deployed using Heroku by following these steps:
1. Code Institute Template to be used for the heroku deployment as files within are required and ensure new line charachter is include in text areas as heroku can have problems reading the text.
2. In the Terminal type 'pip3 freeze > requirements.txt'. This updates the Code Institue Template requirements.txt file and ensures all packages or imports will work within Heroku. Also ensure to include any additional libraries like coloroama within the requirements.txt to ensure that they are uploaded and can work with heroku.
3. Login to Heroku or create a Heroku account.
4. On the Heroku Dashboard click the "Create New App" button.
5. Choose a name for your application and which must be a unique name and select your region, and press the Create app button.
6. Navigate to the settings Tab, ensure to include the python build pack and then the Node.js build pack as they are both required for the Code Institute template.
7. Add two Config VAR and CREDS keys. Enter the PORT and Value of the creds.json file and for the second Config Var use the Key of "PORT" and Value "8000"
8. Navigate to the deploy tab and choose GitHub as a deployment method.
9. Search for the repository you would like to use.
10. Click manual deploy method and press build. Ensure you have the "Master/Main" Branch selected..
11. When the app has been built click the "View" button and you will be directed to the deployed heroku site with you application.

How fork a repository by following the below steps:
1. Go to the GitHub repository.
2. Click the fork icon on the top right of the page.
3. Hit the tab with the owner of the forked repository.
4. As default the repository will be named the same as original Repo but can be changed in box besode ownser tab.
5. You can add description for repository to the fork file in the text area below the fork repository tabs.
6. Below the description box you can choose to fork the default branch or all branches for the repository.
7. Click create fork.


You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Within the file dropdown menu click the clone repository button.
3. Click the repository tab you would like to clone.
4. Choose the repository you would like to clone in dropdown menu.
5. Click and highlight repository you would like to clone.
6. Click clone button below menu.
---

## Credits

  
### Code used and adapted

In order of appearance:
- <a href="https://www.youtube.com/watch?v=alJH_c9t4zw">Knowledge Mavens</a> was used to understand The Battleships Python OOP formation and how to structure the code and have adapted functions to achieve the end result. Inspiration was also taken in sections of the page for design of my Battleships game.
- <a href="https://realpython.com/python-sleep/">Real Python</a> to assist in using Time dealys within Python Code.
- <a href="https://www.w3schools.com/python/default.asp">W3 Schools</a> was used to assist me in small programming methods I had throughout the entire Project. 
- <a href="https://www.youtube.com/watch?v=u51Zjlnui4Y">Tech with Tim</a> video was used to assist on the ability to use colorama within my python project. 
- <a href="https://stackoverflow.com/questions/48881196/how-can-i-split-up-a-long-f-string-in-python"></a>Stack Overflow</a> to assist in how to split f-string lines that are too long. 
- <a href="https://openai.com/blog/chatgpt">Chat GPT</a> to assist in checking code methods and as a reference to show where i have gone wrong with some Python code.
- <a href="https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopmentecomm">Code Institute</a> Software development course was used to assist me in small programming methods I had throughout the entire Project through the well taught and informative Tutorials. I also used the Love Sandwiches tutorials to learn how to Install Gspread and link to external Gsheet.

## Acknowledgment

* I would like to Thank my partner Sarah and 2 little boys for allowing me the opportunity and time to study and work on this project even when times were tough and hectic.
* I would like to Thank Mo Shami for his patience, encourangement and guidance throughout this project.
* I would like to thank the people within the Slack community. The Slack community has been a wealth of knowledge and help throughout this project from new users like me and all alumni, CI staff and beyond. This community is a credit to Code Institution and encourages the work ethic but also willingness to help. 
* I would lastly like to Thank the team at Code Institute for the opportunity to be involved in this course and also the staff that have been nothing but encouraging, friendly and helpful through this process.