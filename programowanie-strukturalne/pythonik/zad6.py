def christmasTree(height):
    for i in range(1, height):
        for j in range(1, height//2):
            print(' ', end="")
        for k in range (1,i):
            print('*', end="")

num = input('Podaj wysokosc choinki: ')
num = int(num)
christmasTree(num)
