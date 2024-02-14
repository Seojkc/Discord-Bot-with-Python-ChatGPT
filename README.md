# Discord-Bot-with-Python-ChatGPT
It’s a mainly python programed discord bot able to answer any random questions using ChatGPT API

Libraries used : Discord, OpenAI, Spacy, Regex

The code implements a Discord chatbot using the discord.py library and integrates OpenAI's ChatCompletion model to generate responses based on the conversation's topic.

**Key Features:**
**Conversation History Storage:**

The code uses a list (storage) to store the conversation history, allowing the bot to maintain context across messages.
**Topic-based Responses:**

The bot determines the topic of the conversation using OpenAI's ChatCompletion model and responds accordingly. Topics include "Python," "greeting," "Basketball," and a general fallback ("other").
**Dynamic Greetings:**

The bot dynamically greets users based on the detected topic, providing a personalized and context-aware interaction.
**Code Modularity:**

The code is well-organized into functions and classes, promoting modularity and readability.

API Calls
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


regex patterns are created in such a way even if the order of the questions changes, still matches the pattern
for example the pattern matches for the both questions "what is token python?" and "what python token is?"

strategy used to find best match:
each words in the user questions including the errors found are saved into a list.
list having the most length means,it have the best match question to the expressions.
