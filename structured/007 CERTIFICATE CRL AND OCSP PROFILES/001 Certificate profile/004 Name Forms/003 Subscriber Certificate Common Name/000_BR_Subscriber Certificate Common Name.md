#### 7.1.4.3 Subscriber Certificate Common Name Attribute

If present, this attribute MUST contain exactly one entry that is one of the values contained in the Certificate's `subjectAltName` extension (see [Section 7.1.2.7.12](#712712-subscriber-certificate-subject-alternative-name)). The value of the field MUST be encoded as follows:

  * If the value is an IPv4 address, then the value MUST be encoded as an IPv4Address as specified in RFC 3986, Section 3.2.2.
  * If the value is an IPv6 address, then the value MUST be encoded in the text representation specified in RFC 5952, Section 4.
  * If the value is a Fully-Qualified Domain Name or Wildcard Domain Name, then the value MUST be encoded as a character-for-character copy of the `dNSName` entry value from the `subjectAltName` extension. Specifically, all Domain Labels of the Fully-Qualified Domain Name or FQDN portion of the Wildcard Domain Name must be encoded as LDH Labels, and P-Labels MUST NOT be converted to their Unicode representation.

