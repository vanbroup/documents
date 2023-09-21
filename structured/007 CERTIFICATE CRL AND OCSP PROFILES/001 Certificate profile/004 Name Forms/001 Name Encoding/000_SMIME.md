#### 7.1.4.1 Name encoding

For every valid Certification Path (as defined by [RFC 5280, Section 6](https://datatracker.ietf.org/doc/html/rfc5280#section-6)):

* For each Certificate in the Certification Path, the encoded content of the Issuer Distinguished Name field of a Certificate SHALL be byte-for-byte identical with the encoded form of the Subject Distinguished Name field of the Issuing CA Certificate.
* For each CA Certificate in the Certification Path, the encoded content of the Subject Distinguished Name field of a Certificate SHALL be byte-for-byte identical among all Certificates whose Subject Distinguished Names can be compared as equal according to [RFC 5280, Section 7.1](https://datatracker.ietf.org/doc/html/rfc5280#section-7.1), and including expired and revoked Certificates.

