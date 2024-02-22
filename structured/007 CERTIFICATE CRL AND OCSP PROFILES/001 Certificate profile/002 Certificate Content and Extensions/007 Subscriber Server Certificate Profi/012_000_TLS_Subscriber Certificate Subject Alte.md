##### 7.1.2.7.12 Subscriber Certificate Subject Alternative Name

For Subscriber Certificates, the Subject Alternative Name MUST be present and MUST contain at least one `dNSName` or `iPAddress` `GeneralName`. See below for further requirements about the permitted fields and their validation requirements.

If the `subject` field of the certificate is an empty SEQUENCE, this extension MUST be marked critical, as specified in [RFC 5280, Section 4.2.1.6](https://tools.ietf.org/html/rfc5280#section-4.2.1.6). Otherwise, this extension MUST NOT be marked critical.

Table: `GeneralName` within a `subjectAltName` extension

| __Name Type__               | __Permitted__ | __Validation__ |
| ---                         | -             | ------         |
| `otherName`                 | N             | -              |
| `rfc822Name`                | N             | -              |
| `dNSName`                   | Y             | The entry MUST contain either a Fully-Qualified Domain Name or Wildcard Domain Name that the CA has validated in accordance with [Section 3.2.2.4](#3224-validation-of-domain-authorization-or-control). Wildcard Domain Names MUST be validated for consistency with [Section 3.2.2.6](#3226-wildcard-domain-validation). The entry MUST NOT contain an Internal Name. The Fully-Qualified Domain Name or the FQDN portion of the Wildcard Domain Name contained in the entry MUST be composed entirely of P-Labels or Non-Reserved LDH Labels joined together by a U+002E FULL STOP (".") character. The zero-length Domain Label representing the root zone of the Internet Domain Name System MUST NOT be included (e.g. "example.com" MUST be encoded as "example.com" and MUST NOT be encoded as "example.com."). |
| `x400Address`               | N             | -              |
| `directoryName`             | N             | -              |
| `ediPartyName`              | N             | -              |
| `uniformResourceIdentifier` | N             | -              |
| `iPAddress`                 | Y             | The entry MUST contain the IPv4 or IPv6 address that the CA has confirmed the Applicant controls or has been granted the right to use through a method specified in [Section 3.2.2.5](#3225-authentication-for-an-ip-address). The entry MUST NOT contain a Reserved IP Address. |
| `registeredID`              | N             | -              |

