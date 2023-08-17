#### 7.1.2.2 Subordinate CA Certificate

a. `certificatePolicies`

   This extension MUST be present and SHOULD NOT be marked critical.

   `certificatePolicies:policyIdentifier` Required; see [Section 7.1.6.3](#7163-subordinate-ca-certificates) for requirements on Policy Identifiers.

   The following fields MUST be present if the Subordinate CA is not an Affiliate of the entity that controls the Root CA.

   * `certificatePolicies:policyQualifiers:policyQualifierId` (Optional)

     `id-qt 1` [RFC5280].

   * `certificatePolicies:policyQualifiers:qualifier:cPSuri` (Optional)

     HTTP URL for the Root CA's Certificate Policies, Certification Practice Statement, Relying Party agreement, or other pointer to online policy information provided by the CA.

b. `cRLDistributionPoints`

   This extension MUST be present and MUST NOT be marked critical. It MUST contain the HTTP URL of the CA's CRL service.

c. `authorityInformationAccess`

   This extension MUST be present. It MUST NOT be marked critical.

   It MUST contain the HTTP URL of the Issuing CA's certificate (`accessMethod` = 1.3.6.1.5.5.7.48.2).
   If the CA provides OCSP responses, it MUST contain the HTTP URL of the Issuing CA's OCSP responder (`accessMethod` = 1.3.6.1.5.5.7.48.1).

d. `basicConstraints`

   This extension MUST be present and MUST be marked critical. The `cA` field MUST be set true. The `pathLenConstraint` field MAY be present.

e. `keyUsage`

   This extension MUST be present and MUST be marked critical. Bit positions for `keyCertSign` and `cRLSign` MUST be set. If the Subordinate CA Private Key is used for signing OCSP responses, then the `digitalSignature` bit MUST be set.

g. `extKeyUsage`

This extension MUST be present and SHOULD NOT be marked critical.

If the Subordinate CA will be used to issue Code Signing Certificates:

* `id-kp-codeSigning` MUST be present.
* `id-kp-timeStamping` MUST NOT be present.

If the Subordinate CA will be used to issue Timestamp Certificates:

* `id-kp-timeStamping` MUST be present.
* `id-kp-codeSigning` MUST NOT be present.

Additionally, the following EKUs MUST NOT be present:

* `anyExtendedKeyUsage`
* `id-kp-serverAuth`
* `id-kp-emailProtection`

Other values SHOULD NOT be present. If any other value is present, the CA MUST have a business agreement with a Platform vendor requiring that EKU in order to issue a Platform-specific code signing certificate with that EKU.

h. `authorityKeyIdentifier`

   This extension MUST be present and MUST NOT be marked critical.

