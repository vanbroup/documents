#### 7.1.4.2 Subject Attribute Encoding

This document defines requirements for the content and validation of a number of attributes that may appear within the `subject` field of a `tbsCertificate`. CAs SHALL NOT include these attributes unless their content has been validated as specified by, and only if permitted by, the relevant certificate profile specified within [Section 7.1.2](#712-certificate-content-and-extensions).

CAs that include attributes in the Certificate `subject` field that are listed in the table below SHALL encode those attributes in the relative order as they appear in the table and follow the specified encoding requirements for the attribute.

Table: Encoding and Order Requirements for Selected Attributes

| __Attribute__            | __OID__    | __Specification__                               | __Encoding Requirements__                  | __Max Length[^maxlength]__ |
| ----                     | --         | ---                                             | ----                                       | - |
| `domainComponent`        | `0.9.2342.19200300.100.1.25` | [RFC 4519](https://tools.ietf.org/html/rfc4519) | MUST use `IA5String`     | 63 |
| `countryName`            | `2.5.4.6`  | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `PrintableString`                 | 2 |
| `stateOrProvinceName`    | `2.5.4.8`  | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 128 |
| `localityName`           | `2.5.4.7`  | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 128 |
| `postalCode`             | `2.5.4.17` | X.520                                           | MUST use `UTF8String` or `PrintableString` | 40 |
| `streetAddress`          | `2.5.4.9`  | X.520                                           | MUST use `UTF8String` or `PrintableString` | 128 |
| `organizationName`       | `2.5.4.10` | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 64 |
| `surname`                | `2.5.4.4`  | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 64[^surname_givenname] |
| `givenName`              | `2.5.4.42` | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 64[^surname_givenname] |
| `organizationalUnitName` | `2.5.4.11` | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 64 |
| `commonName`             | `2.5.4.3`  | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 64 |

[^surname_givenname]: **Note**: Although RFC 5280 specifies the upper bound as 32,768 characters, this was a transcription error from X.520 (08/2005). The effective (interoperable) upper bound is 64 characters.

CAs that include attributes in the Certificate `subject` field that are listed in the table below SHALL follow the specified encoding requirements for the attribute.

Table: Encoding Requirements for Selected Attributes

| __Attribute__            | __OID__    | __Specification__                               | __Encoding Requirements__                  | __Max Length[^maxlength]__ |
| ----                     | --         | ---                                             | ----                                       | - |
| `businessCategory`       | `2.5.4.15` | X.520                                           | MUST use `UTF8String` or `PrintableString` | 128 |
| `jurisdictionCountry`    | `1.3.6.1.4.1.311.60.2.1.3` | Guidelines for the Issuance and Management of Extended Validation Certificates | MUST use `PrintableString` | 2 |
| `jurisdictionStateOrProvince`    | `1.3.6.1.4.1.311.60.2.1.2` | Guidelines for the Issuance and Management of Extended Validation Certificates | MUST use `UTF8String` or `PrintableString` | 128 |
| `jurisdictionLocality`    | `1.3.6.1.4.1.311.60.2.1.1` | Guidelines for the Issuance and Management of Extended Validation Certificates | MUST use `UTF8String` or `PrintableString` | 128 |
| `serialNumber`    | `2.5.4.5` | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `PrintableString` | 64 |
| `organizationIdentifier` | `2.5.4.97` | X.520 | MUST use `UTF8String` or `PrintableString` | None |

[^maxlength]: **Note**: ASN.1 length limits for DirectoryString are expressed as character limits, not byte limits.

