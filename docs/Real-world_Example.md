# Real-World Example
Imagine you are checking your email normally when you suddenly receive a message that appears to come from Nubank reporting suspicious activity in your account. The email states that your account has been temporarily frozen and that you must review attached documents to restore access. The message creates a sense of urgency and fear, encouraging you to act quickly. This is the first phase of many cyberattacks: social engineering. The attacker manipulates the user's emotions to increase the chances that the victim will click on a malicious link or download an infected file. Once the victim downloads or opens the attachment (often disguised as a PDF or document), malicious code may execute on the system. At this point, the malware begins its operation, installing itself on the device and allowing the attacker to perform unauthorized actions.

# Essential Concepts
To understand how attackers extract sensitive information, it is necessary to understand the fundamental mechanisms behind malware-based attacks. Although attack techniques vary depending on the attacker’s objectives, most attacks share several common characteristics:

- They exploit vulnerabilities in digital systems that store valuable data
- They rely on malicious software to gain financial or strategic benefits
- Malware is one of the most common tools used in cyberattacks
- Social engineering remains one of the most effective techniques used by attackers

# How Malware Actually Works
Once a system is infected, malware can execute processes without the user's knowledge or consent. Instead of directly damaging files immediately, most modern malware performs several steps in sequence in order to maintain control over the system and achieve its objective.

## Delivery

The malware first needs to reach the target system. Common delivery methods include:

- phishing emails

- malicious downloads

- compromised websites

- infected USB devices

- exploitation of software vulnerabilities

## Execution

After delivery, the malicious code must be executed. This can happen when:

- the user opens an infected file

- a vulnerability is exploited automatically

- a seemingly legitimate program runs hidden malicious code

## Installation

The malware then attempts to install itself on the system. This may involve:

- copying malicious files into system directories

- modifying system configuration files

- creating hidden processes

- The goal is to ensure that the malware remains active.

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
