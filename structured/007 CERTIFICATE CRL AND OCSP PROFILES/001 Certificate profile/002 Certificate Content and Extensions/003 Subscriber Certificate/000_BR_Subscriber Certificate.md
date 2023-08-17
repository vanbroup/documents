#### 7.1.2.3 Subscriber Certificate

a. `certificatePolicies`

   This extension MUST be present and SHOULD NOT be marked critical.

   * `certificatePolicies:policyIdentifier` (Required)

      A Policy Identifier, defined by the issuing CA, that indicates a Certificate Policy asserting the issuing CA's adherence to and compliance with these Requirements.

   The following extensions MAY be present:

   * `certificatePolicies:policyQualifiers:policyQualifierId` (Recommended)

      `id-qt 1` [RFC 5280].

   * `certificatePolicies:policyQualifiers:qualifier:cPSuri` (Optional)

      HTTP URL for the Subordinate CA's Certification Practice Statement, Relying Party Agreement or other pointer to online information provided by the CA.

b. `cRLDistributionPoints`

   This extension MAY be present. If present, it MUST NOT be marked critical, and it MUST contain the HTTP URL of the CA's CRL service.

c. `authorityInformationAccess`

   This extension MUST be present. It MUST NOT be marked critical, and it MUST contain the HTTP URL of the Issuing CA's OCSP responder (`accessMethod` = 1.3.6.1.5.5.7.48.1). It SHOULD also contain the HTTP URL of the Issuing CA's certificate (`accessMethod` = 1.3.6.1.5.5.7.48.2).

d. `basicConstraints` (optional)

   The `cA` field MUST NOT be true.

e. `keyUsage` (optional)

   If present, bit positions for `keyCertSign` and `cRLSign` MUST NOT be set.

f. `extKeyUsage` (required)

   Either the value `id-kp-serverAuth` [RFC5280] or `id-kp-clientAuth` [RFC5280] or both values MUST be present. `id-kp-emailProtection` [RFC5280] MAY be present. Other values SHOULD NOT be present. The value `anyExtendedKeyUsage` MUST NOT be present.

g. `authorityKeyIdentifier` (required)

   This extension MUST be present and MUST NOT be marked critical. It MUST contain a `keyIdentifier` field and it MUST NOT contain a `authorityCertIssuer` or `authorityCertSerialNumber` field.

