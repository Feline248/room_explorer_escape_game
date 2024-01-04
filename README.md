To play, open the terminal, command prompt, or equivalent program,
navigate to the room_explorer_game folder, and then type either py
on a windows system or python3 on mac or linux followed by
.\room_explorer_code\main.py

Example:
> cd .\Documents\CSC131\Python\room_explorer_game\
> py .\room_explorer_code\main.py

make sure you run the main.py file and not test.py

DO NOT move any files inside the room_explorer_game folder, it will
make the program crash when sounds are played

You can type "a", "controls", or "help" in the game for instructions.
There is also a controls.txt file in the info folder, as well as 
a map of the house and an audio file of recording bloopers.


The section below is for the grading of the assignment
------------------------------------------------------                                                                                                                                         
Name: 
Rachel Dahl
                                                                                                                                         
Description: 
A text-based puzzle game. The goal is to 
solve all of the puzzles and escape the house.
                                                                                                                                         
Improvements: 
-Item is now a seperate class

-There are 3 child classes of Item: Grabbable, SoundItem, and CodeItem

-controls and inventory can now be printed

-puzzles and an end goal of escaping were added

-some scenes and items play sounds

-added bonus puzzles that aren't part of the main story

-added the keyword 'use' to use objects and enter codes

-added some fun secret commands that the player can figure out

-added a hints system
