##### 7.1.2.9.3 Precertificate Poison

The Precertificate MUST contain the Precertificate Poison extension (OID: 1.3.6.1.4.1.11129.2.4.3).

This extension MUST have an `extnValue` `OCTET STRING` which is exactly the hex-encoded bytes `0500`, the encoded representation of the ASN.1 NULL value, as specified in [RFC 6962, Section 3.1](https://tools.ietf.org/doc/html/rfc6962#section-3.1).

