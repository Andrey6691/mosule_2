parol = int(input('Введите число от 3 до 30:  '))
for i in range(1, 20):
    for j in range(i+1, 20):
        if i == j:
            continue
        else:
            sum_ = i + j
            if parol % sum_ == 0:
                print(i,j, end =' ')