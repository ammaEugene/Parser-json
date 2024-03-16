OPEN_AI_KEY = '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'

import json

# Функция для анализа текста через ChatGPT API
def analyze_text(text):
    # Здесь должен быть код для отправки запроса к ChatGPT API и анализа результата
    # Возвратим случайные значения для примера
    return {
        "quality_score": 7,
        "topic": "Техническая поддержка",
        "lexical_analysis": 8,
        "mood_analysis": 6,
        "key_moments": ["перепідключити кабель інтернету"],
        "operator_errors": ["нет"],
        "next_steps": ["перевірка з'єднання"],
        "stop_words": ["а", "ї", "чи"],
        "mandatory_actions": ["перепідключити кабель інтернету"],
        "translation": {
            "quality_score": "Якість діалогу",
            "topic": "Тематика діалогу",
            "lexical_analysis": "Лексичний аналіз",
            "mood_analysis": "Аналіз настрою",
            "key_moments": "Ключові моменти діалогу",
            "operator_errors": "Помилки оператора",
            "next_steps": "Дальші дії",
            "stop_words": "Стоп-слова",
            "mandatory_actions": "Обов'язкові дії"
        }
    }

# Открываем JSON файл
with open('GetDummyChats.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Анализируем каждое сообщение в диалоге
for message in data["data"][0]["messages"]:
    if message["type"] == "Оператор":
        print("Сообщение оператора:")
        print(message["message"])
        analysis_result = analyze_text(message["message"])
        for criterion, value in analysis_result.items():
            print(f"{analysis_result['translation'][criterion]}: {value}")
        print()
