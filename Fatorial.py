# Carlos precisa calcular o fatorial de cinco números diferentes simultaneamente. Como cálculos pesados podem demorar, ele quer garantir que todos sejam processados ao mesmo tempo, e os resultados exibidos assim que estiverem prontos.
#
# Crie um programa que calcule o fatorial de cinco números diferentes de forma assíncrona, onde os cálculos devem ser realizados paralelamente e exiba os resultados conforme forem concluídos, em ordem de menor número para maior número.
#
# Dica: use a função sleep para simular um tempo de processamento.
#
# Dica: para testar o funcionamento do seu código, utilize uma lista de números em ordem de tamanho aleatória. Exemplo: numeros = [5, 3, 7, 4, 6]
#
# Saída esperada:
#
# Fatorial de 3 = 6
# Fatorial de 4 = 24
# Fatorial de 5 = 120
# Fatorial de 6 = 720
# Fatorial de 7 = 5040

import asyncio
import math

numeros = [5, 3, 7, 4, 6]

async def fatorial(n):
    await asyncio.sleep(n)
    print(f"Fatorial de {n} = {math.factorial(n)}")

async def main():
    tarefas = [asyncio.create_task(fatorial(n)) for n in numeros]
    await asyncio.gather(*tarefas)

asyncio.run(main())