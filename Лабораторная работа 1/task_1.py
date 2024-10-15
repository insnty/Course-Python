numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index = 4 # индекс пропущенного элемента

sum_ = sum(numbers[0:index]) + sum(numbers[index+1:])
length = len(numbers)
new_value = sum_/length

numbers[4] = new_value

print("Измененный список:", numbers)
