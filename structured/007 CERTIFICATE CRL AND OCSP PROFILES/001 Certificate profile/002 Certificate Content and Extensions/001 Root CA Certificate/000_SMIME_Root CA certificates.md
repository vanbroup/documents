#### 7.1.2.1 Root CA certificates

a. `basicConstraints` (SHALL be present)

   This extension SHALL be marked critical. The `cA` field SHALL be set true. The `pathLenConstraint` field SHOULD NOT be present.

b. `keyUsage` (SHALL be present)

   This extension SHALL be marked critical. Bit positions for `keyCertSign` and `cRLSign` SHALL be set. If the Root CA Private Key is used for signing OCSP responses, then the `digitalSignature` bit SHALL be set.

c. `certificatePolicies` (SHOULD NOT be present)

   This extension SHOULD NOT be present.

d. `extKeyUsage` (SHALL NOT be present)

   This extension SHALL NOT be present.

e. `subjectKeyIdentifier` (SHALL be present)

   This extension SHALL NOT be marked critical. It SHALL contain a value that is included in the `keyIdentifier` field of the `authorityKeyIdentifier` extension in Certificates issued by the Root CA.

