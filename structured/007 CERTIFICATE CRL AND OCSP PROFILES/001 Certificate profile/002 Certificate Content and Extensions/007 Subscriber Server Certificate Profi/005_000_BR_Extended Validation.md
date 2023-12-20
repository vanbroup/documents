##### 7.1.2.7.5 Extended Validation

For a Subscriber Certificate to be Extended Validation, it MUST comply with the Certificate Profile specified in the then-current version of the Guidelines for the Issuance and Management of Extended Validation Certificates.
 In addition, it MUST meet the following profile:

| __Field__             | __Requirements__     |
| --                    | -------              |
| `subject`             | See Guidelines for the Issuance and Management of Extended Validation Certificates, Section 9.2. |
| `certificatePolicies` | MUST be present. MUST assert the [Reserved Certificate Policy Identifier](#7161-reserved-certificate-policy-identifiers) of `2.23.140.1.1` as a `policyIdentifier`. See [Section 7.1.2.7.9](#71279-subscriber-certificate-certificate-policies). |
| All other extensions  | See [Section 7.1.2.7.6](#71276-subscriber-certificate-extensions) and the Guidelines for the Issuance and Management of Extended Validation Certificates. |

In addition, `subject` Attributes MUST NOT contain only metadata such as '.', '-', and ' ' (i.e. space) characters, and/or any other indication that the value is absent, incomplete, or not applicable.

