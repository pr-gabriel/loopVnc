import subprocess  # Usado para abrir outros programas (como o VNC)
import time        # Usado para pausar o programa por alguns segundos
import os          # Usado para lidar com arquivos e caminhos
import random      # Usado para embaralhar listas aleatoriamente

# Função que cria um arquivo de configuração .vnc para o host informado
def criar_arquivo(nome):
    # Conteúdo do arquivo de configuração do VNC
    arquivo = """
ClientCutText=1
ConnMethod=tcp
ConnTime=2024-01-19T15:46:34.913Z
Emulate3=0
FullScreen=0
Host={nome}:7097
Password=04eaa4a663a4e8e0d
SendKeyEvents=0
ServerCutText=0
Shared=1
ShareFiles=0
Uuid=8c26cb45-ced1-4bfb-aaa3-e8142bd36f8b
ViewOnly=0
FullScreen=1
Quality=Low
AcceptBell=1
"""
    # Define o caminho do arquivo
    path = f"/temp/{nome}.vnc"
    # Se o arquivo ainda não existe, cria ele
    if not os.path.exists(path):
        with open(f"{path}", "w") as documento:
            documento.write(arquivo)
    else:
        return  # Se já existir, não faz nada

# Função que abre o VNC Viewer com o arquivo de configuração e fecha após um tempo
def abrir_fechar_vnc(host, duration=20):
    config_file = f"/temp/{host}.vnc"
    # Verifica se o arquivo existe; se não, tenta criá-lo
    if not os.path.exists(config_file):
        print("Arquivo não encontrado.")
        criar_arquivo(host)
        return

    try:
        # Comando para abrir o VNC Viewer com o arquivo de config
        command = ["vncviewer", "-config", config_file]
        process = subprocess.Popen(command)  # Abre o programa
        print(f"Acesso {config_file} iniciado.")
        time.sleep(duration)  # Espera o tempo desejado
        process.terminate()   # Fecha o VNC Viewer
    except:
        print("Erro")  # Caso algo dê errado

# Função que lê os nomes dos hosts de um arquivo chamado "names"
def abrir_host():
    path = "names"
    with open(f"{path}", "r") as arquivo:
        conteudo = arquivo.read().split("\n")  # Lê e separa cada linha
    return conteudo

# Função que verifica se o host já está no arquivo identities, se não estiver, adiciona
def ler_identities(host):
    print(host)
    path = "/home/admin/.vnc/identities"
    with open(f"{path}", "r") as arquivo:
        conteudo = arquivo.read().split("\n")
    
    exist = False  # Flag para saber se já existe
    for linha in conteudo:
        linha = linha.split(":")
        if linha != ['']:
            if linha[0] == host:
                exist = True  # Host já está presente
    
    # Se não existir, adiciona a linha no arquivo
    if exist == False:
        with open(f"{path}", "a") as arq:
            arq.write(f"{host}:7097/extra=0201\n")

# Parte principal do programa
if __name__ == "__main__":
    while True:  # Loop infinito
        hosts = abrir_host()       # Lê todos os hosts do arquivo "names"
        random.shuffle(hosts)      # Embaralha a ordem dos hosts
        for y in hosts:            # Para cada host:
            y = y.strip()              # Remove espaços em branco
            ler_identities(y)         # Atualiza identities se necessário
            tempo_espera = 35         # Tempo de espera com o VNC aberto
            criar_arquivo(y)          # Cria o arquivo .vnc
            abrir_fechar_vnc(y, tempo_espera)  # Abre e fecha o VNC Viewer
