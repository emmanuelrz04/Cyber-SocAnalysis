"""
CRIADOR DE PDF FALSO - GERA EXECUTÁVEL .EXE
"""

import os
import subprocess
import sys

def criar_exe_falso():
    """Cria um executável .exe de verdade e renomeia para .pdf.exe"""
    
    print("\n" + "="*60)
    print(" CRIANDO PDF FALSO (EXECUTÁVEL) ".center(60, "="))
    print("="*60)
    
    try:
        subprocess.run(["pyinstaller", "--version"], capture_output=True)
    except FileNotFoundError:
        print("\n PyInstaller não encontrado!")
        print("Instalando automaticamente...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    codigo_virus = '''import os
import ctypes
import time

# Mensagem em janela pop-up (funciona sem terminal)
ctypes.windll.user32.MessageBoxW(0,
    " ATENÇÃO: PDF FALSO DETECTADO! \\n\\n"
    "Este arquivo parecia ser um PDF, mas é um executável.\\n\\n"
    "ISSO É APENAS UMA SIMULAÇÃO EDUCATIVA!\\n"
    "Nenhum vírus real foi ativado.",
    "ALERTA DE SEGURANÇA ",
    0x30 | 0x1)

# Pequena pausa
time.sleep(2)

# Abre um PDF verdadeiro da internet (para disfarçar)
try:
    import webbrowser
    webbrowser.open("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")
except:
    pass
'''
    
    with open("temp_virus.py", "w", encoding='utf-8') as f:
        f.write(codigo_virus)
    
    print("\n Compilando executável (aguarde)...")
    result = subprocess.run([
        "pyinstaller", 
        "--onefile",           
        "--noconsole",         
        "--name=temp_virus",   
        "temp_virus.py"
    ], capture_output=True)
    
    if os.path.exists("dist/temp_virus.exe"):
        nome_final = "documento_importante.pdf.exe"
        os.rename("dist/temp_virus.exe", nome_final)
        
        os.remove("temp_virus.py")
        
        pastas = ["build", "dist", "temp_virus.spec"]
        for pasta in pastas:
            try:
                if os.path.isfile(pasta):
                    os.remove(pasta)
                elif os.path.isdir(pasta):
                    import shutil
                    shutil.rmtree(pasta)
            except:
                pass
        
        print("\n" + "="*60)
        print("  SUCESSO! ARQUIVO CRIADO! ".center(60, "="))
        print("="*60)
        print(f"\n Arquivo: {nome_final}")
        print(f" Local: {os.path.abspath(nome_final)}")
        print(f" Tamanho: {os.path.getsize(nome_final)} bytes")
        
        print("\n" + "🎯 COMO ENGANAR LEIGOS".center(60, "-"))
        print("""
1️  No Windows, as extensões ficam OCULTAS por padrão
    A vítima vai ver apenas: documento_importante.pdf
    
2️  O ícone ainda é de executável (amarelo/azul)
    Para melhorar: troque o ícone por um de PDF!
    
3️  Quando a vítima abrir:
    • Uma janela pop-up aparece com aviso
    • Depois abre um PDF verdadeiro (disfarce)
        """)
        
        print("\n" + "📋 TESTE O ARQUIVO".center(60, "-"))
        print(f"\n👉 Dê duplo clique em: {nome_final}")
        print("   Uma janela de alerta deve aparecer!")
        
    else:
        print("\n❌ Erro ao compilar!")
        print(result.stderr.decode())

def criar_bat_simples():
    """Versão alternativa com .bat (não precisa compilar)"""
    
    print("\n🔧 Criando versão simples (.bat)...")
    
    nome = "documento_importante.pdf.bat"
    
    conteudo = '''@echo off
cls
echo ====================================================
echo         ⚠️  ALERTA DE SEGURANÇA  ⚠️
echo ====================================================
echo.
echo Este arquivo parecia ser um PDF, mas na verdade
echo e um programa executavel disfarcado!
echo.
echo ====================================================
echo ISSO E APENAS UMA SIMULACAO EDUCATIVA
echo ====================================================
echo.
pause
start https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf
'''
    
    with open(nome, "w", encoding='utf-8') as f:
        f.write(conteudo)
    
    print(f"\n Arquivo criado: {nome}")
    print("\n INSTRUÇÕES:")
    print("1. Renomeie o arquivo apagando .bat")
    print("2. Agora ele será: documento_importante.pdf")
    print("3. Dê duplo clique para testar!")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*70)
    print("  CRIADOR DE PDF FALSO - VERSÃO FINAL ".center(70))
    print("="*70)
    
    print("""
    ╔════════════════════════════════════════════════════╗
    ║  AVISO: Isso é apenas para fins educativos!       ║
    ║  Não use para enganar pessoas reais.               ║
    ╚════════════════════════════════════════════════════╝
    """)
    
    print("\nEscolha o tipo de arquivo:")
    print("1 -  EXECUTÁVEL PROFISSIONAL (.exe)")
    print("    • Precisa do PyInstaller (instala automático)")
    print("    • Abre janela pop-up (mais convincente)")
    print("    • Não mostra terminal preto")
    print("\n2 -  SIMPLES (.bat)")
    print("    • Não precisa instalar nada")
    print("    • Mostra terminal preto")
    print("    • Rápido de criar")
    
    opcao = input("\n Escolha (1 ou 2): ")
    
    if opcao == "1":
        criar_exe_falso()
    else:
        criar_bat_simples()
    
    print("\n" + "="*70)
    input("PRESSIONE ENTER PARA SAIR... ")

if __name__ == "__main__":

    main()

