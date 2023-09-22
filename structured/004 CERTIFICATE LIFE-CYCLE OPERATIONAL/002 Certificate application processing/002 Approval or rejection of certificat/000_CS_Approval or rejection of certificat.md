### 4.2.2 Approval or rejection of certificate applications

CAs MUST not issue new or replacement Code Signing Certificates to an entity that the CA determined intentionally signed Suspect Code. The CA MUST keep meta-data about the reason for revoking a Code Signing Certificate as proof that the Code Signing Certificate was not revoked because the Applicant was intentionally signing Suspect Code.

CAs MAY issue new or replacement Code Signing Certificates to an entity who is the victim of a documented Takeover Attack, resulting in either a loss of control of their code-signing service or loss of the Private Key associated with their Code Signing Certificate.

If the CA is aware that the Applicant was the victim of a Takeover Attack, the CA MUST verify that the Applicant is protecting its Code Signing Private Keys under [Section 6.2.7.4.1](#62741-subscriber-private-key-protection)(1) or [Section 6.2.7.4.1](#62741-subscriber-private-key-protection)(2). The CA MUST verify the Applicant's compliance with [Section 6.2.7.4.1](#62741-subscriber-private-key-protection)(1) or [Section 6.2.7.4.1](#62741-subscriber-private-key-protection)(2) through:

  1. Technical means that confirm the Private Keys are protected using the method described in [Section 6.2.7.4.1](#62741-subscriber-private-key-protection)(1) or [Section 6.2.7.4.1](#62741-subscriber-private-key-protection)(2); or
  2. Relying on a report provided by the Applicant that is signed by an auditor who is approved by the CA and who has IT and security training or is a CISA.

Documentation of a Takeover Attack MAY include a police report (validated by the CA) or public news report that admits that the attack took place. The Subscriber MUST provide a report from an auditor with IT and security training or a CISA that provides information on how the Subscriber was storing and using Private keys and how the intended solution for better security meets the guidelines for improved security.

Except where issuance is expressly authorized by the Application Software Supplier, CAs MUST not issue new Code Signing Certificates to an entity where the CA is aware that the entity has been the victim of two Takeover Attacks or where the CA is aware that entity breached a requirement under this Section to protect Private Keys under [Section 6.2.7.4.1](#62741-subscriber-private-key-protection)(1) or [Section 6.2.7.4.1](#62741-subscriber-private-key-protection)(2).

