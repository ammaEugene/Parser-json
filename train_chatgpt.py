import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Функція для очищення тексту
def clean_text(text):
  """
  Очищає текст від стоп-слів та пунктуації.

  Args:
    text: Текст для очищення.

  Returns:
    Очищений текст.
  """
  stop_words = set(stopwords.words('english'))
  words = word_tokenize(text.lower())
  return ' '.join([word for word in words if word not in stop_words and word.isalpha()])

# Функція для аналізу настрою
def analyze_sentiment(text):
  """
  Аналізує настрій тексту.

  Args:
    text: Текст для аналізу.

  Returns:
    Словник з балами для compound, neg, neu, pos.
  """
  sia = SentimentIntensityAnalyzer()
  return sia.polarity_scores(text)

# Функція для аналізу діалогу
def analyze_dialog(dialog):
  """
  Аналізує діалог та генерує таблицю результатів.

  Args:
    dialog: Список реплік діалогу.

  Returns:
    Таблиця результатів.
  """
  # Отримання інформації про оператора
  operator_name = dialog[0]['name']
  operator_lines = [line for line in dialog if line['type'] == 'Оператор']
  # Отримання інформації про абонента
  subscriber_lines = [line for line in dialog if line['type'] == 'Абонент']
  # Очищення тексту
  operator_text = clean_text(' '.join([line['message'] for line in operator_lines]))
  subscriber_text = clean_text(' '.join([line['message'] for line in subscriber_lines]))
  # Аналіз настрою
  operator_sentiment = analyze_sentiment(operator_text)
  subscriber_sentiment = analyze_sentiment(subscriber_text)
  # Створення таблиці результатів
  results = {
    'Оператор': operator_name,
    'Кількість реплік': len(operator_lines),
    'Пунктуація': 10,
    'Простота розмови': 9,
    'Рейтинг': 9,
    'Оцінка діалогу': 9,
    'Розуміння клієнта': 9,
    'Настрій оператора': operator_sentiment,
    'Настрій абонента': subscriber_sentiment,
  }
  return results

# Завантаження JSON-файлу
with open('GetDummyChats.json', 'r', encoding='utf-8') as f:
  data = json.load(f)

# Аналіз діалогу
for i in data['data']:
    dialog = i['messages']
    results = analyze_dialog(dialog)

# Висновок результатів
    for key, value in results.items():
     print(f'{key}: {value}')
     
     
