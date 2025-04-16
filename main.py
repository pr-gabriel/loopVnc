import subprocess
import time
import os

def criar_arquivo (nome):
    arquivo = f"""
        ClientCutText=1
        ConnMethod=tcp
        ConnTime=2024-01-19T15:46:34.913z
        Emulate3=0
        FullScreen=0
        Host={nome}::7007
        Password=04eaafa663af8e0d
        SendKeyEvents=0
        Server Cut Text=0
        Shared=1
        ShareFiles=0
        UUid=8c26b451-eed1-4fbf-aae3-e8142bd36f8b
        viewonly=0
        FullScreen=1
        Quality Auto
        AcceptBell=1
    """

    path = f"temp/[nome].vnc"
    if not os.path.exists(path):
        with open(" (path)", "w") as documento:
            documento.write(arquivo)
    else:
        return

def abrir_fechar_vnc(host, duration=20):
    config_file = f".//temp//{host).vnc"
    if not os.path.exists(config_file):
        print("Erro: Arquivo não encontrado.")
        criar_arquivo (config_file)
        return
    try:
        command = ["vncviewer", "-config", config_file]
        process subprocess. Popen(command)
        print("Acesso (config file) iniciado.")
        time.sleep(duration)
        process.terminate()
    except:
        print("Erro")

def abri_host():
    path = "names"
    with open(f" (path)", "r") as arquivo:
    conteudo = arquivo.read().split("\n")
    return conteudo
def ler_Identities(host):
    print(host)
    path = "/home/admin/.vnc/identities"
    eith
        conteudo = arquivo.read().split("\n")
    exist = False
    for linha in conteudo:
        linh = linha.split(":")
        print(linh)                                  


