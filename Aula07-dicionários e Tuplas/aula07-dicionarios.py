eng2esp = dict()
print(eng2esp)

eng2esp["one"] = "uno"
print(eng2esp)

eng2esp = {
    'one':'uno',
    'two':'dos',
    'three':'tres'
}
print(eng2esp)
print(eng2esp["two"])

#operadore in

print('dos' in eng2esp)
valores = eng2esp.values()
print('one' in valores)

#contador de letras
def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
dict_contagem = count_letters("papaguaio")
dict_contagem01 = count_letters("Papaguaio")
print(dict_contagem, dict_contagem01)