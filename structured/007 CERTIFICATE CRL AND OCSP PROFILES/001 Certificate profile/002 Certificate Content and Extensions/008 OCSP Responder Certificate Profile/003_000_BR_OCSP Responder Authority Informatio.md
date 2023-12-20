##### 7.1.2.8.3 OCSP Responder Authority Information Access

For OCSP Responder certificates, this extension is NOT RECOMMENDED, as the Relying Party should already possess the necessary information. In order to validate the given Responder certificate, the Relying Party must have access to the Issuing CA's certificate, eliminating the need to provide `id-ad-caIssuers`. Similarly, because of the requirement for an OCSP Responder certificate to include the `id-pkix-ocsp-nocheck` extension, it is not necessary to provide `id-ad-ocsp`, as such responses will not be checked by Relying Parties.

If present, the `AuthorityInfoAccessSyntax` MUST contain one or more `AccessDescription`s. Each `AccessDescription` MUST only contain a permitted `accessMethod`, as detailed below, and each `AuthorityInfoAccessSyntax` MUST contain all required `AccessDescription`s.

| __Access Method__ | __OID__            | __Access Location__         | __Presence__    | __Maximum__ | __Description__ |
| --                | --                 | ----                        | -               | -          | ---             |
| `id-ad-ocsp`      | 1.3.6.1.5.5.7.48.1 | `uniformResourceIdentifier` | NOT RECOMMENDED | \*         | A HTTP URL of the Issuing CA's OCSP responder. |
| Any other value   | -                  | -                           | MUST NOT        | -          | No other `accessMethod`s may be used. |

