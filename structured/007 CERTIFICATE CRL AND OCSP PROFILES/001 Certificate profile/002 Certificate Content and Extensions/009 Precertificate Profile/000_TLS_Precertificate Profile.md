#### 7.1.2.9 Precertificate Profile

A Precertificate is a signed data structure that can be submitted to a Certificate Transparency log, as defined by [RFC 6962](https://tools.ietf.org/doc/html/rfc6962). A Precertificate appears structurally identical to a Certificate, with the exception of a special critical poison extension in the `extensions` field, with the OID of `1.3.6.1.4.1.11129.2.4.3`. This extension ensures that the Precertificate will not be accepted as a Certificate by clients conforming to [RFC 5280](https://tools.ietf.org/doc/html/rfc5280). The existence of a signed Precertificate can be treated as evidence of a corresponding Certificate also existing, as the signature represents a binding commitment by the CA that it may issue such a Certificate.

A Precertificate is created after a CA has decided to issue a Certificate, but prior to the actual signing of the Certificate. The CA MAY construct and sign a Precertificate corresponding to the Certificate, for purposes of submitting to Certificate Transparency Logs. The CA MAY use the returned Signed Certificate Timestamps to then alter the Certificate's `extensions` field, adding a Signed Certificate Timestamp List, as defined in [Section 7.1.2.11.3](#712113-signed-certificate-timestamp-list) and as permitted by the relevant profile, prior to signing the Certificate.

Once a Precertificate is signed, relying parties are permitted to treat this as a binding commitment from the CA of the intent to issue a corresponding Certificate, or more commonly, that a corresponding Certificate exists. A Certificate is said to be corresponding to a Precertificate based upon the value of the `tbsCertificate` contents, as transformed by the process defined in [RFC 6962, Section 3.2](https://tools.ietf.org/doc/html/rfc6962#section-3.2).

This profile describes the transformations that are permitted to a Certificate to construct a Precertificate. CAs MUST NOT issue a Precertificate unless they are willing to issue a corresponding Certificate, regardless of whether they have done so. Similarly, a CA MUST NOT issue a Precertificate unless the corresponding Certificate conforms to these Baseline Requirements, regardless of whether the CA signs the corresponding Certificate.

A Precertificate may be issued either directly by the Issuing CA or by a Technically Constrained Precertificate Signing CA, as defined in [Section 7.1.2.4](#7124-technically-constrained-precertificate-signing-ca-certificate-profile). If issued by a Precertificate Signing CA, then in addition to the precertificate poison and signed certificate timestamp list extensions, the Precertificate `issuer` field and, if present, `authorityKeyIdentifier` extension, may differ from the Certificate, as described below.


Table: When the Precertificate is issued directly by the Issuing CA

| __Field__                  | __Description__ |
| ---                        | ------          |
| `tbsCertificate`           | |
|     `version`              | Encoded value MUST be byte-for-byte identical to the `version` field of the Certificate |
|     `serialNumber`         | Encoded value MUST be byte-for-byte identical to the `serialNumber` field of the Certificate |
|     `signature`            | Encoded value MUST be byte-for-byte identical to the `signature` field of the Certificate  |
|     `issuer`               | Encoded value MUST be byte-for-byte identical to the `issuer` field of the Certificate |
|     `validity`             | Encoded value MUST be byte-for-byte identical to the `validity` field of the Certificate |
|     `subject`              | Encoded value MUST be byte-for-byte identical to the `subject` field of the Certificate |
|     `subjectPublicKeyInfo` | Encoded value MUST be byte-for-byte identical to the `subjectPublicKeyInfo` field of the Certificate |
|     `issuerUniqueID`       | Encoded value MUST be byte-for-byte identical to the `issuerUniqueID` field of the Certificate, or omitted if omitted in the Certificate |
|     `subjectUniqueID`      | Encoded value MUST be byte-for-byte identical to the `subjectUniqueID` field of the Certificate, or omitted if omitted in the Certificate |
|     `extensions`           | See [Section 7.1.2.9.1](#71291-precertificate-profile-extensions---directly-issued) |
| `signatureAlgorithm`       | Encoded value MUST be byte-for-byte identical to the `tbsCertificate.signature`. |
| `signature`                | |


Table: When the Precertificate is issued by a Precertificate Signing CA on behalf of an Issuing CA

| __Field__                  | __Description__ |
| ---                        | ------          |
| `tbsCertificate`           | |
|     `version`              | Encoded value MUST be byte-for-byte identical to the `version` field of the Certificate |
|     `serialNumber`         | Encoded value MUST be byte-for-byte identical to the `serialNumber` field of the Certificate |
|     `signature`            | Encoded value MUST be byte-for-byte identical to the `signature` field of the Certificate  |
|     `issuer`               | Encoded value MUST be byte-for-byte identical to the `subject` field of the [Precertificate Signing CA Certificate](#7124-technically-constrained-precertificate-signing-ca-certificate-profile) |
|     `validity`             | Encoded value MUST be byte-for-byte identical to the `validity` field of the Certificate |
|     `subject`              | Encoded value MUST be byte-for-byte identical to the `subject` field of the Certificate |
|     `subjectPublicKeyInfo` | Encoded value MUST be byte-for-byte identical to the `subjectPublicKeyInfo` field of the Certificate |
|     `issuerUniqueID`       | Encoded value MUST be byte-for-byte identical to the `issuerUniqueID` field of the Certificate, or omitted if omitted in the Certificate |
|     `subjectUniqueID`      | Encoded value MUST be byte-for-byte identical to the `subjectUniqueID` field of the Certificate, or omitted if omitted in the Certificate |
|     `extensions`           | See [Section 7.1.2.9.2](#71292-precertificate-profile-extensions---precertificate-ca-issued) |
| `signatureAlgorithm`       | Encoded value MUST be byte-for-byte identical to the `tbsCertificate.signature`. |
| `signature`                | |

**Note**: This profile requires that the `serialNumber` field of the Precertificate be identical to that of the corresponding Certificate. [RFC 5280, Section 4.1.2.2](https://tools.ietf.org/doc/html/rfc5280#section-4.1.2.2) requires that the `serialNumber` of certificates be unique. For the purposes of this document, a Precertificate shall not be considered a "certificate" subject to that requirement, and thus may have the same `serialNumber` of the corresponding Certificate. However, this does not permit two Precertificates to share the same `serialNumber`, unless they correspond to the same Certificate, as this would otherwise indicate there are two corresponding Certificates that share the same `serialNumber`.

