## 7.3 OCSP profile

If an OCSP response is for a Root CA or Subordinate CA Certificate, including Cross Certificates, and that Certificate has been revoked, then the `revocationReason` field within the `RevokedInfo` of the `CertStatus` SHALL be present.

The `CRLReason` indicated SHALL contain a value permitted for CRLs, as specified in [Section 7.2.2](#722-crl-and-crl-entry-extensions).

