#### 7.1.2.4 Technically Constrained Precertificate Signing CA Certificate Profile

This Certificate Profile MUST be used when issuing a CA Certificate that will be used as a Precertificate Signing CA, as described in [RFC 6962, Section 3.1](https://tools.ietf.org/html/rfc6962#section-3.1). If a CA Certificate conforms to this profile, it is considered Technically Constrained.

A Precertificate Signing CA MUST only be used to sign Precertificates, as defined in [Section 7.1.2.9](#7129-precertificate-profile). When a Precertificate Signing CA issues a Precertificate, it shall be interpreted as if the Issuing CA of the Precertificate Signing CA has issued a Certificate with a matching `tbsCertificate` of the Precertificate, after applying the modifications specified in [RFC 6962, Section 3.2](https://tools.ietf.org/html/rfc6962#section-3.2).

As noted in RFC 6962, Section 3.2, the `signature` field of a Precertificate is not altered as part of these modifications. As such, the Precertificate Signing CA MUST use the same signature algorithm as the Issuing CA when issuing Precertificates, and, correspondingly, MUST use a public key of the same public key algorithm as the Issuing CA, although MAY use a different CA Key Pair.

| __Field__                  | __Description__ |
| ---                        | ------          |
| `tbsCertificate`           | |
|     `version`              | MUST be v3(2) |
|     `serialNumber`         | MUST be a non-sequential number greater than zero (0) and less than 2¹⁵⁹ containing at least 64 bits of output from a CSPRNG. |
|     `signature`            | See [Section 7.1.3.2](#7132-signature-algorithmidentifier) |
|     `issuer`               | MUST be byte-for-byte identical to the `subject` field of the Issuing CA. See [Section 7.1.4.1](#7141-name-encoding) |
|     `validity`             | See [Section 7.1.2.10.1](#712101-ca-certificate-validity) |
|     `subject`              | See [Section 7.1.2.10.2](#712102-ca-certificate-naming) |
|     `subjectPublicKeyInfo` | The algorithm identifier MUST be byte-for-byte identical to the algorithm identifier of the `subjectPublicKeyInfo` field of the Issuing CA. See [Section 7.1.3.1](#7131-subjectpublickeyinfo) |
|     `issuerUniqueID`       | MUST NOT be present |
|     `subjectUniqueID`      | MUST NOT be present |
|     `extensions`           | See [Section 7.1.2.4.1](#71241-technically-constrained-precertificate-signing-ca-extensions) |
| `signatureAlgorithm`       | Encoded value MUST be byte-for-byte identical to the `tbsCertificate.signature`. |
| `signature`                | |

