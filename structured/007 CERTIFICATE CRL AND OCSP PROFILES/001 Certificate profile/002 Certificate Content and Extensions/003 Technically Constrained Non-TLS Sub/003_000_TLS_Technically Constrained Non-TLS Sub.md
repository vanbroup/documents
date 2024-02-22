##### 7.1.2.3.3 Technically Constrained Non-TLS Subordinate CA Extended Key Usage

The Issuing CA MUST verify that the Subordinate CA Certificate is authorized to issue certificates for each included extended key usage purpose. Multiple, independent key purposes (e.g. `id-kp-timeStamping` and `id-kp-codeSigning`) are NOT RECOMMENDED.

| __Key Purpose__                    | __OID__                 | __Presence__ |
| ----                               | ----                    | -            |
| `id-kp-serverAuth`                 | 1.3.6.1.5.5.7.3.1       | MUST NOT     |
| `id-kp-OCSPSigning`                | 1.3.6.1.5.5.7.3.9       | MUST NOT     |
| `anyExtendedKeyUsage`              | 2.5.29.37.0             | MUST NOT     |
| Precertificate Signing Certificate | 1.3.6.1.4.1.11129.2.4.4 | MUST NOT     |
| Any other value                    | -                       | MAY          |

