import json
import os
import datetime

notes_file = "notes.json"

if not os.path.exists(notes_file):
    with open(notes_file, "w") as f:
        json.dump([], f)


def load_notes():
    with open(notes_file, "r") as f:
        return json.load(f)


def save_notes(notes):
    with open(notes_file, "w") as f:
        json.dump(notes, f)


def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно создана!")


def read_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата/время: {note['timestamp']}")
        print("-" * 30)


def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новый текст: ")
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована!")
            break
    else:
        print("Заметка с таким ID не найдена.")


def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена!")
            break
    else:
        print("Заметка с таким ID не найдена.")


if __name__ == "__main__":
    notes = load_notes()

    while True:
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите корректный пункт меню.")
