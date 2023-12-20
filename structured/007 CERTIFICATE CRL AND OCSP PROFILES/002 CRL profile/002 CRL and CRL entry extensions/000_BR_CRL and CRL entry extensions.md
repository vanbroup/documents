### 7.2.2 CRL and CRL entry extensions

Table: CRL Extensions

| __Extension__              | __Presence__    | __Critical__ | __Description__ |
| ----                       | -               | -            | ----- |
| `authorityKeyIdentifier`   | MUST            | N            | See [Section 7.1.2.11.1](#712111-authority-key-identifier) |
| `CRLNumber`                | MUST            | N            | MUST contain an INTEGER greater than or equal to zero (0) and less than 2¹⁵⁹, and convey a strictly increasing sequence. |
| `IssuingDistributionPoint` | *               | Y            | See [Section 7.2.2.1 CRL Issuing Distribution Point](#7221-crl-issuing-distribution-point) |
| Any other extension        | NOT RECOMMENDED | -            | - |

Table: revokedCertificates Component

| __Component__        | __Presence__ | __Description__ |
| ----                 | -            | ----- |
| `serialNumber`       | MUST         | MUST be byte-for-byte identical to the serialNumber contained in the revoked Certificate. |
| `revocationDate`     | MUST         | Normally, the date and time revocation occurred. See the footnote following this table for circumstances where backdating is permitted. | 
| `crlEntryExtensions` | *            | See the "crlEntryExtensions Component" table for additional requirements. |

**Note:** The CA SHOULD update the revocation date in a CRL entry when it is determined that the private key of the Certificate was compromised prior to the revocation date that is indicated in the CRL entry for that Certificate. Backdating the revocationDate field is an exception to best practice described in RFC 5280 (Section 5.3.2); however, these requirements specify the use of the revocationDate field to support TLS implementations that process the revocationDate field as the date when the Certificate is first considered to be compromised.

Table: crlEntryExtensions Component 

| __CRL Entry Extension__   | __Presence__    | __Description__ |
| ---                       | -               | ------          |
| `reasonCode`              | *               | When present (OID 2.5.29.21), MUST NOT be marked critical and MUST indicate the most appropriate reason for revocation of the Certificate. <br><br> MUST be present unless the CRL entry is for a Certificate not technically capable of causing issuance and either 1) the CRL entry is for a Subscriber Certificate subject to these Requirements revoked prior to July 15, 2023 or 2) the reason for revocation (i.e., reasonCode) is unspecified (0). <br><br>See the "CRLReasons" table for additional requirements. |
| Any other value           | NOT RECOMMENDED | - |

Table: CRLReasons

| __RFC 5280 reasonCode__   | __RFC 5280 reasonCode value__ | __Description__ |
| ---                       | -    | ------          |
| unspecified               | 0    | Represented by the omission of a reasonCode. MUST be omitted if the CRL entry is for a Certificate not technically capable of causing issuance unless the CRL entry is for a Subscriber Certificate subject to these Requirements revoked prior to July 15, 2023. 
| keyCompromise             | 1    | Indicates that it is known or suspected that the Subscriber’s Private Key has been compromised. |
| affiliationChanged        | 3    | Indicates that the Subject's name or other Subject Identity Information in the Certificate has changed, but there is no cause to suspect that the Certificate's Private Key has been compromised. |
| superseded                | 4    | Indicates that the Certificate is being replaced because: the Subscriber has requested a new Certificate, the CA has reasonable evidence that the validation of domain authorization or control for any fully‐qualified domain name or IP address in the Certificate should not be relied upon, or the CA has revoked the Certificate for compliance reasons such as the Certificate does not comply with these Baseline Requirements or the CA's CP or CPS. |
| cessationOfOperation      | 5    | Indicates that the website with the Certificate is shut down prior to the expiration of the Certificate, or if the Subscriber no longer owns or controls the Domain Name in the Certificate prior to the expiration of the Certificate.
| certificateHold           | 6    | MUST NOT be included if the CRL entry is for 1) a Certificate subject to these Requirements, or 2) a Certificate not subject to these Requirements and was either A) issued on-or-after 2020-09-30 or B) has a `notBefore` on-or-after 2020-09-30.
| privilegeWithdrawn        | 9    | Indicates that there has been a subscriber-side infraction that has not resulted in keyCompromise, such as the Certificate Subscriber provided misleading information in their Certificate Request or has not upheld their material obligations under the Subscriber Agreement or Terms of Use. |

The Subscriber Agreement, or an online resource referenced therein, MUST inform Subscribers about the revocation reason options listed above and provide explanation about when to choose each option. Tools that the CA provides to the Subscriber MUST allow for these options to be easily specified when the Subscriber requests revocation of their Certificate, with the default value being that no revocation reason is provided (i.e. the default corresponds to the CRLReason “unspecified (0)” which results in no reasonCode extension being provided in the CRL). 

The privilegeWithdrawn reasonCode SHOULD NOT be made available to the Subscriber as a revocation reason option, because the use of this reasonCode is determined by the CA and not the Subscriber.

When a CA obtains verifiable evidence of Key Compromise for a Certificate whose CRL entry does not contain a reasonCode extension or has a reasonCode extension with a non-keyCompromise reason, the CA SHOULD update the CRL entry to enter keyCompromise as the CRLReason in the reasonCode extension. 

