#03pt2

preco=float(input())
valor=float(input())
valor_percen= preco * valor/100

aumento_percen = preco + valor_percen
desconto_percen = preco - valor_percen

print(f'{aumento_percen:.2f}')
print(f'{desconto_percen:.2f}')
