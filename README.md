# My Hangman Game

For my third project I have created a version of the popular game 'Hangman'. The player guesses either letter by letter or by inputting the full word until it is correct or they have run out of tries ( a maximum of 10).

This game is targeted towards those who are interested in very simple word activities, or the working of Python.

The live project can be found [here](https://project3--hangman-4b777c3fbb05.herokuapp.com/).

![Am I Responsive](documentation/amiresponsive.png)

## The Rules

- To start the game you are asked to type your name

![Type Your Name](documentation/typeyourname.png)

- You are then prompted to guess either a letter that may be part of the word, or the whole word at once

![Good Luck Choose A Letter](documentation/goodluckchoosealetter.png)

- If you guess a letter it will show where in the word that letter belongs

- If you guess the full word you will see the message 'Congratulations! The word was (insert correct word here)

![Congratulations](documentation/congratulations.png)

- If you guess incorrectly (up to a maximum of ten times) you will see the warning 'That's not right. You have x tries remaining'

![That's Not Right](documentation/thatsnotright.png)

- After you have used all of your attempts you will receive the message 'Better Luck Next Time! The word was (insert correct word here)

![Better Luck Next Time](documentation/betterlucknexttime.png)

- In both scenarios you will be able to either play again by clicking 'y' then Enter, or any other key then Enter to exit the game

<br>
To explain this further I have included a Flowchart using Lucidchart:

![Flowchart](documentation/hangmanflowchart.png)

## Future Plans

- To further improve the user experience in future versions I would limit the guesses (i.e only allow single letters with an appropriate warning if this is not adhered to).
- I would also include improved graphics with incorrect guesses resulting in a symbolic body part being added to the hangman's noose as per the classic game

## Testing

I have tested this project by completing the following:

- Inputting the through the CI PEP8 Python validator which confirmed that there were no errors

![PEP8 Validator](documentation/pep8pythonvalidator.png)

- Playinh multiple games via the Code Anywhere terminal and the Heroku deployment portal to determine the various outcomes and to ensure that the message prompts and alerts were valid and relevant

## Bugs

- I removed the capitqal letters from the list of possible words as they were not being recognised. A future solution would be to write the relevant code to fix this, however, this was an issue that I was unable to resolve on this occasion
- I also added commas after each option in the words list as the terminal would generate all of them when a guess was made as I hadn't coded correctly
- As per the 'deploying our project' tutorial I added \n to any input method used to work around the known quirk

## Technologies Used


