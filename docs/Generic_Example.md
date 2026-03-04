# Attack Chain Analysis – Phishing Scenario

This project applies the Cyber Kill Chain model to analyze a phishing-based attack from a SOC (Security Operations Center) perspective. The objective is to understand how the attack progresses and identify detection opportunities across different stages of the attack lifecycle.

---

## Common Threats

- Phishing emails impersonating legitimate companies  
- Spoofed sender domains  
- Fake login pages  
- Encoded malicious attachments (e.g., base64 files)  
- Embedded remote tracking content  

---

## Attack Stages (Cyber Kill Chain Model)

### Reconnaissance

- Collection of publicly available information:
  - Email addresses  
  - Organizational structure  
  - Service providers  
- Sources may include:
  - Social media  
  - Data leaks  
  - Automated harvesting tools  

---

### Weaponization

- Creation of the phishing artifact:
  - Spoofed email template  
  - Fake authentication page  
  - Malicious or encoded attachment  
  - Remote tracking mechanisms  

---

### Delivery

- Transmission of the phishing email to the victim.
- Indicators of compromise:
  - Suspicious or recently registered domains  
  - Sender/domain mismatches  
  - Encoded attachments  
  - Reputation-based alerts  

- SOC monitoring focus:
  - Email gateway logs  
  - Domain validation checks  

---

### Exploitation

- Victim interaction with malicious content:
  - Clicking links  
  - Downloading attachments  
  - Submitting credentials  

- Detection opportunities:
  - Abnormal login attempts  
  - Access from unfamiliar IP addresses  
  - Logins outside behavioral patterns  

---

### Installation

- Possible malware execution and persistence.
- Monit
