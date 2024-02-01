##### 7.1.2.9.1 Precertificate Profile Extensions - Directly Issued

These extensions apply in the context of a Precertificate directly issued from a CA, and not from a Precertificate Signing CA Certificate, as defined in [Section 7.1.2.4](#7124-technically-constrained-precertificate-signing-ca-certificate-profile).

| __Extension__                                        | __Presence__ | __Critical__ | __Description__ |
| ----                                                 | -            | -            | ----- |
| Precertificate Poison (OID: 1.3.6.1.4.1.11129.2.4.3) | MUST         | Y            | See [Section 7.1.2.9.3](#71293-precertificate-poison) |
| Signed Certificate Timestamp List                    | MUST NOT     | -            | |
| Any other extension                                  | \*           | \*           | The order, criticality, and encoded values of all other extensions MUST be byte-for-byte identical to the `extensions` field of the Certificate |

**Note**: This requirement is expressing that if the Precertificate Poison extension is removed from the Precertificate, and the Signed Certificate Timestamp List is removed from the certificate, the contents of the `extensions` field MUST be byte-for-byte identical to the Certificate.

