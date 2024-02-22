##### 7.1.2.7.3 Individual Validated

For a Subscriber Certificate to be Individual Validated, it MUST meet the following profile:

| __Field__             | __Requirements__     |
| --                    | -------              |
| `subject`             | See following table. |
| `certificatePolicies` | MUST be present. MUST assert the [Reserved Certificate Policy Identifier](#7161-reserved-certificate-policy-identifiers) of `2.23.140.1.2.3` as a `policyIdentifier`. See [Section 7.1.2.7.9](#71279-subscriber-certificate-certificate-policies). |
| All other extensions  | See [Section 7.1.2.7.6](#71276-subscriber-certificate-extensions) |

All `subject` names MUST be encoded as specified in [Section 7.1.4](#714-name-forms).

The following table details the acceptable `AttributeType`s that may appear within the `type` field of an `AttributeTypeAndValue`, as well as the contents permitted within the `value` field.

Table: Individual Validated `subject` Attributes

| __Attribute Name__             | __Presence__    | __Value__   | __Verification__ |
| ---                            | -               | ------      | --               |
| `countryName`                  | MUST            | The two-letter ISO 3166-1 country code for the country associated with the Subject. If a Country is not represented by an official ISO 3166-1 country code, the CA MUST specify the ISO 3166-1 user-assigned code of `XX`, indicating that an official ISO 3166-1 alpha-2 code has not been assigned. | [Section 3.2.3](#323-authentication-of-individual-identity) |
| `stateOrProvinceName`          | MUST / MAY      | MUST be present if `localityName` is absent, MAY be present otherwise. If present, MUST contain the Subject's state or province information. | [Section 3.2.3](#323-authentication-of-individual-identity) |
| `localityName`                 | MUST / MAY      | MUST be present if `stateOrProvinceName` is absent, MAY be present otherwise. If present, MUST contain the Subject's locality information. | [Section 3.2.3](#323-authentication-of-individual-identity) |
| `postalCode`                   | NOT RECOMMENDED | If present, MUST contain the Subject's zip or postal information. | [Section 3.2.3](#323-authentication-of-individual-identity) |
| `streetAddress`                | NOT RECOMMENDED | If present, MUST contain the Subject's street address information. Multiple instances MAY be present. | [Section 3.2.3](#323-authentication-of-individual-identity) |
| `organizationName`             | NOT RECOMMENDED | If present, MUST contain the Subject's name or DBA. | [Section 3.2.3](#323-authentication-of-individual-identity) |
| `surname`                      | MUST            | The Subject's surname. | [Section 3.2.3](#323-authentication-of-individual-identity) |
| `givenName`                    | MUST            | The Subject's given name. | [Section 3.2.3](#323-authentication-of-individual-identity) |
| `organizationalUnitName`       | MUST NOT        | -           | -           |
| `commonName`                   | NOT RECOMMENDED | If present, MUST contain a value derived from the `subjectAltName` extension according to [Section 7.1.4.3](#7143-subscriber-certificate-common-name-attribute). | |
| Any other attribute            | NOT RECOMMENDED | -           | See [Section 7.1.4.4](#7144-other-subject-attributes) |

In addition, `subject` Attributes MUST NOT contain only metadata such as '.', '-', and ' ' (i.e. space) characters, and/or any other indication that the value is absent, incomplete, or not applicable.

