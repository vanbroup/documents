#### 7.1.2.3 Subscriber certificates

a. `certificatePolicies` (SHALL be present)

   This extension SHOULD NOT be marked critical. It SHALL include exactly one of the reserved `policyIdentifiers` listed in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers), and MAY contain one or more identifiers documented by the CA in its CP and/or CPS. 

   If the value of this extension includes a `PolicyInformation` which contains a qualifier of type `id-qt-cps` (OID: 1.3.6.1.5.5.7.2.1), then the value of the qualifier SHALL be a HTTP or HTTPS URL for the Issuing CA's CP and/or CPS, Relying Party Agreement, or other pointer to online policy information provided by the Issuing CA. If a qualifier of type `id-qt-unotice` (OID: 1.3.6.1.5.5.7.2.2) is included, then it SHALL contain `explicitText` and SHALL NOT contain `noticeRef`. 

b. `cRLDistributionPoints` (SHALL be present)

   This extension SHOULD NOT be marked critical. It SHALL contain at least one `distributionPoint` whose `fullName` value includes a GeneralName of type `uniformResourceIdentifier` that includes a URI where the Issuing CA's CRL can be retrieved.
   
   | Generation | Allowed URI scheme | 
   |------|-----------------------|
   | Strict and Multipurpose | Every `uniformResourceIdentifier` SHALL have the URI scheme HTTP. Other schemes SHALL NOT be present. |
   | Legacy | At least one `uniformResourceIdentifier` SHALL have the URI scheme HTTP. Other schemes (LDAP, FTP, ...) MAY be present. |

c. `authorityInformationAccess` (SHOULD be present)

   This extension SHALL NOT be marked critical.
   
   1. `id-ad-ocsp`
   
      The `authorityInformationAccess` extension MAY contain one or more `accessMethod` values of type `id-ad-ocsp` that specifies the URI of the Issuing CA's OCSP responder. 
   
      | Generation | Allowed URI scheme | 
      |------|-----------------------|
      | Strict and Multipurpose | When provided, every `accessMethod` SHALL have the URI scheme HTTP. Other schemes SHALL NOT be present. |
      | Legacy | When provided, at least one `accessMethod` SHALL have the URI scheme HTTP. Other schemes (LDAP, FTP, ...) MAY be present. | 
  
   1. `id-ad-caIssuers`
  
      The `authorityInformationAccess` extension SHOULD contain at least one `accessMethod` value of type `id-ad-caIssuers` that specifies the URI of the Issuing CA's Certificate. 
   
      | Generation | Allowed URI scheme | 
      |------|-----------------------|
      | Strict and Multipurpose | When provided, every `accessMethod` SHALL have the URI scheme HTTP. Other schemes SHALL NOT be present. |
      | Legacy | When provided, at least one `accessMethod` SHALL have the URI scheme HTTP. Other schemes (LDAP, FTP, ...) MAY be present. | 
   
d. `basicConstraints` (optional)

   This extension MAY be present. The `cA` field SHALL NOT be true. `pathLenConstraint` field SHALL NOT be present.

e. `keyUsage` (SHALL be present)

   This extension SHOULD be marked critical. 

   | Generation | `rsaEncryption`       | `id-ecPublicKey`            |`id-Ed25519` and `id-Ed448`            |
   |------|-----------------------|-----------------------------|-----------------------------|
   | Strict | For signing only, bit positions SHALL be set for `digitalSignature` and MAY be set for `nonRepudiation`.<br>For key management only, bit positions SHALL be set for `keyEncipherment`.<br>For dual use, bit positions SHALL be set for `digitalSignature` and `keyEncipherment` and MAY be set for `nonRepudiation`. |For signing only, bit positions SHALL be set for `digitalSignature` and MAY be set for `nonRepudiation`.<br>For key management only, bit positions SHALL be set for `keyAgreement` and MAY be set for `encipherOnly` or `decipherOnly`.<br>For dual use, bit positions SHALL be set for `digitalSignature` and `keyAgreement` and MAY be set for `nonRepudiation` and for `encipherOnly` or `decipherOnly` (only if `keyAgreement` is set).| Bit positions SHALL be set for `digitalSignature` and MAY be set for `nonRepudiation`. |
   | Multipurpose<br> and Legacy | For signing only, bit positions SHALL be set for `digitalSignature` and MAY be set for `nonRepudiation`.<br>For key management only, bit positions SHALL be set for `keyEncipherment` and MAY be set for `dataEncipherment`.<br>For dual use, bit positions SHALL be set for `digitalSignature` and `keyEncipherment` and MAY be set for `nonRepudiation` and `dataEncipherment`. |For signing only, bit positions SHALL be set for `digitalSignature` and MAY be set for `nonRepudiation`.<br>For key management only, bit positions SHALL be set for `keyAgreement` and MAY be set for `encipherOnly` or `decipherOnly`.<br>For dual use, bit positions SHALL be set for `digitalSignature` and `keyAgreement` and MAY be set for `nonRepudiation` and for `encipherOnly` or `decipherOnly` (only if `keyAgreement` is set).| Bit positions SHALL be set for `digitalSignature` and MAY be set for `nonRepudiation`. |

   Other bit positions SHALL NOT be set.

f. `extKeyUsage` (SHALL be present)

   | Generation | `KeyPurposeId`      | 
   |------|-----------------------|
   | Strict | `id-kp-emailProtection` SHALL be present. Other values SHALL NOT be present. |
  | Multipurpose and Legacy |`id-kp-emailProtection` SHALL be present. Other values MAY be present. |

   The values `id-kp-serverAuth`, `id-kp-codeSigning`, `id-kp-timeStamping`, and `anyExtendedKeyUsage` SHALL NOT be present.

g. `authorityKeyIdentifier` (SHALL be present)

   This extension SHALL NOT be marked critical. The `keyIdentifier` field SHALL be present. `authorityCertIssuer` and `authorityCertSerialNumber` fields SHALL NOT be present.

h. `subjectAlternativeName` (SHALL be present)

   This extension SHOULD NOT be marked critical unless the `subject` field is an empty sequence.

   The value of this extension SHALL be encoded as specified in [Section 7.1.4.2.1](#71421-subject-alternative-name-extension).

i. `smimeCapabilities` (optional)

   This extension MAY be present and SHALL NOT be marked critical. May indicate cryptographic capabilities of the sender of a signed S/MIME message, defined in [RFC 4262](https://datatracker.ietf.org/doc/html/rfc4262).

j. `subjectDirectoryAttributes` (optional)

   | Generation | `subjectDirectoryAttributes`      | 
   |------|-----------------------|
   | Strict and Multipurpose | Prohibited |
   | Legacy | MAY be present and SHALL NOT be marked critical. |

   This extension MAY be present. This extension is used to contain verified attributes which are not part of the Subject's Distinguished Name such as dateOfBirth, placeOfBirth, gender, countryOfCitizenship, or countryOfResidence in accordance with [RFC 3739 Section 3.2.2](https://tools.ietf.org/html/rfc3739#section-3.2.2). 

k. qcStatements (optional)

   This extension MAY be present and SHALL NOT be marked critical. Indicates a Certificate that is issued as Qualified within a defined legal framework from an identified country or set of countries in accordance with [RFC 3739 Section 3.2.6](https://tools.ietf.org/html/rfc3739#section-3.2.6) and/or ETSI EN 319 412-5, Section 4.

l. Legal Entity Identifier (optional)

   | Generation | LEI      | 
   |------|-----------------------|
   | `Mailbox-validated` | Prohibited |
   | `Organization-validated` | LEI (1.3.6.1.4.1.52266.1) MAY be present and SHALL NOT be marked critical.  Role (1.3.6.1.4.1.52266.2) SHALL NOT be present.|
   | `Sponsor-validated` | LEI (1.3.6.1.4.1.52266.1) or for role (1.3.6.1.4.1.52266.2) MAY be present and SHALL NOT be marked critical.  |
   | `Individual-validated` | Prohibited |

   The Legal Entity Identifier (LEI) is a 20-character, alpha-numeric code used in accordance with ISO 17442-1:2020, Clause 6 and ISO 17442-2:2020, Clause 4.

   The CA SHALL verify that the RegistrationStatus for the LEI record is ISSUED and the EntityStatus is ACTIVE. The CA SHALL only allow use of an LEI if the ValidationSources entry is FULLY_CORROBORATED. An LEI SHALL NOT be used if ValidationSources entry is PARTIALLY_CORROBORATED, PENDING, or ENTITY_SUPPLIED_ONLY.

   In cases where the "role" LEI is used, the CA SHALL verify that the LEI data reference is assigned to the Individual Subject whose identity has been verified in accordance with [Section 3.2.4](#324-authentication-of-individual-identity).

m. Adobe Extensions (optional)

   | Generation | Adobe Extensions      | 
   |------|-----------------------|
   | Strict | Prohibited |
   | Multipurpose and Legacy | MAY be present and SHALL NOT be marked critical. May include the Adobe Time-stamp X509 extension (1.2.840.113583.1.1.9.1) or the Adobe ArchiveRevInfo extension (1.2.840.113583.1.1.9.2) |

n. `subjectKeyIdentifier` (SHOULD be present)

   This extension SHALL NOT be marked critical. It SHOULD contain a value that is derived from the Public Key included in the Subscriber Certificate.

