### 7.1.5 Name constraints

For a Subordinate CA Certificate to be considered Technically Constrained, the Certificate SHALL include an Extended Key Usage (EKU) extension specifying all extended key usages for which the Subordinate CA Certificate is authorized to issue Certificates. The `anyExtendedKeyUsage` KeyPurposeId SHALL NOT appear within this extension.

If the Subordinate CA Certificate includes the `id-kp-emailProtection` extended key usage, then for the Subordinate CA Certificate to be considered Technically Constrained it SHALL include the `nameConstraints` X.509v3 extension with constraints on `rfc822Name` and `directoryName` as follows:

   1. For each `rfc822Name` in `permittedSubtrees`, each `rfc822Name` SHALL contain either a FQDN or a U+002E FULL STOP (".") character followed by a FQDN. The `rfc822Name` SHALL NOT contain an email address. The CA SHALL confirm that the Applicant has registered the FQDN contained in the `rfc822Name` or has been authorized by the domain registrant to act on the registrant's behalf in line with the verification practices of [Section 3.2.2.3](#3223-validating-applicant-as-operator-of-associated-mail-servers).

   2. For each `directoryName` in `permittedSubtrees`, the CA SHALL confirm the Applicant's and/or Subsidiary's Organizational name and location such that end entity Certificates issued from the Subordinate CA Certificate will be in compliance with [Section 7.1.2.4](#7124-all-certificates).

