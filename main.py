import json
import datetime

def create_note():
    title = input("Введите заголовок: ")
    body = input("Введите текст: ")
    timestamp = datetime.datetime.now().isoformat()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    print("Запись сохранена")

def read_notes():
    filter_date = input("Введите дату в формате: (yyyy-mm-dd): ")
    filtered_notes = [note for note in notes if note["timestamp"].startswith(filter_date)]
    if filtered_notes:
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"title: {note['title']}")
            print(f"body: {note['body']}")
            print(f"date/timestamp: {note['timestamp']}")
            print("-----------")
    else:
        print("Заметки с данной датой не найдены")

def edit_note():
    note_id = int(input("Введите ID для редакции: "))
    for note in notes:
        if note["id"] == note_id:
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новый текст ")
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.datetime.now().isoformat()
            print("Заметка успешно отредактирована")
            return
    print("Заметка с данным ID не найдена")

def delete_note():
    note_id = int(input("Введите ID для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            print("Запись успешно удалена")
            return
    print("Заметка с данным ID не найдена")
try:
    with open("notes.json", "r") as file:
        notes = json.load(file)
except FileNotFoundError:
    notes = []

while True:
    print("Меню команд:")
    print("1. добавить заметку")
    print("2. найти по дате")
    print("3. отредактировать заметку")
    print("4. удалить заметку")
    print("5. выход")

    choice = input("Введите номер команды: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
    
        with open("notes.json", "w") as file:
            json.dump(notes, file, indent=4)
        break
    else:
        print("Неверно введена команда. Попробуйте снова.")
        