import json
from pathlib import Path

# Вказуємо варіант 13
variant_number = 13

# Зчитуємо масив варіантів безпосередньо з JSON
data = json.loads(Path(__file__).with_name("student_variants.json").read_text(encoding="utf-8"))
card = data[variant_number - 1]

# 1. Зчитуємо кількість елементів n
n = int(input())

# Перевірка допустимості кількості n (від 1 до 10)
if n < 1 or n > 10:
    print("Помилка: n поза межами [1, 10]")
else:
    total_sum = 0

    # 2. Цикл for для обробки n значень
    for _ in range(n):
        val = int(input())
        
        # Перевірка допустимого діапазону одного значення [0, 24]
        if val < card["lo"] or val > card["hi"]:
            print(f"Помилка: значення поза межами [{card['lo']}, {card['hi']}]")
            break
        
        # Якщо значення менше threshold (7) — пропускаємо його
        if val < card["threshold"]:
            continue
            
        # Додаємо до загальної суми
        total_sum += val
    else:
        # Виводимо підсумкову суму годин
        print(total_sum)