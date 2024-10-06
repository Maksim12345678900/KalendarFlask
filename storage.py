from models import Event

# Хранилище для событий
events = {}

# Функция для получения всех событий
def get_events():
    return list(events.values())  # Возвращаем список всех событий

# Функция для получения события по его ID
def get_event(event_id):
    return events.get(event_id)  # Возвращаем событие по ID, если оно существует

# Функция для создания нового события
def create_event(date, title, text):
    # Проверяем, существует ли уже событие на эту дату
    if date in events.values():
        raise ValueError("Нельзя добавить больше одного события в день")
    # Создаем новое событие и добавляем его в хранилище
    new_event = Event(date, title, text)
    events[new_event.id] = new_event
    return new_event.id  # Возвращаем ID нового события

# Функция для обновления существующего события
def update_event(event_id, date, title, text):
    # Проверяем, существует ли событие с данным ID
    if event_id not in events:
        raise ValueError("Событие не найдено")
    # Обновляем данные события
    events[event_id].date = date
    events[event_id].title = title
    events[event_id].text = text
    events[event_id].validate()  # Проверка длины заголовка и текста после обновления

# Функция для удаления события по его ID
def delete_event(event_id):
    # Проверяем, существует ли событие с данным ID
    if event_id not in events:
        raise ValueError("Событие не найдено")
    # Удаляем событие из хранилища
    del events[event_id]
