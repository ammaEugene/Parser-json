DIALOG_SEPARATOR = '\n\n-------------------------------------\n\n'

import json
import re

def analyze_conversations(json_data):
    conversations = []
    for chat_data in json_data['data']:
        conversation = []
        for message in chat_data['messages']:
            match = re.search(r'(.+)\s(.+)', message['name'])
            if match:
                name = f"{match.group(1)} {match.group(2)}"
            else:
                name = message['name']
            conversation.append({
                'type': message['type'],
                'name': name,
                'text': message['message']
            })
        conversations.append(conversation)
    return conversations

# Load the JSON data
with open('GetDummyChats.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Analyze conversations
conversations = analyze_conversations(json_data)

# Print the conversations in alternating order
for conversation in conversations:
    for message in conversation:
        if message['type'] == 'Абонент':
            print(f"Абонент: {message['text']}")
        elif message['type'] == 'Оператор':
            print(f"{message['name']}: {message['text']}")
        else:  # Handling for potential other message types
            print(f"Неизвестный тип: {message['text']}") 
    print(DIALOG_SEPARATOR)