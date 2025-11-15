# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    weight, height = map(float, input("Введите 2 числа ").split())
    bmi = weight / height
    print(bmi)
   

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()