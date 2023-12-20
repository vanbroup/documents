##### 7.1.2.9.2 Precertificate Profile Extensions - Precertificate CA Issued

These extensions apply in the context of a Precertificate from a Precertificate Signing CA Certificate, as defined in [Section 7.1.2.4](#7124-technically-constrained-precertificate-signing-ca-certificate-profile). For such Precertificates, the `authorityKeyIdentifier`, if present in the Certificate, is modified in the Precertificate, as described in [RFC 6962, Section 3.2](https://tools.ietf.org/doc/html/rfc6962#section-3.2).

| __Extension__                                        | __Presence__ | __Critical__ | __Description__ |
| ----                                                 | -            | -            | ----- |
| Precertificate Poison (OID: 1.3.6.1.4.1.11129.2.4.3) | MUST         | Y            | See [Section 7.1.2.9.3](#71293-precertificate-poison) |
| `authorityKeyIdentifier`                             | \*           | \*           | See [Section 7.1.2.9.4](#71294-precertificate-authority-key-identifier) |
| Signed Certificate Timestamp List                    | MUST NOT     | -            | |
| Any other extension                                  | \*           | \*           | The order, criticality, and encoded values of all other extensions MUST be byte-for-byte identical to the `extensions` field of the Certificate |

