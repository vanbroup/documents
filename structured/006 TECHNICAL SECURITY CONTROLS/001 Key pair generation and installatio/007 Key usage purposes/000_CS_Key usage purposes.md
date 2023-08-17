### 6.1.7 Key usage purposes

Private Keys corresponding to Root Certificates MUST NOT be used to sign Certificates or create other Signatures except in the following cases:

1.  Self-signed Certificates to represent the Root CA itself;
2.  Certificates for Subordinate CAs and Cross Certificates;
3.  Certificates for infrastructure purposes (administrative role certificates, internal CA operational device certificates);
4.  Certificates for OCSP Response verification; and
5.  Signatures for OCSP Responses.

