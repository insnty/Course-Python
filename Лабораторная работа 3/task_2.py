# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=","):
    first_list = first_group.split(separator)
    second_list = second_group.split(separator)
    intersection_set = set(first_list).intersection(second_list)
    intersection_list = list(intersection_set)
    intersection_list.sort()
    return intersection_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, "|")
print(result)
