##### 6.2.7.4.1 Subscriber Private Key protection

For Non-EV Code Signing Certificates issued prior to June 1, 2023, the CA MUST obtain a representation from the Subscriber that the Subscriber will use one of the following options to generate and protect their Code Signing Certificate Private Keys:

1.  A Trusted Platform Module (TPM) that generates and secures a Key Pair and that can document the Subscriber’s Private Key protection through a TPM key attestation. 
2.	 A suitable Hardware Crypto Module with a unit design form factor certified as conforming to at least FIPS 140-2 Level 2, Common Criteria EAL 4+, or equivalent. 
3.	 Another type of hardware storage token with a unit design form factor of SD Card or USB token (not necessarily certified as conformant with FIPS 140-2 Level 2 or Common Criteria EAL 4+). The Subscriber MUST also warrant that it will keep the token physically separate from the device that hosts the code signing function until a signing session is begun. 

For Non-EV Code Signing Certificates issued prior to June 1, 2023, a CA MUST recommend that the Subscriber protect Private Keys using the method described in Section 6.2.7.4.1(1) or 6.2.7.4.1(2) over the method described in Section 6.2.7.4.1(3) and obligate the Subscriber to protect Private Keys in accordance with [Section 9.6.3](#963-subscriber-representations-and-warranties) (2).

For EV Code Signing Certificates issued prior to June 1, 2023, CAs SHALL ensure that the Subscriber’s Private Key is generated, stored and used in a Hardware Crypto Module that meets or exceeds the requirements of FIPS 140-2 level 2 or Common Criteria EAL 4+. Acceptable methods of satisfying this requirement include (but are not limited to) the following:

4.	 The CA ships a suitable Hardware Crypto Module, with a preinstalled Private Key, in the form of a smartcard or USB device or similar;
5.	 The Subscriber counter-signs certificate requests that can be verified by using a manufacturer’s certificate indicating that the Private Key is managed in a suitable Hardware Crypto Module;
6.	 The Subscriber provides a suitable IT audit indicating that its operating environment achieves a level of security at least equivalent to that of FIPS 140-2 level 2.

Effective June 1, 2023, Subscriber Private Keys for Code Signing Certificates SHALL be protected per the following requirements.
The CA MUST obtain a contractual representation from the Subscriber that the Subscriber will use one of the following options to generate and protect their Code Signing Certificate Private Keys in a Hardware Crypto Module with a unit design form factor certified as conforming to at least FIPS 140-2 Level 2 or Common Criteria EAL 4+:

7.	 Subscriber uses a Hardware Crypto Module meeting the specified requirement;  
8.	 Subscriber uses a cloud-base key generation and protection solution with the following requirements:
    a.	Key creation, storage, and usage of Private Key must remain within the security boundaries of the cloud solution’s Hardware Crypto Module that conforms to the specified requirements;
    b.	Subscription at the level that manages the Private Key must be configured to log all access, operations, and configuration changes on the resources securing the Private Key.   
9.	 Subscriber uses a Signing Service which meets the requirements of [Section 6.2.7.3](#6273-private-key-storage-for-signing-services).

