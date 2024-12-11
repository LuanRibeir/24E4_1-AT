import os

def listar(diretorio):
    try:
        # Lista todos os itens no diretorio atual
        for item in os.listdir(diretorio):
            caminho_completo = os.path.join(diretorio, item)
            
            if os.path.isfile(caminho_completo):
                print(f"Arquivo: {caminho_completo}")
            elif os.path.isdir(caminho_completo):
                # Chama a função recursivamente para o subdiretório
                listar(caminho_completo)
    except PermissionError:
        print(f"Permissão negada ao acessar: {diretorio}")

# Exemplo
direc = "./"
listar(direc)
