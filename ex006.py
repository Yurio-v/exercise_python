num = int(input('digite um número: '))

import math
d = num * 2
t = num * 3
raiz = math.sqrt(num)

print(f'O número informado é {num}\n O dobro do número é {d}\n O triplo do número é {t}')
print('A raíz quadrada do número é {:.0f}'.format(raiz))
