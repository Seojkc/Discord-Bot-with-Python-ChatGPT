from regex import *
from spacy import *


"""
Seo James, Mohawk College, Oct 2023
"""
"""
The file_input function is used to store the data from the txt file containing. Each line is read and added to the array. 
args: filename - the name of the file is passed as argument 

regularexpressions.txt contains the regex expressions of each questions

questions.txt contains 44 questions. 2 questions in one line for each answer. 

regex patterns are created in such a way even if the order of the questions changes, still matches the pattern
for example the pattern matches for the both questions "what is token python?" and "what python token is?"

strategy used to find best match:
each words in the user questions including the errors found are saved into a list.
list having the most length means,it have the best match question to the expressions.

Link:
https://discord.com/api/oauth2/authorize?client_id=1155975555515158598&permissions=274877913088&scope=bot

""" 

loadSpacyNlp = load("en_core_web_sm")


def file_input(filename):
    """Loads each line of the file into a list and returns it."""
    lines = []
    with open(filename) as file: # opens the file and assigns it to a variable
        for line in file:
            lines.append(line.strip()) # the strip method removes extra whitespace
    return lines

#function for the u
def understand(utterance):
    """This method processes an utterance to determine which intent it
    matches. The index of the intent is returned, or -1 if no intent
    is found."""

    global intents # declare that we will use a global variable
    global pattern
    pattern=[rf'{item}' for item in pattern]

    try:
        #String is formatted to all lowercase and empty spaces are removed from the string. 
        userQuestion = utterance
        # variable initialized to keep track of index. 
        maxCount=0
        maxCountIndex = -1
        
        
        #condition set for the userinput to have atleast 2 words. 
        if len(userQuestion.split(' '))<=2 and len(findall(r'\b(hi|hello|good (morning|afternoon|evening)|hey|namaskaram{e<=1,s<=1})\b', userQuestion,IGNORECASE))>0:
            maxCount=200
            maxCountIndex=0
        elif len(userQuestion.split(' '))<=2 and len(findall(r'\b(goodbye|see|yo(u|u again)|good night{e<=2})\b', userQuestion,IGNORECASE))>0 :
            maxCount=200
            maxCountIndex=len(pattern)-1
        else:
            for eachExpression in pattern:
              
                matches = findall(eachExpression, userQuestion,IGNORECASE)
                sumOfFound=0

                for word in matches:
                    if(len(word)>0):
                        sumOfFound+=1
                if(maxCount<sumOfFound):
                    maxCount=sumOfFound
                   
                    maxCountIndex=pattern.index(eachExpression)
                    
        if(maxCount<=1):
            maxCountIndex=-1    
        return maxCountIndex
    except ValueError:
        return -1

def generate(intent,utterance):
    
    
    """This function returns an appropriate response given a user's
    intent."""

    global responses # declare that we will use a global variable
    if intent == -1:
        doc = loadSpacyNlp(utterance)

        # Replies that I have used here are Taken from the 'COMMON REPLIES' from Chat GPT
        for entity in doc.ents:

            if entity.label_ == "PERSON":
                google_search_link = f"https://www.google.com/search?q={entity.text.replace(' ', '+')}"
                return f"Aha! {entity.text}, the enigmatic mystery wrapped in a human form. Their identity remains a puzzle to me, like a character from an unsolved riddle. Perhaps you can share more about this intriguing individual? Meanwhile, you might find some clues on [Google]( {google_search_link})."
            elif entity.label_ == "ORG":
                return f"I'm familiar with {entity.text}, but I may not have detailed information."
            elif entity.label_ == "LOC" or entity.label_ == "GPE":
                return f"{entity.text} is a location, but I might not have specific details. Google Maps may help you with this https://www.google.com/maps/search/"+entity.text.replace(" ", "%20")
            elif entity.label_ == "PRODUCT":
                return f"Ah, the elusive {entity.text}—a digital unicorn dancing in the realm of technology. While I recognize its mystical presence, my knowledge might be akin to catching a glimpse of a shooting star. Feel free to illuminate me with more details about this enigmatic creation!"
            elif entity.label_ == "DATE":
                return f"{entity.text} is a date, but I may not have specific details."
            elif entity.label_ == "LANGUAGE":
                return f"Unfortunately, I don't speak {entity.text} "
           
        else:
            return "Sorry, I don't know about that!!!"


    return responses[intent]

## Load the questions, answers and expressions
intents, responses,pattern = file_input("questions.txt") , file_input("answers.txt"),file_input("regularexpressions.txt") 

## Main Function
utterance = ""
def main():
    """Implements a chat session in the shell."""
    print("Hello! I know stuff about chat bots. When you're done talking, just say 'goodbye'.")
    global utterance
    global response
    while True:
        utterance = input(">>> ")
        if utterance == "goodbye":
            break
        
        
        intent = understand(utterance)
        response = generate(intent,utterance)
       

    print("Nice talking to you!")

## Run the chat code
# the if statement checks whether or not this module is being run
# as a standalone module. If it is beign imported, the if condition
# will be false and it will not run the chat method.
if __name__ == "__main__":
    main()