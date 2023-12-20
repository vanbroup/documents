##### 7.1.2.1.2 Root CA Extensions

| __Extension__                     | __Presence__    | __Critical__ | __Description__ |
| ----                              | -               | -            | ----- |
| `authorityKeyIdentifier`          | RECOMMENDED     | N            | See [Section 7.1.2.1.3](#71213-root-ca-authority-key-identifier) |
| `basicConstraints`                | MUST            | Y            | See [Section 7.1.2.1.4](#71214-root-ca-basic-constraints) |
| `keyUsage`                        | MUST            | Y            | See [Section 7.1.2.10.7](#712107-ca-certificate-key-usage) |
| `subjectKeyIdentifier`            | MUST            | N            | See [Section 7.1.2.11.4](#712114-subject-key-identifier) |
| `extKeyUsage`                     | MUST NOT        | N            | - |
| `certificatePolicies`             | NOT RECOMMENDED | N            | See [Section 7.1.2.10.5](#712105-ca-certificate-certificate-policies) |
| Signed Certificate Timestamp List | MAY             | N            | See [Section 7.1.2.11.3](#712113-signed-certificate-timestamp-list) |
| Any other extension               | NOT RECOMMENDED | -            | See [Section 7.1.2.11.5](#712115-other-extensions) |

