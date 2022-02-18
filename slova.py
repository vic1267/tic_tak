while True:


    print('сколько букв слова известно? ---------->>>')
    col_iz_b = int(input())
    list_iz_b = []

    for i in range(col_iz_b):
        print(i + 1, 'введите буквы по очереди ------->>>')
        list_iz_b.append(input())

    col_neiz_b = int(input('сколько букв не используются?------->>>'))
    list_neiz_b = []

    for i in range(col_neiz_b):
        print(i + 1, 'буква >>>')
        list_neiz_b.append(input())

    f = open('text.txt', 'r')
    s = [line.strip() for line in f]
    f.close()
    list_result = []
    list_result1 = []


    def fun1(buk1):
        for j in range(len(s)):
            if buk1 in s[j]:
                list_result.append(s[j])


    def fun2(buk1, buk2):
        for j in range(len(s)):
            if buk1 in s[j] and buk2 in s[j]:
                list_result.append(s[j])


    def fun3(buk1, buk2, buk3):
        for j in range(len(s)):
            if buk1 in s[j] and buk2 in s[j] and buk3 in s[j]:
                list_result.append(s[j])


    def fun4(buk1, buk2, buk3, buk4):
        for j in range(len(s)):
            if buk1 in s[j] and buk2 in s[j] and buk3 in s[j] and buk4 in s[j]:
                list_result.append(s[j])


    def fun_ud(buk):
        for j in range(len(list_result)):
            for k in list_result:
                if buk in k:
                    list_result.remove(k)


    if col_iz_b == 1:
        fun1(list_iz_b[0])
    if col_iz_b == 2:
        fun2(list_iz_b[0], list_iz_b[1])
    if col_iz_b == 3:
        fun3(list_iz_b[0], list_iz_b[1], list_iz_b[2])
    if col_iz_b == 4:
        fun4(list_iz_b[0], list_iz_b[1], list_iz_b[2], list_iz_b[3])

    if col_neiz_b != 0:
        for i in list_neiz_b:
            fun_ud(i)


    def fun_iz_buk(buk, mest):
        for i in list_result:
            ss = list(i)
            if buk == ss[mest]:
                list_result1.append(i)


    buk_mesto = input('если буквы на своем месте? да/нет -------->>>>>')
    kolvo_buk = int(input('сколько таких букв? ---------------------->>>>>'))

    if buk_mesto == 'нет':
        for i in range(len(list_result)):
            print(list_result[i])
    print(len(list_result))

    if buk_mesto == 'да':
        for i in range(kolvo_buk):
            form = input('введите букву ------------->>>')
            form1 = int(input('... и ее место ------->>>'))
            fun_iz_buk(form, form1 - 1)
        for i in range(len(list_result1)):
            print(list_result1[i])
    print(len(list_result1))
    yn = input('Слово найдено? да/нет ------->>>>>')
    if yn == 'нет':
        pass
    if yn == 'да':
        print('Приходи еще')
        break
