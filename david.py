import time

# Definição da Class que sustenta todo o código

class Condomino:
    """
        Essa class é responsável não só por compreender as instâncias "Condômino" do nosso problema mas também por armazená-la e manipulá-la. Note que é iniciada uma lista
        assim que a Class é chamada. Qualquer linha que não envolva o uso da class não consegue requisitar acesso à lista, pois ela pertence à classe.
        Chamamos esta lista no código inteiro como [Condominio.conds].

        Uma vez que a demanda do projeto requisita que o condômino possa ser devedor ou pagador, nota-se que são um par de condições opostas, então decidi armazenar isso
        na classe como um valor booleano.

    """
    conds = []

    def __init__(self, cpf, name, appartement, debit, state):
        self.__class__.conds.append(self)

        self.cpf = cpf
        self.name = name
        self.ap = appartement
        self.debit = debit
        self.state = state


        def excluir(self):
            """
                Ao ser chamada, a função *excluir()* remove o condômino da lista de condôminos e em seguida deleta a instância.
            """
            if self in Condomino.conds:
                Condomino.conds.remove(self)
            else:
                print('Usuário será deletado mas não foi encontrado na lista de condôminos.')
            del self


def main():
    print('')
    while True:
        try:
            options = [
            '1 = Inserir um condomino digitando o CPF, Nome, Apartamento, Debito',
            '2 = Consulte o Condomino pelo CPF',
            '3 = Atualize ou um condômino pelo CPF(devedor ou Pagador)',
            '4 = Exibir os Condominos pagadores',
            '5 = Exibir os Condominos devedores',
            '6 = Remover um Condomino',
            '7 = Listar todos os condôminos',
            '8 = Sair',
            ]
            for item in options:
                print(item)
            
            option = int(input('->: '))

            if option >= 1 and option <= 8:
                if option == 1:
                    cleaner()
                    cadastrar()

                elif option == 2:
                    cleaner()
                    consultar()

                elif option == 3:
                    cleaner()
                    consultar()

                elif option == 4:
                    loaddelay()
                    showpagadores()
                    main()

                elif option == 5:
                    loaddelay()
                    showdevedores()
                    main()

                elif option == 6:
                    cleaner()
                    consultar()

                elif option == 7:
                    cleaner()
                    listar()

                elif option == 8:
                    goodbye()

                else:
                    print('Opção não cadastrada\n') # Inseriu um número, mas não está no menu [int]
                    time.sleep(3)

            else:
                pass


        except Exception: # Inseriu caracter não integer que não está cadastrado no menu

            print ('Comando não [Exception triggered]\n')




def listar():
    for registro in Condomino.conds:
        estado = "Pagador" if registro.state == True else "Devedor"

        print('========================================================================')
        print("{} (CPF:{}) - Apt:{} - Débito atual: R${} [{}]".format(registro.name, registro.cpf, registro.ap, registro.debit, estado))
    print('========================================================================\n')
    
    answ = input('Digite qualquer coisa para voltar ao menu...\n ->:')
    main()



def cadastrar():
    cads = True

    while cads == True:
        print('Cadastro de Condômino:')
        
        nome = str(input('Insira o nome do condômino: '))
        cpf = input('Insira o CPF deste condômino: ')
        apartamento = input('Insira o apartamento: ')
        debito = input('Insira o débito do condômino: ')
        
        while True:
            condicao = input('\nPara cadastrar esta pessoa como pagador, digite 1, para devedor, 2.\n ->:')
            
            if condicao == '1':
                estado = True
                break
            elif condicao == '2':
                estado = False
                break
            else:
                print('Opção inexistente, tente novamente!\n')
                pass


        novocad = Condomino(cpf, nome, apartamento, debito, estado)
        
        print('====================\n Cadastro finalizado!')
        time.sleep(2)
        cleaner()

        while True:
            resp = input('Continuar cadastrando pessoas? S/N\n')
            if resp.lower() == 's':
                print('Certo, vamos a um novo cadastro!\n ==================== \n')
                break
            if resp.lower() == 'n':
                cads = False
                print('Voltando ao menu principal')
                print('\n')
                break
            else:
                print('Responda apenas com S (para sim) e N (para não)! Continuaremos os cadastros por padrão.\n')
                pass


def consultar():
    print('====================\n Módulo de consulta.')

    cpf_da_consulta = input('Digite o CPF do condômino! \n ->: ')

    print('\n Buscando!...')

    for registro in Condomino.conds:
        if registro.cpf == cpf_da_consulta:
            print('Condômino encontrado!')
            print("{} (CPF:{}) - Apt:{} - Débito atual: R${}\n".format(registro.name, registro.cpf, registro.ap, registro.debit))

            while True:
                acao = input('Para alterar o débito deste condômino, digite 1. \nPara excluir o condômino, digite 2.\nPara retornar ao menu, digite 3.\n ->: ')

                if acao == '1':
                    novovalor = input('Insira o novo valor de débito do condômino!\n ->:')
                    registro.debit = novovalor
                    print('Valor de débito alterado, retornando ao menu principal...\n')
                    main()
                elif acao == '2':
                    registro.excluir()
                    print('Condômino apagado.\n Retornando ao menu principal...\n')
                    main()
                elif acao == '3':
                    print('Voltando ao menu principal...\n')
                    main()
                else:
                    print('Comando não compreendido.\n')

        else:
            pass
    print('O CPF não foi encontrado, esta pessoa não está registrada ou você cometeu um erro de digitação.\n Voltando ao menu...')
    time.sleep(3)
    main()


def showpagadores():
    print('Lista de condôminos quites! \n========================================================================')
    for registro in Condomino.conds:
        if registro.state == True:
            print('========================================================================')
            print("{} (CPF:{}) - Apt:{} - Débito atual: R${}".format(registro.name, registro.cpf, registro.ap, registro.debit))
            print('========================================================================')
        else:
            pass

    unlocker = input('Digite qualquer coisa para voltar ao menu...\n ->:')
    main()


def showdevedores():
    print('Lista de devedores! \n========================================================================')
    for registro in Condomino.conds:
        if registro.state == False:
            print('========================================================================')
            print("{} (CPF:{}) - Apt:{} - Dívida atual: R${}".format(registro.name, registro.cpf, registro.ap, registro.debit))
            print('========================================================================')
        else:
            pass

    unlocker = input('Digite qualquer coisa para voltar ao menu...\n ->:')
    main()


def goodbye():
    print('Finalizada a execução do programa.\n       Goodbye!')
    exit()


"""
    Abaixo apenas triggers e defs de delay e estilo simples
"""

def cleaner():
    for i in range(50):
        print('')

def loaddelay():
    time.sleep(0.5)
    print('Processando!')
    print('.'), time.sleep(0.2), print('.'), time.sleep(0.2), print('.')

if __name__ == '__main__':
    print('========================================================\n Bem-vindo!')
    main()