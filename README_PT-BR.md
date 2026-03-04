# Projeto: Simulação de emails Phishing e PDF contaminado
---
## 📋 Índice
- [O que é o projeto](#o-que-é-o-projeto)
- [Estrutura das pastas](#estrutura-das-pastas)  
- [Objetivo do projeto](#objetivo-do-projeto)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Como rodar o projeto](#como-rodar-o-projeto)
- [Resultado](#resultado)
- [Observações importantes](#observações-importantes)

---

## 🎯 O que é o projeto

Este projeto é uma **demonstração educativa** sobre **segurança digital**, criado para apresentar:

- ✅ Como funcionam **golpes de phishing** (email falso do Nubank)
- ✅ Como arquivos maliciosos podem ser **disfarçados de PDF**
- ✅ A importância de **verificar fontes** antes de clicar em links ou anexos
- ✅ Exemplos práticos de **engenharia social**

> ⚠️ **ATENÇÃO:** Este projeto é **100% educativo** e não contém nenhum malware real. Todos os exemplos são simulações controladas.

---
## Objetivo do projeto
Este projeto tem como objetivo relatar, exemplificar e explicar como golpes digitais são praticados no ambiente virtual. A análise é baseada em: engenharia social, que abordam tecnicas pscicológicas que invasores contra suas vítimas para as coloca-la em situação de vulnerabilidade; como também a técnica, que aborda a utilização de ferramentas digitais para a criação de malwares e softwares modificados com códigos e funções ilegais.

---

## Tecnologias utilizadas
Para as exemplificações utilizamos: 
```bash
- linguagem de programação python
- dependências: fpdf2 e pyinstaller
- Ide: Visual Studio code
```
---
## Como você pode testar os arquivos na prática:
É importante frizar que nenhum dos arquivos mencionados estão 100% livres de virus. Os códigos utilizam a lógica já existente dentro da IDE.

## Pré-requisitos:
```bash

- IDE de sua preferência
- Python
- fpdf
- pyinstaller
- Um computador disponível
```
---

## Instalação windows
Primeiro, vamos instalar a IDE (Neste exemplo será utilizado o VSCODE). 
- Clique no link oficial para baixar: [Visual Studio Code](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user) 
- Espere o arquivo baixar
- Depois de baixado, execute ele
- Vá avançando no instalador até fazer a instalação dele por completo
- Depois de baixado, abra ele para verificar se a instalação ocorreu corretamente
  
Agora, o próximo passo é instalar o python.
- Clique no link oficial para baixar [Python](https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe)
- Espere o arquivo baixar
- Depois de baixado, execute ele
- Durante a instalação, na primeira tela do instalador, você deve marcar para SIM (☑️ Add Python to PATH)
- Depois disto, vá avançando no instalador até finalizar a instalação
- Agora entre no CMD e digite: python --version
- Se aparecer o nome python + sua versão, a instalação foi um sucesso

(Opicional) Caso você quiser colocar um icone personalizado no seu arquivo para deixa-lo mais realista, siga os seguintes passos:
- Clique no link para baixar o [Resource Hacker](https://www.angusj.com/resourcehacker/reshacker_setup.exe)
  
Agora vamos configurar o Visual Studio Code.
- Entre no VSCODE
- Se o instalador não fez um atalho na área de trabalho e você não sabe onde o executável se encontra: entre no CMD
- Aperte a tecla "Win" (Windows)
- digite: CMD (Ou prompt de comando)
- entre no terminal e digite: Code para entrar automaticamente
- Vá na área de extensões (Ela é representada com o icone de um conjunto de quatro caixas)
- Dentro da área de extensões digite: Python e baixe a versão oficial da microsoft
- Espere baixar e quando concluir clique no mesmo icone que você usou para entrar para fechar a aba

Seu ambiente já está quase pronto. Agora você precisa fazer dowload dos arquivos para executar o código.
- Primeiro, baixe o arquivo

Depois de baixado as tecnologias necessárias

---
## 📁 Estrutura das pastas
```
📂 Cyber Soc Analysis/
│
├── 📂 Docs/
│   ├── 📂 Generic_Examples/
│   │   ├── 🖼️ print1.png
│   │   └── 🖼️ print2.png
│   │
│   ├── 📂 Real-world_Example/
│   │   ├── 📂 Virus.PDF/
│   │   │   ├── 📄 documento_importante.pdf.exe
│   │   │   ├── 📄 criador.py
│   │   │   ├── 🖼️ icone_pdf.ico
│   │   │   └── 📄 instrucoes.txt
│   │   │
│   │   ├── 🖼️ email_nubank.png
│   │   └── 📄 descricao.md
│   │
│   ├── 📄 Attack-chain.md
│   └── 📄 Threat-Overview.md
│
├── 📄 README.md
└── 📄 README_PT-BR.md                      
```
