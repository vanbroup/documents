##### 7.1.2.8.2 OCSP Responder Extensions

| __Extension__                     | __Presence__    | __Critical__ | __Description__ |
| ----                              | -               | -            | -----           |
| `authorityKeyIdentifier`          | MUST            | N            | See [Section 7.1.2.11.1](#712111-authority-key-identifier) |
| `extKeyUsage`                     | MUST            | -            | See [Section 7.1.2.8.5](#71285-ocsp-responder-extended-key-usage) |
| `id-pkix-ocsp-nocheck`            | MUST            | N            | See [Section 7.1.2.8.6](#71286-ocsp-responder-id-pkix-ocsp-nocheck) |
| `keyUsage`                        | MUST            | Y            | See [Section 7.1.2.8.7](#71287-ocsp-responder-key-usage) |
| `basicConstraints`                | MAY             | Y            | See [Section 7.1.2.8.4](#71284-ocsp-responder-basic-constraints) |
| `nameConstraints`                 | MUST NOT        | -            | - |
| `subjectAltName`                  | MUST NOT        | -            | - |
| `subjectKeyIdentifier`            | SHOULD          | N            | See [Section 7.1.2.11.4](#712114-subject-key-identifier) |
| `authorityInformationAccess`      | NOT RECOMMENDED | N            | See [Section 7.1.2.8.3](#71283-ocsp-responder-authority-information-access) |
| `certificatePolicies`             | MUST NOT        | N            | See [Section 7.1.2.8.8](#71288-ocsp-responder-certificate-policies) |
| `crlDistributionPoints`           | MUST NOT        | N            | See [Section 7.1.2.11.2](#712112-crl-distribution-points) |
| Signed Certificate Timestamp List | MAY             | N            | See [Section 7.1.2.11.3](#712113-signed-certificate-timestamp-list) |
| Any other extension               | NOT RECOMMENDED | -            | See [Section 7.1.2.11.5](#712115-other-extensions) |

