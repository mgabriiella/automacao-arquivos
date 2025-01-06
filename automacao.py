import os
import shutil
from datetime import datetime, timedelta

# Caminhos das pastas e arquivos de log ajustados para o ambiente descrito
source_folder = r"C:\Users\User\Downloads\valcann\backupsFrom"
destination_folder = r"C:\Users\User\Downloads\valcann\backupsTo"
source_log = r"C:\Users\User\Downloads\valcann\backupsFrom.log"
destination_log = r"C:\Users\User\Downloads\valcann\backupsTo.log"

# Tempo limite de 3 dias para filtrar os arquivos
limite_tempo = datetime.now() - timedelta(days=3)

def listar_arquivos_na_pasta(pasta, arquivo_log):
    """
    Lista todos os arquivos de uma pasta e salva as informações no log.
    """
    with open(arquivo_log, "w") as log:
        log.write("=== Lista de Arquivos ===\n")
        arquivos_encontrados = 0  # Contador para verificar se há arquivos
        for nome_arquivo in os.listdir(pasta):
            caminho_completo = os.path.join(pasta, nome_arquivo)
            if os.path.isfile(caminho_completo):
                arquivos_encontrados += 1
                estatisticas = os.stat(caminho_completo)
                tamanho = estatisticas.st_size
                data_criacao = datetime.fromtimestamp(estatisticas.st_ctime)
                data_modificacao = datetime.fromtimestamp(estatisticas.st_mtime)
                
                log.write(
                    f"Nome: {nome_arquivo}, Tamanho: {tamanho} bytes, "
                    f"Criação: {data_criacao}, Modificação: {data_modificacao}\n"
                )
        if arquivos_encontrados == 0:
            log.write("Nenhum arquivo encontrado na pasta.\n")
    print(f"Log salvo em: {arquivo_log}")

def gerenciar_arquivos():
    """
    Remove arquivos antigos (mais de 3 dias) e copia arquivos recentes (menos ou igual a 3 dias).
    """
    for nome_arquivo in os.listdir(source_folder):
        caminho_completo = os.path.join(source_folder, nome_arquivo)
        if os.path.isfile(caminho_completo):
            data_criacao = os.stat(caminho_completo).st_ctime
            if datetime.fromtimestamp(data_criacao) < limite_tempo:
                # Remove arquivos antigos
                os.remove(caminho_completo)
                print(f"Removido: {nome_arquivo}")
            else:
                # Copia arquivos recentes
                shutil.copy2(caminho_completo, destination_folder)
                print(f"Copiado: {nome_arquivo} para {destination_folder}")

def log_arquivos_copiados():
    """
    Gera um log com todos os arquivos na pasta de destino.
    """
    with open(destination_log, "w") as log:
        log.write("=== Arquivos na pasta backupsTo ===\n")
        arquivos_encontrados = 0  # Contador para verificar se há arquivos
        for nome_arquivo in os.listdir(destination_folder):
            caminho_completo = os.path.join(destination_folder, nome_arquivo)
            if os.path.isfile(caminho_completo):
                arquivos_encontrados += 1
                estatisticas = os.stat(caminho_completo)
                tamanho = estatisticas.st_size
                data_criacao = datetime.fromtimestamp(estatisticas.st_ctime)
                data_modificacao = datetime.fromtimestamp(estatisticas.st_mtime)
                
                # Escreve no log as informações dos arquivos encontrados
                log.write(
                    f"Nome: {nome_arquivo}, Tamanho: {tamanho} bytes, "
                    f"Criação: {data_criacao}, Modificação: {data_modificacao}\n"
                )
        if arquivos_encontrados == 0:
            log.write("Nenhum arquivo encontrado na pasta.\n")
    print(f"Log dos arquivos copiados salvo em: {destination_log}")


def main():
    # Criação dos diretórios, se não existirem
    os.makedirs(source_folder, exist_ok=True)
    os.makedirs(destination_folder, exist_ok=True)

    # Listando arquivos da pasta de origem e gerando o log
    print("Listando arquivos na pasta de origem...")
    listar_arquivos_na_pasta(source_folder, source_log)

    # Gerenciando os arquivos (removendo antigos e copiando os recentes)
    print("Gerenciando arquivos...")
    gerenciar_arquivos()

    # Gerando log dos arquivos copiados
    print("Gerando log dos arquivos copiados...")
    log_arquivos_copiados()

    print("Processo concluído com sucesso!")

if __name__ == "__main__":
    main()
