#05

#calcular a quantidade de piso, quantidade de tinta
#volume da sala em metros cubicos para o ar condicinado
#3 numeros para altura , comprimento e largura


altu=int(input())
compr=int(input())
larg=int(input())

area_piso=larg*compr
volume_sala=larg*compr*altu
area_paredes=2*altu*larg+2*altu*compr

print(area_piso)
print(volume_sala)
print(area_paredes)
