##### 7.1.2.7.2 Domain Validated

For a Subscriber Certificate to be Domain Validated, it MUST meet the following profile:

| __Field__             | __Requirements__     |
| --                    | -------              |
| `subject`             | See following table. |
| `certificatePolicies` | MUST be present. MUST assert the [Reserved Certificate Policy Identifier](#7161-reserved-certificate-policy-identifiers) of `2.23.140.1.2.1` as a `policyIdentifier`. See [Section 7.1.2.7.9](#71279-subscriber-certificate-certificate-policies). |
| All other extensions  | See [Section 7.1.2.7.6](#71276-subscriber-certificate-extensions) |

All `subject` names MUST be encoded as specified in [Section 7.1.4](#714-name-forms).

The following table details the acceptable `AttributeType`s that may appear within the `type` field of an `AttributeTypeAndValue`, as well as the contents permitted within the `value` field.

Table: Domain Validated `subject` Attributes

| __Attribute Name__       | __Presence__    | __Value__   | __Verification__ |
| ---                      | -               | ------      | -- |
| `countryName`            | MAY             | The two-letter ISO 3166-1 country code for the country associated with the Subject. | [Section 3.2.2.3](#3223-verification-of-country) |
| `commonName`             | NOT RECOMMENDED | If present, MUST contain a value derived from the `subjectAltName` extension according to [Section 7.1.4.3](#7143-subscriber-certificate-common-name-attribute). | |
| Any other attribute      | MUST NOT        | -           | -                |

