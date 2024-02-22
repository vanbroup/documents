#### 7.1.2.2 Cross-Certified Subordinate CA Certificate Profile

This Certificate Profile MAY be used when issuing a CA Certificate using the same Subject Name and Subject Public Key Information as one or more existing CA Certificate(s), whether a Root CA Certificate or Subordinate CA Certificate.

Before issuing a Cross-Certified Subordinate CA, the Issuing CA MUST confirm that the existing CA Certificate(s) are subject to these Baseline Requirements and were issued in compliance with the then-current version of the Baseline Requirements at time of issuance.

| __Field__                  | __Description__ |
| ---                        | ------          |
| `tbsCertificate`           | |
|     `version`              | MUST be v3(2) |
|     `serialNumber`         | MUST be a non-sequential number greater than zero (0) and less than 2¹⁵⁹ containing at least 64 bits of output from a CSPRNG. |
|     `signature`            | See [Section 7.1.3.2](#7132-signature-algorithmidentifier) |
|     `issuer`               | MUST be byte-for-byte identical to the `subject` field of the Issuing CA. See [Section 7.1.4.1](#7141-name-encoding) |
|     `validity`             | See [Section 7.1.2.2.1](#71221-cross-certified-subordinate-ca-validity) |
|     `subject`              | See [Section 7.1.2.2.2](#71222-cross-certified-subordinate-ca-naming) |
|     `subjectPublicKeyInfo` | See [Section 7.1.3.1](#7131-subjectpublickeyinfo) |
|     `issuerUniqueID`       | MUST NOT be present |
|     `subjectUniqueID`      | MUST NOT be present |
|     `extensions`           | See [Section 7.1.2.2.3](#71223-cross-certified-subordinate-ca-extensions) |
| `signatureAlgorithm`       | Encoded value MUST be byte-for-byte identical to the `tbsCertificate.signature`. |
| `signature`                | |

