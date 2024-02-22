##### 7.1.2.8.6 OCSP Responder id-pkix-ocsp-nocheck

The CA MUST include the `id-pkix-ocsp-nocheck` extension (OID: 1.3.6.1.5.5.7.48.1.5).

This extension MUST have an `extnValue` `OCTET STRING` which is exactly the hex-encoded bytes `0500`, the encoded representation of the ASN.1 NULL value, as specified in [RFC 6960, Section 4.2.2.2.1](https://tools.ietf.org/html/rfc6960#section-4.2.2.2.1).

