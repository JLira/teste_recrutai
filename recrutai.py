contas = {
    'ID_Conta_1': {'FOOD': 100, 'MEAL': 200, 'CASH': 300},
    'ID_Conta_2': {'FOOD': 150, 'MEAL': 50, 'CASH': 400}
}

transacoes = []

# função para atualizar saldo após a transação


def atualizar_saldo(id_conta, categoria, valor):
    if id_conta in contas and categoria in contas[id_conta]:
        saldo = contas[id_conta][categoria]
        if saldo >= valor:
            contas[id_conta][categoria] -= valor
            return True
        return False

# função para armazenar os resultados de cada transação


def armazenar_transacao(id_transacao, id_conta, categoria, valor, estabelecimento, mcc):
    transacao = {
        'id': id_transacao,
        'account_id': id_conta,
        'ammount': valor,
        'merchant': estabelecimento,
        'mcc': mcc
    }
    transacoes.append(transacao)


# função para buscar transaçoes por conta e estabelicimento
def buscar_transacoes(id_conta=None, estabelecimento=None):
    resultados = []
    for transacao in transacoes:
        if (not id_conta or transacao['account_id'] == id_conta) and \
           (not estabelecimento or transacao['merchant'] == estabelecimento):
            resultados.append(transacao)
    return resultados


# Função para autorizar a transação
def autorizar_transacao(id_conta, categoria, valor, estabelecimento, mcc, id_transacao):
    if atualizar_saldo(id_conta, categoria, valor):
        armazenar_transacao(id_transacao, id_conta, categoria, valor, estabelecimento, mcc)
        print("Transação autorizada.")
    else:
        print("Transação recusada: Saldo insuficiente ou conta/categoria inválida.")


# Testes


# 1. Transação Recusada devido a saldo insuficiente em FOOD
autorizar_transacao('ID_Conta_1', 'FOOD', 120, 'Restaurante A', '1234', 'ID_Transacao_1')

# 2. Transação Aprovada em CASH
autorizar_transacao('ID_Conta_1', 'CASH', 50, 'Loja B', '5678', 'ID_Transacao_2')

# 3. Transação Aprovada em FOOD
autorizar_transacao('ID_Conta_2', 'FOOD', 150, 'Restaurante C', '4321', 'ID_Transacao_3')

# 1. Transação Recusada
if not atualizar_saldo('ID_Conta_1', 'FOOD', 120):
    print("Transação Recusada: Saldo insuficiente em FOOD")

# 2. Transação Aprovada em CASH
if atualizar_saldo('ID_Conta_1', 'CASH', 50):
    print("Transação Aprovada em CASH")

# 3. Transação Aprovada em FOOD
if atualizar_saldo('ID_Conta_2', 'FOOD', 150):
    print("Transação Aprovada em FOOD")

# 4. Duas Compras Consecutivas (Aprovada e Recusada)
if atualizar_saldo('ID_Conta_2', 'MEAL', 30):
    print("Primeira compra aprovada em MEAL")
else:
    print("Primeira compra recusada em MEAL")

if atualizar_saldo('ID_Conta_2', 'MEAL', 80):
    print("Segunda compra aprovada em MEAL")
else:
    print("Segunda compra recusada em MEAL")

# Armazenar transações
armazenar_transacao('ID_Transacao_1', 'ID_Conta_1',
                    'FOOD', 120, 'Restaurante A', '1234')
armazenar_transacao('ID_Transacao_2', 'ID_Conta_1',
                    'CASH', 50, 'Loja B', '5678')
armazenar_transacao('ID_Transacao_3', 'ID_Conta_2',
                    'FOOD', 150, 'Restaurante C', '4321')

# Buscar transações
resultados = buscar_transacoes(
    id_conta='ID_Conta_1', estabelecimento='Restaurante A')
print("Transações da conta 1 no Restaurante A:")
for resultado in resultados:
    print(resultado)
