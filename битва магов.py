import random
import time

while True:
    print()
    print('Новая игра!')
    print()
    print('Выбор палочки:')
    print('1. Шанс на срабатывание 60%.')
    print('2. Шанс на срабатывание 80%.')
    print('3. Шанс на срабатывание 100%.')
    x=int(input()) # шанс
    if x==1:
        mag1=6
    elif x==2:
        mag1=8
    elif x==3:
        mag1=10
    mag2=7 # шанс
    mag3=9 # шанс

    life=[1,2,3]
    kolvo=1

    while True:
        print('Раунд', kolvo)
        cat=len(life)
        if 1 in life:
            print('Кого атаковать?')
            if 2 in life and not(3 in life):
                print('1. Первый колдун (шанс 70%).')
            elif 3 in life and not(2 in life):
                print('2. Второй колдун (шанс 90%).')
            else:
                print('1. Первый колдун (шанс 70%).')
                print('2. Второй колдун (шанс 90%).')
            print('3. Выстрел в воздух')
            x=int(input())
            rand=random.randint(0,10)
            if x==1:
                if mag1<rand:
                    print("Заклинание не сработало.")
                else:
                    print('Заклинание сработало. Первый колдун повержен.')
                    life.remove(2)
            elif x==2:
                if mag1<rand:
                    print("Заклинание не сработало.")
                else:
                    print('Заклинание сработало. Второй колдун повержен.')
                    life.remove(3)
            elif x==2:
                print('Вы совершили выстрел в воздух.')
        time.sleep(0.5)
        if 2 in life:
            print('Ход первого колдуна.')
            rand=random.randint(0,10)
            if (1 in life) and (3 in life) and mag1>mag2:
                print('Первый колдун совершил выстрел в воздух.')            
            elif 1 in life and not(3 in life):
                if mag2<rand:
                    print('Заклинание не сработало. Он целился в вас.')
                else:
                    print('Он целился в вас. Заклинание сработало.')
                    print('Вы повержены.')
                    life.remove(1)
            elif 3 in life and not(1 in life):
                if mag2<rand:
                        print('Заклинание не сработало. Он целился во второго колдуна.')
                else:
                    print('Он целился во второго колдуна. Заклинание сработало.')
                    print('Второй колдун повержен')
                    life.remove(3)
            else:
                if mag1>mag3:
                    if mag2<rand:
                        print('Заклинание не сработало. Он целился в вас.')
                    else:
                        print('Он целился в вас. Заклинание сработало.')
                        print('Вы повержены.')
                        life.remove(1)
                else:
                    if mag2<rand:
                        print('Заклинание не сработало. Он целился во второго колдуна.')
                    else:
                        print('Он целился во второго колдуна. Заклинание сработало.')
                        print('Второй колдун повержен')
                        life.remove(3)
        time.sleep(0.5)
        if 3 in life:
            print('Ход второго колдуна.')
            rand=random.randint(0,10)
            if 1 in life and not(2 in life):
                if mag3<rand:
                    print('Заклинание не сработало. Он целился в вас.')
                else:
                    print('Он целился в вас. Заклинание сработало.')
                    print('Вы повержены.')
                    life.remove(1)
            elif 2 in life and not(1 in life):
                if mag3<rand:
                    print('Заклинание не сработало. Он целился в первого колдуна.')
                else:
                    print('Он целился в первого колдуна. Заклинание сработало.')
                    print('Первый колдун повержен')
                    life.remove(2)
            else:
                if mag1>mag2:
                    if mag3<rand:
                        print('Заклинание не сработало. Он целился в вас.')
                    else:
                        print('Он целился в вас. Заклинание сработало.')
                        print('Вы повержены.')
                        life.remove(1)
                else:
                    if mag3<rand:
                        print('Заклинание не сработало. Он целился в первого колдуна.')
                    else:
                        print('Он целился в первого колдуна. Заклинание сработало.')
                        print('Первый колдун повержен')
                        life.remove(2)
        if cat==len(life):
            print('За раунд никто не был повержен.')
            print('Всех колдунов превратили в кошек.')
            print('Вы проиграли.')
            break
        kolvo+=1
        if len(life)==1:
            print("Победитель", life[0],'колдун')
            break
