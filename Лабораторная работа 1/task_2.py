# TODO Найдите количество книг, которое можно разместить на дискете

amount_pages = 100          #Количество страниц в книге
amount_rows = 50            #Число строк на странице
amount_symbol = 25          #Количество символов в строке
size_symbol_bytes = 4       #Байты для хранения кода одного символа
diskMB = 1.44               #Информационный объем дискеты

oneBookBytes = amount_pages * amount_rows * amount_symbol * size_symbol_bytes
diskBytes = diskMB * 1024 * 1024
countBooks = int(diskBytes // oneBookBytes)

print("Количество книг, помещающихся на дискету:", countBooks)
