##### 7.1.2.10.3 CA Certificate Authority Information Access

If present, the `AuthorityInfoAccessSyntax` MUST contain one or more `AccessDescription`s. Each `AccessDescription` MUST only contain a permitted `accessMethod`, as detailed below, and each `accessLocation` MUST be encoded as the specified `GeneralName` type.

The `AuthorityInfoAccessSyntax` MAY contain multiple `AccessDescription`s with the same `accessMethod`, if permitted for that `accessMethod`. When multiple `AccessDescription`s are present with the same `accessMethod`, each `accessLocation` MUST be unique, and each `AccessDescription` MUST be ordered in priority for that `accessMethod`, with the most-preferred `accessLocation` being the first `AccessDescription`. No ordering requirements are given for `AccessDescription`s that contain different `accessMethod`s, provided that previous requirement is satisfied.

| __Access Method__ | __OID__            | __Access Location__         | __Presence__ | __Maximum__ | __Description__ |
| --                | --                 | ----                        | -            | -          | ---             |
| `id-ad-ocsp`      | 1.3.6.1.5.5.7.48.1 | `uniformResourceIdentifier` | MAY          | \*         | A HTTP URL of the Issuing CA's OCSP responder. |
| `id-ad-caIssuers` | 1.3.6.1.5.5.7.48.2 | `uniformResourceIdentifier` | MAY          | \*         | A HTTP URL of the Issuing CA's certificate. |
| Any other value   | -                  | -                           | MUST NOT     | -          | No other `accessMethod`s may be used. |

