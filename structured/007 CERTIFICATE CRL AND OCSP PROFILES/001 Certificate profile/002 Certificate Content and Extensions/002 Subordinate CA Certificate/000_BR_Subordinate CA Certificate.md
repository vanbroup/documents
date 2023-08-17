#### 7.1.2.2 Subordinate CA Certificate

a. `certificatePolicies`

   This extension MUST be present and SHOULD NOT be marked critical.

   `certificatePolicies:policyIdentifier` (Required)

   The following fields MAY be present if the Subordinate CA is not an Affiliate of the entity that controls the Root CA.

   * `certificatePolicies:policyQualifiers:policyQualifierId` (Optional)

     `id-qt 1` [RFC5280].

   * `certificatePolicies:policyQualifiers:qualifier:cPSuri` (Optional)

     HTTP URL for the Root CA's Certificate Policies, Certification Practice Statement, Relying Party Agreement, or other pointer to online policy information provided by the CA.

b. `cRLDistributionPoints`

   This extension MUST be present and MUST NOT be marked critical. It MUST contain the HTTP URL of the CA's CRL service.

c. `authorityInformationAccess`

   This extension SHOULD be present. It MUST NOT be marked critical.

   It SHOULD contain the HTTP URL of the Issuing CA's certificate (`accessMethod` = 1.3.6.1.5.5.7.48.2).
   It MAY contain the HTTP URL of the Issuing CA's OCSP responder (`accessMethod` = 1.3.6.1.5.5.7.48.1).

d. `basicConstraints`

   This extension MUST be present and MUST be marked critical. The `cA` field MUST be set true. The `pathLenConstraint` field MAY be present.

e. `keyUsage`

   This extension MUST be present and MUST be marked critical. Bit positions for `keyCertSign` and `cRLSign` MUST be set. If the Subordinate CA Private Key is used for signing OCSP responses, then the `digitalSignature` bit MUST be set.

f. `nameConstraints` (optional)

   If present, this extension SHOULD be marked critical[^*].

[^*]: Non-critical Name Constraints are an exception to RFC 5280 (4.2.1.10), however, they MAY be used until the Name Constraints extension is supported by Application Software Suppliers whose software is used by a substantial portion of Relying Parties worldwide.

g. `extKeyUsage` (optional/required)

   For Cross Certificates that share a Subject Distinguished Name and Subject Public Key with a Root Certificate operated in accordance with these Requirements, this extension MAY be present. If present, this extension SHOULD NOT be marked critical. This extension MUST only contain usages for which the issuing CA has verified the Cross Certificate is authorized to assert. This extension MAY contain the `anyExtendedKeyUsage` [RFC5280] usage, if the Root Certificate(s) associated with this Cross Certificate are operated by the same organization as the issuing Root Certificate.

   For all other Subordinate CA Certificates, including Technically Constrained Subordinate CA Certificates:

   This extension MUST be present and SHOULD NOT be marked critical[^**].

   For Subordinate CA Certificates that will be used to issue TLS certificates, the value `id-kp-serverAuth` [RFC5280] MUST be present. The value `id-kp-clientAuth` [RFC5280] MAY be present. The values `id-kp-emailProtection` [RFC5280], `id-kp-codeSigning` [RFC5280], `id-kp-timeStamping` [RFC5280], and `anyExtendedKeyUsage` [RFC5280] MUST NOT be present. Other values SHOULD NOT be present.

   For Subordinate CA Certificates that are not used to issue TLS certificates, then the value `id-kp-serverAuth` [RFC5280] MUST NOT be present. Other values MAY be present, but SHOULD NOT combine multiple independent key purposes (e.g. including `id-kp-timeStamping` [RFC5280] with `id-kp-codeSigning` [RFC5280]).

[^**]: While RFC 5280, Section 4.2.1.12, notes that this extension will generally only appear within end-entity certificates, these Requirements make use of this extension to further protect relying parties by limiting the scope of subordinate certificates, as implemented by a number of Application Software Suppliers.

h. `authorityKeyIdentifier` (required)

   This extension MUST be present and MUST NOT be marked critical. It MUST contain a `keyIdentifier` field and it MUST NOT contain a `authorityCertIssuer` or `authorityCertSerialNumber` field.

