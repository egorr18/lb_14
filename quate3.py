def analyze_notes(filename='notes.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("Файл нотаток не знайдено.")
        return

    entries = content.strip().split('\n\n')
    total_entries = len(entries)

    locations = set()
    word_count = 0

    for entry in entries:
        lines = entry.strip().split('\n')
        for line in lines:
            if line.lower().startswith("локація:"):
                location = line.split(":", 1)[1].strip()
                locations.add(location)
            elif line.lower().startswith("текст:"):
                text = line.split(":", 1)[1].strip()
                word_count += len(text.split())

    print("Аналітика подорожей:")
    print(f"Кількість записів: {total_entries}")
    print(f"Відвідано унікальних локацій: {len(locations)}")
    print(f"Загальна кількість слів у текстах: {word_count}")

if __name__ == "__main__":
    analyze_notes()

