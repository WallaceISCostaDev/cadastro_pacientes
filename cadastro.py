# Execução do Programa
print('-----Seja bem-vindo!-----')

# Funções 
pacientes = [
    {
        "nome": "Ana Souza",
        "idade": 34,
        "sexo": "Feminino",
        "cpf": "123.456.789-00",
        "idoso": False,
        "status": "Autista"
    },
    {
        "nome": "Carlos Oliveira",
        "idade": 70,
        "sexo": "Masculino",
        "cpf": "987.654.321-00",
        "idoso": True,
        "status": "Deficiente"
    },
    {
        "nome": "Maria Silva",
        "idade": 25,
        "sexo": "Feminino",
        "cpf": "234.567.890-11",
        "idoso": False,
        "status": "Gestante"
    },
    {
        "nome": "José Santos",
        "idade": 45,
        "sexo": "Masculino",
        "cpf": "345.678.901-22",
        "idoso": False,
        "status": "Não informado"
    },
    {
        "nome": "Patrícia Costa",
        "idade": 80,
        "sexo": "Feminino",
        "cpf": "456.789.012-33",
        "idoso": True,
        "status": "Não informado"
    },
    {
        "nome": "Lucas Pereira",
        "idade": 38,
        "sexo": "Masculino",
        "cpf": "567.890.123-44",
        "idoso": False,
        "status": "Não informado"
    },
    {
        "nome": "Fernanda Lima",
        "idade": 60,
        "sexo": "Feminino",
        "cpf": "678.901.234-55",
        "idoso": True,
        "status": "Autista"
    },
    {
        "nome": "Carlos Eduardo",
        "idade": 29,
        "sexo": "Masculino",
        "cpf": "789.012.345-66",
        "idoso": False,
        "status": "Não informado"
    },
    {
        "nome": "Juliana Rocha",
        "idade": 50,
        "sexo": "Feminino",
        "cpf": "890.123.456-77",
        "idoso": False,
        "status": "Deficiente"
    },
    {
        "nome": "Roberto Almeida",
        "idade": 75,
        "sexo": "Masculino",
        "cpf": "901.234.567-88",
        "idoso": True,
        "status": "Não informado"
    }
]

# Funções de ação
def cadastro_paciente():
    print("Cadastro de paciente realizado com sucesso!")

def consulta_paciente():
    print("Consulta de paciente realizada com sucesso!")

def inserir_paciente():
    print("Paciente inserido na fila de atendimento!")
def mapear_status(status): #verifica o status e atribui um número conforme prioridade
    if status == 'Deficiente':
        return 3
    elif status == 'Autista':
        return 2
    elif status == 'Não informado':
        return 1
    return 0
def visualizar_fila():
    # Ordena os pacientes idoso>>>status
    fila_ordenada = sorted(pacientes, key=lambda paciente: (paciente['idoso'], mapear_status(paciente['status'])),reverse=True)
    print('-----Fila de Atendimento-----')
    for posicao, paciente in enumerate(fila_ordenada,start=1): #imprime
        print(f'Posição na fila: #{posicao}')
        print('Nome: ',paciente['nome'])
        print('Idade: ',paciente['idade'])
        print('Condição: ',paciente['status'])
        print('-' *10)
              

   
# Trecho do código que solicita acesso à opção desejada
while True:
    try:
        option_choice = int(input('Digite a opcao desejada:\n'  # Recebe variável referente à escolha
                                '(1) Cadastrar Paciente\n'
                                '(2) Consultar Paciente\n'
                                '(3) Inserir na Fila de Atendimento\n'
                                '(4) Visualizar fila de Atendimento\n'))
        
        # Verifica se a opção escolhida é válida
        if option_choice == 1:
            cadastro_paciente()
            break  # Sai do loop após a escolha
        elif option_choice == 2:
            consulta_paciente()
            break  # Sai do loop após a escolha
        elif option_choice == 3:
            inserir_paciente()
            break  # Sai do loop após a escolha
        elif option_choice == 4:
            visualizar_fila()
            break  # Sai do loop após a escolha
        else:
            print('Selecione uma opção válida!')
            continue  # Continua o loop se a opção for inválida

    except ValueError:  # Lança mensagem de erro caso digitado algo que não seja número
        print('Valor inválido, digite novamente.')


    