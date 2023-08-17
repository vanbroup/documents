###### 6.2.7.4.2 Subscriber Private Key verification

Effective June 1, 2023, for Code Signing Certificates, CAs SHALL ensure that the Subscriber’s Private Key is generated, stored, and used in a suitable Hardware Crypto Module that meets or exceeds the requirements specified in [Section 6.2.7.4.1](#62741-subscriber-private-key-protection). One of the following methods MUST be employed to satisfy this requirement:

1.	 The CA ships a suitable Hardware Crypto Module, with one or more pre-generated Key Pairs that the CA has generated using the Hardware Crypto Module; 
2.	 The Subscriber counter-signs certificate requests that can be verified by using a manufacturer’s certificate, commonly known as key attestation, indicating that the Private Key was generated in a non-exportable way using a suitable Hardware Crypto Module; 
3.	 The Subscriber uses a CA prescribed crypto library and a suitable Hardware Crypto Module combination for the Key Pair generation and storage;
4.	 The Subscriber provides an internal or external IT audit indicating that it is only using a suitable Hardware Crypto Module to generate Key Pairs to be associated with Code Signing Certificates;
5.	 The Subscriber provides a suitable report from the cloud-based key protection solution subscription and resources configuration protecting the Private Key in a suitable Hardware Crypto Module;
6.	 The CA relies on a report provided by the Applicant that is signed by an auditor who is approved by the CA and who has IT and security training or is a CISA witnesses the Key Pair creation in a suitable Hardware Crypto Module solution including a cloud-based key generation and protection solution;
7.	 The Subscriber provides an agreement that they use a Signing Service meeting the requirements of [Section 6.2.7.3](#6273-private-key-storage-for-signing-services);
8.	 Any other method the CA uses to satisfy this requirement. The CA SHALL specify and describe in detail those other methods in its Certificate Policy or Certification Practice Statement, and SHALL propose those methods to the CA/Browser Forum Code Signing Working Group for inclusion into these requirements until June 1, 2023, using the questions@cabforum.org mailing list. After that date, the Code Signing Working Group will discuss the removal of this "any other method" and allow only CA/Browser Forum-approved methods.

