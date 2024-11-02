# Найти сумму произведений из списка словарей

import json

filename = 'input.json'

def task() -> float:
    with open(filename) as file:
        data = json.load(file)
    list_multiplication = [(obj["score"] * obj["weight"]) for obj in data]
    sum_multiplication = sum(list_multiplication)
    return round(sum_multiplication, 3)

print(task())
