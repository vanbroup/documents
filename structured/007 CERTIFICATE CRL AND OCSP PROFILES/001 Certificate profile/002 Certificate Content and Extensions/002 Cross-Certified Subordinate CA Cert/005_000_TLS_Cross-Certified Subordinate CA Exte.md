##### 7.1.2.2.5 Cross-Certified Subordinate CA Extended Key Usage - Restricted

Table: Restricted TLS Cross-Certified Subordinate CA Extended Key Usage Purposes (i.e., for restricted Cross-Certified Subordinate CAs issuing TLS certificates directly or transitively)

| __Key Purpose__        | __Description__ |
| ---                    | -------         |
| `id-kp-serverAuth`     | MUST be present.|
| `id-kp-clientAuth`     | MAY be present.|
| `id-kp-emailProtection`| MUST NOT be present.|
| `id-kp-codeSigning`    | MUST NOT be present.|
| `id-kp-timeStamping`   | MUST NOT be present.|
| `anyExtendedKeyUsage`  | MUST NOT be present.|
| Any other value        | NOT RECOMMENDED.|

Table: Restricted Non-TLS Cross-Certified Subordinate CA Extended Key Usage Purposes (i.e., for restricted Cross-Certified Subordinate CAs not issuing TLS certificates directly or transitively)

| __Key Purpose__        | __Description__ |
| ---                    | -------         |
| `id-kp-serverAuth`     | MUST NOT be present.|
| `anyExtendedKeyUsage`  | MUST NOT be present.|
| Any other value        | MAY be present.|

Each included Extended Key Usage key usage purpose:

  1. MUST apply in the context of the public Internet (e.g. MUST NOT be for a service that is only valid in a privately managed network), unless:
     a. the key usage purpose falls within an OID arc for which the Applicant demonstrates ownership; or,
     b. the Applicant can otherwise demonstrate the right to assert the key usage purpose in a public context.
  2. MUST NOT include semantics that will mislead the Relying Party about the certificate information verified by the CA, such as including a key usage purpose asserting storage on a smart card, where the CA is not able to verify that the corresponding Private Key is confined to such hardware due to remote issuance.
  3. MUST be verified by the Issuing CA (i.e. the Issuing CA MUST verify the Cross-Certified Subordinate CA is authorized to assert the key usage purpose).

CAs MUST NOT include additional key usage purposes unless the CA is aware of a reason for including the key usage purpose in the Certificate.

