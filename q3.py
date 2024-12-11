contatos = [
    {"nome": "Igor", "telefone": "11111111"},
    {"nome": "Pedro", "telefone": "22222222"},
    {"nome": "Maria", "telefone": "333333333"},
]

# Percorre a lista elemento por elemento até encontrar o nome ou atingir o final da lista
def busca_linear(contatos, nome):
    for contato in contatos:
        # Verifica se o nome corresponde ao parametro
        if contato["nome"] == nome:
            return contato["telefone"]
    return "Contato não foi encontrado"

print(busca_linear(contatos, "Pedro"))
