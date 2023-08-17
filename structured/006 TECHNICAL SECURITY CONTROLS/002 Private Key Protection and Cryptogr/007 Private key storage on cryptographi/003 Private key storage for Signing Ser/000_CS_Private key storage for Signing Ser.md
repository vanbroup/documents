#### 6.2.7.3 Private key storage for Signing Services

The Signing Service MUST ensure that a Subscriber's Private Key is generated, stored, and used in a secure environment that has controls to prevent theft or misuse. A Signing Service MUST enforce multi-factor authentication to access and authorize Code Signing and obtain a representation from the Subscriber that they will securely store the tokens required for multi-factor access. A system used to host a Signing Service MUST NOT be used for web browsing. The Signing Service MUST run a regularly updated antivirus solution to scan the service for possible virus infection. The Signing Service MUST comply with the Network and Certificate System Security Requirements as a "Delegated Third Party".

For Code Signing Certificates, Signing Services shall protect Private Keys in a Hardware Crypto Module conforming to at least FIPS 140-2 level 2 or Common Criteria EAL 4+.

Techniques that MAY be used to satisfy this requirement include:

1.  Use of an HSM, verified by means of a manufacturer's certificate;
2.  A cloud-based key generation and protection solution with the following requirements:
    a.  Key creation, storage, and usage of Private Key must remain within the security boundaries of the cloud solution’s Hardware Crypto Module that conforms to the specified requirements;
    b.  Subscription at the level that manages the Private Key must be configured to log all access, operations, and configuration changes on the resources securing the Private Key.
3.	 A Hardware Crypto Module provided by the CA;
4.	 Contractual terms in the Subscriber Agreement requiring the Subscriber to protect the Private Key to a standard of at least FIPS 140-2 level 2 or Common Criteria EAL 4+ and with compliance being confirmed by means of an audit.

