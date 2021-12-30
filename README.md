## HOW TO RUN

Due to the file not being signed or having any publisher details windows might think the app is malware
I will attempt to resolve this is the future

The safest way to run this game on your computer is by downloading the mitchs_game_update.py file in the SOURCE CODE folder and run it through a python shell.
You will need to install colourama to run the game this way. Version: colorama-0.4.4 Site: https://pypi.org/project/colorama/ 
You will also need python installed. Version: 3.8.5 Site: https://www.python.org/downloads/ 

## Purpose

The files in this repository are for that of a story game created with python version 3.8.5

The purpose of this project was to get familiar with the coding language python, demonstrate learnt skills and create an interactive story game with many choices and endings.

### Story

You found this USB outside your local bank, curiosity gets the better of you so after taking it home you plug it into your computer.
The only file on it is TASK Break-Time Games, you click on it.

This is where our story begins.
From here you will go on a journey to discover who TASK is and what they are really up to.
The user will interact with SILVIA throughout the story and be tasked with navigating through linux based systems to uncover the story.
There are be choices to be made that will have consequences on the ending of the story.
Throughout the story there will be commands given to you that you can enter but extra commands were also added, try find them yourself or use the cheat sheet below. *SPOILER WARNING*

### Cheet Sheet *SPOILER WARNING*

When the game is first launched you are sent into a game of Rock, Paper or Scissors against the computer that chooses its selection randomly.
You will need to beat the computer three times to uncover the secret message that will unlock extra dialog in any of the endings, this is optional however.
The secret message is: Security is fun!

SILVIA will ask you to enter R P or S, However if you enter an invalid command repeatedly you will crash her system and this will trigger the start of the narrative.
After 7 invalid inputs that are no empty you will see a block of error messages, wait a few seconds and a link will appear.
Entering the link into your web browser will take you to a photo of binary code.
If you enter the binary into a binary to text converter you will get the text "Hello, Elliot" *This is a reference to the tv show Mr Robot*
Enter: "Hello, Elliot" back into the program to continue

Once SILVIA restarts you can enter -help to see a list of possible commands to enter but please note:
"who is TASK" will progress the story past this current point and you will not be able to check the other responses 
There is an additional unlisted command: "how are you" enter this to see additional story dialog

SILVIA will ask you to tell her who you really are, enter your name
She will then ask if you're apart of the revolution, there are three possible responses:
"yes" which leads to her getting mad at you
"no" which leads to her not believing you
"what revolution" which leads to her explaining the revolution
If no valid input is entered 3 times she will get so mad she closes the game

SILVIA will then ask you "is that what you really want":
Eneter a yes or no response 

At this point in the story SILVIA wants you to access TASK's network remotely via the SSH port on a connected machine.
SILVIA will download the ssh key to your machine
Enter: ssh admin@249.548.33.8  
Then Enter: ls

At this point you are introduces to the mysterious unkn0wn_h0st
Here there is a choice that will impact the ending you get.
If you chose to do what SILVIA wants then you cannot get the good ending
If you chose to do what unkn0wn_h0st wants then you can get the good ending
To choose SILVIA enter: cd Cooling_System && ls 
Then skip to the next section
To choose unkn0wn_h0st enter: cd Backup_Documents && ls
Then enter: cat removed_report.txt
After the story dialog ends you will be asked to enter: cd ..
Do this to go back and then enter the original command: cd Cooling_System && ls

SILVIA will want to find out who the hacker is
Enter: less RPS_backdoor.exe
SILVIA will now susspect you as exploit_user
You must enter: who is exploit_user
SILVIA will stop talking to you at this point
Enter: I found this on a usb, I have nothing to do with the revolution
Next enter: I dont want to help them, let me fix this
SILVIA will start talking to you again and ask you if you want people to die
If you say yes she will get mad and close your connection, ending the game
if you say no she will start to trust you
SILVIA will now lose connection and unkn0wn_h0st will explain his plan

This is where you decide what ending you want to have
IF YOU CHOSE UNKN0WN_H0ST
when unkn0wn_host asks if you will finish the revolution enter: yes
SILVIA will ask if you got the secret code, enter it here if you want.
Then SILVIA will shutdown
Enter: disable Cooling_System_function.sh
This will disable the cooling systems
Enter: curl http:///Mjx0nbaa.el/fH4ltPYHS5KK9.exe
This will download the payload to your machine
Enter: ./fH4ltPYHS5KK9.exe
This will execute unkn0wn_h0sts ending


IF YOU CHOSE SILVIA
Then there are two possible endings
The first ending is if you didnt read the removed_report.txt
You will be asked to restart the communications system
Enter: Com_Sys restart
SILVIA will ask if you got the secret code, enter it here if you want.
Next SILVIA's first ending will execute

The second ending is if you read removed_report.txt
SILVIA will ask if you got the secret code, enter it here if you want.
SILVIA will then ask you to delete all traces of her code 
Enter: rm SILVIA --all --permanent
This will trigger the good ending


I hope you enjoy my game!
Created by Mitch Tassicker
