num = int(input("escolha um numero: "))
if num < 2:
    print(num, "não e um numero primo.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "não é primo. ")
            break
    else:
         print(num, "esse numero é primo") 
       