print('                          Здравствуйте, вы используете наш калькулятор подсчета оплаты кредита за месяц\n'
      '                            -------------------------------------------------------------------------\n'
      '     Данный подсчет рассчитан на "Переменный" вариант\n')

class Bank:
    def __init__(self, summ, perc, period):
        self.summ = summ
        self.perc = perc
        self.period = period

    # Метод подсчета
    def diff_int(self):
        arr = []
        mp_cnt = self.period * 12
        rest = self.summ
        mp_real = self.summ / (self.period * 12)
        while mp_cnt != 0:
            mp = mp_real + (rest * self.perc / 1200)
            arr.append(round(mp, 2))
            rest -= mp_real
            mp_cnt -= 1
        return arr, round(sum(arr), 2)


b = 'Сумма'
c = 'Проценты'
d = 'Выход'

# Ввод пользователем данные
summ1 = int(input('Введите сумму: '))
perc1 = float(input('Введите процентную ставку: '))
period1 = int(input('Введите период (год): '))

# Начало посчета
diff = Bank(summ1, perc1, period1).diff_int()

for i, v in enumerate(diff):
    if i == 0:
        for j, p in enumerate(v):
            print("Оплата за этот месяц:{:7d} : {:.2f} Рублей\n".format(j + 1, p))

# Цикл выполняемых действий
while True:
    print('\nВы можете выбрать несколько функций:\n'
          '1. Какую сумму вы ввели (Для этого введите "Сумма")\n'
          '2. Процентная ставка (Для этого введите "Проценты")\n'
          '3. Выйти из калькулятора (Для этого введите "Выход")\n')
    a = input('Введите действие: ')

    if a == b:
        if summ1 >= 5:
            print(f'\nВведенная сумма составляет: {summ1} Рублей')
        else:
            print(f'\nВведенная сумма составляет: {summ1} Рубля')
    elif a == c:
        print(f'\nПроцентная ставка составляет: {perc1}%')

    elif a == d:
        print('До свидания!')
        exit()

    else:
        print('\nНеккоректный ввод или вы ничего не написали\n')
