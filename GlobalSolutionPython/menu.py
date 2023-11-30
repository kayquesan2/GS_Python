import time
primeira_vez = True
continuar = True

while (continuar):

    lista_nomeItens = []
    lista_nomeItens.append('Máscara')
    lista_nomeItens.append('Alcool em gel')
    lista_nomeItens.append('Cloroquina')
    
    if primeira_vez:
        nome = input("Qual o seu primeiro nome? ")
        primeira_vez = False
    
    print(f'===> Seja bem vindo {nome} ao Health RPG!!! <===\n')
    print('1. Iniciar\n')
    print('2. Desenvolvedores\n')
    print('3. Sair\n')
    opcao = int(input('Escolha uma opção: '))

    while opcao < 1 or opcao > 3:
        opcao = int(input('Escolha uma opção entre 1 e 3: '))
        
    vida_jogador = 100
    vida_coronavirus = 100
    ataque_jogador = 20
    ataque_coronavirus = 35

    while (True):
        if opcao == 1:

            print('Iniciando o game...\n')
            time.sleep(4)
            print('Uma névoa sinistra paira sobre a cidade, trazendo consigo a temida Covid 19, conhecido como corona virus. O vírus se espalhou, e as pessoas estão em pânico.')
            time.sleep(4)
            print('A COVID-19 é uma doença respiratória causada pelo coronavírus SARS-CoV-2. Ela foi identificada pela primeira vez na cidade de Wuhan, na China, em dezembro de 2019, e desde então se espalhou globalmente, tornando-se uma pandemia.\n')
            time.sleep(4)
            print('Sintomas comuns incluem febre, tosse, dificuldade respiratória, fadiga e perda de olfato e paladar. A transmissão ocorre principalmente por gotículas respiratórias durante a fala, tosse ou espirro de uma pessoa infectada, além do contato próximo.\n')
            print('Sua missão é utilizar os itens corretos para combater e se proteger dessa ameaça invisível. O destino da cidade está em suas mãos! Boa sorte!\n')
            print("Começando a batalha!!!\n")
            print('Seu item inicial de ataque é a lâmina cerrada\n')

            while vida_jogador > 0 and vida_coronavirus > 0:
                print('Informações do jogo: ')
                print(f'Jogador: {nome} | Vida: {vida_jogador} | Ataque: {ataque_jogador}\n')
                print(f'Inimigo: Corona Vírus | Vida: {vida_coronavirus} | Ataque: {ataque_coronavirus}\n')
                print('--- SEU TURNO ---\n')
                print("Escolha qual opção deseja: \n")
                print('1. Atacar\n')
                print('2. Abrir inventário\n')
                escolha = int(input('R: '))

                if escolha == 1:
                    print('Você atacou o Corona Vírus\n')
                    time.sleep(5)
                    vida_AposDano = vida_coronavirus - ataque_jogador
                    vida_coronavirus = vida_AposDano
                    if vida_coronavirus > 0:
                        print(f'O Corona Virus sofreu {ataque_jogador} de dano e sua vida atual é {vida_AposDano}\n')
                    else:
                        print(f'O Corona Virus sofreu {ataque_jogador} de dano e sua vida atual é 0\n')
                    time.sleep(3)
                elif escolha == 2:
                    print('--- Lista de Itens --- ')
                    for i in range (0, len(lista_nomeItens), 1):
                        print(f'Item n°:{i} | Nome: {lista_nomeItens[i]} ')
                    while True:
                        item_escolhido = int(input(('Digite o n° do item que deseja usar: ')))
                        if item_escolhido < 0 or item_escolhido >= len(lista_nomeItens):
                            print('Opção Inválida! Tente novamente!')
                        else:
                            if lista_nomeItens[item_escolhido] == 'Máscara':
                                defesa_reduzida = 20
                                ataque_coronavirus = ataque_coronavirus - defesa_reduzida
                                print(f'Você usou a máscara. O dano do Corona foi reduzido em {defesa_reduzida} pontos')
                                lista_nomeItens.pop(item_escolhido)
                                break
                            elif lista_nomeItens[item_escolhido] == 'Alcool em gel':
                                ataque_aumentado = 15
                                ataque_jogador = ataque_jogador + ataque_aumentado
                                print(f'Você usou o alcool em gel. Seu ataque foi aumentado em {ataque_aumentado} pontos')
                                lista_nomeItens.pop(item_escolhido)
                                break
                            else:
                                print('Opa, esse item não teve efeito nenhum. Aparentemente você caiu em uma fake news. Tome cuidado!')
                                lista_nomeItens.pop(item_escolhido)
                                break
                if vida_coronavirus > 0:
                    print('--- É a vez do Corona ---\n')
                    print('O Corona Virus atacou')
                    time.sleep(4)
                    vida_AposDano = vida_jogador - ataque_coronavirus
                    vida_jogador = vida_AposDano
                    if vida_jogador > 0:
                        print(f'Você sofreu {ataque_coronavirus} de dano e sua vida atual é {vida_AposDano}\n')
                    else:
                        print(f'Você sofreu {ataque_coronavirus} de dano e sua vida atual é 0\n')
                    time.sleep(3)

            if vida_coronavirus <= 0:
                print('Parabéns, você venceu a batalha e derrotou o Corona Vírus! Agora derrote-o na vida real!')
            elif vida_jogador <= 0:
                print("Game Over!")
            resposta = input('Deseja jogar novamente? (S/N)').upper()
            while resposta != 'S' and resposta != 'N':
                resposta = input('Resposta inválida. Digite apenas S ou N. Deseja jogar novamente? (S/N)').upper()
            if resposta == 'S':
                continuar = True
            else:
                continuar = False
            break

  
        elif opcao == 2:
            print('\nEste game foi desenvolvido pelos seguintes desenvolvedores: \n')
            print('Kayque Ferreira dos Santos - RM: 552605\n')
            print('Marco Aurélio Morais Ennes - RM: 553201\n')
            print('André Alves da Silva - RM: 552639')
            print("...")
            time.sleep(3)
            break
        else: 
            continuar = False
            break

print('Saindo do game...')
time.sleep(2)