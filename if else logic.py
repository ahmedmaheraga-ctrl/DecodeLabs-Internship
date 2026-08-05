print("==================================================================")
print("WELCOME TO RULE-BASED AI CHATBOT")
print("Type 'exit', 'bye', or 'quit' to end the chat")
print("==================================================================")

while True:
    
    user_input = input("you : ").lower().strip()

    if not user_input:
        continue

    if user_input in ["bye", "exit", "quit"]:
        print("chatpot : goodbye and have a nice day")

    elif user_input in ["hello" , "hi", "hey"]:
        print("chatpot : hello there!")

    elif user_input in ["how are you"]:
        print("chatpot : i am great what about you")
    
    elif user_input in ["who are you"]:
        print("chatpot : i am here to help you by answering your question")
    
    elif user_input in ["help"]:
        print("chatpot : Try saying 'hello', asking 'what is your name', or typing 'exit' to leave.")
    
    else :
        print("chatpot : i am sorry i can not understand you for options you can type help")
    
if __name__==__main__:
    chatpot()