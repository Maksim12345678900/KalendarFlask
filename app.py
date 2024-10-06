from flask import Flask, request, jsonify
from models import Event
from storage import get_events, get_event, create_event, update_event, delete_event

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Обработчик для получения всех событий
@app.route('/api/v1/calendar/', methods=['GET'])
def get_all_events():
    # Получаем список событий из хранилища
    events = get_events()
    # Возвращаем события в формате JSON
    return jsonify([{"id": event.id, "date": event.date, "title": event.title, "text": event.text} for event in events])

# Обработчик для получения события по его ID
@app.route('/api/v1/calendar/<int:event_id>', methods=['GET'])
def get_event_by_id(event_id):
    # Получаем событие по ID
    event = get_event(event_id)
    if event is None:
        # Если событие не найдено, возвращаем ошибку 404
        return jsonify({"error": "Событие не найдено"}), 404
    # Возвращаем найденное событие в формате JSON
    return jsonify({"id": event.id, "date": event.date, "title": event.title, "text": event.text})

# Обработчик для создания нового события
@app.route('/api/v1/calendar/', methods=['POST'])
def create_new_event():
    # Получаем данные из запроса
    data = request.get_json()
    date = data["date"]
    title = data["title"]
    text = data["text"]
    # Создаем новое событие и получаем его ID
    event_id = create_event(date, title, text)
    # Возвращаем ID нового события и статус 201 (Создано)
    return jsonify({"id": event_id}), 201

# Обработчик для обновления существующего события
@app.route('/api/v1/calendar/<int:event_id>', methods=['PUT'])
def update_event_by_id(event_id):
    # Получаем данные из запроса
    data = request.get_json()
    date = data["date"]
    title = data["title"]
    text = data["text"]
    # Обновляем событие по его ID
    update_event(event_id, date, title, text)
    # Возвращаем ID обновленного события
    return jsonify({"id": event_id})

# Обработчик для удаления события по его ID
@app.route('/api/v1/calendar/<int:event_id>', methods=['DELETE'])
def delete_event_by_id(event_id):
    # Удаляем событие по его ID
    delete_event(event_id)
    # Возвращаем сообщение об успешном удалении
    return jsonify({"message": "Событие удалено"}), 200

# Запускаем приложение
if __name__ == '__main__':
    app.run(debug=True)