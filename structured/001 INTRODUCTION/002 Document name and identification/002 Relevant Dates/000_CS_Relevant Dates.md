### 1.2.2 Relevant Dates

| **Compliance** | **Section(s)** | **Summary Description (See Full Text for Details)** |
|--|--|----------|
| 2021-06-01 | 6.1.5 | CAs SHALL support minimum RSA-3072 for Code Signing Certificates, Root Certificates and Subordinate CA Certificates. CAs SHALL NOT support SHA-1 digest algorithm for Code Signing Certificates.|
| 2021-06-01 | 5.3 | After 2021-06-01, the CA shall meet the requirements of EV Guidelines Section 14.1 for Non-EV and EV Code Signing Certificates.|
| 2021-06-01 | 6.2.7.4 | For EV Code Signing Certificates, Signing Services shall protect private keys in a FIPS 140-2 level 2 (or equivalent) crypto module. After 2021-06-01, the same protection requirements SHALL apply to Non EV Code Signing Certificates.|
| 2021-11-01 | 3.2.2.1 (5) | The method used to verify the identity of the Certificate Requester SHALL be per section 3.2.3.|
| 2022-03-31 | 7.1.6.3 | Subordinate CA Certificates issued for Subordinate CA that issues Timestamp Certificates and is an Affiliate of the Issuing CA must include the reserved identifier specified in Section 7.1.6.1.|
| 2022-04-30 | 7.1.3.2.1 | CAs SHALL NOT support SHA-1 digest algorithm for Timestamp tokens.|
| 2022-07-01 | 7.2.2 | For Code Signing Certificates, the time encoded in the Invalidity Date CRL entry extension MUST be equal to the time encoded in the revocationDate field of the CRL entry. |
| 2023-06-01 | 6.2.7.4.2 | Effective June 1, 2023, for Code Signing Certificates, CAs SHALL ensure that the Subscriber’s Private Key is generated, stored, and used in a suitable Hardware Crypto Module that meets or exceeds the requirements specified in section 6.2.7.4.1 (7-9).|
| 2023-06-01 | 6.2.7.4.2 | Effective June 1, 2023, for Code Signing Certificates, CAs SHALL ensure that the Subscriber’s Private Key is generated, stored, and used in a suitable Hardware Crypto Module that meets or exceeds the requirements specified in section 6.2.7.4.1 using one of the methods in 6.2.7.4.2.|
| 2023-06-01 | 6.2.7.4.2 | Any other method the CA uses to satisfy the Subscriber’s compliance with the private key protection requirements. The CA SHALL specify and describe in detail those other methods in its Certificate Policy or Certification Practice Statement, and SHALL propose those methods to the CA/Browser Forum Code Signing Working Group for inclusion into these requirements until June 1, 2023, using the questions@cabforum.org mailing list. After that date, the Code Signing Working Group will discuss the removal of this "any other method" and allow only CA/Browser Forum approved methods.|
| 2024-04-15 | 4.9.1 | This ballot updates the "Circumstances for revocation" in order to align it with the TLS and S/MIME BRs and set stricter requirements for revocation due to Private Key Compromise and use in Suspect Code. |

