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

## Trojan (Cavalo de troia)
  
This type of malware disguises itself as a legitimate program. When the user installs the software, it opens a remote access backdoor for the attacker, enabling partial or total control of the system.

## Ransomware

This malware encrypts important files on the computer, such as documents, photos, and databases. Subsequently, the attacker demands a payment to release the decryption key.

## Spyware

Designed to spy on the user. It can record computer activities, capture passwords, and collect personal information without the victim's awareness.

## Keylogger

A specific type of spyware that records everything typed on the keyboard. In this manner, the attacker can obtain login credentials, banking passwords, and other sensitive data.

## Worms (vermes)

Unlike other types of malware, worms can spread automatically across a network, infecting multiple computers without direct user interaction.

# How Malware Maintains Persistence on the System

After infecting a device, many malware variants attempt to ensure persistence, meaning they remain active even after the computer is restarted.
This can be achieved through:

- Creation of hidden system processes

- Modification of operating system files

- Installation of automatic services

- Alteration of startup configurations
  
# Communication with External Servers

In many attacks, malware connects to servers controlled by the attacker, known as Command and Control (C2) servers. This communication enables the attacker to:

- Send new commands to the malware

- Receive stolen data from the system

- Update the malicious software

- Utilize the infected computer in coordinated attack networks
  
These networks are called botnets, which can be employed for Distributed Denial of Service (DDoS) attacks, spam distribution, or illegal cryptocurrency mining.

---

# Notable Real-World Cases

## WannaCry

A ransomware that exploited vulnerabilities in Microsoft Windows to spread automatically across corporate networks.
Outcome: hundreds of thousands of computers infected globally.

## Stuxnet

A sophisticated malware designed to sabotage industrial equipment at nuclear facilities in Iran. It was one of the first examples of a cyberweapon capable of causing physical damage.

## NotPetya

A destructive malware that spread rapidly across corporate networks and caused billions in damages.
