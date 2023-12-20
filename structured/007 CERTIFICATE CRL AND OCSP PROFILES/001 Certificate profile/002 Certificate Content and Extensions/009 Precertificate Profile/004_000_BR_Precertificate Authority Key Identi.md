##### 7.1.2.9.4 Precertificate Authority Key Identifier

For Precertificates issued by a Precertificate Signing CA, the contents of the `authorityKeyIdentifier` extension MUST be one of the following:

1. SHOULD be as defined in the profile below, or;
2. MAY be byte-for-byte identical with the contents of the `authorityKeyIdentifier` extension of the corresponding Certificate.


| __Field__                   | __Description__ |
| ---                         | ------- |
| `keyIdentifier`             | MUST be present. MUST be identical to the `subjectKeyIdentifier` field of the [Precertificate Signing CA Certificate](#7124-technically-constrained-precertificate-signing-ca-certificate-profile) |
| `authorityCertIssuer`       | MUST NOT be present |
| `authorityCertSerialNumber` | MUST NOT be present |


**Note**: [RFC 6962](https://datatracker.ietf.org/doc/html/rfc6962) describes how the `authorityKeyIdentifier` present on a Precertificate is transformed to contain the value of the Precertificate Signing CA's `authorityKeyIdentifier` extension (i.e. reflecting the actual issuer certificate's `keyIdentifier`), thus matching the corresponding Certificate when verified by clients. These Baseline Requirements RECOMMEND the use of the Precertificate Signing CA's `keyIdentifier` in Precertificates issued by it in order to ensure consistency between the `subjectKeyIdentifier` and `authorityKeyIdentifier` of all certificates in the chain. Although [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280) does not strictly require such consistency, a number of client implementations enforce such consistency for Certificates, and this avoids any risks from Certificate Transparency Logs incorrectly implementing such checks.

