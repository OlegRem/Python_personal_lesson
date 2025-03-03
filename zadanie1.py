# Часть 1: Списки и кортежи согласно задания
#1 список numbers_list из 10 целых чисел
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#2 кортеж fruits_tuple с пятью различными названиями фруктов
fruits_tuple = ('яблоко', 'банан', 'киви', 'манго', 'ананас')

#3 все числа в сумме в numbers_list и вывод
sum_numbers = sum(numbers_list)
print("Сумма чисел в numbers_list:", sum_numbers)

#4 Выводим третий элемент кортжа fruits_tuple.
#Индекс 2 соответствует третьему элементу (так как у нас нумерация начинается с 0)
print("Третий фрукт в fruits_tuple:", fruits_tuple[2])

# Часть 2: Словари и множества согласно задания
#5 Создаем словарь student_info с информацией о студенте: имя, возраст, факультет.
student_info = {
    'имя': 'Олег',
    'возраст': 40,
    'факультет': 'Бизнес-информатика'
}

#6 Здесь создаем множество courses_set с названиями учебных предметов
courses_set = {"математика", "физика", "информатика"}

#7 показываем на экран имя студента из словаря student_info.
print("Имя студента:", student_info['имя'])

#8 Добавляем новый учебный предмет в множество courses_set.
courses_set.add("Химия")
print("Обновленный набор предметов:", courses_set)


#Часть 3: Диапазоны (срезы)

#9 Создаем список alphabet с первыми 10 буквами английского алфавита (от a до j)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#10 Используя срезы, выводим первые 5ть букв алфвита
print("Первые 5 букв алфавита:", alphabet[:5])

#11 Используя срезы, выводим буквы с 5-й по 10-ю включительно
#Так как индексация начинается с 0, 5-я буква находится на позиции 4, а 10-я на позиции 9.
print("Буквы с 5-й по 10-ю:", alphabet[4:10])

#12 Выводим каждую вторую букву из списка alphabet.
print("Каждая вторая буква алфавита:", alphabet[::2])
