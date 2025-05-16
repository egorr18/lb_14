def search_notes(filename='notes.txt'):
    query = input("Введіть дату або ключове слово для пошуку: ").lower()

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("Файл нотаток не знайдено.")
        return

    entries = content.strip().split('\n\n')  # розділяємо нотатки
    found = [entry for entry in entries if query in entry.lower()]

    if found:
        print(f"\nЗнайдено {len(found)} запис(ів):\n")
        for entry in found:
            print(entry)
            print("-" * 40)
    else:
        print("Записів не знайдено за цим запитом.")

if __name__ == "__main__":
    search_notes()
