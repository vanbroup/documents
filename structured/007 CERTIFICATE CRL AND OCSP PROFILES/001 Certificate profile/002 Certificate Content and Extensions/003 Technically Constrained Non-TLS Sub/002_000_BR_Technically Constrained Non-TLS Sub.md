##### 7.1.2.3.2 Technically Constrained Non-TLS Subordinate CA Certificate Policies

If present, the Certificate Policies extension MUST be formatted as one of the two tables below:

Table: No Policy Restrictions (Affiliated CA)

| __Field__          | __Presence__    | __Contents__ |
| ---                | -               | ------       |
| `policyIdentifier` | MUST            | When the Issuing CA wishes to express that there are no policy restrictions, the Subordinate CA MUST be an Affiliate of the Issuing CA. The Certificate Policies extension MUST contain only a single `PolicyInformation` value, which MUST contain the `anyPolicy` Policy Identifier. |
|     `anyPolicy`    | MUST            | |
| `policyQualifiers` | NOT RECOMMENDED | If present, MUST contain only permitted `policyQualifiers` from the table below. |


Table: Policy Restricted

| __Field__                | __Presence__    | __Contents__ |
| ---                      | -               | ------       |
| `policyIdentifier`       | MUST            | One of the following policy identifiers: |
|     A [Reserved Certificate Policy Identifier](#7161-reserved-certificate-policy-identifiers) | MUST NOT | |
|     `anyPolicy`          | MUST NOT        | The `anyPolicy` Policy Identifier MUST NOT be present. |
|     Any other identifier | MAY             | If present, MUST be documented by the CA in its Certificate Policy and/or Certification Practice Statement. |
| `policyQualifiers`       | NOT RECOMMENDED | If present, MUST contain only permitted `policyQualifiers` from the table below. |


Table: Permitted `policyQualifiers`

| __Qualifier ID__                     | __Presence__ | __Field Type__ |  __Contents__ |
| ---                                  | -            | -              | -----         |
| `id-qt-cps` (OID: 1.3.6.1.5.5.7.2.1) | MAY          | `IA5String`    | The HTTP or HTTPS URL for the Issuing CA's Certificate Policies, Certification Practice Statement, Relying Party Agreement, or other pointer to online policy information provided by the Issuing CA. |
| Any other qualifier                  | MUST NOT     | -              | -             |


