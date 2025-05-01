# Lucas trabalha em um sistema de notificações que precisa enviar mensagens para usuários. No entanto, algumas notificações só devem ser enviadas se o usuário tiver ativado essa opção no sistema. Além disso, se o usuário for VIP, ele deve receber uma notificação prioritária antes das demais.
#
# Com base nesse cenário, crie um programa que simule o envio de notificações para três usuários. Cada usuário tem um status diferente:
#
# Ana: VIP (deve receber uma notificação prioritária antes das normais).
# João: Usuário comum, mas ativou as notificações.
# Carla: Usuária comum, mas desativou as notificações (não deve receber nada).
# O programa deve exibir quais notificações foram enviadas e quais usuários não receberam nada.
#
# Saída esperada:
#
# Enviando notificações...
# Notificação VIP para Ana enviada!
# Notificação normal para João enviada!
# Carla desativou as notificações. Nada foi enviado.
# Todas as notificações foram processadas!

import asyncio
usuarios = [
    {"nome": 'Ana', "VIP": True, "notificacao_ativa": True},
    {"nome": 'João', "VIP": False, "notificacao_ativa": True},
    {"nome": 'Carla', "VIP": False, "notificacao_ativa": False}
]
async def notificacao(usuario):
    if not usuario["notificacao_ativa"]:
        print(f"{usuario['nome']} desativou as notificações. Nada foi enviado.")
        return
    if usuario["VIP"]:
        print(f"Notificação VIP para {usuario['nome']} enviada!")
        return
    print(f'Notificação normal para {usuario["nome"]} enviada!')

async def main():
    print("Enviando notificações...")
    tarefas = [asyncio.create_task(notificacao(u)) for u in usuarios]
    await asyncio.gather(*tarefas)
    print("Todas as notificações foram processadas!")
asyncio.run(main())





