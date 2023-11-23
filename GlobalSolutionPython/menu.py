import time

print('===> Seja bem vindo ao Health RPG!!! <===\n')
print('1. Start\n')
print('2. Desenvolvedores\n')
print('3.  Exit\n')

while (True):

    opcao = int(input('Escolha uma opção: '))

    while opcao < 1 or opcao > 3:
        opcao = int(input('Escolha uma opção entre 1 e 3: '))
    
    if opcao == 1:
        print('Iniciando o game...\n')
        time.sleep(5)
        print('FASE 1\n')
        print('Uma névoa sinistra paira sobre a cidade, trazendo consigo a temida Covid 19, conhecido como corona virus. O vírus se espalhou, e as pessoas estão em pânico.')
        time.sleep(7)
        print('A COVID-19 é uma doença respiratória causada pelo coronavírus SARS-CoV-2. Ela foi identificada pela primeira vez na cidade de Wuhan, na China, em dezembro de 2019, e desde então se espalhou globalmente, tornando-se uma pandemia.\n')
        time.sleep(10)
        print('Sintomas comuns incluem febre, tosse, dificuldade respiratória, fadiga e perda de olfato e paladar. A transmissão ocorre principalmente por gotículas respiratórias durante a fala, tosse ou espirro de uma pessoa infectada, além do contato próximo.\n')
        print('Sua missão é utilizar os itens corretos para combater e se proteger dessa ameaça invisível. O destino da cidade está em suas mãos! Boa sorte!\n') 

        
    elif opcao == 2:
        print('\nEste game foi desenvolvido pelos seguintes desenvolvedores: \n')
        print('Kayque Ferreira dos Santos - RM: 552605\n')
        print('Marco Aurélio Morais Ennes - RM: 553201\n')
        print('André Alves da Silva - RM: 552639 ...')
    else: 
        print('Saindo do game...')
        break

