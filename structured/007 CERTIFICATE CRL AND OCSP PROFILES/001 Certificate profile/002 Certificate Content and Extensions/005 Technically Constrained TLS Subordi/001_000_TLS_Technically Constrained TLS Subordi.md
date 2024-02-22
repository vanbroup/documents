##### 7.1.2.5.1 Technically Constrained TLS Subordinate CA Extensions

| __Extension__                     | __Presence__    | __Critical__          | __Description__ |
| ----                              | -               | -                     | ----- |
| `authorityKeyIdentifier`          | MUST            | N                     | See [Section 7.1.2.11.1](#712111-authority-key-identifier) |
| `basicConstraints`                | MUST            | Y                     | See [Section 7.1.2.10.4](#712104-ca-certificate-basic-constraints) |
| `certificatePolicies`             | MUST            | N                     | See [Section 7.1.2.10.5](#712105-ca-certificate-certificate-policies) |
| `crlDistributionPoints`           | MUST            | N                     | See [Section 7.1.2.11.2](#712112-crl-distribution-points) |
| `keyUsage`                        | MUST            | Y                     | See [Section 7.1.2.10.7](#712107-ca-certificate-key-usage) |
| `subjectKeyIdentifier`            | MUST            | N                     | See [Section 7.1.2.11.4](#712114-subject-key-identifier) |
| `extKeyUsage`                     | MUST[^eku_ca]   | N                     | See [Section 7.1.2.10.6](#712106-ca-certificate-extended-key-usage) |
| `nameConstraints`                 | MUST            | \*[^name_constraints] | See [Section 7.1.2.5.2](#71252-technically-constrained-tls-subordinate-ca-name-constraints) |
| `authorityInformationAccess`      | SHOULD          | N                     | See [Section 7.1.2.10.3](#712103-ca-certificate-authority-information-access) |
| Signed Certificate Timestamp List | MAY             | N                     | See [Section 7.1.2.11.3](#712113-signed-certificate-timestamp-list) |
| Any other extension               | NOT RECOMMENDED | -                     | See [Section 7.1.2.11.5](#712115-other-extensions) |

