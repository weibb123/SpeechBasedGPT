import openai
import speech_recognition as sr

def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

recogn = sr.Recognizer()

openai.api_key = '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'
text = ''
while text !='quit':
    print('How many I help you?:')

    with sr.Microphone() as source:
        audio = recogn.record(source, duration=5)
    
    text = recogn.recognize_google(audio)
    arr_text = [text]

    print(text)
    if text != 'quit':
        get_completion_from_messages(arr_text)