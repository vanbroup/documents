##### 7.1.2.11.3 Signed Certificate Timestamp List

If present, the Signed Certificate Timestamp List extension contents MUST be an `OCTET STRING` containing the encoded `SignedCertificateTimestampList`, as specified in [RFC 6962, Section 3.3](https://tools.ietf.org/html/rfc6962#section-3.3).

Each `SignedCertificateTimestamp` included within the `SignedCertificateTimestampList` MUST be for a `PreCert` `LogEntryType` that corresponds to the current certificate.

