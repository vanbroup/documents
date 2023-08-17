#### 7.1.2.2 Subordinate CA certificates

The issuance of end entity S/MIME Certificates by Extant S/MIME CAs is described in [Appendix B](#appendix-b---transition-of-extant-smime-cas).

a. `certificatePolicies` (SHALL be present)

   This extension SHOULD NOT be marked critical.

   All `policyIdentifier`s included in this extension SHALL be included in accordance with [Section 7.1.6.3](#7163-subordinate-ca-certificates).

   If the value of this extension includes a `PolicyInformation` which contains a qualifier of type `id-qt-cps` (OID: 1.3.6.1.5.5.7.2.1), then the value of the qualifier SHALL be a HTTP or HTTPS URL for the Issuing CA's CP and/or CPS, Relying Party Agreement, or other pointer to online policy information provided by the Issuing CA. If a qualifier of type `id-qt-unotice` (OID: 1.3.6.1.5.5.7.2.2) is included, then it SHALL contain `explicitText` and SHALL NOT contain `noticeRef`. 

b. `cRLDistributionPoints` (SHALL be present)

   This extension SHALL NOT be marked critical. It SHALL contain the HTTP URL of the CA's CRL service.

c. `authorityInformationAccess` (SHOULD be present)

   This extension SHALL NOT be marked critical.

   It SHOULD contain the HTTP URL of the Issuing CA Certificate (`accessMethod` = 1.3.6.1.5.5.7.48.2).
   It MAY contain the HTTP URL of the Issuing CA OCSP responder (`accessMethod` = 1.3.6.1.5.5.7.48.1).

d. `basicConstraints` (SHALL be present)

   This extension SHALL be marked critical. The `cA` field SHALL be set true. The `pathLenConstraint` field MAY be present.

e. `keyUsage` (SHALL be present)

   This extension SHALL be marked critical. Bit positions for `keyCertSign` and `cRLSign` SHALL be set. If the Subordinate CA Private Key is used for signing OCSP responses, then the `digitalSignature` bit SHALL be set.

f. `nameConstraints` (MAY be present)

   This extension SHOULD be marked critical[^*].

[^*]: Non-critical Name Constraints are an exception to [RFC 5280 (4.2.1.10)](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.10), however, they MAY be used until the `nameConstraints` extension is supported by Application Software Suppliers whose software is used by a substantial portion of Relying Parties worldwide.

g. `extKeyUsage` (MAY be present for Cross Certificates; SHALL be present otherwise)

   For Cross Certificates that share a Subject Distinguished Name and Subject Public Key with a Root CA Certificate operated in accordance with these Requirements, this extension MAY be present. If present, this extension SHOULD NOT be marked critical. This extension SHALL only contain usages for which the Issuing CA has verified the Cross Certificate is authorized to assert. This extension SHALL NOT contain the `anyExtendedKeyUsage` usage.

   For all other Subordinate CA Certificates, including Technically Constrained Subordinate CA Certificates, this extension SHALL be present and SHOULD NOT be marked critical[^**].

   For Subordinate CA Certificates that will be used to issue S/MIME Certificates, the value `id-kp-emailProtection` SHALL be present. The values `id-kp-serverAuth`, `id-kp-codeSigning`, `id-kp-timeStamping`, and `anyExtendedKeyUsage` SHALL NOT be present. Other values MAY be present.

[^**]: While [RFC 5280, Section 4.2.1.12](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12), notes that this extension will generally only appear within end-entity Certificates, these Requirements make use of this extension to further protect relying parties by limiting the scope of Subordinate Certificates, as implemented by a number of Application Software Suppliers.

h. `authorityKeyIdentifier` (SHALL be present)

   This extension SHALL NOT be marked critical. It SHALL contain a `keyIdentifier` field and it SHALL NOT contain a `authorityCertIssuer` or `authorityCertSerialNumber` field.

i. `subjectKeyIdentifier` (SHALL be present)

   This extension SHALL NOT be marked critical. It SHALL contain a value that is included in the `keyIdentifier` field of the `authorityKeyIdentifier` extension in Certificates issued by the Subordinate CA.

