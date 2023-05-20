# Проект по определению уровня английского языка в субтитрах

Запрос сформирован тем, что просмотр фильмов на оригинальном языке это популярный и действенный метод прокачаться при изучении иностранных языков. Важно выбрать фильм, который подходит студенту по уровню сложности, т.ч. студент понимал 50 - 70 % диалогов. Чтобы выполнить это условие, преподаватель должен посмотреть фильм и решить, какому уровню он соответствует. Однако это требует больших временных затрат.

<b>Цель:</b> разработать ML решение для автоматического определения уровня сложности англоязычных фильмов.

<b>Для чего мы это делаем? Где будет применяться?</b> Решение будет применяться преподавателями английского языка, чтобы оценить уровень лексики, который используется в фильме и который потребуется студенту, чтобы понять большую часть происходящего.
<b>Задача:</b> Разработать ML решение для автоматического определения уровня сложности англоязычных фильмов. За время работы над проектом вы обучите языковую модель, разработаете для неё веб-интерфейс и создадите микросервис.

<b>План работ:</b>
1. Предобработка данных
2. Выбор метрики
3. Создание модели
4. Анализ результатов
5. Сохранение модели и создание приложения Streamlit

<b>Необходимые библиотеки:</b>
- NLTK
- Numpy
- pandas
- PyPDF2
- pysrt
- re
- sklearn