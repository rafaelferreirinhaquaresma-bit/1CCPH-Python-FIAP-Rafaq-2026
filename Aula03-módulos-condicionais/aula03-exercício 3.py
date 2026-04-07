def bigger():
    a = int(input('digite o primeiro número: '))
    b = int(input('digite o segundo número: '))
    if a > b:
        print(f'O primeiro valor {a} é maior')
    elif b > a:
        print(f'O segundo valor {b} é maior')
    elif a == b:
        print("Os números são iguais")

bigger()