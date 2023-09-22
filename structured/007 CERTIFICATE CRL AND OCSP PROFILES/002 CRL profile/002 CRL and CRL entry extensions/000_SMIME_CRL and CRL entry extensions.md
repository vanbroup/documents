### 7.2.2 CRL and CRL entry extensions

If present, the `reasonCode` (OID 2.5.29.21) extension SHALL NOT be marked critical.

If a CRL entry is for a Root CA or Subordinate CA Certificate, including Cross Certificates, this CRL entry extension SHALL be present. The `CRLreason` of certificateHold (6) SHALL NOT be used for Root CA or Subordinate CA Certificates.

If a CRL entry is for a Certificate not technically capable of causing issuance, this CRL entry extension SHOULD be present, but MAY be omitted, subject to the following requirements.

The `CRLReason` indicated SHALL NOT be unspecified (0). If the reason for revocation is unspecified, CAs SHALL omit the `reasonCode` entry extension. 

The Repository MAY include CRL entries that have a `CRLreason` of certificateHold (6) for Certificates that include the Certificate Policy identifiers for the Legacy or Multipurpose Generations. The Repository SHALL NOT include CRL entries that have a `CRLreason` of certificateHold (6) for Certificates that include the Certificate Policy identifiers for the Strict Generation.

If a `reasonCode` CRL entry extension is present, the `CRLReason` SHALL indicate the most appropriate reason for revocation of the Certificate, as defined by the CA within its CP/CPS.

