main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


# TODO  Напишите функцию count_letters
def count_letters(text):
    dict_letters = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            # если символ является буквой
            if char not in dict_letters:
                # если символа нет в словаре
                dict_letters[char] = 1
            else:
                # если символ уже добавлен в словарь
                dict_letters[char] += 1
    # print(dict_letters)
    return dict_letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_letters):
    quantity_letters = sum(dict_letters.values())
    for key in dict_letters:
        count = dict_letters.get(key)
        dict_letters[key] = count / quantity_letters
    # print(dict_letters)
    return dict_letters


# TODO Распечатайте в столбик букву и её частоту в тексте
dict_count_letters = count_letters(main_str)
dict_frequency = calculate_frequency(dict_count_letters)
for letter in dict_frequency:
    print(f"{letter}: {dict_frequency.get(letter):.2f}")
