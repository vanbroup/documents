##### 7.1.2.7.9 Subscriber Certificate Certificate Policies

If present, the Certificate Policies extension MUST contain at least one `PolicyInformation`. Each `PolicyInformation` MUST match the following profile:

| __Field__                | __Presence__    | __Contents__ |
| ---                      | -               | ------       |
| `policyIdentifier`       | MUST            | One of the following policy identifiers: |
|     A [Reserved Certificate Policy Identifier](#7161-reserved-certificate-policy-identifiers) | MUST | The Reserved Certificate Policy Identifier (see [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers)) associated with the given Subscriber Certificate type (see [Section 7.1.2.7.1](#71271-subscriber-certificate-types)). |
|     `anyPolicy`          | MUST NOT        | The `anyPolicy` Policy Identifier MUST NOT be present. |
|     Any other identifier | MAY             | If present, MUST be defined and documented in the CA's Certificate Policy and/or Certification Practice Statement. |
| `policyQualifiers`       | NOT RECOMMENDED | If present, MUST contain only permitted `policyQualifiers` from the table below. |


This Profile RECOMMENDS that the first `PolicyInformation` value within the Certificate Policies extension contains the Reserved Certificate Policy Identifier (see [7.1.6.1](#7161-reserved-certificate-policy-identifiers))[^first_policy_note]. Regardless of the order of `PolicyInformation` values, the Certificate Policies extension MUST contain exactly one Reserved Certificate Policy Identifier.


Table: Permitted `policyQualifiers`

| __Qualifier ID__                     | __Presence__ | __Field Type__ |  __Contents__ |
| ---                                  | -            | -              | -----         |
| `id-qt-cps` (OID: 1.3.6.1.5.5.7.2.1) | MAY          | `IA5String`    | The HTTP or HTTPS URL for the Issuing CA's Certificate Policies, Certification Practice Statement, Relying Party Agreement, or other pointer to online policy information provided by the Issuing CA. |
| Any other qualifier                  | MUST NOT     | -              | -             |

[^first_policy_note]: Although RFC 5280 allows `PolicyInformation`s to appear in any order, several client implementations have implemented logic that considers the `policyIdentifier` that matches a given filter. As such, ensuring the Reserved Certificate Policy Identifier is the first `PolicyInformation` reduces the risk of interoperability challenges.

