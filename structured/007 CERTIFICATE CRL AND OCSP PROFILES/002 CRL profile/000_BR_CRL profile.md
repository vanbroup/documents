## 7.2 CRL profile

Prior to 2024‐03‐15, the CA SHALL issue CRLs in accordance with the profile specified in these Requirements or the profile specified in Version 1.8.7 of the Baseline Requirements for the Issuance and Management of Publicly‐Trusted Certificates. Effective 2024‐03‐15, the CA SHALL issue CRLs in accordance with the profile specified in these Requirements.

If the CA asserts compliance with these Baseline Requirements, all CRLs that it issues MUST comply with the following CRL profile, which incorporates, and is derived from [RFC 5280](https://tools.ietf.org/html/rfc5280). Except as explicitly noted, all normative requirements imposed by RFC 5280 shall apply, in addition to the normative requirements imposed by this document. CAs SHOULD examine [RFC 5280, Appendix B](https://tools.ietf.org/html/rfc5280#appendix-B) for further issues to be aware of.

A full and complete CRL is a CRL whose scope includes all Certificates issued by the CA.

A partitioned CRL (sometimes referred to as a "sharded CRL") is a CRL with a constrained scope, such as all Certificates issued by the CA during a certain period of time ("temporal sharding"). Aside from the presence of the Issuing Distribution Point extension (OID 2.5.29.28) in partitioned CRLs, both CRL formats are syntactically the same from the perspective of this profile.

Minimally, CAs MUST issue either a "full and complete" CRL or a set of "partitioned" CRLs which cover the complete set of Certificates issued by the CA. In other words, if issuing only partitioned CRLs, the combined scope of those CRLs must be equivalent to that of a full and complete CRL. 

CAs MUST NOT issue indirect CRLs (i.e., the issuer of the CRL is not the issuer of all Certificates that are included in the scope of the CRL).

Table: CRL Fields

| __Field__                  | __Presence__    | __Description__ |
| ---                        | ------          | ------          |
| `tbsCertList`              |                 |                 |
|     `version`              | MUST            | MUST be v2(1), see [Section 7.2.1](#721-version-numbers) |
|     `signature`            | MUST            | See [Section 7.1.3.2](#7132-signature-algorithmidentifier) |
|     `issuer`               | MUST            | MUST be byte-for-byte identical to the `subject` field of the Issuing CA. |
|     `thisUpdate`           | MUST            | Indicates the issue date of the CRL. |
|     `nextUpdate`           | MUST            | Indicates the date by which the next CRL will be issued. For CRLs covering Subscriber Certificates, at most 10 days after the `thisUpdate`. For other CRLs, at most 12 months after the `thisUpdate`. |
|     `revokedCertificates`  | *               | MUST be present if the CA has issued a Certificate that has been revoked and the corresponding entry has yet to appear on at least one regularly scheduled CRL beyond the revoked Certificate's validity period. The CA SHOULD remove an entry for a corresponding Certificate after it has appeared on at least one regularly scheduled CRL beyond the revoked Certificate's validity period. See the "revokedCertificates Component" table for additional requirements.  |
|     `extensions`           | MUST            | See the "CRL Extensions" table for additional requirements. |
| `signatureAlgorithm`       | MUST            | Encoded value MUST be byte-for-byte identical to the `tbsCertList.signature`. |
| `signature`                | MUST            | - |
| Any other value            | NOT RECOMMENDED | - |

