# Robotalker 0.1 by Justin Gray
# Program for making your computer speak to your smart device
# Currently supported devices: Google Home & Amazon Echo
import pyttsx3

# Initialize the Text-to-speech module
engine = pyttsx3.init()

# Number code for devices
# 1: GOOGLE HOME 
# 2: AMAZON ECHO
smart_device = 1

# Main menu of commands
def mainMenu():
    print("Commands:")
    print("[1] - Play music")
    print("[2] - Set alarm")
    print("[3] - Check weather")
    print("[4] - Check time")
    print("[5] - Watch TV or Movie")
    print("[6] - User Command")
    print("[0] - Quit")

def selectDevice():
    print("Please select your Smart Device: ")
    while True:
        user_device = input("[G]oogle Home or [A]mazon Echo: ")
        if user_device.upper() == "G":
            smart_device = 1
            break
        elif user_device.upper() == "A":
            smart_device = 2
            break
        else:
            print("Please select G or A")

    return(smart_device)

def speakCommand(command,device):
    if device == 1:
        #command = "Ok Google,"+command
        engine.say("OK Google,"+command)
    elif device == 2:
        engine.say("Hey Alexa,"+command)
    engine.runAndWait()

print("Robotalker 0.1")
# Initial prompt to select which device the user has
device = selectDevice()
while True:

    # Display the main command menu
    mainMenu()

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


    
        


