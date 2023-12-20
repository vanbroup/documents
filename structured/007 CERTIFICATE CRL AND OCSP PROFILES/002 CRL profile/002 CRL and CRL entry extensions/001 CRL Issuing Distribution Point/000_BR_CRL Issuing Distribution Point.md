#### 7.2.2.1 CRL Issuing Distribution Point

Partitioned CRLs MUST contain an Issuing Distribution Point extension. The `distributionPoint` field of the Issuing Distribution Point extension MUST be present. Additionally, the `fullName` field of the DistributionPointName value MUST be present, and its value MUST conform to the following requirements:

1. If a Certificate within the scope of the CRL contains a CRL Distribution Points extension, then at least one of the `uniformResourceIdentifiers` in the CRL Distribution Points's `fullName` field MUST be included in the `fullName` field of the CRL's Issuing Distribution Point extension. The encoding of the `uniformResourceIdentifier` value in the Issuing Distribution Point extension SHALL be byte-for-byte identical to the encoding used in the Certificate's CRL Distribution Points extension.
2. Other GeneralNames of type `uniformResourceIdentifier` MAY be included.
3. Non-`uniformResourceIdentifier` GeneralName types MUST NOT be included.

The `indirectCRL` and `onlyContainsAttributeCerts` fields MUST be set to `FALSE` (i.e., not asserted).

The CA MAY set either of the `onlyContainsUserCerts` and `onlyContainsCACerts` fields to `TRUE`, depending on the scope of the CRL. 

The CA MUST NOT assert both of the `onlyContainsUserCerts` and `onlyContainsCACerts` fields. 

The `onlySomeReasons` field SHOULD NOT be included; if included, then the CA MUST provide another CRL whose scope encompasses all revocations regardless of reason code. 

This extension is NOT RECOMMENDED for full and complete CRLs.

