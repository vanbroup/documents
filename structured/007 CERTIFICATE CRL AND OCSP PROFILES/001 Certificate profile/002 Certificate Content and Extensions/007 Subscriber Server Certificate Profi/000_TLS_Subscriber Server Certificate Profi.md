#### 7.1.2.7 Subscriber (Server) Certificate Profile

| __Field__                  | __Description__ |
| ---                        | ------          |
| `tbsCertificate`           | |
|     `version`              | MUST be v3(2) |
|     `serialNumber`         | MUST be a non-sequential number greater than zero (0) and less than 2¹⁵⁹ containing at least 64 bits of output from a CSPRNG. |
|     `signature`            | See [Section 7.1.3.2](#7132-signature-algorithmidentifier) |
|     `issuer`               | MUST be byte-for-byte identical to the `subject` field of the Issuing CA. See [Section 7.1.4.1](#7141-name-encoding) |
|     `validity`             | |
|          `notBefore`       | A value within 48 hours of the certificate signing operation. |
|          `notAfter`        | See [Section 6.3.2](#632-certificate-operational-periods-and-key-pair-usage-periods) |
|     `subject`              | See [Section 7.1.2.7.1](#71271-subscriber-certificate-types) |
|     `subjectPublicKeyInfo` | See [Section 7.1.3.1](#7131-subjectpublickeyinfo) |
|     `issuerUniqueID`       | MUST NOT be present |
|     `subjectUniqueID`      | MUST NOT be present |
|     `extensions`           | See [Section 7.1.2.7.6](#71276-subscriber-certificate-extensions) |
| `signatureAlgorithm`       | Encoded value MUST be byte-for-byte identical to the `tbsCertificate.signature`. |
| `signature`                | |

