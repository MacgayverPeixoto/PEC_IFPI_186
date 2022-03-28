#1
#definindo o valor de PI
pix=float(3.141592)
#Entrada de dados para obter o raio
raio= float(input())
#Comprimento
compri= float(2* pix*raio)
#Área do Círculo
areac=float(pix*raio**2)
#Área da Esfera
esfera=float(4*pix*raio**2)
#Volume da esfera
volume=float(4/3*pix*raio**3)
#
print('%.6f'%compri)
print('%.6f'%areac)
print('%.6f'%esfera)
print('%.6f'%volume)
