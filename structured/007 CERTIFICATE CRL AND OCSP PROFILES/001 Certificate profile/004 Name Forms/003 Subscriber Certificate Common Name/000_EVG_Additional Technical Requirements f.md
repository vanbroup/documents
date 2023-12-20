#### 7.1.4.3 Additional Technical Requirements for EV Certificates

All provisions of the Baseline Requirements concerning Minimum Cryptographic Algorithms, Key Sizes, and Certificate Extensions apply to EV Certificates with the following exceptions:

1. If a Subordinate CA Certificates is issued to a Subordinate CA not controlled by the entity that controls the Root CA, the policy identifiers in the `certificatePolicies` extension MUST include the CA's Extended Validation policy identifier.

   Otherwise, it MAY contain the anyPolicy identifier.

2. The following fields MUST be present if the Subordinate CA is not controlled by the entity that controls the Root CA.

   * `certificatePolicies:policyQualifiers:policyQualifierId`

      `id-qt 1` [RFC 5280]

   * `certificatePolicies:policyQualifiers:qualifier:cPSuri`

      HTTP URL for the Root CA's Certification Practice Statement

3. The `certificatePolicies` extension in EV Certificates issued to Subscribers MUST include the following:

   * `certificatePolicies:policyIdentifier` (Required)

      The Issuer's EV policy identifier

   * `certificatePolicies:policyQualifiers:policyQualifierId` (Required)

      `id-qt 1` [RFC 5280]

   * `certificatePolicies:policyQualifiers:qualifier:cPSuri` (Required)

      HTTP URL for the Subordinate CA's Certification Practice Statement

4. The `cRLDistributionPoints` extension MUST be present in Subscriber Certificates if the certificate does not specify OCSP responder locations in an `authorityInformationAccess` extension.


