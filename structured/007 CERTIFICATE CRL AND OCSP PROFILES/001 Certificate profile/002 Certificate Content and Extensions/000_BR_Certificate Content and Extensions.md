### 7.1.2 Certificate Content and Extensions

If the CA asserts compliance with these Baseline Requirements, all certificates that it issues MUST comply with one of the following certificate profiles, which incorporate, and are derived from [RFC 5280](https://tools.ietf.org/html/rfc5280). Except as explicitly noted, all normative requirements imposed by RFC 5280 shall apply, in addition to the normative requirements imposed by this document. CAs SHOULD examine [RFC 5280, Appendix B](https://tools.ietf.org/html/rfc5280#appendix-B) for further issues to be aware of.

  * CA Certificates
    * [Section 7.1.2.1 - Root CA Certificate Profile](#7121-root-ca-certificate-profile)
    * Subordinate CA Certificates
      * Cross Certificates
        * [Section 7.1.2.2 - Cross-Certified Subordinate CA Certificate Profile](#7122-cross-certified-subordinate-ca-certificate-profile)
      * Technically Constrained CA Certificates
        * [Section 7.1.2.3 - Technically-Constrained Non-TLS Subordinate CA Certificate Profile](#7123-technically-constrained-non-tls-subordinate-ca-certificate-profile)
        * [Section 7.1.2.4 - Technically-Constrained Precertificate Signing CA Certificate Profile](#7124-technically-constrained-precertificate-signing-ca-certificate-profile)
        * [Section 7.1.2.5 - Technically-Constrained TLS Subordinate CA Certificate Profile](#7125-technically-constrained-tls-subordinate-ca-certificate-profile)
      * [Section 7.1.2.6 - TLS Subordinate CA Certificate Profile](#7126-tls-subordinate-ca-certificate-profile)
  * [Section 7.1.2.7 - Subscriber (End-Entity) Certificate Profile](#7127-subscriber-server-certificate-profile)
  * [Section 7.1.2.8 - OCSP Responder Certificate Profile](#7128-ocsp-responder-certificate-profile)
  * [Section 7.1.2.9 - Precertificate Profile](#7129-precertificate-profile)

