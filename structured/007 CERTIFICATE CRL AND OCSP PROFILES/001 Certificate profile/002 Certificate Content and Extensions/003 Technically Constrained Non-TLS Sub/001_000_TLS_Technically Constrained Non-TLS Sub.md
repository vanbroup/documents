##### 7.1.2.3.1 Technically Constrained Non-TLS Subordinate CA Extensions

| __Extension__                     | __Presence__    | __Critical__          | __Description__ |
| ----                              | -               | -                     | ----- |
| `authorityKeyIdentifier`          | MUST            | N                     | See [Section 7.1.2.11.1](#712111-authority-key-identifier) |
| `basicConstraints`                | MUST            | Y                     | See [Section 7.1.2.10.4](#712104-ca-certificate-basic-constraints) |
| `crlDistributionPoints`           | MUST            | N                     | See [Section 7.1.2.11.2](#712112-crl-distribution-points) |
| `keyUsage`                        | MUST            | Y                     | See [Section 7.1.2.10.7](#712107-ca-certificate-key-usage) |
| `subjectKeyIdentifier`            | MUST            | N                     | See [Section 7.1.2.11.4](#712114-subject-key-identifier) |
| `extKeyUsage`                     | MUST[^eku_ca]   | N                     | See [Section 7.1.2.3.3](#71233-technically-constrained-non-tls-subordinate-ca-extended-key-usage)|
| `authorityInformationAccess`      | SHOULD          | N                     | See [Section 7.1.2.10.3](#712103-ca-certificate-authority-information-access) |
| `certificatePolicies`             | MAY             | N                     | See [Section 7.1.2.3.2](#71232-technically-constrained-non-tls-subordinate-ca-certificate-policies) |
| `nameConstraints`                 | MAY             | \*[^name_constraints] | See [Section 7.1.2.10.8](#712108-ca-certificate-name-constraints) |
| Signed Certificate Timestamp List | MAY             | N                     | See [Section 7.1.2.11.3](#712113-signed-certificate-timestamp-list) |
| Any other extension               | NOT RECOMMENDED | -                     | See [Section 7.1.2.11.5](#712115-other-extensions) |

