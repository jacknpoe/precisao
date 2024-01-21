# validações de números ponto flutuante
print(0.4 + 0.1 == 0.5)
print(0.4 + 0.2 == 0.6)
print("-------")

# validação usando decimal
from decimal import Decimal
print(Decimal('0.4') + Decimal('0.1') == Decimal('0.5'))
print(Decimal('0.4') + Decimal('0.2') == Decimal('0.6'))
print("-------")

precisao = 0.1 ** 15
print(abs(0.4+0.1-0.5)<precisao)
print(abs(0.4+0.2-0.6)<precisao)
print("-------")
