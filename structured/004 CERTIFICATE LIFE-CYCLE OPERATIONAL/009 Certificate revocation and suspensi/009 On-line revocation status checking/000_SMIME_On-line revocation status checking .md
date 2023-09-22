### 4.9.9 On-line revocation/status checking availability

When provided, OCSP responses SHALL conform to [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960) and/or [RFC 5019](https://datatracker.ietf.org/doc/html/rfc5019). OCSP responses SHALL either:

1. Be signed by the CA that issued the Certificates whose revocation status is being checked, or
2. Be signed by an OCSP Responder whose Certificate is signed by the CA that issued the Certificate whose revocation status is being checked.
   
In the latter case, the OCSP signing Certificate SHALL contain the ocspSigning EKU (1.3.6.1.5.5.7.3.9) and an extension of type `id-pkix-ocsp-nocheck`, as defined by [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960).

