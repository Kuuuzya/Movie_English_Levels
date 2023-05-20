import streamlit as st
import pandas as pd
import pickle
from io import StringIO
import pysrt
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('wordnet')

# Вычленение того, что не относится к словам
HTML = r'<.*?>'
TAG = r'{.*?}'
COMMENTS = r'[\(\[][A-Za-z ]+[\)\]]'
UPPER = r'[[A-Za-z ]+[\:\]]'
LETTERS = r'[^a-zA-Z\'.,!? ]'
SPACES = r'([ ])\1+'
DOTS = r'[\.]+'
SYMB = r"[^\w\d'\s]"

st.markdown('<h1 align="center">Movie English Level</h1>', unsafe_allow_html=True)
st.write('---')
st.markdown(
    '\n<h3>Это приложение для определение уровня английского языка, необходимого для понимания '
    '50 - 70% фильма.</h3>',
    unsafe_allow_html=True
)
st.markdown(
    '\n<b>Загрузите файл с субтитрами на английском языке в формате ".srt" и узнайте уровень английского, '
    'который требуется для комфортного просмотра фильма на английском языке!</b>',
    unsafe_allow_html=True
)

file = st.file_uploader("Загрузить субтитры в формате '.srt'", type='srt')

if st.button('Определить уровень'):
    film_subs = []
    encodings = ['', 'UTF-8-SIG', 'ISO-8859-1', 'utf-8', 'Windows-1252', 'ascii']
    encoding_number = 0

    while not film_subs:
        try:
            string = StringIO(file.getvalue().decode(encodings[encoding_number]))
            film_subs = string.getvalue()
        except LookupError:
            encoding_number += 1

    # Проверка возможности правильности кодирования, иначе - использование другого
    # Очистка
    text = re.sub(HTML, ' ', film_subs[1:])
    text = re.sub(TAG, ' ', text)
    text = re.sub(COMMENTS, ' ', text)
    text = re.sub(UPPER, ' ', text)
    text = re.sub(LETTERS, ' ', text)
    text = re.sub(DOTS, r'.', text)
    text = re.sub(SPACES, r'\1', text)
    text = re.sub(SYMB, '', text)
    text = re.sub('www', '', text)
    text = text.lstrip()
    text = text.encode('ascii', 'ignore').decode()
    text = text.lower()

    # Лемматизация слов и добавление их в отдельный список
    film_words = []
    text_list = text.split()
    lemmatizer = WordNetLemmatizer()

    for i in range(len(text_list)):
        word = lemmatizer.lemmatize(text_list[i])
        # Проверка на наличие слова в списке и отсутствия в списке имен собственных
        if word not in film_words:
            film_words.append(word)

    # Объединение слов в одну строчку
    film_words = " ".join(film_words)

    # Загрузка модели и предсказание
    with open('main.pcl', 'rb') as model_file:
        model = pickle.load(model_file)

    pred = model.predict([film_words])

    # Получение уровня английского
    pred_str = ''
    if pred[0] == 0:
        pred_str = 'A1, начальный'
    elif pred[0] == 1:
        pred_str = 'A2, ниже среднего'
    elif pred[0] == 2:
        pred_str = 'B1, средний'
    elif pred[0] == 3:
        pred_str = 'B2, выше среднего'
    elif pred[0] == 4:
        pred_str = 'C1, продвинутый'

    extension = file.name.split(".")[-1]  # Получаем расширение файла
    filename = file.name[:-len(extension) - 1]

st.markdown(
        f'<b>Уровень английского для просмотра фильма {filename}:<br> {pred_str}.</b><br>Смотрите фильм или подтягивайте английский!',
        unsafe_allow_html=True
    )
st.markdown('<br><br><i><a href="https://github.com/Kuuuzya/Movie_English_Levels">Этот проект в GitHub</a></i><br><i>©Kuuuzya. Другие проекты в <a href="https://github.com/Kuuuzya/">GitHub</a></i>', unsafe_allow_html=True)
