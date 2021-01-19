from math import factorial, e


def combinations(n: int, k: int):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def bernoulli(n: int, k: int, p: float):
    c = combinations(n, k)
    q = 1 - p
    return c*(p**k)*(q**(n-k))


def poisson(n: int, m: int, p: float):
    lam = p*n
    return lam**m * e**(-1*lam) / factorial(m)


def task_1():
    """
    Задача:
        Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
        Стрелок выстрелил 100 раз.
        Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
    Решение:
        В задаче распределение дискретное, малое количество событий,
        вероятность события высокая, соответственно:
        Распределение биномиальное. Используем формулу Бернулли.
        n = 100
        k = 85
        p = 0.8
        q = 1-p = 0.2
        n-k = 100-85 = 15
                   85     85    15
        P(k=85) = C    * p   * q
                   100
    Ответ:
        Вероятность того, что стрелок попадет в цель ровно 85 раз составляет 4.81%
    """
    n = 100
    k = 85
    p = 0.8

    print("Задача 1")
    print(f"    n = {n}, k = {k}, p = {p}. Используем формулу Бернулли.")
    result = bernoulli(n, k, p)
    print(f"    Ответ: вероятность того, что стрелок попадет в цель ровно {k} раз составляет {result:.4f}")
    print()


def task_2():
    """
    Задача:
        Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
        В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
        Какова вероятность, что ни одна из них не перегорит в первый день?
        Какова вероятность, что перегорят ровно две?
    Решение:
        В задаче распределение дискретное, большое количество событий,
        вероятность события низкая, соответственно:
        применяем формулу Пуассона
        p = 0.0004
        n = 5000
        lambda = p*n = 5000*0.0004 = 2
        m_1 = 0
        m_2 = 2
    Ответ:
        Вероятность, что ни одна из них не перегорит в первый день составляет 13.53%
        Вероятность, что перегорят ровно две лампы составляет 27.07%
    """
    print("Задача 2")
    n = 5000
    p = 0.0004
    m_1 = 0
    m_2 = 2
    print(f"    n = {n}, p = {p:.4f}. Используем формулу Пуассона.")
    result_1 = poisson(n, m_1, p)
    result_2 = poisson(n, m_2, p)
    print(f"    Ответ 1. Вероятность, что ни одна из ламп не перегорит в первый день составляет {result_1:.4f}")
    print(f"    Ответ 2: Вероятность, что перегорят ровно две лампы составляет {result_2:.4f}")
    print()


def task_3():
    """
    Задача:
        Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
    Решение:
        В задаче распределение дискретное, малое количество событий,
        вероятность события высокая, соответственно:
        Распределение биномиальное. Используем формулу Бернулли.
        n = 144
        k = 70
        p = 0.5 (орел или решка)
        q = 1-p = 0.5
        n-k = 144-70 = 74
                   70     70    74
        P(k=70) = C    * p   * q
                   144
    Ответ:
        Вероятность, что орел выпадет ровно 70 раз составляет 6.28%
    """
    n = 144
    k = 70
    p = 0.5

    print("Задача 3")
    print(f"    n = {n}, k = {k}, p = {p}. Используем формулу Бернулли.")
    result = bernoulli(n, k, p)
    print(f"    Ответ: вероятность, что орел выпадет ровно {k} раз составляет {result:.4f}")
    print()


def task_4():
    """

    Задача:
        В первом ящике находится 10 мячей, из которых 7 - белые.
        Во втором ящике - 11 мячей, из которых 9 белых.
        Из каждого ящика вытаскивают случайным образом по два мяча.
        I.   Какова вероятность того, что все мячи белые?
        II.  Какова вероятность того, что ровно два мяча белые?
        III. Какова вероятность того, что хотя бы один мяч белый?
    Решение:
        I. Какова вероятность того, что все мячи белые?
            Событие наступает, когда последовательно достают белые мячи из ящиков
            Первый вариант решения:
            Вероятность достать первый белый мяч из 1-го ящика 7/10,
            затем вероятность достать второй белый мяч из 1-го ящика 6/9,
            далее вероятность достать первый белый мяч из 2-го ящика 9/11,
            далее вероятность достать второй белый мяч из 2-го ящика 8/10:
            7/10 * 6/9 * 9/11 * 8/10 = 0.3055 или 30.5%
            Второй вариант решения:
            Перестановки 7 белых мячей в первом ящике
             2
            C = 7! / 2!*(7-2)! = 21
             7
            Всего перестановок в первом ящике (10 мячей)
             2
            C = 10! / 2!*(10-2)! = 45
             10

            Перестановки 9 белых мячей во втором ящике
             2
            C = 9! / 2!*(9-2)! = 36
             9
            Всего перестановок во втором ящике (11 мячей)
             2
            C = 11! / 2!*(11-2)! = 55
             11
            События последовательны, рассчитываем вероятность:
            (21/45) * (36/55) = 0.3055 или 30.5%
        Ответ: вероятность того, что все 4 извлеченных мяча белые составляет 30.5%


        II. Какова вероятность того, что ровно два мяча белые?
            три варианта извлечения белых мячей:
            1) 2 белых в первом ящике, 2 черных во втором:
                (21/45) * (1/55) = 0.0085
            2) 2 черных в первом ящике, 2 белых во втором:
                (3/45) * (36/55) = 0.0436
            3) белый и черный в первом, белый и черный во втором:
                (7*3/45) * (9*2/55) = 0.1527
            итого вероятность 0.0085 + 0.0436 + 0.1527 = 0.2048 или 20.5%
        Ответ: вероятность того, что ровно два мяча белые составляет 20.5%


        III. Какова вероятность того, что хотя бы один мяч белый?
            Для решения задачи достаточно посчитать вероятность случая,
            когда выпадают все мячи черные и вычесть вероятность из 1.
            Вероятность достать первый черный мяч из 1-го ящика 3/10,
            затем вероятность достать второй черный мяч из 1-го ящика 2/9,
            далее вероятность достать первый черный мяч из 2-го ящика 2/11,
            далее вероятность достать второй черный мяч из 2-го ящика 1/10:
            3/10 * 2/9 * 2/11 * 1/10 = 0.0012
            1 - 0.0012 = 0,9988
        Ответ: вероятность того, что хотя бы один мяч белый составляет 0,9988 или близка к 100%

    """
    print("Задача 4")

    # Вычисляем комбинации
    n_box_1_total = 10  # Всего мячей в первом ящике
    n_box_1_white = 7  # Белых мячей в первом ящике
    n_box_1_black = n_box_1_total - n_box_1_white  # Черных мячей в первом ящике
    n_box_2_total = 11  # Всего мячей во втором ящике
    n_box_2_white = 9  # Белых мячей во втором ящике
    n_box_2_black = n_box_2_total - n_box_2_white  # Черных мячей во втором ящике
    k_box_one = 1  # Один мяч
    k_box_two = 2  # Два мяча
    combs_box_1_total = combinations(n_box_1_total, k_box_two)  # Всего перестановок двух мячей в первом ящике
    combs_box_2_total = combinations(n_box_2_total, k_box_two)  # Всего перестановок двух мячей во втором ящике
    combs_box_1_white_one = combinations(n_box_1_white, k_box_one)  # Перестановок одного белого мяча в первом ящике
    combs_box_1_black_one = combinations(n_box_1_black, k_box_one)  # Перестановок одного черного мяча в первом ящике
    combs_box_1_white_two = combinations(n_box_1_white, k_box_two)  # Перестановок двух белых мячей в первом ящике
    combs_box_1_black_two = combinations(n_box_1_black, k_box_two)  # Перестановок двух черных мячей в первом ящике
    combs_box_2_white_one = combinations(n_box_2_white, k_box_one)  # Перестановок одного белого мяча во втором ящике
    combs_box_2_black_one = combinations(n_box_2_black, k_box_one)  # Перестановок одного белого мяча во втором ящике
    combs_box_2_white_two = combinations(n_box_2_white, k_box_two)  # Перестановок двух белых мячей во втором ящике
    combs_box_2_black_two = combinations(n_box_2_black, k_box_two)  # Перестановок двух черных мячей во втором ящике
    print(f"    Комбинации мячей, порядок не имеет значения:")
    print(f"        Ящик 1: "
          f"один белый = {combs_box_1_white_one}, "
          f"один черный = {combs_box_1_black_one}, "
          f"два белых = {combs_box_1_white_two}, "
          f"два черных = {combs_box_1_black_two}, "
          f"всего = {combs_box_1_total}")
    print(f"        Ящик 2: "
          f"один белый = {combs_box_2_white_one}, "
          f"один черный = {combs_box_2_black_one}, "
          f"два белых = {combs_box_2_white_two}, "
          f"два черных = {combs_box_2_black_two}, "
          f"всего = {combs_box_2_total}")
    print()
    print(f"    Вопрос I. Какова вероятность того, что все мячи белые?")
    result_1_v1 = (7 / 10) * (6 / 9) * (9 / 11) * (8 / 10)
    print(f"        Способ полной вероятности.")
    print(f"        Вариант 1. Ответ: вероятность того, что все мячи белые {result_1_v1:.4f}")
    result_1_2 = (combs_box_1_white_two / combs_box_1_total) * (combs_box_2_white_two / combs_box_2_total)
    print(f"        Сочетанием.")
    print(f"        Вариант 2. Ответ: вероятность того, что все мячи белые {result_1_2:.4f}")
    print()

    print(f"    Вопрос II. Какова вероятность того, что ровно два мяча белые?")
    # вероятность 2 белых из первого ящика и 2 черных из второго ящика
    result_2_white2_black2 = (combs_box_1_white_two / combs_box_1_total) * (combs_box_2_black_two / combs_box_2_total)
    print(f"        вероятность 2 белых из первого ящика и 2 черных из второго ящика = {result_2_white2_black2:.4f}")
    # вероятность 2 черных из первого ящика и 2 белых из второго ящика
    result_2_black2_white2 = (combs_box_1_black_two / combs_box_1_total) * (combs_box_2_white_two / combs_box_2_total)
    print(f"        вероятность 2 черных из первого ящика и 2 белых из второго ящика = {result_2_black2_white2:.4f}")
    # вероятность 1 белый и 1 черный из первого ящика и 1 белый и 1 черный из второго ящика
    result_2_white1_black1 = \
        (combs_box_1_white_one * combs_box_1_black_one / combs_box_1_total) * \
        (combs_box_2_white_one * combs_box_2_black_one / combs_box_2_total)
    print(f"        вероятность 1 белый и 1 черный из 1-го ящика и 1 белый и 1 черный из 2-го ящика = "
          f"{result_2_white1_black1:.4f}")
    result_2_v1 = result_2_white2_black2 + result_2_black2_white2 + result_2_white1_black1
    print(f"        сумма вероятностей {result_2_white2_black2:.4f} + {result_2_black2_white2:.4f} + "
          f"{result_2_white1_black1:.4f} = {result_2_v1:.4f}")
    print(f"        Вариант 1. Ответ: вероятность того, что ровно два мяча белые составляет {result_2_v1:.4f}")

    # Проверка способом полной вероятности
    a1 = (7/10)*(3/9) * (9/11)*(2/10)  # бч бч
    a2 = (7/10)*(3/9) * (2/11)*(9/10)  # бч чб
    a3 = (7/10)*(6/9) * (2/11)*(1/10)  # бб чч
    a4 = (3/10)*(2/9) * (9/11)*(8/10)  # чч бб
    a5 = (3/10)*(7/9) * (9/11)*(2/10)  # чб бч
    a6 = (3/10)*(7/9) * (2/11)*(9/10)  # чб чб
    result_2_v2 = a1 + a2 + a3 + a4 + a5 + a6
    print(f"        Проверка способом полной вероятности.")
    print(f"        Вариант 2. Ответ: вероятность того, что ровно два мяча белые составляет {result_2_v2:.4f}")
    print()

    print(f"    Вопрос III. Какова вероятность того, что хотя бы один мяч белый?")
    print(f"        Вычислим вероятность появления только черных мячей и вычтем из 1")
    result_3_black2_black2 = (combs_box_1_black_two / combs_box_1_total) * (combs_box_2_black_two / combs_box_2_total)
    result_3_v1 = 1 - result_3_black2_black2
    print(f"        Вероятность появления только черных мячей = {result_3_black2_black2:.4f}")
    print(f"        Вероятность появления хотя бы одного белого мяча: "
          f"1 - {result_3_black2_black2:.4f} = {result_3_v1:.4f}")
    print(f"        Вариант 1. Ответ: Вероятность того, что хотя бы один мяч белый составляет {result_3_v1:.4f}")

    result_3_v2 = 1 - (3 / 10) * (2 / 9) * (2 / 11) * (1 / 10)
    print(f"        Проверка способом полной вероятности.")
    print(f"        Вариант 2. Ответ: Вероятность того, что хотя бы один мяч белый составляет {result_3_v2:.4f}")
    print()


task_1()
task_2()
task_3()
task_4()
