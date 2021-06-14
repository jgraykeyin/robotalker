# Robotalker 0.1 by Aahil Ayaz
# Program for making your computer speak to your smart device.
# Built around the pyttsx3 module: https://pypi.org/project/pyttsx3/
# Currently supported devices: Clauimax & Baymax

import pyttsx3

# Initialize the Text-to-speech module
engine = pyttsx3.init()
# Select the voice 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Number code for devices
# 1: CLAUIMAX
# 2: BAYMAX
smart_device = 1

# Main menu of commands
def mainMenu():
    command_list = ["Commands:", 
                "[1] - Play Music",
                "[2] - Set Alarm",
                "[3] - Check Weather",
                "[4] - Check Time",
                "[5] - Watch TV or Movie",
                "[6] - Connect To My Phone",
                "[7] - Scan Location",
    "[8] - Check For Any Severe Or Minor Injury",
                    "[9] - Throw Ball", 
                    "[10] - Check Schedule",
                    "[11] Check signs for danger",
                    "[11] Whats My Name?",
                    
    return command_list

# Each supported device will need to have a menu button here
def selectDevice():
    while True:
        user_device = input("[C] Clauimax or [B] Baymax: ")
        if user_device.upper() == "G":
            smart_device = 1
            break
        elif user_device.upper() == "A":
            smart_device = 2
            break

    return(smart_device)

# Trigger the Text-To-Speech command
def speakCommand(command,device):
    if device == 1:
        engine.say("Clauimax,"+command)
    elif device == 2:
        engine.say("Baymax,"+command)
    engine.runAndWait()

# Initial prompt to select which device the user has
print("Robotalker 0.1")
print("Please select your Smart Device: ")
device = selectDevice()
while True:

    # Display the main command menu
    main_menu = mainMenu()
    for item in main_menu:
        print(item)

    while True:
        try:
            user_command = int(input("> "))
        except:
            print("Please input a number")
        else:
            break

    if user_command == 0:
        # Quit the program
        break
    elif user_command == 1:
        # Play Music
        speakCommand("play music",device)
    elif user_command == 2:
        # Set an alarm
        print("Example> 'Tomorrow at 6 am'")
        user_alarm = input("Set alarm for: ")
        user_alarm = "set alarm for " + user_alarm
        speakCommand(user_alarm,device)
    elif user_command == 3:
        # Check the weather
        speakCommand("what's the weather today?",device)
    elif user_command == 4:
        # Check the time
        speakCommand("what time is it?", device)
    elif user_command == 5:
        # Play a show or movie
        print = "What would you like to watch?"
        user_watch = input("> ")
        user_watch = "play " + user_watch
        speakCommand(user_watch,device)
    elif user_command == 6:
        # Custom command entered by the user
        print("Connect To My Phone?")
        user_command = input("> ")
        speakCommand(user_connect,device)


print("Thanks for using Robotalker!")
