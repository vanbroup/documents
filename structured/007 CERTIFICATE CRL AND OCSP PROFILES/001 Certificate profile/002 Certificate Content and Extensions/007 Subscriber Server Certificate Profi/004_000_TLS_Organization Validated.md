##### 7.1.2.7.4 Organization Validated

For a Subscriber Certificate to be Organization Validated, it MUST meet the following profile:

| __Field__             | __Requirements__     |
| --                    | -------              |
| `subject`             | See following table. |
| `certificatePolicies` | MUST be present. MUST assert the [Reserved Certificate Policy Identifier](#7161-reserved-certificate-policy-identifiers) of `2.23.140.1.2.2` as a `policyIdentifier`. See [Section 7.1.2.7.9](#71279-subscriber-certificate-certificate-policies). |
| All other extensions  | See [Section 7.1.2.7.6](#71276-subscriber-certificate-extensions) |

All `subject` names MUST be encoded as specified in [Section 7.1.4](#714-name-forms).

The following table details the acceptable `AttributeType`s that may appear within the `type` field of an `AttributeTypeAndValue`, as well as the contents permitted within the `value` field.

Table: Organization Validated `subject` Attributes

| __Attribute Name__             | __Presence__    | __Value__   | __Verification__ |
| ---                            | -               | ------      | --               |
| `domainComponent`       | MAY | If present, this field MUST contain a Domain Label from a Domain Name. The `domainComponent` fields for the Domain Name MUST be in a single ordered sequence containing all Domain Labels from the Domain Name. The Domain Labels MUST be encoded in the reverse order to the on-wire representation of domain names in the DNS protocol, so that the Domain Label closest to the root is encoded first. Multiple instances MAY be present. | [Section 3.2]
| `countryName`                  | MUST            | The two-letter ISO 3166-1 country code for the country associated with the Subject. If a Country is not represented by an official ISO 3166-1 country code, the CA MUST specify the ISO 3166-1 user-assigned code of `XX`, indicating that an official ISO 3166-1 alpha-2 code has not been assigned. | [Section 3.2.2.1](#3221-identity) |
| `stateOrProvinceName`          | MUST / MAY      | MUST be present if `localityName` is absent, MAY be present otherwise. If present, MUST contain the Subject's state or province information. | [Section 3.2.2.1](#3221-identity) |
| `localityName`                 | MUST / MAY      | MUST be present if `stateOrProvinceName` is absent, MAY be present otherwise. If present, MUST contain the Subject's locality information. | [Section 3.2.2.1](#3221-identity) |
| `postalCode`                   | NOT RECOMMENDED | If present, MUST contain the Subject's zip or postal information. | [Section 3.2.2.1](#3221-identity)) |
| `streetAddress`                | NOT RECOMMENDED | If present, MUST contain the Subject's street address information. Multiple instances MAY be present.| [Section 3.2.2.1](#3221-identity) |
| `organizationName`             | MUST            | The Subject's name or DBA. The CA MAY include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations; e.g. if the official record shows "Company Name Incorporated", the CA MAY use "Company Name Inc." or "Company Name". | [Section 3.2.2.2](#3222-dbatradename) |
| `surname`                      | MUST NOT        | -           | -           |
| `givenName`                    | MUST NOT        | -           | -           |
| `organizationalUnitName`       | MUST NOT        | -           | -           |
| `commonName`                   | NOT RECOMMENDED | If present, MUST contain a value derived from the `subjectAltName` extension according to [Section 7.1.4.3](#7143-subscriber-certificate-common-name-attribute). | |
| Any other attribute            | NOT RECOMMENDED | -           | See [Section 7.1.4.4](#7144-other-subject-attributes) |

In addition, `subject` Attributes MUST NOT contain only metadata such as '.', '-', and ' ' (i.e. space) characters, and/or any other indication that the value is absent, incomplete, or not applicable.

