##### 7.1.2.7.6 Subscriber Certificate Extensions

| __Extension__                     | __Presence__    | __Critical__ | __Description__ |
| ----                              | -               | -            | ----- |
| `authorityInformationAccess`      | MUST            | N            | See [Section 7.1.2.7.7](#71277-subscriber-certificate-authority-information-access) |
| `authorityKeyIdentifier`          | MUST            | N            | See [Section 7.1.2.11.1](#712111-authority-key-identifier) |
| `certificatePolicies`             | MUST            | N            | See [Section 7.1.2.7.9](#71279-subscriber-certificate-certificate-policies) |
| `extKeyUsage`                     | MUST            | N            | See [Section 7.1.2.7.10](#712710-subscriber-certificate-extended-key-usage) |
| `subjectAltName`                  | MUST            | *            | See [Section 7.1.2.7.12](#712712-subscriber-certificate-subject-alternative-name) |
| `nameConstraints`                 | MUST NOT        | -            | - |
| `keyUsage`                        | SHOULD          | Y            | See [Section 7.1.2.7.11](#712711-subscriber-certificate-key-usage) |
| `basicConstraints`                | MAY             | Y            | See [Section 7.1.2.7.8](#71278-subscriber-certificate-basic-constraints) |
| `crlDistributionPoints`           | *               | N            | See [Section 7.1.2.11.2](#712112-crl-distribution-points) |
| Signed Certificate Timestamp List | MAY             | N            | See [Section 7.1.2.11.3](#712113-signed-certificate-timestamp-list) |
| `subjectKeyIdentifier`            | NOT RECOMMENDED | N            | See [Section 7.1.2.11.4](#712114-subject-key-identifier) |
| Any other extension               | NOT RECOMMENDED | -            | See [Section 7.1.2.11.5](#712115-other-extensions) |

**Notes**: 
- whether or not the `subjectAltName` extension should be marked Critical depends on the contents of the Certificate's `subject` field, as detailed in [Section 7.1.2.7.12](#712712-subscriber-certificate-subject-alternative-name).
- whether or not the CRL Distribution Points extension must be present depends on 1) whether the Certificate includes an Authority Information Access extension with an id-ad-ocsp accessMethod and 2) the Certificate's validity period, as detailed in [Section 7.1.2.11.2](#712112-crl-distribution-points).

