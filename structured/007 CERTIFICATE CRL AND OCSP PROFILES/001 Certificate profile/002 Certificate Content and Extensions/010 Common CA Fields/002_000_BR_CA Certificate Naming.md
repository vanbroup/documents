##### 7.1.2.10.2 CA Certificate Naming

All `subject` names MUST be encoded as specified in [Section 7.1.4](#714-name-forms).

The following table details the acceptable `AttributeType`s that may appear within the `type` field of an `AttributeTypeAndValue`, as well as the contents permitted within the `value` field.

| __Attribute Name__       | __Presence__    | __Value__ | __Verification__ |
| ---                      | -               | ------    | -- |
| `countryName`            | MUST            | The two-letter ISO 3166-1 country code for the country in which the CA's place of business is located. | [Section 3.2.2.3](#3223-verification-of-country) |
| `stateOrProvinceName`    | MAY             | If present, the CA's state or province information. | [Section 3.2.2.1](#3221-identity) |
| `localityName`           | MAY             | If present, the CA's locality. | [Section 3.2.2.1](#3221-identity) |
| `postalCode`             | MAY             | If present, the CA's zip or postal information. | [Section 3.2.2.1](#3221-identity) |
| `streetAddress`          | MAY             | If present, the CA's street address. Multiple instances MAY be present. | [Section 3.2.2.1](#3221-identity) |
| `organizationName`       | MUST            | The CA's name or DBA. The CA MAY include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations; e.g. if the official record shows "Company Name Incorporated", the CA MAY use "Company Name Inc." or "Company Name". | [Section 3.2.2.2](#3222-dbatradename) |
| `organizationalUnitName`  | This attribute MUST NOT be included in Root CA Certificates defined in [Section 7.1.2.1](#7121-root-ca-certificate-profile) or TLS Subordinate CA Certificates defined in [Section 7.1.2.5](#7125-technically-constrained-tls-subordinate-ca-certificate-profile) or Technically-Constrained TLS Subordinate CA Certificates defined in [Section 7.1.2.6](#7126-tls-subordinate-ca-certificate-profile). This attribute SHOULD NOT be included in other types of CA Certificates. | -           | -           |
| `commonName`             | MUST            | The contents SHOULD be an identifier for the certificate such that the certificate's Name is unique across all certificates issued by the issuing certificate. | |
| Any other attribute      | NOT RECOMMENDED | -           | See [Section 7.1.4.4](#7144-other-subject-attributes) |

