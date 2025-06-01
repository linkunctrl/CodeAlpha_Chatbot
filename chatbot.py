def greet(name):
    print(f"Welcome to ChatBot {name}!")
    


def get_response(prompt, name):
        if prompt == "Hi":
            print(f"Hi back {name}")
        elif prompt == "How old are you?":
            print("I'm 5 seconds old.")
        elif prompt == "bye":
            print(f"You're leaving already? ByeBye {name}")
            return False
        else:
            print("Please enter a valid prompt.")  
        return True


namep = input("What's your name? ")
greet(namep)
while True:
    promptp = input("Enter a prompt from: 'Hi' | 'How old are you?' | 'bye'\n")
    continue_conversation = get_response(promptp, namep)    
    if not continue_conversation:
        break

