"""
Exercício de imprimir Olá mundo
"""

print("Olá mundo")
msg = 'Olá {0}'
print(msg.format('mundo'))
msg2 = '{0} {1}'
print(msg2.format('Olá', 'mundo'))
msg3 = 'Olá mundo'
for item in msg3:
    print(item, end="")