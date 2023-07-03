import openai
from keyWord import cyber_keywords

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a cybersecurity expert that specializes in cyber attack warnings"}]

def is_cybersecurity_related(query):
    
    keywords = cyber_keywords
    query = query.lower()
    for keyword in keywords:
        if keyword in query:       
            return True
    return False
     
def CustomChatBot(ask_me):
    messages.append({"role": "user", "content": ask_me})

    if is_cybersecurity_related(ask_me):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
    else:
        return "Please provide a cybersecurity or cyber attack warning-related query."
