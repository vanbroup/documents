##### 7.1.2.11.2 CRL Distribution Points

The CRL Distribution Points extension MUST be present in:
- Subordinate CA Certificates; and
- Subscriber Certificates that 1) do not qualify as "Short-lived Subscriber Certificates" and 2) do not include an Authority Information Access extension with an id-ad-ocsp accessMethod.

The CRL Distribution Points extension SHOULD NOT be present in:
- Root CA Certificates.

The CRL Distribution Points extension is OPTIONAL in:
- Short-lived Subscriber Certificates.

The CRL Distribution Points extension MUST NOT be present in:
- OCSP Responder Certificates.

When present, the CRL Distribution Points extension MUST contain at least one `DistributionPoint`; containing more than one is NOT RECOMMENDED. All `DistributionPoint` items must be formatted as follows:

Table: `DistributionPoint` profile

| __Field__           | __Presence__    | __Description__ |
| ---                 | --              | ------          |
| `distributionPoint` | MUST            | The `DistributionPointName` MUST be a `fullName` formatted as described below. |
| `reasons`           | MUST NOT        |                 |
| `cRLIssuer`         | MUST NOT        |                 |

A `fullName` MUST contain at least one `GeneralName`; it MAY contain more than one. All `GeneralName`s MUST be of type `uniformResourceIdentifier`, and the scheme of each MUST be "http". The first `GeneralName` must contain the HTTP URL of the Issuing CA's CRL service for this certificate.

