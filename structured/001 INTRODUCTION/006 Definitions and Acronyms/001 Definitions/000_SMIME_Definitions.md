### 1.6.1 Definitions

**Affiliate**: A corporation, partnership, joint venture or other entity controlling, controlled by, or under common control with another entity, or an agency, department, political subdivision, or any entity operating under the direct control of a Government Entity.

**Applicant**: The Natural Person or Legal Entity that applies for (or seeks renewal of) a Certificate. Once the Certificate issues, the Applicant is referred to as the Subscriber. For Certificates issued to devices, the Applicant is the entity that controls or operates the device named in the Certificate, even if the device is sending the actual Certificate Request.

**Applicant Representative**: A Natural Person or human sponsor who is either the Applicant, employed by the Applicant, or an authorized agent who has express authority to represent the Applicant:

  1. who signs and submits, or approves a Certificate Request on behalf of the Applicant; 
  2. who signs and submits a Subscriber Agreement on behalf of the Applicant; and/or
  3. who acknowledges the Terms of Use on behalf of the Applicant when the Applicant is an Affiliate of the CA or is the CA.

**Application Software Supplier**: A supplier of email client software or other relying-party application software such as mail user agents (web-based or application based) and email service providers that process S/MIME Certificates.

**Assumed Name**: Also known as "doing business as", "DBA", or "d/b/a" name in the US and "trading as" name in the UK.

**Attestation**: A letter attesting that Subject Information is correct written by an accountant, lawyer, government official, or other reliable third party customarily relied upon for such information.

**Audit Period**: In a period-of-time audit, the period between the first day (start) and the last day of operations (end) covered by the auditors in their engagement. (This is not the same as the period of time when the auditors are on-site at the CA.) The coverage rules and maximum length of audit periods are defined in [Section 8.1](#81-frequency-or-circumstances-of-assessment).

**Audit Report**: A report from a Qualified Auditor stating the Qualified Auditor's opinion on whether an entity's processes and controls comply with the mandatory provisions of these Requirements.

**CAA**: From [RFC 8659](http://tools.ietf.org/html/rfc8659): "The Certification Authority Authorization (CAA) DNS Resource Record allows a DNS domain name holder to specify one or more Certification Authorities (CAs) authorized to issue Certificates for that domain name. CAA Resource Records allow a public CA to implement additional controls to reduce the risk of unintended Certificate mis-issue."

**CA Key Pair**: A Key Pair where the Public Key appears as the Subject Public Key Info in one or more Root CA Certificate(s) and/or Subordinate CA Certificate(s).

**Certificate**: An electronic document that uses a digital signature to bind a Public Key and an identity.

**Certification Authority (or CA)**: An organization that is responsible for the creation, issuance, revocation, and management of Certificates. The term applies equally to both Root CAs and Subordinate CAs.

**Certificate Data**: Certificate requests and data related thereto (whether obtained from the Applicant or otherwise) in the CA's possession or control or to which the CA has access.

**Certificate Management Process**: Processes, practices, and procedures associated with the use of keys, software, and hardware, by which the CA verifies Certificate Data, issues Certificates, maintains a Repository, and revokes Certificates.

**Certificate Policy (or CP)**: A set of rules that indicates the applicability of a named Certificate to a particular community and/or PKI implementation with common security requirements.

**Certification Practice Statement (or CPS)**: One of several documents forming the governance framework in which Certificates are created, issued, managed, and used.

**Certificate Problem Report**: Complaint of suspected Key Compromise, Certificate misuse, or other types of fraud, compromise, misuse, or inappropriate conduct related to Certificates.

**Certificate Profile**: A set of documents or files that defines requirements for Certificate content and Certificate extensions in accordance with [Section 7](#7-certificate-crl-and-ocsp-profiles) e.g., a section in a CA’s CPS or a Certificate template file used by CA software.

**Certificate Revocation List**: A regularly updated time-stamped list of revoked Certificates that is created and digitally signed by the CA that issued the Certificates.

**Certificate Type**: The S/MIME Baseline Requirements define Certificate Profiles differentiated by the type of Subject, (for example Mailbox, Organization, Sponsored, Individual).

**Control**: "Control" (and its correlative meanings, "controlled by" and "under common control with") means possession, directly or indirectly, of the power to: (1) direct the management, personnel, finances, or plans of such entity; (2) control the election of a majority of the directors; or (3) vote that portion of voting shares required for "control" under the law of the entity's Jurisdiction of Incorporation or Registration but in no case less than 10%.

**Conversion**: The process of converting text from one writing system to ASCII characters.

**Country**: Either a member of the United Nations OR a geographic region recognized as a Sovereign State by at least two UN member nations.

**Cross Certificate**: A Certificate that is used to establish a trust relationship between two Root CAs.

**CSPRNG**: A pseudo-random number generator intended for use in a cryptographic system.

**Delegated Third Party**: A Natural Person or Legal Entity that is not the CA but is authorized by the CA, and whose activities are not within the scope of the appropriate CA audits, to assist in the Certificate Management Process by performing or fulfilling one or more of the CA requirements found herein.

**Digital Identity Document**: a government-issued identity document that is issued in a machine-processable form, that is digitally signed by the issuer, and that is in purely digital form.

**Domain Label**: From [RFC 8499](http://tools.ietf.org/html/rfc8499): "An ordered list of zero or more octets that makes up a portion of a domain name. Using graph theory, a label identifies one node in a portion of the graph of all possible domain names."

**Domain Name**: An ordered list of one or more Domain Labels assigned to a node in the Domain Name System.

**Electronic Identification (eID)**:  A credential containing Individual identification data and/or attributes and which is used for authentication for an online service. 

**Enterprise RA**: An employee or agent of an organization unaffiliated with the CA who authorizes issuance of Certificates to that organization.

**Expiry Date**: The "Not After" date in a Certificate that defines the end of a Certificate's validity period.

**Extant S/MIME CA**: A Subordinate CA that:

   1. Is a Publicly-Trusted Subordinate CA Certificate whose `notBefore` field is before September 1, 2023 and has issued end entity S/MIME Certificates;
   2. The CA Certificate includes no Extended Key Usage extension, contains `anyExtendedKeyUsage` in the EKU extension, or contains `id-kp-emailProtection` in the EKU extension; 
   3. The CA Certificate complies with the profile defined in [RFC 5280](http://tools.ietf.org/html/rfc5280). The following two deviations from the [RFC 5280](http://tools.ietf.org/html/rfc5280) profile are acceptable:
      a. The CA Certificate contains a `nameConstraints` extension that is not marked critical; 
      b. The CA Certificate contains a policy qualifier of type UserNotice which contains `explicitText` that uses an encoding that is not permitted by [RFC 5280](http://tools.ietf.org/html/rfc5280) (i.e., the `DisplayText` is encoded using BMPString or VisibleString); and
   4. The CA Certificate contains the `anyPolicy` identifier (2.5.29.32.0) or specific OIDs in the `certificatePolicies` extension that do not include those defined in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers) of these Requirements.

**Fully-Qualified Domain Name**: A Domain Name that includes the Domain Labels of all superior nodes in the Internet Domain Name System.

**Generation**: The S/MIME Baseline Requirements define several Generations of Certificate Profile for each Certificate Type.

**Government Entity**: A government-operated legal entity, agency, department, ministry, branch, or similar element of the government of a country, or political subdivision within such country (such as a state, province, city, county, etc.).

**Individual**: A Natural Person.

**Individual-Validated**: Refers to a Certificate Subject that includes only Individual (Natural Person) attributes, rather than attributes linked to an Organization. 

**Issuing CA**: In relation to a particular Certificate, the CA that issued the Certificate. This could be either a Root CA or a Subordinate CA.

**Jurisdiction of Incorporation**: The country and (where applicable) the state or province or locality where the organization's legal existence was established by a filing with (or an act of) an appropriate government agency or entity (e.g., where it was incorporated). In the context of a Government Entity, the country and (where applicable) the state or province where the Entity's legal existence was created by law.

**Key Compromise**: A Private Key is said to be compromised if its value has been disclosed to an unauthorized person, or an unauthorized person has had access to it.

**Key Generation Script**: A documented plan of procedures for the generation of a CA Key Pair.

**Key Pair**: The Private Key and its associated Public Key.

**Legacy Profile**: The S/MIME Legacy Generation profiles provide flexibility for existing reasonable S/MIME certificate practices to become auditable under the S/MIME Baseline Requirements. This includes options for Subject DN attributes, `extKeyUsage`, and other extensions. The Legacy Profiles will be deprecated in a future version of the S/MIME Baseline Requirements.

**Legal Entity**: An association, corporation, partnership, proprietorship, trust, government entity or other entity with legal standing in a country's legal system.

**Mailbox-Validated (MV)**: Refers to a Certificate Subject that is limited to (optional) `subject:emailAddress` and/or `subject:serialNumber` attributes.

**Mailbox Address**: Also Email Address. The format of a Mailbox Address is defined as a "Mailbox" as specified in Section 4.1.2 of [RFC 5321](http://tools.ietf.org/html/rfc5321) and amended by Section 3.2 of [RFC 6532](http://tools.ietf.org/html/rfc6532), with no additional padding or structure.

**Mailbox Field**: In Subscriber Certificates contains a Mailbox Address of the Subject via `rfc822Name` or `otherName` value of type `id-on-SmtpUTF8Mailbox` in the `subjectAltName` extension, or in Subordinate CA Certificates via `rfc822Name` in permittedSubtrees within the `nameConstraints` extension.

**Multipurpose Profile**: The S/MIME Multipurpose Generation profiles are aligned with the more defined Strict Profiles, but with additional options for `extKeyUsage` and other extensions. This is intended to allow flexibility for crossover use cases between document signing and secure email. 

**Natural Person**: An Individual; a human being as distinguished from a Legal Entity.

**Object Identifier**: A unique alphanumeric or numeric identifier registered under the International Organization for Standardization's applicable standard for a specific object or object class.

**OCSP Responder**: An online server operated under the authority of the CA and connected to its Repository for processing Certificate status requests. See also, Online Certificate Status Protocol.

**Online Certificate Status Protocol**: An online Certificate-checking protocol that enables relying-party application software to determine the status of an identified Certificate. See also OCSP Responder.

**Organization-Validated**: Refers to a Certificate Subject that includes only Organizational (Legal Entity) attributes, rather than attributes linked to an Individual.

**Parent Company**: A company that Controls a Subsidiary Company.

**Personal Name**: Personal Name is a name of an Individual Subject typically presented as `subject:givenName` and/or `subject:surname`. However, the Personal Name may be in a format preferred by the Subject, the CA, or Enterprise RA as long as it remains a meaningful representation of the Subject’s verified name.

**Physical Identity Document**: a government-issued identity document issued in physical and human-readable form (such as a passport or national identity card).

**Private Key**: The key of a Key Pair that is kept secret by the holder of the Key Pair, and that is used to create Digital Signatures and/or to decrypt electronic records or files that were encrypted with the corresponding Public Key.

**Pseudonym**: A fictitious identity that a person assumes for a particular purpose. Unlike an anonymous identity, a pseudonym can be linked to the person's real identity.

**Public Key**: The key of a Key Pair that can be publicly disclosed by the holder of the corresponding Private Key and that is used by a Relying Party to verify Digital Signatures created with the holder's corresponding Private Key and/or to encrypt messages so that they can be decrypted only with the holder's corresponding Private Key.

**Public Key Infrastructure**: A set of hardware, software, people, procedures, rules, policies, and obligations used to facilitate the trustworthy creation, issuance, management, and use of Certificates and keys based on Public Key Cryptography.

**Publicly-Trusted Certificate**: A Certificate that is trusted by virtue of the fact that its corresponding Root CA Certificate is distributed as a trust anchor in widely-available application software.

**Qualified Auditor**: A Natural Person or Legal Entity that meets the requirements of [Section 8.2](#82-identityqualifications-of-assessor).

**Random Value**: A value specified by a CA to the Applicant that exhibits at least 112 bits of entropy.

**Registered Domain Name**: A Domain Name that has been registered with a Domain Name Registrar.

**Registration Authority (RA)**: Any Legal Entity that is responsible for identification and authentication of subjects of Certificates, but is not a CA, and hence does not sign or issue Certificates. An RA MAY assist in the certificate application process or revocation process or both. When "RA" is used as an adjective to describe a role or function, it does not necessarily imply a separate body, but can be part of the CA.

**Reliable Data Source**: An identification document or source of data used to verify Subject Identity Information that is generally recognized among commercial enterprises and governments as reliable, and which was created by a third party for a purpose other than the Applicant obtaining a Certificate.

**Reliable Method of Communication**: A method of communication, such as a postal/courier delivery address, telephone number, or email address, that was verified using a source other than the Applicant Representative.

**Relying Party**: Any Natural Person or Legal Entity that relies on a Valid Certificate. An Application Software Supplier is not considered a Relying Party when software distributed by such Supplier merely displays information relating to a Certificate.

**Repository**: An online database containing publicly-disclosed PKI governance documents (such as Certificate Policies and Certification Practice Statements) and Certificate status information, either in the form of a CRL or an OCSP response.

**Requirements**: The S/MIME Baseline Requirements found in this document.

**Root CA**: The top level Certification Authority whose Root CA Certificate is distributed by Application Software Suppliers and that issues Subordinate CA Certificates.

**Root CA Certificate**: The self-signed Certificate issued by the Root CA to identify itself and to facilitate verification of Certificates issued to its Subordinate CAs.

**Sovereign State**: A state or country that administers its own government, and is not dependent upon, or subject to, another power.

**Sponsor-validated**: Refers to a Certificate Subject which combines Individual (Natural Person) attributes in conjunction with an `subject:organizationName` (an associated Legal Entity) attribute. Registration for Sponsor-validated Certificates MAY be performed by an Enterprise RA where the `subject:organizationName` is either that of the delegated enterprise, or an Affiliate of the delegated enterprise, or that the delegated enterprise is an agent of the named Subject Organization. 

**Strict Profile**: The S/MIME Strict Generation profiles are the long term target profile for S/MIME Certificates with `extKeyUsage` limited to `id-kp-emailProtection`, and stricter use of Subject DN attributes and other extensions.

**Subject**: The Natural Person, device, system, unit, or Legal Entity identified in a Certificate as the Subject. The Subject is either the Subscriber or a mailbox under the control and operation of the Subscriber.

**Subject Identity Information**: Information that identifies the Certificate Subject. Subject Identity Information does not include a Mailbox Address listed in the `subject:commonName` or `subject:emailAddress` fields, or in the `subjectAltName` extension.

**Subordinate CA**: A Certification Authority whose Certificate is signed by the Root CA, or another Subordinate CA.

**Subscriber**: A Natural Person or Legal Entity to whom a Certificate is issued and who is legally bound by a Subscriber Agreement or Terms of Use.

**Subscriber Agreement**: An agreement between the CA and the Applicant/Subscriber that specifies the rights and responsibilities of the parties.

**Subsidiary Company**: A company that is controlled by a Parent Company.

**Supplementary Evidence**: Used in addition to authoritative evidence to strengthen the reliability of the identity verification and/or as evidence for attributes that are not evidenced by the authoritative evidence.

**Technically Constrained Subordinate CA Certificate**: A Subordinate CA Certificate which uses a combination of Extended Key Usage settings and Name Constraint settings to limit the scope within which the Subordinate CA Certificate MAY issue Certificates to Subscriber or additional Subordinate CAs.

**Terms of Use**: Provisions regarding the safekeeping and acceptable uses of a Certificate issued in accordance with these Requirements when the Applicant/Subscriber is an Affiliate of the CA or is the CA.

**Valid Certificate**: A Certificate that passes the validation procedure specified in [RFC 5280](http://tools.ietf.org/html/rfc5280).

**Validation Specialist**: Someone who performs the information verification duties specified by these Requirements.

**Validity Period**: From [RFC 5280](http://tools.ietf.org/html/rfc5280): "The period of time from notBefore through notAfter, inclusive."

