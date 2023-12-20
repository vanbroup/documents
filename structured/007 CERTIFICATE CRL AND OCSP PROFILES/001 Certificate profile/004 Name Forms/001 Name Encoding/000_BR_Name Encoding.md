#### 7.1.4.1 Name Encoding

The following requirements apply to all Certificates listed in [Section 7.1.2](#712-certificate-content-and-extensions). Specifically, this includes Technically Constrained Non-TLS Subordinate CA Certificates, as defined in [Section 7.1.2.3](#7123-technically-constrained-non-tls-subordinate-ca-certificate-profile), but does not include certificates issued by such CA Certificates, as they are out of scope of these Baseline Requirements.

For every valid Certification Path (as defined by [RFC 5280, Section 6](https://tools.ietf.org/html/rfc5280#section-6)):

* For each Certificate in the Certification Path, the encoded content of the Issuer Distinguished Name field of a Certificate SHALL be byte-for-byte identical with the encoded form of the Subject Distinguished Name field of the Issuing CA certificate.
* For each CA Certificate in the Certification Path, the encoded content of the Subject Distinguished Name field of a Certificate SHALL be byte-for-byte identical among all Certificates whose Subject Distinguished Names can be compared as equal according to [RFC 5280, Section 7.1](https://tools.ietf.org/html/rfc5280#section-7.1), and including expired and revoked Certificates.

When encoding a `Name`, the CA SHALL ensure that:

  * Each `Name` MUST contain an `RDNSequence`.
  * Each `RelativeDistinguishedName` MUST contain exactly one `AttributeTypeAndValue`.
  * Each `RelativeDistinguishedName`, if present, is encoded within the `RDNSequence` in the order that it appears in [Section 7.1.4.2](#7142-subject-attribute-encoding).
    * For example, a `RelativeDistinguishedName` that contains a `countryName` `AttributeTypeAndValue` pair MUST be encoded within the `RDNSequence` before a `RelativeDistinguishedName` that contains a `stateOrProvinceName` `AttributeTypeAndValue`.
  * Each `Name` MUST NOT contain more than one instance of a given `AttributeTypeAndValue` across all `RelativeDistinguishedName`s unless explicitly allowed in these Requirements.

**Note**: [Section 7.1.2.2.2](#71222-cross-certified-subordinate-ca-naming) provides an exception to the above `Name` encoding requirements when issuing a [Cross-Certified Subordinate CA Certificate](#7122-cross-certified-subordinate-ca-certificate-profile), as described within that section.

