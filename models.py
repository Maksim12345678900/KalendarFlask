from uuid import uuid4

class Event:
    def __init__(self, date, title, text):
        self.id = uuid4().hex  # Уникальный идентификатор события
        self.date = date  # Дата события
        self.title = title  # Заголовок события
        self.text = text  # Текст события

        self.validate()  # Проверка длины заголовка и текста

    def validate(self):
        if len(self.title) > 30:
            raise ValueError("Максимальная длина заголовка - 30 символов")
        if len(self.text) > 200:
            raise ValueError("Максимальная длина поля Текст - 200 символов")

    # Метод для строкового представления события
    def __repr__(self):
        return f"Event({self.id}, {self.date}, {self.title}, {self.text})"