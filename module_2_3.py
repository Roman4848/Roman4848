my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    if my_list[i] < 0:
        break
    elif my_list[i] > 0:
        print(my_list[i])
    i += 1


#while 1>0: # while True: - Это тоже самое
#    number = int(input("Введите число:"))
#    if number % 2 == 0:
#        print("Число четное")
#        continue   #continue - Пропускаетвыполнение всех оставшихсякоманд и переходит на следуещее повторения кода
#    else:
#        print("Число нечетное")
#        break    #break - помогает выйти из цыкла
#    print("Меня не забыли")
#print("Я за циклом")

#
#
#
#
#
#
#
#
#
#
#
#
#
#