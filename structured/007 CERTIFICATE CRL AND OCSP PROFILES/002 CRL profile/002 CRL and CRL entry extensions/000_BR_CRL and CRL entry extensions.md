### 7.2.2 CRL and CRL entry extensions

1. `reasonCode` (OID 2.5.29.21)

   If present, this extension MUST NOT be marked critical.

   If a CRL entry is for a Root CA or Subordinate CA Certificate, including Cross Certificates, this CRL entry extension MUST be present.
   If a CRL entry is for a Certificate not technically capable of causing issuance, this CRL entry extension SHOULD be present, but MAY be omitted, subject to the following requirements.

   The `CRLReason` indicated MUST NOT be unspecified (0). If the reason for revocation is unspecified, CAs MUST omit `reasonCode` entry extension, if allowed by the previous requirements.
   If a CRL entry is for a Certificate not subject to these Requirements and was either issued on-or-after 2020-09-30 or has a `notBefore` on-or-after 2020-09-30, the `CRLReason` MUST NOT be certificateHold (6).
   If a CRL entry is for a Certificate subject to these Requirements, the `CRLReason` MUST NOT be certificateHold (6).

   If a `reasonCode` CRL entry extension is present, the `CRLReason` MUST indicate the most appropriate reason for revocation of the certificate, as defined by the CA within its CP/CPS.
   
2. `issuingDistributionPoint` (OID 2.5.29.28)

   Effective 2023-01-15, if a CRL does not contain entries for all revoked unexpired certificates issued by the CRL issuer, then it MUST contain a critical Issuing Distribution Point extension and MUST populate the `distributionPoint` field of that extension.

