##### 7.1.2.10.5 CA Certificate Certificate Policies

If present, the Certificate Policies extension MUST contain at least one `PolicyInformation`. Each `PolicyInformation` MUST match the following profile:


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
|     A [Reserved Certificate Policy Identifier](#7161-reserved-certificate-policy-identifiers) | MUST | The CA MUST include at least one Reserved Certificate Policy Identifier (see [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers)) associated with the given Subscriber Certificate type (see [Section 7.1.2.7.1](#71271-subscriber-certificate-types)) directly or transitively issued by this Certificate. |
|     `anyPolicy`          | MUST NOT        | The `anyPolicy` Policy Identifier MUST NOT be present. |
|     Any other identifier | MAY             | If present, MUST be defined by the CA and documented by the CA in its Certificate Policy and/or Certification Practice Statement. |
| `policyQualifiers`       | NOT RECOMMENDED | If present, MUST contain only permitted `policyQualifiers` from the table below. |


This Profile RECOMMENDS that the first `PolicyInformation` value within the Certificate Policies extension contains the Reserved Certificate Policy Identifier (see [7.1.6.1](#7161-reserved-certificate-policy-identifiers))[^first_policy_note]. Regardless of the order of `PolicyInformation` values, the Certificate Policies extension MUST contain exactly one Reserved Certificate Policy Identifier.


**Note**: policyQualifiers is NOT RECOMMENDED to be present in any Certificate issued under this Certificate Profile because this information increases the size of the Certificate without providing any value to a typical Relying Party, and the information may be obtained by other means when necessary.


If the `policyQualifiers` is permitted and present within a `PolicyInformation` field, it MUST be formatted as follows:


Table: Permitted `policyQualifiers`

| __Qualifier ID__                     | __Presence__ | __Field Type__ |  __Contents__ |
| ---                                  | -            | -              | -----         |
| `id-qt-cps` (OID: 1.3.6.1.5.5.7.2.1) | MAY          | `IA5String`    | The HTTP or HTTPS URL for the Issuing CA's Certificate Policies, Certification Practice Statement, Relying Party Agreement, or other pointer to online policy information provided by the Issuing CA. |
| Any other qualifier                  | MUST NOT     | -              | -             |

