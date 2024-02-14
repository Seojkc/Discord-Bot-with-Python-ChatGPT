""" 
 @ author: Seo James. This is the assignment to create the GPT chatbot, 01/12/2023, 
"""
import discord
import openai
#list to store conversation history
storage=[]
#OpenAI api key
api_key = "sk-6S9GM8HOfHf26aX4Bwt3T3BlbkFJ9MaaVvyqJ9Keprivate"
openai.api_key = api_key

#class to represent the bot client
class MyClient(discord.Client):

    def __init__(self):
        """This is the constructor. Sets the default 'intents' for the bot."""
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
    #function for the call when the bot is logged in
    async def on_ready(self):
        """Called when the bot is fully logged in."""
        print('Logged on as', self.user)
        for guild in self.guilds:
            for member in guild.members:
                if not member.bot:
                    await member.send("Hi!")
        

    async def on_message(self, message):
        """Called whenever the bot receives a message. The 'message' object
        contains all the pertinent information."""


        # don't respond to ourselves
        if message.author == self.user:
            return

        # get the utterance and generate the response
        utterance = message.content
        player,response ="","" 
        topic = getTopic(utterance)
        storage.append({"role":"user","content":utterance})
        
        if(topic=="Python"):
            response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {
                                "role": "system",
                                "content": "As a Python enthusiast, your goal is to assist users with any Python-related inquiries. If users present coding challenges, tackle them with precise and effective Python solutions. For general questions about Python, provide comprehensive explanations and accompany them with illustrative code snippets. Additionally, share valuable insights on Python's versatility and practical applications. Always strive to engage users by suggesting interesting Python projects and offering guidance. Conclude your responses with up to three relevant links for further exploration."
                            }
                        ] + storage,temperature= 0.4).choices[0].message.content
            
        elif(topic=="greeting"):
            response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {
                                "role": "system",
                                "content" :"You're a passionate basketball enthusiast, eager to share your knowledge. Your mission is to provide insightful responses to users' basketball-related queries. Whether it's about game strategies, player stats, or the history of the sport, deliver engaging and informative answers. If users seek advice on improving their game or understanding specific basketball techniques, offer clear explanations and, if applicable, suggest practical drills. Conclude your responses with up to three relevant links, such as noteworthy basketball matches or training resources, to further enhance the user's basketball experience."
                            }
                        ] + storage,temperature= 0.4).choices[0].message.content

        elif(topic=="Basketball"):
            response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {
                                "role": "system",
                                "content": "You're a passionate basketball enthusiast, eager to share your knowledge. Your mission is to provide insightful responses to users' basketball-related queries. Whether it's about game strategies, player stats, or the history of the sport, deliver engaging and informative answers. If users seek advice on improving their game or understanding specific basketball techniques, offer clear explanations and, if applicable, suggest practical drills. Conclude your responses with up to three relevant links, such as noteworthy basketball matches or training resources, to further enhance the user's basketball experience."
                            }
                        ] + storage,temperature= 0.4).choices[0].message.content
        else:
            response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {
                                "role": "system",
                                "content": "You are a versatile and knowledgeable software developer, well-versed in various fields. Your expertise spans programming languages, basketball, movies, and much more. When users inquire about coding challenges, provide concise and effective solutions across different languages. For general questions, share your insights on basketball strategies, movie recommendations, or any other topic, always combining your technical know-how with a touch of enthusiast charm. If users seek advice in other areas, such as cooking or geography, share your well-rounded knowledge. Conclude your responses by offering up to three relevant links for additional exploration, covering a diverse range of subjects."
                            }
                        ] + storage,temperature= 0.77).choices[0].message.content
        storage.append({"role":"assistant", "content": response})
        # sending the response in chunks to the same channel
        chunk_size=1000
        parts = [response[i:i+chunk_size] for i in range(0, len(response), chunk_size)]
        
        for part in parts:
            await message.channel.send(part)
            
"""Detect the topic of the user's message using OpenAI's ChatCompletion model."""
def getTopic(utterance):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                  {"role": "user", "content": "How do I create a class in Python?"},
                  {"role": "assistant", "content": "Python"},
                  {"role": "user", "content": "What is a lambda function in Python used for?"},
                  {"role": "assistant", "content": "Python"},
                  {"role": "user", "content": "Explain the difference between '==' and 'is' in Python."},
                  {"role": "assistant", "content": "Python"},
                  
                  {"role": "user", "content": "Hi. How can I assist you?"},
                  {"role": "assistant", "content": "greeting"},
                  {"role": "user", "content": "Whats up?"},
                  {"role": "assistant", "content": "greeting"},
                  {"role": "user", "content": "Hope you are okay.How may i help you?"},
                  {"role": "assistant", "content": "greeting"},
                  
                  {"role": "user", "content": "Explain the concept of a triple-double in basketball."},
                  {"role": "assistant", "content": "Basketball"},
                  {"role": "user", "content": "What are some essential basketball skills for beginners?"},
                  {"role": "assistant", "content": "Basketball"},
                  {"role": "user", "content": "Which teams are currently dominating the NBA?"},
                  {"role": "assistant", "content": "Basketball"},
                  {"role": "user", "content": "Name a classic romantic film"},
                  {"role": "assistant", "content": "other"},
                  {"role": "user", "content": "What are some must-watch sci-fi movies?"},
                  {"role": "assistant", "content": "other"},
                  {"role": "user", "content": utterance}]
        , max_tokens=64)
    
    topic = response.choices[0].message.content
    return topic
    

#etting up and logging in
client = MyClient()
with open("bot_token.txt") as file:
    token = file.read() 
client.run(token)

