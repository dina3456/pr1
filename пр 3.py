lst = [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3,11, 'Привіт', 'Анаконда']  # Список, який містить числа та рядки.

def def_lst_unique(lst):
    lst_unique = []  # Створює список для збереження унікальних значень.
    lst_append = []  # Список для перетворення рядків у нижній регістр та зберігання всіх значень.
    for a in lst:  # Цикл, що проходить по всіх елементах вхідного списку `lst`.
        if type(a) == str:  # Перевіряє, чи елемент є рядком.
            a_lower = a.lower()  # Перетворює рядок у нижній регістр.
            lst_append.append(a_lower)  # Додає перетворений рядок до `lst_append`.
        else:
            lst_append.append(a)  # Якщо це не рядок, додає елемент без змін.

    lst_in_set = set()  # Створює порожню множину для перевірки унікальності значень.
    for item in lst_append:  # Цикл для проходження по всіх елементах у `lst_append`.
        if item not in lst_in_set:  # Перевіряє, чи елемент ще не є у множині.
            lst_unique.append(item)  # Додає унікальний елемент до `lst_unique`.
            lst_in_set.add(item)  # Додає елемент до множини для уникнення повторень.

    return lst_unique and lst_in_set  # Повертає список унікальних значень та множину.

def def_lst_sort(lst):
    lst_str = []  # Створює список для зберігання рядків.
    lst_int = []  # Створює список для зберігання чисел.

    lst_sort = r.copy()  # Копіює список `r` для сортування.
    for k in lst_sort:  # Цикл для проходження по всіх елементах списку `lst_sort`.
        if type(k) == int:  # Перевіряє, чи елемент є числом.
            lst_int.append(k)  # Додає число до списку `lst_int`.
        elif type(k) == str:  # Перевіряє, чи елемент є рядком.
            lst_str.append(k)  # Додає рядок до списку `lst_str`.

    lst_str.sort()  # Сортує список рядків у алфавітному порядку.
    lst_int.sort()  # Сортує список чисел у порядку зростання.

    return lst_int + lst_str  # Об'єднує відсортовані списки чисел і рядків та повертає їх.

r = def_lst_unique(lst)  # Викликає функцію `def_lst_unique` для отримання унікальних значень зі списку `lst`.
sorted_list = def_lst_sort(r)  # Викликає функцію `def_lst_sort` для сортування унікальних значень.

print(sorted_list)  # Виводить відсортований список.
