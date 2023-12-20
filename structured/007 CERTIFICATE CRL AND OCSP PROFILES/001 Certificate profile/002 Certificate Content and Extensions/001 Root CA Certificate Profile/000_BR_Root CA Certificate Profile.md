#### 7.1.2.1 Root CA Certificate Profile

| __Field__                  | __Description__ |
| ---                        | ------          |
| `tbsCertificate`           | |
|     `version`              | MUST be v3(2) |
|     `serialNumber`         | MUST be a non-sequential number greater than zero (0) and less than 2¹⁵⁹ containing at least 64 bits of output from a CSPRNG. |
|     `signature`            | See [Section 7.1.3.2](#7132-signature-algorithmidentifier) |
|     `issuer`               | Encoded value MUST be byte-for-byte identical to the encoded `subject` |
|     `validity`             | See [Section 7.1.2.1.1](#71211-root-ca-validity) |
|     `subject`              | See [Section 7.1.2.10.2](#712102-ca-certificate-naming) |
|     `subjectPublicKeyInfo` | See [Section 7.1.3.1](#7131-subjectpublickeyinfo) |
|     `issuerUniqueID`       | MUST NOT be present |
|     `subjectUniqueID`      | MUST NOT be present |
|     `extensions`           | See [Section 7.1.2.1.2](#71212-root-ca-extensions) |
| `signatureAlgorithm`       | Encoded value MUST be byte-for-byte identical to the `tbsCertificate.signature`. |
| `signature`                | |

