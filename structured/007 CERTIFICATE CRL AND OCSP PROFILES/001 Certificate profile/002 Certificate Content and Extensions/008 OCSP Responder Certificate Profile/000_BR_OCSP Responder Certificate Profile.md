#### 7.1.2.8 OCSP Responder Certificate Profile

If the Issuing CA does not directly sign OCSP responses, it MAY make use of an OCSP Authorized Responder, as defined by [RFC 6960](https://tools.ietf.org/html/rfc6960#section-4.2.2.2). The Issuing CA of the Responder MUST be the same as the Issuing CA for the Certificates it provides responses for.

| __Field__                  | __Description__ |
| ---                        | ------          |
| `tbsCertificate`           | |
|     `version`              | MUST be v3(2) |
|     `serialNumber`         | MUST be a non-sequential number greater than zero (0) and less than 2¹⁵⁹ containing at least 64 bits of output from a CSPRNG. |
|     `signature`            | See [Section 7.1.3.2](#7132-signature-algorithmidentifier) |
|     `issuer`               | MUST be byte-for-byte identical to the `subject` field of the Issuing CA. See [Section 7.1.4.1](#7141-name-encoding) |
|     `validity`             | See [Section 7.1.2.8.1](#71281-ocsp-responder-validity) |
|     `subject`              | See [Section 7.1.2.10.2](#712102-ca-certificate-naming) |
|     `subjectPublicKeyInfo` | See [Section 7.1.3.1](#7131-subjectpublickeyinfo) |
|     `issuerUniqueID`       | MUST NOT be present |
|     `subjectUniqueID`      | MUST NOT be present |
|     `extensions`           | See [Section 7.1.2.8.2](#71282-ocsp-responder-extensions) |
| `signatureAlgorithm`       | Encoded value MUST be byte-for-byte identical to the `tbsCertificate.signature`. |
| `signature`                | |

