import random;
g_field=["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"];
def s_field():                                                          # Показ текущего игрового поля
    n=0;
    while n<9:
        a=[];
        for i in range(0,3):
            a.append(g_field[n+i]);
            if a[i].strip(" ")!="[ ]":
                a[i]=" "+a[i]+ " ";                                     # приведем в нормальный вид
        print(a[0], a[1], a[2]);
        n+=3;
def pc_step(hover,inx,val):                                             # Алгоритм быстрых побед ПК над пользователем
    n_old=val.count("[ ]");
    global g_field;
    for e in ("X","0"):                                                 # Перебираем между крестиком и ноликом, и...
        if (val.count(e)==2 and hover=="hor" and n_old==1):             # если две клеточки уже заполнены...
            g_field[inx]=g_field[inx + 1]=g_field[inx + 2]=e;           # забиваем третью тем же знаком
            s_field();                                                  # выводим поле в консоль
            return True;                                                # и отмечаем победу ПК над пользователем
        if (val.count(e) == 2 and hover == "ver" and n_old==1):         # и так далее, для вертикалей и диагоналей
            g_field[inx] = g_field[inx + 3] = g_field[inx + 6] = e;
            s_field();
            return True;
        if (val.count(e) == 2 and hover == "dia_a" and n_old==1):
            g_field[0] = g_field[4] = g_field[8] = e;
            return True;
        if (val.count(e) == 2 and hover == "dia_b" and n_old==1):
            g_field[2] = g_field[4] = g_field[6] = e;
            return True;
def attack():                                                                   # Ход ПК
    hor=ver=free_cs=[];
    print("Мой ход:");
    for i in 0,3,6:                                                             # Смотрим строки
        if pc_step("hor",i,[g_field[i],g_field[i+1],g_field[i+2]])==True:       # и проверяем, может ли ПК победить
            count_i(i, 0);                                                      # если да - уходим сообщить об этом
    for i in 0,1,2:                                                             # А тут смотрим столбцы, и так далее
        if pc_step("ver",i,[g_field[i],g_field[i+3],g_field[i+6]])==True:
            count_i(i, 0);
    if pc_step("dia_a",0,[g_field[0],g_field[4],g_field[8]])==True:
        count_i(0,0);
        s_field();
    if pc_step("dia_b",0,[g_field[2],g_field[4],g_field[6]])==True:
        s_field();
        count_i(0,0);
    for x in range (0,9):                                                       # Если победить не удалось, начинаем
        if g_field[x]=="[ ]":                                                   # искать свободные клетки
            free_cs.append(x);                                                  # и забиваем их в список
    sym="X" if random.randint(0,1)==1 else "0"                                  # Выбираем, каким символом ходить
    rand=random.randint(0,len(free_cs)-1);                                      # ** Алгоритм "заглуплен" и может
    g_field[free_cs[rand]]=sym;                                                 # "подставиться", иначе у человека
    print(f"{free_cs[rand]+1}:{sym}")                                           # нет шансов - не смотрим на символ
    count_i(free_cs[rand],0);                                                   # ...И уходим показать результат хода ПК
def count_i(c,player):                                                          # Программа результата хода (и ПК и чел)
    global g_field;                                                             # А это - так, на всякий случай
    hor=ver=["[ ]"];
    x=p=ct=0;
    for p_h in range(0,9,3):                                                    # Смотрим, не "сыграла" ли строка
        if (p_h <= c <= (p_h+2)):
            hor=[g_field[p_h],g_field[p_h+1],g_field[p_h+2]];
            if (hor[0] != "[ ]" and hor.count(hor[0]) == 3):                    # И если все символы в строке совпали...
                g_field[p_h]=g_field[p_h + 1]=g_field[p_h + 2] = "-";           # ..перечеркиваем их...
                p=player+10;                                                    # И объявляем победу (чью именно - ниже)
    for p_v in range(0,3):                                                      # Тут смотрим вертикали и так далее
        if (c in (p_v,p_v+3,p_v+6)):
            ver=[g_field[p_v],g_field[p_v+3],g_field[p_v+6]];
            if (ver[0] != "[ ]" and ver.count(ver[0]) == 3):
                g_field[p_v] = g_field[p_v + 3] = g_field[p_v + 6] = "|";
                p=player+10;
    if (g_field[0]==g_field[4]==g_field[8]!="[ ]"):                             # Диагонали тоже проверим
        g_field[0]=g_field[4]=g_field[8]="\\";
        p=player+10;
    if (g_field[2]==g_field[4]==g_field[6]!="[ ]"):
        g_field[2]=g_field[4]=g_field[6]="/";
        p=player+10;
    if (p==10):                                                                 # В случае победы...
        print("Вот и всё");
        s_field();
        print("Игра окончена. И я Вас победил.");
        exit(0);                                                                # .. сообщаем и завершаем программу
    if (p==11):
        print("Есть:")
        s_field();
        print("Всё. Вы победили.");
        exit(0);
    if g_field.count("[ ]")==0:                                                 # на всяки случай
        print("НИЧЬЯ ...");
        s_field();
        exit(0);
    if (player==1):                                                             # Ну а если победы нет, то играем дальше
        attack();                                                               # и если ходил человек, то сейчас очередь ПК
        s_field();                                                              # Покажем поле после хода
    else:
        s_field();                                                              # А если ходил ПК, то покажем поле
        i_field();                                                              # .. и предложим сделать ход человеку
def m_f_field():                                                                # В случае, если ПК ходит первым...
    global g_field;
    cell=random.randint(1,9);                                                   # ..то смотрим, куда ставить...
    sym="X" if random.randint(0,1)==1 else "0";                                 # ..и что ставить
    print(f"Мой ход:\n{cell}:{sym}\nИтог хода:")
    g_field[cell-1]=sym;
def i_field():                                                                  # Ход человека
    global g_field;
    i=input("Ваш ход:\n");
    if (len(i)!=3  or 1 > int(i[0]) > 10 or i[1]!=":" or (i[2] not in ["X","0"])):  # Нормально ввел? ...
        print("Неверный ввод. Сперва следует номер клетки, затем двоеточие, затем крестик Х или нолик 0.\nЕще раз:")
        s_field();                                                              # Нет - тогда покажем еще раз поле,
        i_field();                                                              # вдруг поймет. Затем повторим еще раз
    else:
        if (g_field[int(i[0])-1]!="[ ]"):                                       # А может вводит не туда?
            print(f"Клетка номер {i[0]} уже занята.\nЕще раз:")
            s_field();
            i_field();
        else:                                                                   # Ввод прошел проверку
            print("Хорошо.");
            g_field[int(i[0]) - 1]=i[2];                                        # Записываем ход
            s_field();                                                          # и покажем, что получилось
            count_i(int(i[0])-1,1);                                             # теперь время вычислить, не победил ли человек
print (f"Крестики-нолики.\n 1  2  3\n 4  5  6\n 7  8  9");
if (random.randint(0,1)==1):                                                    # Кто сейчас ходит первым?
    m_f_field();                                                                # Если ПК
else:
    print("Сперва пишется номер клетки, затем двоеточие, затем символ - X или 0 (раскладка английская).")
s_field();                                                                      # Сперва покажем поле, затем просим ход
i_field();