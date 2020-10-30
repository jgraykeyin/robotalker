# Robotalker 0.1 by Justin Gray
# Program for making your computer speak to your smart device
# Currently supported devices: Google Home & Amazon Echo
import pyttsx3

# Initialize the Text-to-speech module
engine = pyttsx3.init()
# Select the voice 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Number code for devices
# 1: GOOGLE HOME 
# 2: AMAZON ECHO
smart_device = 1

# Main menu of commands
def mainMenu():
    command_list = ["Commands:", 
                "[1] - Play Music",
                "[2] - Set Alarm",
                "[3] - Check Weather",
                "[4] - Check Time",
                "[5] - Watch TV or Movie",
                "[6] - User Command",
                "[0] - Quit"]
    return command_list

# Each supported device will need to have a menu button here
def selectDevice():
    while True:
        user_device = input("[G]oogle Home or [A]mazon Echo: ")
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
        engine.say("OK Google,"+command)
    elif device == 2:
        engine.say("Hey Alexa,"+command)
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
        break
    elif user_command == 1:
        speakCommand("play music",device)
    elif user_command == 2:
        print("Example> 'Tomorrow at 6 am'")
        user_alarm = input("Set alarm for: ")
        user_alarm = "set alarm for " + user_alarm
        speakCommand(user_alarm,device)
    elif user_command == 3:
        speakCommand("what's the weather today?",device)
    elif user_command == 4:
        speakCommand("what time is it?", device)
    elif user_command == 5:
        print = "What would you like to watch?"
        user_watch = input("> ")
        user_watch = "play " + user_watch
        speakCommand(user_watch,device)
    elif user_command == 6:
        print("What would you like to say to your device?")
        user_command = input("> ")
        speakCommand(user_command,device)


print("Thanks for using Robotalker!")