a = ('Воскресенье', 'Суббота', 'Пятница', 'Четверг', 'Среда', 'Вторник', 'Понедельник')
b = int(input("сколько выходных на неделе: "))
v = ''
m = ''

for b in range(b):
    v = str(a[b]) + ' ' + v
print("Ваши выходные дни: ", v)

for b in range(6, b, -1):
    m = str(a[b]) + ' ' + m
print("Ваши рабочие дни: ", m)
