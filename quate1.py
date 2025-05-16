def add_note(filename='notes.txt'):
    print("Додавання нової нотатки:")
    date = input("Введіть дату (у форматі РРРР-ММ-ДД): ")
    location = input("Введіть локацію: ")
    text = input("Введіть текст нотатки: ")

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"Дата: {date}\n")
        file.write(f"Локація: {location}\n")
        file.write(f"Текст: {text}\n")
        file.write("\n")  # Порожній рядок для розділення нотаток

    print("Нотатку успішно додано!\n")

def main():
    print("Щоденник мандрівника")
    while True:
        add_note()
        cont = input("Бажаєте додати ще нотатку? (так/ні): ").strip().lower()
        if cont != 'так':
            print("Роботу завершено.")
            break

if __name__ == "__main__":
    main()
