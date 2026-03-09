# Exemplo real
Imagine que você está navegando normalmente pelo seu email, e que de repente você se depara com um suposto email da nubank sobre uma atividade suspeita em sua conta. Ao clicar vocẽ nota que há uma mensagem dizendo que seus dados foram congelados e que eles só seriam liberados mediante processos que incluem baixar documentos e arquivos suspeitos. A primeira fase da invazão começa pela mente do usuário por meio da imposição de medo e urgência. Depois de instabilizado, a vítima clica no link ou baixa o arquivo solicitado, que é aí que o malware entra em ação, invadindo os demais arquivos e danificando sistemas do dispositivo afetado.

# Pontos essênciais
Para se amlisar como tais métodos de extração de informações sigilosas são realizados, é necessário se entender os fundamentos de como tais ataques acontecem na pŕatica. Os métodos podem se variar de acordo com o objetivo e intenções do invazor, porém em sua maioria eles contam com os seguintes pontos.

- Exploram falhas de sistemas digitais que armazenam dados valiosos
- Utilizam software malicioso para onterem lucro
- Malware é uma das ferramentas mais comuns em ataques cibernéticos
- Engenharia social é a maior ferramenta de invazores e pessoas mal intencionadas

# Afinal, como um malware funciona?
Depois de infectado o sistema, ele começa a executar comandos em segundo plano sem o consentimento do usuário através de códigos do painel de controle do sistema para se extrair dados importantes das vítimas. O processo pode ocorrer de maneira silenciosa e demorar dias em execução. Os tipos de malwares podem assumir diferentes tipos, sendo os principais: 

## Trojan (Cavalo de Troia)
  
Esse tipo de malware se disfarça como um programa legítimo. Quando o usuário instala o software, ele abre uma porta de acesso remoto para o invasor, permitindo controle parcial ou total do sistema.

## Ransomware

Esse malware criptografa arquivos importantes do computador, como documentos, fotos e bancos de dados. Depois disso, o invasor exige um pagamento para liberar a chave de descriptografia.

## Spyware

Projetado para espionar o usuário. Pode registrar atividades do computador, capturar senhas e coletar informações pessoais sem que a vítima perceba.

## Keylogger

Um tipo específico de spyware que registra tudo que é digitado no teclado. Dessa forma, o invasor pode obter logins, senhas bancárias e outros dados confidenciais.

## Worms (vermes)

Diferente de outros malwares, worms conseguem se espalhar automaticamente pela rede, infectando vários computadores sem interação direta do usuário.

# Como o malware se mantém no sistema

Após infectar um dispositivo, muitos malwares tentam garantir persistência, ou seja, continuar ativos mesmo depois que o computador é reiniciado.
Isso pode acontecer por meio de:

- criação de processos ocultos no sistema

- modificação de arquivos do sistema operacional

- instalação de serviços automáticos

- alteração de configurações de inicialização

# Comunicação com servidores externos

Em muitos ataques, o malware se conecta a servidores controlados pelo invasor, conhecidos como servidores de comando e controle (C2). Essa comunicação permite que o atacante:

- envie novos comandos para o malware

- receba dados roubados do sistema

- atualize o software malicioso

- utilize o computador infectado em redes de ataques coordenados

Essas redes são chamadas de botnets, que podem ser usadas para ataques de negação de serviço (DDoS), envio de spam ou mineração ilegal de criptomoedas.

---

# Casos reais famosos

## WannaCry

Um ransomware que explorou vulnerabilidades do Microsoft Windows para se espalhar automaticamente por redes corporativas.
Resultado: centenas de milhares de computadores infectados globalmente.

## Stuxnet

Um malware sofisticado criado para sabotar equipamentos industriais em instalações nucleares no Irã. Foi um dos primeiros exemplos de arma cibernética capaz de causar danos físicos.

## NotPetya

Um malware destrutivo que se espalhou rapidamente entre redes corporativas e causou bilhões em prejuízos.
## SOC Perspective
From a SOC (Blue Team) standpoint, these threats can be identified through log analysis, abnormal access patterns, user reports, and indicators of compromise.
