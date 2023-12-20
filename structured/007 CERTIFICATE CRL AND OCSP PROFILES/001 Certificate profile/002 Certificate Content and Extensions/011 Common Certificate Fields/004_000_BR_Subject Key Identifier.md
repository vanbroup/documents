##### 7.1.2.11.4 Subject Key Identifier

If present, the `subjectKeyIdentifier` MUST be set as defined within [RFC 5280, Section 4.2.1.2](https://tools.ietf.org/html/rfc5280#section-4.2.1.2). The CA MUST generate a `subjectKeyIdentifier` that is unique within the scope of all Certificates it has issued for each unique public key (the `subjectPublicKeyInfo` field of the `tbsCertificate`). For example, CAs may generate the subject key identifier using an algorithm derived from the public key, or may generate a sufficiently-large unique number, such by using a CSPRNG.

