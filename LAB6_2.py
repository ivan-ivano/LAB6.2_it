import random


def generate_list(k):
    b = []
    for k in range(k):
        b.append(random.randint(-40, 50))
    return b


def search_min_element_index(lst, min_index=-1):
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            if min_index < 0:
                min_index = i
            else:
                if lst[i] < lst[min_index]:
                    min_index = i
        i += 1
    if min_index < 0:
        return None
    else:
        return min_index


def replace_elements(lst, n):
    lst[0], lst[n] = lst[n], lst[0]
    return lst


if __name__ == '__main__':
    n = int(input('Введіть кількість елементів списку: '))
    a = generate_list(n)
    min_index = search_min_element_index(a)
    print(a)
    try:
        print('Найменший парний елемент:', a[min_index])
        print(replace_elements(a, min_index))
    except TypeError:
        print('Немає парних елементів')
