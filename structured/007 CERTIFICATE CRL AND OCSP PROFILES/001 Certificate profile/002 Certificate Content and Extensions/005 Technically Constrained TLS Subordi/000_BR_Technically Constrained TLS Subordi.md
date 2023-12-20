#### 7.1.2.5 Technically Constrained TLS Subordinate CA Certificate Profile

This Certificate Profile MAY be used when issuing a CA Certificate that will be considered Technically Constrained, and which will be used to issue TLS certificates directly or transitively.

| __Field__                  | __Description__ |
| ---                        | ------          |
| `tbsCertificate`           | |
|     `version`              | MUST be v3(2) |
|     `serialNumber`         | MUST be a non-sequential number greater than zero (0) and less than 2¹⁵⁹ containing at least 64 bits of output from a CSPRNG. |
|     `signature`            | See [Section 7.1.3.2](#7132-signature-algorithmidentifier) |
|     `issuer`               | MUST be byte-for-byte identical to the `subject` field of the Issuing CA. See [Section 7.1.4.1](#7141-name-encoding) |
|     `validity`             | See [Section 7.1.2.10.1](#712101-ca-certificate-validity) |
|     `subject`              | See [Section 7.1.2.10.2](#712102-ca-certificate-naming) |
|     `subjectPublicKeyInfo` | See [Section 7.1.3.1](#7131-subjectpublickeyinfo) |
|     `issuerUniqueID`       | MUST NOT be present |
|     `subjectUniqueID`      | MUST NOT be present |
|     `extensions`           | See [Section 7.1.2.5.1](#71251-technically-constrained-tls-subordinate-ca-extensions) |
| `signatureAlgorithm`       | Encoded value MUST be byte-for-byte identical to the `tbsCertificate.signature`. |
| `signature`                | |

