#### 7.1.2.3 Code signing and Timestamp Certificate

a. `certificatePolicies`

   This extension MUST be present and SHOULD NOT be marked critical.

   * `certificatePolicies:policyIdentifier` (Required)

      A Policy Identifier, defined by the issuing CA, that indicates a Certificate Policy asserting the issuing CA's adherence to and compliance with these Requirements.

   The following fields MAY be present:

   * `certificatePolicies:policyQualifiers:policyQualifierId` (Recommended)

      `id-qt 1` [RFC 5280].

   * `certificatePolicies:policyQualifiers:qualifier:cPSuri` (Optional)

      HTTP URL for the Subordinate CA's Certification Practice Statement, Relying Party agreement or other pointer to online information provided by the CA.


b. `cRLDistributionPoints`

   This extension MUST be present. It MUST NOT be marked critical, and it MUST contain the HTTP URL of the CA's CRL service.

c. `authorityInformationAccess`

   This extension MUST be present. It MUST NOT be marked critical.

   It MUST contain the HTTP URL of the Issuing CA's certificate (`accessMethod` = 1.3.6.1.5.5.7.48.2).
   If the CA provides OCSP responses, it MUST contain the HTTP URL of the Issuing CA's OCSP responder (`accessMethod` = 1.3.6.1.5.5.7.48.1).
    
d. `basicConstraints` (optional)

   The `cA` field MUST NOT be true.

e. `keyUsage`

   This extension MUST be present and MUST be marked critical.

   The bit position for `digitalSignature` MUST be set. Bit positions for `keyCertSign` and `cRLSign` MUST NOT be set. All other bit positions SHOULD NOT be set.

f. `extKeyUsage`

   If the Certificate is a Code Signing Certificate, then `id-kp-codeSigning` MUST be present and the following EKUs MAY be present:

   * Lifetime Signing OID (`1.3.6.1.4.1.311.10.3.13`)
   * `id-kp-emailProtection`
   * Document Signing (`1.3.6.1.4.1.311.3.10.3.12`)

   If the Certificate is a Timestamp Certificate, then `id-kp-timeStamping` MUST be present and MUST be marked critical.

   Additionally, the following EKUs MUST NOT be present:

   * `anyExtendedKeyUsage`
   * `id-kp-serverAuth`

   Other values SHOULD NOT be present. If any other value is present, the CA MUST have a business agreement with a Platform vendor requiring that EKU in order to issue a Platform-specific code signing certificate with that EKU.

g. `authorityKeyIdentifier`

   This extension MUST be present and MUST NOT be marked critical.

