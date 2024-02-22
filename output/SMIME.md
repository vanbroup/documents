---
title: Baseline Requirements for the Issuance and Management of Publicly-Trusted S/MIME Certificates
subtitle: Version 1.0.2
author:
  - CA/Browser Forum
date: December 8, 2023
copyright: |
  Copyright 2023 CA/Browser Forum
  This work is licensed under the Creative Commons Attribution 4.0 International license.
---

# 1. INTRODUCTION

## 1.1 Overview

This document describes an integrated set of technologies, protocols, identity-proofing, lifecycle management, and auditing requirements that are necessary (but not sufficient) for the issuance and management of Publicly-Trusted Certificates; Certificates that are trusted by virtue of the fact that their corresponding Root Certificate is distributed in widely-available application software. The requirements are not mandatory for Certification Authorities unless and until they become adopted and enforced by relying-party Application Software Suppliers.

**Notice to Readers**

The CP for the Issuance and Management of Publicly-Trusted Certificates describe a subset of the requirements that a Certification Authority must meet in order to issue Publicly Trusted Certificates. This document serves two purposes: to specify Baseline Requirements and to provide guidance and requirements for what a CA should include in its CPS. Except where explicitly stated otherwise, these Requirements apply only to relevant events that occur on or after 1 July 2012 (the original effective date of these requirements).

These Requirements do not address all of the issues relevant to the issuance and management of Publicly-Trusted Certificates. In accordance with RFC 3647 and to facilitate a comparison of other certificate policies and CPSs (e.g. for policy mapping), this document includes all sections of the RFC 3647 framework. However, rather than beginning with a "no stipulation" comment in all empty sections, the CA/Browser Forum is leaving such sections initially blank until a decision of "no stipulation" is made. The CA/Browser Forum may update these Requirements from time to time, in order to address both existing and emerging threats to online security. In particular, it is expected that a future version will contain more formal and comprehensive audit requirements for delegated functions.

These Requirements only address Certificates intended to be used for authenticating servers accessible through the Internet. Similar requirements for code signing, S/MIME, time-stamping, VoIP, IM, Web services, etc. may be covered in future versions.

These Requirements do not address the issuance, or management of Certificates by enterprises that operate their own Public Key Infrastructure for internal purposes only, and for which the Root Certificate is not distributed by any Application Software Supplier.

These Requirements are applicable to all Certification Authorities within a chain of trust. They are to be flowed down from the Root Certification Authority through successive Subordinate Certification Authorities.

## 1.1 Overview

This S/MIME Baseline Requirements document describes an integrated set of technologies, protocols, identity-proofing, lifecycle management, and auditing requirements that are necessary for the issuance and management of Publicly-Trusted S/MIME Certificates.

An S/MIME Certificate for the purposes of this document can be identified by the existence of an Extended Key Usage (EKU) for `id-kp-emailProtection` (OID: 1.3.6.1.5.5.7.3.4) and the inclusion of a `rfc822Name` or an `otherName` of type `id-on-SmtpUTF8Mailbox` in the `subjectAltName` extension.

**Notice for Readers**

An S/MIME Certificate contains a Public Key bound to a Mailbox Address and MAY also contain the identity of a Natural Person or Legal Entity that controls such email address. The Key Pair can then be used to sign, verify, encrypt, and decrypt email. 

This Certificate Policy (CP) describes a subset of the requirements that a CA SHALL meet in order to issue Publicly-Trusted S/MIME Certificates. This document serves two purposes: to specify Baseline Requirements and to provide guidance and requirements for what a Certification Authority (CA) should include in its Certification Practice Statement (CPS). These Requirements apply only to relevant events that occur on or after the relevant Effective Date described in [Section 1.2.1](#121-revisions) of these Requirements.

These Requirements do not address all of the issues relevant to the issuance and management of Publicly-Trusted S/MIME Certificates. To facilitate a comparison of other CP and/or CPS (e.g., for policy mapping), this document includes all sections of the [RFC 3647](https://datatracker.ietf.org/doc/html/rfc3647) framework. The CA/Browser Forum MAY update these Requirements from time to time.

These Requirements do not address the issuance or management of Certificates by enterprises that operate their own Public Key Infrastructure for internal purposes only, and for which the Root CA Certificate is not distributed by any Application Software Supplier. 

These Requirements are applicable to all CAs within a Publicly-Trusted chain of trust. They are to be flowed down from the Root CA through successive Subordinate CAs.

## 1.2 Document name and identification

This certificate policy (CP) contains the requirements for the issuance and management of publicly-trusted SSL certificates, as adopted by the CA/Browser Forum.

The following Certificate Policy identifiers are reserved for use by CAs to assert compliance with this document (OID arc 2.23.140.1.2) as follows:

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) domain-validated(1)} (2.23.140.1.2.1);` and

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) organization-validated(2)} (2.23.140.1.2.2);` and

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) individual-validated(3)} (2.23.140.1.2.3)`.

## 1.2 Document name and identification

This Certificate Policy contains the Baseline Requirements for the Issuance and Management of Publicly-Trusted S/MIME Certificates, as adopted by the CA/Browser Forum.

These Requirements describe four Certificate profiles differentiated by the type of Subject:

| Certificate Type | Description |
|------|-------------|
| Mailbox-validated | Subject is limited to (optional) `subject:emailAddress` and/or `subject:serialNumber` attributes. |
| Organization-validated | Includes only Organizational (Legal Entity) attributes in the Subject. |
| Sponsor-validated | Combines Individual (Natural Person) attributes in conjunction with an `subject:organizationName` (an associated Legal Entity) attribute. Registration for Sponsor-validated Certificates MAY be performed by an Enterprise RA.|
| Individual-validated | Includes only Individual (Natural Person) attributes in the Subject. |

In addition, Generations (known as Legacy, Multipurpose, and Strict) are specified for each of these Certificate Types, acknowledging both the current diversity of practice in issuing S/MIME Certificates as well as the desire to move towards more closely-defined practices over time.

The following Certificate Policy identifiers are reserved for use by CAs as a means of asserting compliance with this document (OID arc 2.23.140.1.5) as follows:

**Mailbox-validated**  
`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) mailbox-validated (1) legacy (1)}` (2.23.140.1.5.1.1); and  

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) mailbox-validated (1) multipurpose (2)}` (2.23.140.1.5.1.2); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) mailbox-validated (1) strict (3)}` (2.23.140.1.5.1.3); and 

**Organization-validated**  
`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) organization-validated (2) legacy (1)}` (2.23.140.1.5.2.1); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) organization-validated (2) multipurpose (2)}` (2.23.140.1.5.2.2); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) organization-validated (2) strict (3)}` (2.23.140.1.5.2.3); and 

**Sponsor-validated**  
`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) sponsor-validated (3) legacy (1)}` (2.23.140.1.5.3.1); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) sponsor-validated (3) multipurpose (2)}` (2.23.140.1.5.3.2); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) sponsor-validated (3) strict (3)}` (2.23.140.1.5.3.3); and 

**Individual-validated**  
`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) individual-validated (4) legacy (1)}` (2.23.140.1.5.4.1); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) individual-validated (4) multipurpose (2)}` (2.23.140.1.5.4.2); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) individual-validated (4) strict (3)}` (2.23.140.1.5.4.3). 

### 1.2.1 Revisions

| **Ver.** | **Ballot** | **Description** | **Adopted** | **Effective\*** |
|-|-|-----|--|--|
| 1.0.0 | 62 | Version 1.0 of the Baseline Requirements Adopted | 22-Nov-11 | 01-Jul-12 |
| 1.0.1 | 71 | Revised Auditor Qualifications | 08-May-12 | 01-Jan-13 |
| 1.0.2 | 75 | Non-critical Name Constraints allowed as exception to RFC 5280 | 08-Jun-12 | 08-Jun-12 |
| 1.0.3 | 78 | Revised Domain/IP Address Validation, High Risk Requests, and Data Sources | 22-Jun-12 | 22-Jun-12 |
| 1.0.4 | 80 | OCSP responses for non-issued certificates | 02-Aug-12 | 01-Feb-13 01-Aug-13 |
| -- | 83 | Network and Certificate System Security Requirements adopted | 03-Aug-13 | 01-Jan-13 |
| 1.0.5 | 88 | User-assigned country code of XX allowed | 12-Sep-12 | 12-Sep-12 |
| 1.1.0 | -- | Published as Version 1.1 with no changes from 1.0.5 | 14-Sep-12 | 14-Sep-12 |
| 1.1.1 | 93 | Reasons for Revocation and Public Key Parameter checking | 07-Nov-12 | 07-Nov-12 01-Jan-13 |
| 1.1.2 | 96 | Wildcard certificates and new gTLDs | 20-Feb-13 | 20-Feb-13 01-Sep-13 |
| 1.1.3 | 97 | Prevention of Unknown Certificate Contents | 21-Feb-13 | 21-Feb-13 |
| 1.1.4 | 99 | Add DSA Keys (BR v.1.1.4) | 3-May-2013 | 3-May-2013 |
| 1.1.5 | 102 | Revision to subject domainComponent language in Section 9.2.3 | 31-May-2013 | 31-May-2013 |
| 1.1.6 | 105 | Technical Constraints for Subordinate Certificate Authorities | 29-July-2013 | 29-July-2013 |
| 1.1.7 | 112 | Replace Definition of "Internal Server Name" with "Internal Name" | 3-April-2014 | 3-April-2014 |
| 1.1.8 | 120 | Affiliate Authority to Verify Domain | 5-June-2014 | 5-June-2014 |
| 1.1.9 | 129 | Clarification of PSL mentioned in Section 11.1.3 | 4-Aug-2014 | 4-Aug-2014 |
| 1.2.0 | 125 | CAA Records | 14-Oct-2014 | 15-Apr-2015 |
| 1.2.1 | 118 | SHA-1 Sunset | 16-Oct-2014 | 16-Jan-2015 1-Jan-2016 1-Jan-2017 |
| 1.2.2 | 134 | Application of RFC 5280 to Pre-certificates | 16-Oct-2014 | 16-Oct-2014 |
| 1.2.3 | 135 | ETSI Auditor Qualifications | 16-Oct-2014 | 16-Oct-2014 |
| 1.2.4 | 144 | Validation Rules for .onion Names | 18-Feb-2015 | 18-Feb-2015 |
| 1.2.5 | 148 | Issuer Field Correction | 2-April-2015 | 2-April-2015 |
| 1.3.0 | 146 | Convert Baseline Requirements to RFC 3647 Framework | 16-Apr-2015 | 16-Apr-2015 |
| 1.3.1 | 151 | Addition of Optional OIDs for Indicating Level of Validation | 28-Sep-2015 | 28-Sep-2015 |
| 1.3.2 | 156 | Amend Sections 1 and 2 of Baseline Requirements | 3-Dec-2015 | 3-Dec-2016 |
| 1.3.3 | 160 | Amend Section 4 of Baseline Requirements | 4-Feb-2016 | 4-Feb-2016 |
| 1.3.4 | 162 | Sunset of Exceptions | 15-Mar-2016 | 15-Mar-2016 |
| 1.3.5 | 168 | Baseline Requirements Corrections (Revised) | 10-May-2016 | 10-May-2016 |
| 1.3.6 | 171 | Updating ETSI Standards in CABF documents | 1-July-2016 | 1-July-2016 |
| 1.3.7 | 164 | Certificate Serial Number Entropy | 8-July-2016 | 30-Sep-2016 |
| 1.3.8 | 169 | Revised Validation Requirements | 5-Aug-2016 | 1-Mar-2017 |
| 1.3.9 | 174 | Reform of Requirements Relating to Conflicts with Local Law | 29-Aug-2016 | 27-Nov-2016 |
| 1.4.0 | 173 | Removal of requirement to cease use of public key due to incorrect info | 28-July-2016 | 11-Sept-2016 |
| 1.4.1 | 175 | Addition of givenName and surname | 7-Sept-2016 | 7-Sept-2016 |
| 1.4.2 | 181 | Removal of some validation methods listed in Section 3.2.2.4 | 7-Jan-2017 | 7-Jan-2017 |
| 1.4.3 | 187 | Make CAA Checking Mandatory | 8-Mar-2017 | 8-Sep-2017 |
| 1.4.4 | 193 | 825-day Certificate Lifetimes | 17-Mar-2017 | 1-Mar-2018 |
| 1.4.5 | 189 | Amend Section 6.1.7 of Baseline Requirements | 14-Apr-2017 | 14-May-2017 |
| 1.4.6 | 195 | CAA Fixup | 17-Apr-2017 | 18-May-2017 |
| 1.4.7 | 196 | Define “Audit Period” | 17-Apr-2017 | 18-May-2017 |
| 1.4.8 | 199 | Require commonName in Root and Intermediate Certificates | 9-May-2017 | 8-June-2017 |
| 1.4.9 | 204 | Forbid DTPs from doing Domain/IP Ownership | 11-July-2017 | 11-Aug-2017 |
| 1.5.0 | 212 | Canonicalise formal name of the Baseline Requirements | 1-Sept-2017 | 1-Oct-2017 |
| 1.5.1 | 197 | Effective Date of Ballot 193 Provisions | 1-May-2017 | 2-June-2017 |
| 1.5.2 | 190 | Add Validation Methods with Minor Corrections | 19-Sept-2017 | 19-Oct-2017 |
| 1.5.3 | 214 | CAA Discovery CNAME Errata | 27-Sept-2017 | 27-Oct-2017 |
| 1.5.4 | 215 | Fix Ballot 190 Errata | 4‐Oct‐2017 | 5‐Nov‐2017 |
| 1.5.5 | 217 | Sunset RFC 2527 | 21‐Dec‐2017 | 9‐Mar‐2018 |
| 1.5.6 | 218 | Remove validation methods #1 and #5 | 5‐Feb‐2018 | 9‐Mar‐2018 |
| 1.5.7 | 220 | Minor Cleanups (Spring 2018) | 30‐Mar‐2018 | 29‐Apr‐2018 |
| 1.5.8 | 219 | Clarify handling of CAA Record Sets with no "issue"/"issuewild" property tag | 10-Apr-2018 | 10-May-2018 |
| 1.5.9 | 223 | Update BR Section 8.4 for CA audit criteria | 15-May-2018 | 14-June-2018 |
| 1.6.0 | 224 | WhoIs and RDAP | 22-May-2018 | 22-June-2018 |
| 1.6.1 | SC6 | Revocation Timeline Extension | 14-Sep-2018 | 14-Oct-2018 |
| 1.6.2 | SC12 | Sunset of Underscores in dNSNames | 9-Nov-2018 | 10-Dec-2018 |
| 1.6.3 | SC13 | CAA Contact Property and Associated E-mail Validation Methods | 25-Dec-2018 | 1-Feb-2019 |
| 1.6.4 | SC14 | Updated Phone Validation Methods | 31-Jan-2019 | 16-Mar-2019 |
| 1.6.4 | SC15 | Remove Validation Method Number 9 | 5-Feb-2019 | 16-Mar-2019 |
| 1.6.4 | SC7 | Update IP Address Validation Methods | 8-Feb-2019 | 16-Mar-2019 |
| 1.6.5 | SC16 | Other Subject Attributes | 15-Mar-2019 | 16-Apr-2019 |
| 1.6.6 | SC19 | Phone Contact with DNS CAA Phone Contact v2 | 20-May-2019 | 9-Sep-2019 |
| 1.6.7 | SC23 | Precertificates | 14-Nov-2019 | 19-Dec-2019 |
| 1.6.7 | SC24 | Fall Cleanup v2 | 12-Nov-2019 | 19-Dec-2019 |
| 1.6.8 | SC25 | Define New HTTP Domain Validation Methods v2 | 31-Jan-2020 | 3-Mar-2020 |
| 1.6.9 | SC27 | Version 3 Onion Certificates | 19-Feb-2020 | 27-Mar-2020 |
| 1.7.0 | SC29 | Pandoc-Friendly Markdown Formatting Changes | 20-Mar-2020 | 4-May-2020 |
| 1.7.1 | SC30 | Disclosure of Registration / Incorporating Agency | 13-Jul-2020 | 20-Aug-2020 |
| 1.7.1 | SC31 | Browser Alignment | 16-Jul-2020 | 20-Aug-2020 |
| 1.7.2 | SC33 | TLS Using ALPN Method | 14-Aug-2020 | 22-Sept-2020 |
| 1.7.3 | SC28 | Logging and Log Retention | 10-Sep-2020 | 19-Oct-2020 |
| 1.7.3 | SC35 | Cleanups and Clarifications | 9-Sep-2020 | 19-Oct-2020 |
| 1.7.4 | SC41 | Reformat the BRs, EVGs, and NCSSRs | 24-Feb-2021 | 5-Apr-2021 |
| 1.7.5 | SC42 | 398-day Re-use Period | 22-Apr-2021 | 2-Jun-2021 |
| 1.7.6 | SC44 | Clarify Acceptable Status Codes | 30-Apr-2021 | 3-Jun-2021 |
| 1.7.7 | SC46 | Sunset the CAA Exception for DNS Operator | 2-Jun-2021 | 12-Jul-2021 |
| 1.7.8 | SC45 | Wildcard Domain Validation | 2-Jun-2021 | 13-Jul-2021 |
| 1.7.9 | SC47 | Sunset subject:organizationalUnitName | 30-Jun-2021 | 16-Aug-2021 |
| 1.8.0 | SC48 | Domain Name and IP Address Encoding | 22-Jul-2021 | 25-Aug-2021 |
| 1.8.1 | SC50 | Remove the requirements of 4.1.1 | 22-Nov-2021 | 23-Dec-2021 |
| 1.8.2 | SC53 | Sunset for SHA-1 OCSP Signing | 26-Jan-2022 | 4-Mar-2022 |
| 1.8.3 | SC51 | Reduce and Clarify Log and Records Archival Retention Requirements | 01-Mar-2022 | 15-Apr-2022 |
| 1.8.4 | SC54 | Onion Cleanup | 24-Mar-2022 | 23-Apr-2022 |
| 1.8.5 | SC56 | 2022 Cleanup | 25-Oct-2022 | 30-Nov-2022 |
| 1.8.6 | SC58 | Require distributionPoint in sharded CRLs | 7-Nov-2022 |	11-Dec-2022 |
| 1.8.7 | SC61  | New CRL entries must have a Revocation Reason Code | 1-Apr-2023 | 15-Jul-2023 |
| 2.0.0 | SC62  | Certificate Profiles Update | 22-Apr-2023 | 15-Sep-2023 |
| 2.0.1 | SC63  | Make OCSP optional, require CRLs, and incentivize automation | 17-Aug-2023 | 15-Mar-2024 |



\* Effective Date and Additionally Relevant Compliance Date(s)

### 1.2.1 Revisions

|Version| Ballot|Description                       | Publication Date\*  |
|------|-------|----------------------------------|-----------|
| 1.0.0   | SMC01    |Version 1.0 of the S/MIME Baseline Requirements adopted | January 01, 2023 |
| 1.0.1   | SMC03    |Clarification and corrections | August 11, 2023 |
| 1.0.2   | SMC04    |Addition of ETSI TS 119 411-6 | December 8, 2023 |

\* Publication Date is the date the new version was published following the Intellectual Property Review.

|Version| Ballot|Description                       | Additional<br> Compliance Date |
|------|-------|--------------------------------------|-----------|
|1.0.0 |SMC01 | Initial implementation date | September 01, 2023|
|1.0.1 |SMC03 | Transition end for Extant S/MIME CAs | September 15, 2024|
  
### 1.2.2 Relevant Dates

| **Compliance** | **Section(s)** | **Summary Description (See Full Text for Details)** |
|--|--|----------|
| 2013-01-01 | 6.1.6 | For RSA public keys, CAs SHALL confirm that the value of the public exponent is an odd number equal to 3 or more. |
| 2013-01-01 | 4.9.10 | CAs SHALL support an OCSP capability using the GET method. |
| 2013-01-01 | 5 | CAs SHALL comply with the Network and Certificate System Security Requirements. |
| 2013-08-01 | 4.9.10 | OCSP Responders SHALL NOT respond "Good" for Unissued Certificates. |
| 2013-09-01 | 3.2.2.6 | CAs SHALL revoke any certificate where wildcard character occurs in the first label position immediately to the left of a "registry-controlled" label or "public suffix". |
| 2013-12-31 | 6.1.5 | CAs SHALL confirm that the RSA Public Key is at least 2048 bits or that one of the following ECC curves is used: P-256, P-384, or P-521. A Root CA Certificate issued prior to 31 Dec. 2010 with an RSA key size less than 2048 bits MAY still serve as a trust anchor. |
| 2015-01-16 | 7.1.3 | CAs SHOULD NOT issue Subscriber Certificates utilizing the SHA-1 algorithm with an Expiry Date greater than 1 January 2017. |
| 2015-04-01 | 6.3.2 | CAs SHALL NOT issue certificates with validity periods longer than 39 months, except under certain circumstances. |
| 2015-04-15 | 2.2 | A CA's CPS must state whether it reviews CAA Records, and if so, its policy or practice on processing CAA records for Fully-Qualified Domain Names. |
| 2015-11-01 | 7.1.4.2.1 | Issuance of Certificates with Reserved IP Address or Internal Name prohibited. |
| 2016-01-01 | 7.1.3 | CAs MUST NOT issue any new Subscriber certificates or Subordinate CA certificates using the SHA-1 hash algorithm. |
| 2016-06-30 | 6.1.7 | CAs MUST NOT issue Subscriber Certificates directly from Root CAs. |
| 2016-06-30 | 6.3.2 | CAs MUST NOT issue Subscriber Certificates with validity periods longer than 39 months, regardless of circumstance. |
| 2016‐09‐30 | 7.1 | CAs SHALL generate Certificate serial numbers greater than zero (0) containing at least 64 bits of output from a CSPRNG |
| 2016-10-01 | 7.1.4.2.1 | All Certificates with Reserved IP Address or Internal Name must be revoked. |
| 2016-12-03 | 1 and 2 | Ballot 156 amendments to sections 1.5.2, 2.3, and 2.4 are applicable |
| 2017-01-01 | 7.1.3 | CAs MUST NOT issue OCSP responder certificates using SHA-1 (inferred). |
| 2017-03-01 | 3.2.2.4 | CAs MUST follow revised validation requirements in Section 3.2.2.4. |
| 2017-09-08 | 3.2.2.8 | CAs MUST check and process CAA records |
| 2018-03-01 | 4.2.1 and 6.3.2 | Certificates issued MUST have a Validity Period no greater than 825 days and re-use of validation information limited to 825 days |
| 2018-05-31 | 2.2 | CP and CPS must follow RFC 3647 format |
| 2018-08-01 | 3.2.2.4.1 and .5 | CAs must stop using domain validation methods BR 3.2.2.4.1 and 3.2.2.4.5, stop reusing validation data from those methods |
| 2019-01-15 | 7.1.4.2.1 | All certificates containing an underscore character in any dNSName entry and having a validity period of more than 30 days MUST be revoked prior to January 15, 2019 |
| 2019-05-01 | 7.1.4.2.1 | underscore characters (“_”) MUST NOT be present in dNSName entries |
| 2019-06-01 | 3.2.2.4.3 | CAs SHALL NOT perform validations using this method after May 31, 2019. Completed validations using this method SHALL continue to be valid for subsequent issuance per the applicable certificate data reuse periods.
| 2019-08-01 | 3.2.2.5 | CAs SHALL maintain a record of which IP validation method, including the relevant BR version number, was used to validate every IP Address |
| 2019-08-01 | 3.2.2.5.4 | CAs SHALL NOT perform validations using this method after July 31, 2019. Completed validations using this method SHALL NOT be re-used for certificate issuance after July 31, 2019. Any certificate issued prior to August 1, 2019 containing an IP Address that was validated using any method that was permitted under the prior version of this Section 3.2.2.5 MAY continue to be used without revalidation until such certificate naturally expires |
| 2020-06-03 | 3.2.2.4.6 | CAs MUST NOT perform validation using this method after 3 months from the IPR review date of Ballot SC25 |
| 2020-08-01 | 8.6 | Audit Reports for periods on-or-after 2020-08-01 MUST be structured as defined. |
| 2020-09-01 | 6.3.2 | Certificates issued SHOULD NOT have a Validity Period greater than 397 days and MUST NOT have a Validity Period greater than 398 days. |
| 2020-09-30 | 4.9.10 | OCSP responses MUST conform to the validity period requirements specified. |
| 2020-09-30 | 7.1.4.1 | Subject and Issuer Names for all possible certification paths MUST be byte-for-byte identical. |
| 2020-09-30 | 7.1.6.4 | Subscriber Certificates MUST include a CA/Browser Forum Reserved Policy Identifier in the Certificate Policies extension. |
| 2020-09-30 | 7.2 and 7.3 | All OCSP and CRL responses for Subordinate CA Certificates MUST include a meaningful reason code. |
| 2021-07-01 | 3.2.2.8 | CAA checking is no longer optional if the CA is the DNS Operator or an Affiliate. |
| 2021-07-01 | 3.2.2.4.18 and 3.2.2.4.19 | Redirects MUST be the result of one of the HTTP status code responses defined.  |
| 2021-10-01 | 7.1.4.2.1 | Fully-Qualified Domain Names MUST consist solely of P-Labels and Non-Reserved LDH Labels. |
| 2021-12-01 | 3.2.2.4 | CAs MUST NOT use methods 3.2.2.4.6, 3.2.2.4.18, or 3.2.2.4.19 to issue wildcard certificates or with Authorization Domain Names other than the FQDN. |
| 2022-06-01 | 7.1.3.2.1 | CAs MUST NOT sign OCSP responses using the SHA-1 hash algorithm. |
| 2022-09-01 | 7.1.4.2.2 | CAs MUST NOT include the organizationalUnitName field in the Subject |
| 2023-01-15 | 7.2.2 | Sharded or partitioned CRLs MUST have a distributionPoint |
| 2023-07-15 | 4.9.1.1 and 7.2.2 | New CRL entries MUST have a revocation reason code |
| 2023-09-15 | Section 7 (and others) | CAs MUST use the updated Certificate Profiles passed in Version 2.0.0 |
| 2024-03-15 | 4.9.7 | CAs MUST generate and publish CRLs. |

## 1.3 PKI Participants

The CA/Browser Forum is a voluntary organization of Certification Authorities and suppliers of Internet browser and other relying-party software applications.

## 1.3 PKI participants

The CA/Browser Forum is a voluntary organization of Certification Authorities and Application Software Suppliers including providers of Internet browser and other relying-party software applications, such as mail user agents (web-based or application-based) and email service providers that process S/MIME Certificates.

I do also participate :-)
::: layer-800
The layers 800 to 899 are reserved for Auditors and Assessors.

:::

::: layer-900
CA's can use the layers 900 to 999 to write control statements or additional information to automatically construct their CP/CPS.
:::

### 1.3.1 Certification Authorities

Certification Authority (CA) is defined in [Section 1.6](#16-definitions-and-acronyms). Current CA Members of the CA/Browser Forum are listed here: <https://cabforum.org/members>.

### 1.3.1 Certification authorities

Certification Authority (CA) is defined in [Section 1.6.1](#161-definitions). Current CA Members of the CA/Browser Forum are listed at https://cabforum.org/members.

### 1.3.2 Registration Authorities

With the exception of [Section 3.2.2.4](#3224-validation-of-domain-authorization-or-control) and [Section 3.2.2.5](#3225-authentication-for-an-ip-address), the CA MAY delegate the performance of all, or any part, of [Section 3.2](#32-initial-identity-validation) requirements to a Delegated Third Party, provided that the process as a whole fulfills all of the requirements of [Section 3.2](#32-initial-identity-validation).

Before the CA authorizes a Delegated Third Party to perform a delegated function, the CA SHALL contractually require the Delegated Third Party to:

1. Meet the qualification requirements of [Section 5.3.1](#531-qualifications-experience-and-clearance-requirements), when applicable to the delegated function;
2. Retain documentation in accordance with [Section 5.5.2](#552-retention-period-for-archive);
3. Abide by the other provisions of these Requirements that are applicable to the delegated function; and
4. Comply with
   a. the CA's Certificate Policy/Certification Practice Statement or
   b. the Delegated Third Party's practice statement that the CA has verified complies with these Requirements.

The CA MAY designate an Enterprise RA to verify certificate requests from the Enterprise RA's own organization.
The CA SHALL NOT accept certificate requests authorized by an Enterprise RA unless the following requirements are satisfied:

1. The CA SHALL confirm that the requested Fully-Qualified Domain Name(s) are within the Enterprise
RA's verified Domain Namespace.
2. If the certificate request includes a Subject name of a type other than a Fully-Qualified Domain Name, the CA SHALL confirm that the name is either that of the delegated enterprise, or an Affiliate of the delegated enterprise, or that the delegated enterprise is an agent of the named Subject. For example, the CA SHALL NOT issue a Certificate containing the Subject name "XYZ Co." on the authority of Enterprise RA "ABC Co.", unless the two companies are affiliated (see [Section 3.2](#32-initial-identity-validation)) or "ABC Co." is the agent of "XYZ Co". This requirement applies regardless of whether the accompanying requested Subject FQDN falls within the Domain Namespace of ABC Co.'s Registered Domain Name.

The CA SHALL impose these limitations as a contractual requirement on the Enterprise RA and monitor compliance by the Enterprise RA.

### 1.3.2 Registration authorities

With the exception of [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control), the CA MAY delegate the performance of all, or any part, of [Section 3.2](#32-initial-identity-validation) requirements to a Delegated Third Party, provided that the process as a whole fulfills all of the requirements of [Section 3.2](#32-initial-identity-validation).

Before the CA authorizes a Delegated Third Party to perform a delegated function, the CA SHALL contractually require the Delegated Third Party to:

1. Meet the qualification requirements of [Section 5.3.1](#531-qualifications-experience-and-clearance-requirements), when applicable to the delegated function;
2. Retain documentation in accordance with [Section 5.5.2](#552-retention-period-for-archive);
3. Abide by the other provisions of these Requirements that are applicable to the delegated function; and
4. Comply with (a) the CA's CP and/or CPS or (b) the Delegated Third Party's practice statement that the CA has verified complies with these Requirements.

#### 1.3.2.1 Enterprise registration authorities

The CA MAY delegate to an Enterprise Registration Authority (RA) to verify Certificate Requests for Subjects within the Enterprise RA's own organization. The CA SHALL NOT accept Certificate Requests authorized by an Enterprise RA unless the following requirements are satisfied:

1. If the Certificate Request is for a `Mailbox-validated`, `Organization-validated`, or `Sponsor-validated` profile, the CA SHALL confirm that the Enterprise RA has authorization or control of the requested email domain(s) in accordance with [Section 3.2.2.1](#3221-validating-authority-over-mailbox-via-domain) or [Section 3.2.2.3](#3223-validating-applicant-as-operator-of-associated-mail-servers). 
2. The CA SHALL confirm that the `subject:organizationName` name is either that of the delegated enterprise, or an Affiliate of the delegated enterprise, or that the delegated enterprise is an agent of the named Subject. For example, the CA SHALL NOT issue a Certificate containing the Subject name "XYZ Co." on the authority of Enterprise RA "ABC Co.", unless the two companies are Affiliated as defined in [Section 3.2](#32-initial-identity-validation) or "ABC Co." is the agent of "XYZ Co". This requirement applies regardless of whether the accompanying requested email domain falls within the subdomains of ABC Co.'s Registered Domain Name.

The CA SHALL impose these limitations as a contractual requirement on the Enterprise RA and monitor compliance by the Enterprise RA in accordance with [Section 8.8](#88-review-of-delegated-parties).

An Enterprise RA MAY also submit Certificate Requests using the `Mailbox-validated` profile for users whose email domain(s) are not under the delegated organization’s authorization or control.  In this case, the CA SHALL confirm that the mailbox holder has control of the requested Mailbox Address(es) in accordance with [Section 3.2.2.2](#3222-validating-control-over-mailbox-via-email).


### 1.3.3 Subscribers

As defined in [Section 1.6.1](#161-definitions).

### 1.3.4 Relying Parties

"Relying Party" and "Application Software Supplier" are defined in [Section 1.6.1](#161-definitions). Current Members of the CA/Browser Forum who are Application Software Suppliers are listed here:  
<https://cabforum.org/members>.

### 1.3.4 Relying parties

“Relying Party” and “Application Software Supplier” are defined in [Section 1.6.1](161-definitions). Current Members of the CA/Browser Forum who are Application Software Suppliers are listed at https://cabforum.org/members.

### 1.3.5 Other Participants

Other groups that have participated in the development of these Requirements include the AICPA/CICA WebTrust for Certification Authorities task force and ETSI ESI. Participation by such groups does not imply their endorsement, recommendation, or approval of the final product.

### 1.3.5 Other participants

Other groups that have participated in the development of these Requirements include the CPA Canada WebTrust for Certification Authorities task force and the Accredited Conformity Assessment Bodies’ Council (ACAB’C). Participation by these groups does not imply their endorsement, recommendation, or approval of the final product.

## 1.4 Certificate Usage

## 1.4 Certificate usage

The primary goal of these Requirements is to provide a framework of “reasonable assurance” to senders and recipients of email messages that the Subject identified in an S/MIME Certificate has control of the domain or Mailbox Address being asserted. A variation of this use case is where an Individual or organization digitally signs email to establish its authenticity and source of origin. 

### 1.4.1 Appropriate Certificate Uses

The primary goal of these Requirements is to enable efficient and secure electronic communication, while addressing user concerns about the trustworthiness of Certificates. These Requirements also serve to inform users and help them to make informed decisions when relying on Certificates.

### 1.4.1 Appropriate certificate uses

These Requirements describe an integrated set of technologies, protocols, identity-proofing, lifecycle management, and auditing requirements for the issuance and management of Publicly-Trusted S/MIME Certificates. These Requirements also serve to inform users and help them to make informed decisions when relying on Certificates.

### 1.4.2 Prohibited Certificate Uses


## 1.5 Policy administration

The Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates present criteria established by the CA/Browser Forum for use by Certification Authorities when issuing, maintaining, and revoking publicly-trusted Certificates. This document may be revised from time to time, as appropriate, in accordance with procedures adopted by the CA/Browser Forum. Because one of the primary beneficiaries of this document is the end user, the Forum openly invites anyone to make recommendations and suggestions by email to the CA/Browser Forum at <questions@cabforum.org>. The Forum members value all input, regardless of source, and will seriously consider all such input.

## 1.5 Policy administration

These Requirements MAY be revised from time to time, as appropriate, in accordance with procedures adopted by the CA/Browser Forum. The CA/Browser Forum welcomes recommendations and suggestions regarding this standard by email at <questions@cabforum.org>. 

### 1.5.1 Organization Administering the Document


### 1.5.2 Contact Person

Contact information for the CA/Browser Forum is available here: <https://cabforum.org/leadership/>. In this section of a CA's CPS, the CA shall provide a link to a web page or an email address for contacting the person or persons responsible for operation of the CA.

### 1.5.2 Contact person

Contact information for the CA/Browser Forum is available at https://cabforum.org/leadership/. In this section of a CA’s CPS, the CA SHALL provide a link to a web page or an email address for contacting the person or persons responsible for operation of the CA, including contact information for entities wishing to submit a Certificate Problem Report or revocation request.

### 1.5.3 Person Determining CPS suitability for the policy


### 1.5.4 CPS approval procedures


## 1.6 Definitions and Acronyms

The Definitions found in the CA/Browser Forum's Network and Certificate System Security Requirements are incorporated by reference as if fully set forth herein.

## 1.6 Definitions and acronyms

The Definitions found in the [CA/Browser Forum's Network and Certificate System Security Requirements](https://cabforum.org/network-security-requirements/) are incorporated by reference as if fully set forth herein.

### 1.6.1 Definitions

**Affiliate**: A corporation, partnership, joint venture or other entity controlling, controlled by, or under common control with another entity, or an agency, department, political subdivision, or any entity operating under the direct control of a Government Entity.

**Applicant**: The natural person or Legal Entity that applies for (or seeks renewal of) a Certificate. Once the Certificate is issued, the Applicant is referred to as the Subscriber. For Certificates issued to devices, the Applicant is the entity that controls or operates the device named in the Certificate, even if the device is sending the actual certificate request.

**Applicant Representative**: A natural person or human sponsor who is either the Applicant, employed by the Applicant, or an authorized agent who has express authority to represent the Applicant:

  i. who signs and submits, or approves a certificate request on behalf of the Applicant, and/or
  ii. who signs and submits a Subscriber Agreement on behalf of the Applicant, and/or
  iii. who acknowledges the Terms of Use on behalf of the Applicant when the Applicant is an Affiliate of the CA or is the CA.

**Application Software Supplier**: A supplier of Internet browser software or other relying-party application software that displays or uses Certificates and incorporates Root Certificates.

**Attestation Letter**: A letter attesting that Subject Information is correct written by an accountant, lawyer, government official, or other reliable third party customarily relied upon for such information.

**Audit Period**: In a period-of-time audit, the period between the first day (start) and the last day of operations (end) covered by the auditors in their engagement. (This is not the same as the period of time when the auditors are on-site at the CA.) The coverage rules and maximum length of audit periods are defined in [Section 8.1](#81-frequency-or-circumstances-of-assessment).

**Audit Report**: A report from a Qualified Auditor stating the Qualified Auditor's opinion on whether an entity's processes and controls comply with the mandatory provisions of these Requirements.

**Authorization Domain Name**: The FQDN used to obtain authorization for a given FQDN to be included in a Certificate. The CA may use the FQDN returned from a DNS CNAME lookup as the FQDN for the purposes of domain validation. If a Wildcard Domain Name is to be included in a Certificate, then the CA MUST remove "`*.`" from the left-most portion of the Wildcard Domain Name to yield the corresponding FQDN. The CA may prune zero or more Domain Labels of the FQDN from left to right until encountering a Base Domain Name and may use any one of the values that were yielded by pruning (including the Base Domain Name itself) for the purpose of domain validation.

**Authorized Ports**: One of the following ports: 80 (http), 443 (https), 25 (smtp), 22 (ssh).

**Base Domain Name**: The portion of an applied-for FQDN that is the first Domain Name node left of a registry-controlled or public suffix plus the registry-controlled or public suffix (e.g. "example.co.uk" or "example.com"). For FQDNs where the right-most Domain Name node is a gTLD having ICANN Specification 13 in its registry agreement, the gTLD itself may be used as the Base Domain Name.

**CAA**: From RFC 8659 (<http://tools.ietf.org/html/rfc8659>): "The Certification Authority Authorization (CAA) DNS Resource Record allows a DNS domain name holder to specify one or more Certification Authorities (CAs) authorized to issue certificates for that domain name. CAA Resource Records allow a public CA to implement additional controls to reduce the risk of unintended certificate mis-issue."

**CA Key Pair**: A Key Pair where the Public Key appears as the Subject Public Key Info in one or more Root CA Certificate(s) and/or Subordinate CA Certificate(s).

**Certificate**: An electronic document that uses a digital signature to bind a public key and an identity.

**Certificate Data**: Certificate requests and data related thereto (whether obtained from the Applicant or otherwise) in the CA's possession or control or to which the CA has access.

**Certificate Management Process**: Processes, practices, and procedures associated with the use of keys, software, and hardware, by which the CA verifies Certificate Data, issues Certificates, maintains a Repository, and revokes Certificates.

**Certificate Policy**: A set of rules that indicates the applicability of a named Certificate to a particular community and/or PKI implementation with common security requirements.

**Certificate Problem Report**: Complaint of suspected Key Compromise, Certificate misuse, or other types of fraud, compromise, misuse, or inappropriate conduct related to Certificates.

**Certificate Profile**: A set of documents or files that defines requirements for Certificate content and Certificate extensions in accordance with [Section 7](#7-certificate-crl-and-ocsp-profiles), e.g. a Section in a CA’s CPS or a certificate template file used by CA software.

**Certificate Revocation List**: A regularly updated time-stamped list of revoked Certificates that is created and digitally signed by the CA that issued the Certificates.

**Certification Authority**: An organization that is responsible for the creation, issuance, revocation, and management of Certificates. The term applies equally to both Root CAs and Subordinate CAs.

**Certification Practice Statement**: One of several documents forming the governance framework in which Certificates are created, issued, managed, and used.

**Control**: "Control" (and its correlative meanings, "controlled by" and "under common control with") means possession, directly or indirectly, of the power to: (1) direct the management, personnel, finances, or plans of such entity; (2) control the election of a majority of the directors ; or (3) vote that portion of voting shares required for "control" under the law of the entity's Jurisdiction of Incorporation or Registration but in no case less than 10%.

**Country**: Either a member of the United Nations OR a geographic region recognized as a Sovereign State by at least two UN member nations.

**Cross-Certified Subordinate CA Certificate**: A certificate that is used to establish a trust relationship between two CAs.

**CSPRNG**: A random number generator intended for use in a cryptographic system.

**Delegated Third Party**: A natural person or Legal Entity that is not the CA but is authorized by the CA, and whose activities are not within the scope of the appropriate CA audits, to assist in the Certificate Management Process by performing or fulfilling one or more of the CA requirements found herein.

**DNS CAA Email Contact**: The email address defined in [Appendix A.1.1](#a11-caa-contactemail-property).

**DNS CAA Phone Contact**: The phone number defined in [Appendix A.1.2](#a12-caa-contactphone-property).

**DNS TXT Record Email Contact**: The email address defined in [Appendix A.2.1](#a21-dns-txt-record-email-contact).

**DNS TXT Record Phone Contact**: The phone number defined in [Appendix A.2.2](#a22-dns-txt-record-phone-contact).

**Domain Contact**: The Domain Name Registrant, technical contact, or administrative contact (or the equivalent under a ccTLD) as listed in the WHOIS record of the Base Domain Name or in a DNS SOA record, or as obtained through direct contact with the Domain Name Registrar.

**Domain Label**: From RFC 8499 (<http://tools.ietf.org/html/rfc8499>): "An ordered list of zero or more octets that makes up a portion of a domain name. Using graph theory, a label identifies one node in a portion of the graph of all possible domain names."

**Domain Name**: An ordered list of one or more Domain Labels assigned to a node in the Domain Name System.

**Domain Namespace**: The set of all possible Domain Names that are subordinate to a single node in the Domain Name System.

**Domain Name Registrant**: Sometimes referred to as the "owner" of a Domain Name, but more properly the person(s) or entity(ies) registered with a Domain Name Registrar as having the right to control how a Domain Name is used, such as the natural person or Legal Entity that is listed as the "Registrant" by WHOIS or the Domain Name Registrar.

**Domain Name Registrar**: A person or entity that registers Domain Names under the auspices of or by agreement with:

  i. the Internet Corporation for Assigned Names and Numbers (ICANN),
  ii. a national Domain Name authority/registry, or
  iii. a Network Information Center (including their affiliates, contractors, delegates, successors, or assignees).

**Enterprise RA**: An employee or agent of an organization unaffiliated with the CA who authorizes issuance of Certificates to that organization.

**Expiry Date**: The "Not After" date in a Certificate that defines the end of a Certificate's validity period.

**Fully-Qualified Domain Name**: A Domain Name that includes the Domain Labels of all superior nodes in the Internet Domain Name System.

**Government Entity**: A government-operated legal entity, agency, department, ministry, branch, or similar element of the government of a country, or political subdivision within such country (such as a state, province, city, county, etc.).

**High Risk Certificate Request**: A Request that the CA flags for additional scrutiny by reference to internal criteria and databases maintained by the CA, which may include names at higher risk for phishing or other fraudulent usage, names contained in previously rejected certificate requests or revoked Certificates, names listed on the Miller Smiles phishing list or the Google Safe Browsing list, or names that the CA identifies using its own risk-mitigation criteria.

**Internal Name**: A string of characters (not an IP address) in a Common Name or Subject Alternative Name field of a Certificate that cannot be verified as globally unique within the public DNS at the time of certificate issuance because it does not end with a Top Level Domain registered in IANA's Root Zone Database.

**IP Address**: A 32-bit or 128-bit number assigned to a device that uses the Internet Protocol for communication.

**IP Address Contact**: The person(s) or entity(ies) registered with an IP Address Registration Authority as having the right to control how one or more IP Addresses are used.

**IP Address Registration Authority**: The Internet Assigned Numbers Authority (IANA) or a Regional Internet Registry (RIPE, APNIC, ARIN, AfriNIC, LACNIC).

**Issuing CA**: In relation to a particular Certificate, the CA that issued the Certificate. This could be either a Root CA or a Subordinate CA.

**Key Compromise**: A Private Key is said to be compromised if its value has been disclosed to an unauthorized person, or an unauthorized person has had access to it.

**Key Generation Script**: A documented plan of procedures for the generation of a CA Key Pair.

**Key Pair**: The Private Key and its associated Public Key.

**LDH Label**: From RFC 5890 (<http://tools.ietf.org/html/rfc5890>): "A string consisting of ASCII letters, digits, and the hyphen with the further restriction that the hyphen cannot appear at the beginning or end of the string. Like all DNS labels, its total length must not exceed 63 octets."

**Legal Entity**: An association, corporation, partnership, proprietorship, trust, government entity or other entity with legal standing in a country's legal system.

**Non-Reserved LDH Label**: From RFC 5890 (<http://tools.ietf.org/html/rfc5890>): "The set of valid LDH labels that do not have '`--`' in the third and fourth positions."

**Object Identifier**: A unique alphanumeric or numeric identifier registered under the International Organization for Standardization's applicable standard for a specific object or object class.

**OCSP Responder**: An online server operated under the authority of the CA and connected to its Repository for processing Certificate status requests. See also, Online Certificate Status Protocol.

**Onion Domain Name**: A Fully Qualified Domain Name ending with the RFC 7686 ".onion" Special-Use Domain Name. For example, `2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion` is an Onion Domain Name, whereas `torproject.org` is not an Onion Domain Name.

**Online Certificate Status Protocol**: An online Certificate-checking protocol that enables relying-party application software to determine the status of an identified Certificate. See also OCSP Responder.

**Parent Company**: A company that Controls a Subsidiary Company.

**P-Label**: A XN-Label that contains valid output of the Punycode algorithm (as defined in RFC 3492, Section 6.3) from the fifth and subsequent positions.

**Private Key**: The key of a Key Pair that is kept secret by the holder of the Key Pair, and that is used to create Digital Signatures and/or to decrypt electronic records or files that were encrypted with the corresponding Public Key.

**Pending Prohibition​​**: The use of a behavior described with this label is highly discouraged, as it is planned to be deprecated and will likely be designated as MUST NOT in the future.

**Public Key**: The key of a Key Pair that may be publicly disclosed by the holder of the corresponding Private Key and that is used by a Relying Party to verify Digital Signatures created with the holder's corresponding Private Key and/or to encrypt messages so that they can be decrypted only with the holder's corresponding Private Key.

**Public Key Infrastructure**: A set of hardware, software, people, procedures, rules, policies, and obligations used to facilitate the trustworthy creation, issuance, management, and use of Certificates and keys based on Public Key Cryptography.

**Publicly-Trusted Certificate**: A Certificate that is trusted by virtue of the fact that its corresponding Root Certificate is distributed as a trust anchor in widely-available application software.

**Qualified Auditor**: A natural person or Legal Entity that meets the requirements of [Section 8.2](#82-identityqualifications-of-assessor).

**Random Value**: A value specified by a CA to the Applicant that exhibits at least 112 bits of entropy.

**Registered Domain Name**: A Domain Name that has been registered with a Domain Name Registrar.

**Registration Authority (RA)**: Any Legal Entity that is responsible for identification and authentication of subjects of Certificates, but is not a CA, and hence does not sign or issue Certificates. An RA may assist in the certificate application process or revocation process or both. When "RA" is used as an adjective to describe a role or function, it does not necessarily imply a separate body, but can be part of the CA.

**Reliable Data Source**: An identification document or source of data used to verify Subject Identity Information that is generally recognized among commercial enterprises and governments as reliable, and which was created by a third party for a purpose other than the Applicant obtaining a Certificate.

**Reliable Method of Communication**: A method of communication, such as a postal/courier delivery address, telephone number, or email address, that was verified using a source other than the Applicant Representative.

**Relying Party**: Any natural person or Legal Entity that relies on a Valid Certificate. An Application Software Supplier is not considered a Relying Party when software distributed by such Supplier merely displays information relating to a Certificate.

**Repository**: An online database containing publicly-disclosed PKI governance documents (such as Certificate Policies and Certification Practice Statements) and Certificate status information, either in the form of a CRL or an OCSP response.

**Request Token**: A value, derived in a method specified by the CA which binds this demonstration of control to the certificate request. The CA SHOULD define within its CPS (or a document clearly referenced by the CPS) the format and method of Request Tokens it accepts.

The Request Token SHALL incorporate the key used in the certificate request.

A Request Token MAY include a timestamp to indicate when it was created.

A Request Token MAY include other information to ensure its uniqueness.

A Request Token that includes a timestamp SHALL remain valid for no more than 30 days from the time of creation.

A Request Token that includes a timestamp SHALL be treated as invalid if its timestamp is in the future.

A Request Token that does not include a timestamp is valid for a single use and the CA SHALL NOT re-use it for a subsequent validation.

The binding SHALL use a digital signature algorithm or a cryptographic hash algorithm at least as strong as that to be used in signing the certificate request.

**Note**: Examples of Request Tokens include, but are not limited to:

  i. a hash of the public key; or
  ii. a hash of the Subject Public Key Info [X.509]; or
  iii. a hash of a PKCS#10 CSR.

A Request Token may also be concatenated with a timestamp or other data. If a CA wanted to always use a hash of a PKCS#10 CSR as a Request Token and did not want to incorporate a timestamp and did want to allow certificate key re-use then the applicant might use the challenge password in the creation of a CSR with OpenSSL to ensure uniqueness even if the subject and key are identical between subsequent requests.

**Note**: This simplistic shell command produces a Request Token which has a timestamp and a hash of a CSR.
  ``echo `date -u +%Y%m%d%H%M` `sha256sum <r2.csr` \| sed "s/[ -]//g"``
The script outputs:
  201602251811c9c863405fe7675a3988b97664ea6baf442019e4e52fa335f406f7c5f26cf14f

**Required Website Content**: Either a Random Value or a Request Token, together with additional information that uniquely identifies the Subscriber, as specified by the CA.

**Requirements**: The Baseline Requirements found in this document.

**Reserved IP Address**: An IPv4 or IPv6 address that is contained in the address block of any entry in either of the following IANA registries:

[https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml)

[https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml](https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml)

**Root CA**: The top level Certification Authority whose Root Certificate is distributed by Application Software Suppliers and that issues Subordinate CA Certificates.

**Root Certificate**: The self-signed Certificate issued by the Root CA to identify itself and to facilitate verification of Certificates issued to its Subordinate CAs.

**Short-lived Subscriber Certificate**: For Certificates issued on or after 15 March 2024 and prior to 15 March 2026, a Subscriber Certificate with a Validity Period less than or equal to 10 days (864,000 seconds). For Certificates issued on or after 15 March 2026, a Subscriber Certificate with a Validity Period less than or equal to 7 days (604,800 seconds).

**Sovereign State**: A state or country that administers its own government, and is not dependent upon, or subject to, another power.

**Subject**: The natural person, device, system, unit, or Legal Entity identified in a Certificate as the Subject. The Subject is either the Subscriber or a device under the control and operation of the Subscriber.

**Subject Identity Information**: Information that identifies the Certificate Subject. Subject Identity Information does not include a Domain Name listed in the `subjectAltName` extension or the Subject `commonName` field.

**Subordinate CA**: A Certification Authority whose Certificate is signed by the Root CA, or another Subordinate CA.

**Subscriber**: A natural person or Legal Entity to whom a Certificate is issued and who is legally bound by a Subscriber Agreement or Terms of Use.

**Subscriber Agreement**: An agreement between the CA and the Applicant/Subscriber that specifies the rights and responsibilities of the parties.

**Subsidiary Company**: A company that is controlled by a Parent Company.

**Technically Constrained Subordinate CA Certificate**: A Subordinate CA certificate which uses a combination of Extended Key Usage and/or Name Constraint extensions, as defined within the relevant Certificate Profiles of this document, to limit the scope within which the Subordinate CA Certificate may issue Subscriber or additional Subordinate CA Certificates.

**Terms of Use**: Provisions regarding the safekeeping and acceptable uses of a Certificate issued in accordance with these Requirements when the Applicant/Subscriber is an Affiliate of the CA or is the CA.

**Test Certificate**: This term is no longer used in these Baseline Requirements.

**Trustworthy System**: Computer hardware, software, and procedures that are: reasonably secure from intrusion and misuse; provide a reasonable level of availability, reliability, and correct operation; are reasonably suited to performing their intended functions; and enforce the applicable security policy.

**Unregistered Domain Name**: A Domain Name that is not a Registered Domain Name.

**Valid Certificate**: A Certificate that passes the validation procedure specified in RFC 5280.

**Validation Specialist**: Someone who performs the information verification duties specified by these Requirements.

**Validity Period**: From RFC 5280 (<http://tools.ietf.org/html/rfc5280>): "The period of time from notBefore through notAfter, inclusive."

**WHOIS**: Information retrieved directly from the Domain Name Registrar or registry operator via the protocol defined in RFC 3912, the Registry Data Access Protocol defined in RFC 7482, or an HTTPS website.

**Wildcard Certificate**: A Certificate containing at least one Wildcard Domain Name in the Subject Alternative Names in the Certificate.

**Wildcard Domain Name**: A string starting with "\*." (U+002A ASTERISK, U+002E FULL STOP) immediately followed by a Fully-Qualified Domain Name.

**XN-Label**: From RFC 5890 (<http://tools.ietf.org/html/rfc5890>): "The class of labels that begin with the prefix `"xn--"` (case independent), but otherwise conform to the rules for LDH labels."

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

### 1.6.2 Acronyms

| **Acronym** | **Meaning** |
| --- | --- |
| AICPA | American Institute of Certified Public Accountants |
| ADN | Authorization Domain Name |
| CA | Certification Authority |
| CAA | Certification Authority Authorization |
| ccTLD | Country Code Top-Level Domain |
| CICA | Canadian Institute of Chartered Accountants |
| CP | Certificate Policy |
| CPS | Certification Practice Statement |
| CRL | Certificate Revocation List |
| DBA | Doing Business As |
| DNS | Domain Name System |
| FIPS | (US Government) Federal Information Processing Standard |
| FQDN | Fully-Qualified Domain Name |
| IM | Instant Messaging |
| IANA | Internet Assigned Numbers Authority |
| ICANN | Internet Corporation for Assigned Names and Numbers |
| ISO | International Organization for Standardization |
| NIST | (US Government) National Institute of Standards and Technology |
| OCSP | Online Certificate Status Protocol |
| OID | Object Identifier |
| PKI | Public Key Infrastructure |
| RA | Registration Authority |
| S/MIME | Secure MIME (Multipurpose Internet Mail Extensions) |
| SSL | Secure Sockets Layer |
| TLS | Transport Layer Security |
| VoIP | Voice Over Internet Protocol |

### 1.6.2 Acronyms

|Acronym   |Meaning                                                            |
|----------|-------------------------------------------------------------------|
|CA	   |Certification Authority |
|CAA	   |Certification Authority Authorization |
|CP	   |Certificate Policy |
|CPS	   |Certification Practice Statement |
|CRL	   |Certificate Revocation List |
|DBA	   |Doing Business As |
|DNS	   |Domain Name System |
|ETSI	   |European Telecommunications Standards Institute |
|FIPS	   |(US Government) Federal Information Processing Standard|
|ICAO	   |International Civil Aviation Organization |
|ISO	   |International Organization for Standardization |
|MV	   |Mailbox-validated |
|NIST	   |(US Government) National Institute of Standards and Technology |
|OCSP	   |Online Certificate Status Protocol |
|OID	   |Object Identifier |
|PKI	   |Public Key Infrastructure |
|RA	   |Registration Authority |
|S/MIME  |Secure MIME (Multipurpose Internet Mail Extensions) |
|TLS	   |Transport Layer Security |

### 1.6.3 References

ETSI EN 319 403, Electronic Signatures and Infrastructures (ESI); Trust Service Provider Conformity Assessment - Requirements for conformity assessment bodies assessing Trust Service Providers

ETSI EN 319 411-1, Electronic Signatures and Infrastructures (ESI); Policy and security requirements for Trust Service Providers issuing certificates; Part 1: General requirements

ETSI TS 102 042, Electronic Signatures and Infrastructures (ESI); Policy requirements for certification authorities issuing public key certificates.

FIPS 140-2, Federal Information Processing Standards Publication - Security Requirements For Cryptographic Modules, Information Technology Laboratory, National Institute of Standards and Technology, May 25, 2001.

FIPS 140-3, Federal Information Processing Standards Publication - Security Requirements For Cryptographic Modules, Information Technology Laboratory, National Institute of Standards and Technology, March 22, 2019.

FIPS 186-4, Federal Information Processing Standards Publication - Digital Signature Standard (DSS), Information Technology Laboratory, National Institute of Standards and Technology, July 2013.

ISO 21188:2006, Public key infrastructure for financial services -- Practices and policy framework.

Network and Certificate System Security Requirements, Version 1.7, available at <https://cabforum.org/wp-content/uploads/CA-Browser-Forum-Network-Security-Guidelines-v1.7.pdf>.

NIST SP 800-89, Recommendation for Obtaining Assurances for Digital Signature Applications, <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-89.pdf>.

RFC2119, Request for Comments: 2119, Key words for use in RFCs to Indicate Requirement Levels. S. Bradner. March 1997.

RFC3492, Request for Comments: 3492, Punycode: A Bootstring encoding of Unicode for Internationalized Domain Names in Applications (IDNA). A. Costello. March 2003.

RFC3647, Request for Comments: 3647, Internet X.509 Public Key Infrastructure: Certificate Policy and Certification Practices Framework. S. Chokhani, et al. November 2003.

RFC3912, Request for Comments: 3912, WHOIS Protocol Specification. L. Daigle. September 2004.

RFC3986, Request for Comments: 3986, Uniform Resource Identifier (URI): Generic Syntax. T. Berners-Lee, et al. January 2005.

RFC5019, Request for Comments: 5019, The Lightweight Online Certificate Status Protocol (OCSP) Profile for High-Volume Environments. A. Deacon, et al. September 2007.

RFC5280, Request for Comments: 5280, Internet X.509 Public Key Infrastructure: Certificate and Certificate Revocation List (CRL) Profile. D. Cooper, et al. May 2008.

RFC5890, Request for Comments: 5890, Internationalized Domain Names for Applications (IDNA): Definitions and Document Framework. J. Klensin. August 2010.

RFC5952, Request for Comments: 5952, A Recommendation for IPv6 Address Text Representation. S. Kawamura, et al. August 2010.

RFC6960, Request for Comments: 6960, X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP. S. Santesson, et al. June 2013.

RFC6962, Request for Comments: 6962, Certificate Transparency. B. Laurie, et al. June 2013.

RFC7231, Request For Comments: 7231, Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content. R. Fielding, et al. June 2014.

RFC7482, Request for Comments: 7482, Registration Data Access Protocol (RDAP) Query Format. A. Newton, et al. March 2015.

RFC7538, Request For Comments: 7538, The Hypertext Transfer Protocol Status Code 308 (Permanent Redirect). J. Reschke. April 2015.

RFC8499, Request for Comments: 8499, DNS Terminology. P. Hoffman, et al. January 2019.

RFC8659, Request for Comments: 8659, DNS Certification Authority Authorization (CAA) Resource Record. P. Hallam-Baker, et al. November 2019.

RFC8954, Request for Comments: 8954, Online Certificate Status Protocol (OCSP) Nonce Extension. M. Sahni, Ed. November 2020.

WebTrust for Certification Authorities, SSL Baseline with Network Security, Version 2.5, available at <https://www.cpacanada.ca/-/media/site/operational/ms-member-services/docs/webtrust/wt100bwtbr-25-110120-finalaoda.pdf>.

X.509, Recommendation ITU-T X.509 (08/2005) \| ISO/IEC 9594-8:2005, Information technology – Open Systems Interconnection – The Directory: Public-key and attribute certificate frameworks.

### 1.6.3 References

ETSI EN 319 403, Electronic Signatures and Infrastructures (ESI); Trust Service Provider Conformity Assessment - Requirements for conformity assessment bodies assessing Trust Service Providers.

ETSI EN 319 403-1, Electronic Signatures and Infrastructures (ESI); Trust Service Provider Conformity Assessment; Part 1 - Requirements for conformity assessment bodies assessing Trust Service Providers.

ETSI EN 319 411-1, Electronic Signatures and Infrastructures (ESI); Policy and security requirements for Trust Service Providers issuing certificates; Part 1: General requirements.

ETSI EN 319 411-2, Electronic Signatures and Infrastructures (ESI); Policy and security requirements for Trust Service Providers issuing certificates; Part 2: Requirements for trust service providers issuing EU qualified certificates.

ETSI EN 119 411-6, Electronic Signatures and Infrastructures (ESI); Policy and security requirements for Trust Service Providers issuing certificates; Part 6: Requirements for Trust Service Providers issuing publicly trusted S/MIME certificates.

ETSI EN 319 412-1, Electronic Signatures and Infrastructures (ESI); Certificate Profiles; Part 1: Overview and common data structures.

ETSI EN 319 412-5, Electronic Signatures and Infrastructures (ESI); Certificate Profiles; Part 5: QCStatements.

ETSI TS 119 495, Electronic Signatures and Infrastructures (ESI); Sector Specific Requirements; Certificate Profiles and TSP Policy Requirements for Open Banking.

ETSI TS 119 172-4, Electronic Signatures and Infrastructures (ESI); Signature Policies;. Part 4: Signature applicability rules.

FIPS 140-2, Federal Information Processing Standards Publication - Security Requirements For Cryptographic Modules, Information Technology Laboratory, National Institute of Standards and Technology, May 25, 2001.

ICAO DOC 9303, Machine Readable Travel Documents, Part 10, Logical Data Structure (LDS) for Storage of Biometrics and Other Data in the Contactless Integrated Circuit (IC), International Civil Aviation Organization, Eighth Edition, 2021.

ICAO DOC 9303, Machine Readable Travel Documents, Part 11, Security Mechanisms for MRTDs, International Civil Aviation Organization, Eighth Edition, 2021.

ISO 17065:2012, Conformity assessment — Requirements for bodies certifying products, processes and services.

ISO 17442-1:2020, Financial services — Legal entity identifier (LEI) - Part 1: Assignment.

ISO 17442-2:2020, Financial services — Legal entity identifier (LEI) - Part 2: Application in digital certificates.

Network and Certificate System Security Requirements, Version 1.7 or later. See https://cabforum.org/network-security-requirements/.

NIST SP 800-89, Recommendation for Obtaining Assurances for Digital Signature Applications.

RFC 2119, Request for Comments: 2119, Key words for use in RFCs to Indicate Requirement Levels, S. Bradner. March 1997.

RFC 3647, Request for Comments: 3647, Internet X.509 Public Key Infrastructure: Certificate Policy and Certification Practices Framework, S. Chokhani, et al. November 2003.

RFC 3739, Request for Comments: 3739, Internet X.509 Public Key Infrastructure: Qualified Certificates Profile, S. Santesson, et al. March 2004.

RFC 4262, Request for Comments: 4262, X.509 Certificate Extension for Secure/Multipurpose Internet Mail Extensions (S/MIME) Capabilities, S. Santesson. December 2005.

RFC 5019, Request for Comments: 5019, The Lightweight Online Certificate Status Protocol (OCSP) Profile for High-Volume Environments, A. Deacon, et al. September 2007.

RFC 5280, Request for Comments: 5280, Internet X.509 Public Key Infrastructure: Certificate and Certificate Revocation List (CRL) Profile, Cooper et al. May 2008.

RFC 6818, Updates to the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile. January 2013.

RFC 6960, Request for Comments: 6960, X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP. S. Santesson, et al. June 2013.

RFC 8398, Request for Comments: 8398, Internationalized Email Addresses in X.509 Certificates, MAY 2018. A. Melnikov, et al. May 2018.

RFC 8499, Request for Comments: 8499, DNS Terminology. P. Hoffman, et al. January 2019.

RFC 8659, Request for Comments: 8659, DNS Certification Authority Authorization (CAA) Resource Record, Hallam-Baker, et al. November 2019.

"TLS Baseline Requirements" means the relevant version of the CA/Browser Forum's "Baseline Requirements for the Issuance and Management of Publicly‐Trusted TLS Server Certificates". See https://cabforum.org/baseline-requirements-documents/

WebTrust for Certification Authorities, CPA Canada.

X.509, Recommendation ITU-T X.509 (10/2012) \| ISO/IEC 9594-8:2014 (E), Information technology – Open Systems Interconnection – The Directory: Public-key and attribute certificate frameworks.

### 1.6.4 Conventions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in these Requirements shall be interpreted in accordance with RFC 2119.

By convention, this document omits time and timezones when listing effective requirements such as dates. Except when explicitly specified, the associated time with a date shall be 00:00:00 UTC.

### 1.6.4 Conventions

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in these Requirements shall be interpreted in accordance with [RFC 2119](http://tools.ietf.org/html/rfc2119).

# 2. PUBLICATION AND REPOSITORY RESPONSIBILITIES

The CA SHALL develop, implement, enforce, and annually update a Certificate Policy and/or Certification Practice Statement that describes in detail how the CA implements the latest version of these Requirements.

# 2. PUBLICATION AND REPOSITORY RESPONSIBILITIES

## 2.1 Repositories

The CA SHALL make revocation information for Subordinate Certificates and Subscriber Certificates available in accordance with this Policy.

## 2.1 Repositories

The CA SHALL make revocation information for Subordinate CA Certificates and Subscriber Certificates available in accordance with this Policy.

## 2.2 Publication of information

The CA SHALL publicly disclose its Certificate Policy and/or Certification Practice Statement through an appropriate and readily accessible online means that is available on a 24x7 basis. The CA SHALL publicly disclose its CA business practices to the extent required by the CA's selected audit scheme (see [Section 8.4](#84-topics-covered-by-assessment)).

The Certificate Policy and/or Certification Practice Statement MUST be structured in accordance with RFC 3647 and MUST include all material required by RFC 3647.

Section 4.2 of a CA's Certificate Policy and/or Certification Practice Statement SHALL state the CA's policy or practice on processing CAA Records for Fully-Qualified Domain Names; that policy shall be consistent with these Requirements. It shall clearly specify the set of Issuer Domain Names that the CA recognizes in CAA "issue" or "issuewild" records as permitting it to issue. The CA SHALL log all actions taken, if any, consistent with its processing practice.

The CA SHALL publicly give effect to these Requirements and represent that it will adhere to the latest published version. The CA MAY fulfill this requirement by incorporating these Requirements directly into its Certificate Policy and/or Certification Practice Statements or by incorporating them by reference using a clause such as the following (which MUST include a link to the official version of these Requirements):

> [Name of CA] conforms to the current version of the Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates published at <http://www.cabforum.org>. In the event of any inconsistency between this document and those Requirements, those Requirements take precedence over this document.

The CA SHALL host test Web pages that allow Application Software Suppliers to test their software with Subscriber Certificates that chain up to each publicly trusted Root Certificate. At a minimum, the CA SHALL host separate Web pages using Subscriber Certificates that are

  i. valid,
  ii. revoked, and
  iii. expired.

## 2.2 Publication of certification information

The CA SHALL publicly disclose its CP and/or CPS through an appropriate and readily accessible online means that is available on a 24x7 basis. The CA SHALL publicly disclose its CA business practices to the extent required by the CA's selected audit scheme (see [Section 8](#8-compliance-audit-and-other-assessments)).

The CP and/or CPS SHALL be structured in accordance with [RFC 3647](http://tools.ietf.org/html/rfc3647) and SHALL include all material required by [RFC 3647](http://tools.ietf.org/html/rfc3647).

The CA SHALL publicly give effect to these Requirements and represent that it will adhere to the latest published version. The CA MAY fulfill this requirement by incorporating these Requirements directly into its CP and/or CPS or by incorporating them by reference using a clause such as the following (which SHALL include a link to the official version of these Requirements):

> [Name of CA] conforms to the current version of the Baseline Requirements for the Issuance and Management of Publicly-Trusted S/MIME Certificates published at https://www.cabforum.org. In the event of any inconsistency between this document and those Requirements, those Requirements take precedence over this document.

## 2.3 Time or frequency of publication

The CA SHALL develop, implement, enforce, and annually update a Certificate Policy and/or Certification Practice Statement that describes in detail how the CA implements the latest version of these Requirements. The CA SHALL indicate conformance with this requirement by incrementing the version number and adding a dated changelog entry, even if no other changes are made to the document.

## 2.3 Time or frequency of publication

The CA SHALL develop, implement, enforce, and annually update a Certificate Policy and/or Certification Practice Statement (CP and/or CPS) that describes in detail how the CA implements the latest version of these Requirements. The CA SHALL review and update its CP and/or CPS at least every 365 days, incrementing the version number and adding a dated changelog entry, even if no other changes are made to the document.

## 2.4 Access controls on repositories

The CA shall make its Repository publicly available in a read-only manner.

# 3. IDENTIFICATION AND AUTHENTICATION

## 3.1 Naming

### 3.1.1 Types of names

### 3.1.1 Types of names

When the `subject:commonName` of a Certificate issued to an Individual does not contain a Mailbox Address, it is specified as a Personal Name or Pseudonym as described in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields)(a). 

Names consisting of multiple words are permitted. Given names joined with a hyphen are considered as one single given name. Subjects with more than one given name MAY choose one or several of their given names in any sequence. Subjects MAY choose the order of their given name(s) and surname in accordance with national preference.

The CA MAY allow common variations or abbreviations of Personal Names consistent with local practice. 

### 3.1.2 Need for names to be meaningful

### 3.1.2 Need for names to be meaningful

Personal Names SHALL be a meaningful representation of the Subject’s name as verified in the identifying documentation or Enterprise RA records. 

### 3.1.3 Anonymity or pseudonymity of subscribers

### 3.1.3 Anonymity or pseudonymity of subscribers

The purpose of a Pseudonym is to provide a unique identifier linked to an Individual in a pseudonymized manner when certain privacy conditions are required. For example, a Pseudonym may be used if a government agency requires officials to sign certain decisions via S/MIME so those decisions trace back to individuals, but emphasize the importance of the role over Individual identity in the Certificate. The CA SHALL disclose in its CP and/or CPS if it allows the use of Pseudonyms.

For `Sponsor-validated` certificates, the CA MAY use a `subject:pseudonym` attribute in the Certificate if the associated Subject has been verified according to [Section 3.2.4](#324-authentication-of-individual-identity). If present, the `subject:pseudonym` attribute SHALL be:

  1. either a unique identifier selected by the CA for the Subject of the Certificate; or
  2. an identifier selected by the Enterprise RA which uniquely identifies the Subject of the Certificate within the Organization included in the `subject:organizationName` attribute.

For `Individual-validated` certificates, the CA MAY use the `subject:pseudonym` attribute if the associated Subject has been verified according to [Section 3.2.4](#324-authentication-of-individual-identity). If present, the `subject:pseudonym` attribute SHALL be:

  1. either a unique identifier selected by the CA for the Subject of the Certificate; or
  2. an identifier verified based on government-issued identity documents.

Pseudonym Certificates are not anonymous. CAs and Enterprise RAs SHALL treat Individual identity information relating to a Pseudonym as private in accordance with [Section 9.4.2](#942-information-treated-as-private).

### 3.1.4 Rules for interpreting various name forms

#### 3.1.4.1 Non ASCII character substitution

The CA MAY allow the Conversion of Subject Identity Information usually rendered in non-ASCII characters (including Accent or Umlaut-accented characters) using a system commonly used in the Applicant's Jurisdiction of Incorporation or Registration, or recognized by the United Nations or the International Organization for Standardization (ISO). The CA SHOULD state the used Conversion systems in its CP and/or CPS. For example, regardless of capitalization:

*  Accent characters MAY be represented by their ASCII equivalent. For example é, à, í, ñ, or ç MAY be represented by e, a, i, n, or c, respectively.
*  Umlaut-accented characters such as ä, ö, ü MAY be represented by either ae, oe, ue or a, o, u, respectively.

The CA MAY include an ASCII character name that is not a direct Conversion of the Applicant's registered name provided that it is verified in a Reliable Data Source or suitable Attestation.

#### 3.1.4.2 Geographic names

The CA MAY use geographic endonyms and exonyms in the `subject:localityName` and `subject:stateOrProvinceName` attributes, (e.g., Munich, Monaco di Bavaria, or Мюнхен for München). The CA SHOULD avoid the use of archaic geographic names, (e.g., prefer Mumbai over Bombay).

### 3.1.5 Uniqueness of names

### 3.1.6 Recognition, authentication, and role of trademarks

## 3.2 Initial identity validation

## 3.2 Initial identity validation

The CA SHALL authenticate the identity attributes of the Subject and their control over the Mailbox Addresses to be included in the S/MIME Certificate according to the requirements of the following sections:

| Certificate Type    | Mailbox Control | Organization Identity | Individual Identity | 
|---------|----------|----------|----------|
| `Mailbox-validated` | [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control)  | NA | NA | 
| `Organization-validated` |  [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control)  | [Section 3.2.3](#323-authentication-of-organization-identity) | NA |
| `Sponsor-validated` | [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control) | [Section 3.2.3](#323-authentication-of-organization-identity) | [Section 3.2.4](#324-authentication-of-individual-identity) | 
| `Individual-validated` | [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control) | NA | [Section 3.2.4](#324-authentication-of-individual-identity) | 

### 3.2.1 Method to prove possession of private key

### 3.2.2 Authentication of Organization and Domain Identity

If the Applicant requests a Certificate that will contain Subject Identity Information comprised only of the `countryName` field, then the CA SHALL verify the country associated with the Subject using a verification process meeting the requirements of [Section 3.2.2.3](#3223-verification-of-country) and that is described in the CA's Certificate Policy and/or Certification Practice Statement. If the Applicant requests a Certificate that will contain the countryName field and other Subject Identity Information, then the CA SHALL verify the identity of the Applicant, and the authenticity of the Applicant Representative's certificate request using a verification process meeting the requirements of this [Section 3.2.2.1](#3221-identity) and that is described in the CA's Certificate Policy and/or Certification Practice Statement. The CA SHALL inspect any document relied upon under this Section for alteration or falsification.

### 3.2.2 Validation of mailbox authorization or control

This section defines the permitted processes and procedures for confirming the Applicant's control of Mailbox Addresses to be included in issued Certificates. 

The CA SHALL verify that Applicant controls the email accounts associated with all Mailbox Fields referenced in the Certificate or has been authorized by the email account holder to act on the account holder’s behalf. 

The CA SHALL NOT delegate the verification of mailbox authorization or control.

The CA's CP and/or CPS SHALL specify the procedures that the CA employs to perform this verification. CAs SHALL maintain a record of which validation method, including the relevant version number from the TLS Baseline Requirements or S/MIME Baseline Requirements, was used to validate every domain or email address in issued Certificates.

Completed validations of Applicant authority MAY be valid for the issuance of multiple Certificates over time. In all cases, the validation SHALL have been initiated within the time period specified in the relevant requirement (such as [Section 4.2.1](#421-performing-identification-and-authentication-functions)) prior to Certificate issuance.

**Note:** Mailbox Fields MAY be listed in Subscriber Certificates using `rfc822Name` or `otherNames` of `type id-on-SmtpUTF8Mailbox` in the `subjectAltName` extension. Mailbox Fields MAY be listed in Subordinate CA Certificates via `rfc822Name` in permittedSubtrees within the `nameConstraints` extension.

#### 3.2.2.1 Identity

If the Subject Identity Information is to include the name or address of an organization, the CA SHALL verify the identity and address of the organization and that the address is the Applicant's address of existence or operation. The CA SHALL verify the identity and address of the Applicant using documentation provided by, or through communication with, at least one of the following:

1. A government agency in the jurisdiction of the Applicant's legal creation, existence, or recognition;
2. A third party database that is periodically updated and considered a Reliable Data Source;
3. A site visit by the CA or a third party who is acting as an agent for the CA; or
4. An Attestation Letter.

The CA MAY use the same documentation or communication described in 1 through 4 above to verify both the Applicant's identity and address.

Alternatively, the CA MAY verify the address of the Applicant (but not the identity of the Applicant) using a utility bill, bank statement, credit card statement, government-issued tax document, or other form of identification that the CA determines to be reliable.

#### 3.2.2.1 Validating authority over mailbox via domain

The CA MAY confirm the Applicant, such as an Enterprise RA, has been authorized by the email account holder to act on the account holder’s behalf by verifying the entity's control over the domain portion of the Mailbox Address to be used in the Certificate.

The CA SHALL use only the approved methods in [Section 3.2.2.4 of the TLS Baseline Requirements](https://github.com/cabforum/servercert/blob/main/docs/BR.md#3224-validation-of-domain-authorization-or-control) to perform this verification.

For purposes of domain validation, the term Applicant includes the Applicant's Parent Company, Subsidiary Company, or Affiliate.

#### 3.2.2.2 DBA/Tradename

If the Subject Identity Information is to include a DBA or tradename, the CA SHALL verify the Applicant's right to use the DBA/tradename using at least one of the following:

1. Documentation provided by, or communication with, a government agency in the jurisdiction of the Applicant's legal creation, existence, or recognition;
2. A Reliable Data Source;
3. Communication with a government agency responsible for the management of such DBAs or trade names;
4. An Attestation Letter accompanied by documentary support; or
5. A utility bill, bank statement, credit card statement, government-issued tax document, or other form of identification that the CA determines to be reliable.

#### 3.2.2.2 Validating control over mailbox via email

The CA MAY confirm the Applicant's control over each Mailbox Field to be included in a Certificate by sending a Random Value via email and then receiving a confirming response utilizing the Random Value. 

Control over each Mailbox Address SHALL be confirmed using a unique Random Value. The Random Value SHALL be sent only to the email address being validated and SHALL not be shared in any other way. 

The Random Value SHALL be unique in each email. The Random Value SHALL remain valid for use in a confirming response for no more than 24 hours from its creation. The CA MAY specify a shorter validity period for Random Values in its CP and/or CPS.

The Random Value SHALL be reset upon each instance of the email sent by the CA to a Mailbox Address, however all relevant Random Values sent to that Mailbox Address MAY remain valid for use in a confirming response within the validity period described in this Section. In addition, the Random Value SHALL be reset upon first use by the user if intended for additional use as an authentication factor following the Mailbox Address verification. 

#### 3.2.2.3 Verification of Country

If the `subject:countryName` field is present, then the CA SHALL verify the country associated with the Subject using one of the following:

  a. the IP Address range assignment by country for either
     i. the web site's IP address, as indicated by the DNS record for the web site or
     ii. the Applicant's IP address;
  b. the ccTLD of the requested Domain Name;
  c. information provided by the Domain Name Registrar; or
  d. a method identified in [Section 3.2.2.1](#3221-identity).

The CA SHOULD implement a process to screen proxy servers in order to prevent reliance upon IP addresses assigned in countries other than where the Applicant is actually located.

#### 3.2.2.3 Validating applicant as operator of associated mail server(s)

The CA MAY confirm the Applicant's control over each Mailbox Field to be included in the Certificate by confirming control of the SMTP FQDN to which a message delivered to the Mailbox Address should be directed. The SMTP FQDN SHALL be identified using the address resolution algorithm defined in [RFC 5321 Section 5.1](https://datatracker.ietf.org/doc/html/rfc5321#section-5.1) which determines which SMTP FQDNs are authoritative for a given Mailbox Address. If more than one SMTP FQDN has been discovered, the CA SHALL verify control of an SMTP FQDN following the selection process at [RFC 5321 Section 5.1](https://datatracker.ietf.org/doc/html/rfc5321#section-5.1). Aliases in MX record RDATA SHALL NOT be used for this validation method.

To confirm the Applicant's control of the SMTP FQDN, the CA SHALL use only the currently-approved methods in [Section 3.2.2.4](https://github.com/cabforum/servercert/blob/main/docs/BR.md#3224-validation-of-domain-authorization-or-control) of the TLS Baseline Requirements.

#### 3.2.2.4 CAA records

This version of the S/MIME Baseline Requirements does not require the CA to check for CAA records. The CAA property tags for `issue`, `issuewild`, and `iodef` as specified in [RFC 8659](https://datatracker.ietf.org/doc/html/rfc8659) are not recognized for the issuance of S/MIME Certificates.

### 3.2.3 Authentication of individual identity

If an Applicant subject to this [Section 3.2.3](#323-authentication-of-individual-identity) is a natural person, then the CA SHALL verify the Applicant's name, Applicant's address, and the authenticity of the certificate request.

The CA SHALL verify the Applicant's name using a legible copy, which discernibly shows the Applicant's face, of at least one currently valid government-issued photo ID (passport, drivers license, military ID, national ID, or equivalent document type). The CA SHALL inspect the copy for any indication of alteration or falsification.

The CA SHALL verify the Applicant's address using a form of identification that the CA determines to be reliable, such as a government ID, utility bill, or bank or credit card statement. The CA MAY rely on the same government-issued ID that was used to verify the Applicant's name.

The CA SHALL verify the certificate request with the Applicant using a Reliable Method of Communication.

### 3.2.3 Authentication of organization identity

The following requirements SHALL be fulfilled to authenticate Organization identity included in the `Organization-validated` and `Sponsor-validated` profiles.

#### 3.2.3.1 Attribute collection of organization identity

The CA or RA SHALL collect and retain evidence supporting the following identity attributes for the Organization:

1.	Formal name of the Legal Entity;
2.	A registered Assumed Name for the Legal Entity (if included in the Subject);
3. An organizational unit of the Legal Entity (if included in the Subject);
4.	An address of the Legal Entity (if included in the Subject);
5.	Jurisdiction of Incorporation or Registration of the Legal Entity; and
6.	Unique identifier and type of identifier for the Legal Entity. 

The unique identifier SHALL be included in the Certificate `subject:organizationIdentifier` as specified in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields) and [Appendix A](#appendix-a---registration-schemes).

#### 3.2.3.2 Validation of organization identity

If an Attestation is used as evidence for the validation of the attributes described in this section, then the Attestation SHALL be verified for authenticity as described in [Section 3.2.8](#328-reliability-of-verification-sources).

##### 3.2.3.2.1 Verification of name, address, and unique identifier

The CA or RA SHALL verify the full legal name and an address (if included in the Certificate Subject) of the Legal Entity Applicant using documentation provided by, or through communication with, at least one of the following:

1.	A government agency in the jurisdiction of the Legal Entity’s creation, existence, or recognition; 
2.	A Legal Entity Identifier (LEI) data reference;
3.	A site visit by the CA or a third party who is acting as an agent for the CA; or
4.	An Attestation which includes a copy of supporting documentation used to establish the Applicant's legal existence, such as a certificate of registration, articles of incorporation, operating agreement, statute, or regulatory act.

The CA or RA MAY use the same documentation or communication described in 1 through 4 above to verify both the Applicant's identity and address.

If an LEI data reference is used, the CA or RA SHALL verify that the RegistrationStatus is ISSUED and the EntityStatus is ACTIVE. The CA SHALL only allow use of an LEI if the ValidationSources entry is FULLY_CORROBORATED. An LEI SHALL NOT be used if ValidationSources entry is PARTIALLY_CORROBORATED, PENDING, or ENTITY_SUPPLIED_ONLY.

##### 3.2.3.2.2 Verification of assumed name

Applicants MAY request an Assumed Name to be included in the Certificate. The CA or RA SHALL verify that:

1.	The Applicant has registered its use of the Assumed Name with the appropriate government agency for such filings in the jurisdiction of its incorporation or registration; and 
2.	The Assumed Name filing continues to be valid.

The CA MAY rely on an Attestation that indicates the Assumed Name under which the Applicant conducts business, the government agency with which the Assumed Name is registered, and that such filing continues to be valid.

#### 3.2.3.3 Disclosure of verification sources

The CA or RA SHALL verify the unique identifier used in the Certificate from a register that is maintained or authorized by the relevant government agency. The CA SHALL disclose the authorized sources it uses to verify the Applicant's creation, existence, or recognition. This disclosure SHALL be through an appropriate and readily accessible online means. The CA SHALL document where to obtain this information within Section 3.2 of the CA's CP and/or CPS.

Nothing in these Requirements prohibits the use of third-party vendors to obtain regularly-updated and current information from the government register provided that the third party obtains the information directly from the government.

In the case of a LEI data reference, the CA or RA SHALL verify the associated data record with the [Global Legal Entity Identifier Foundation](https://search.gleif.org/#/search/).

### 3.2.4 Non-verified subscriber information

### 3.2.4 Authentication of individual identity

The following requirements SHALL be fulfilled to authenticate Individual identity attributes included in `Sponsor-validated` and `Individual-validated` Certificate profiles.

The CA, RA, or Enterprise RA SHALL collect and retain evidence supporting the following identity attributes for the Individual Applicant:

1. Given name(s) and surname(s), which SHALL be current names;
2. Pseudonym (if used); 
3. Title (if used);
4. Address (if displayed in Subject); and
5. Further information as needed to uniquely identify the Applicant.

The CA or RA SHALL comply with applicable data protection legislation in the gathering and retention of evidence relating to Individual identity supporting this Requirement in accordance with [Section 9.4](#94-privacy-of-personal-information).

#### 3.2.4.1 Attribute collection of individual identity

The CA SHALL document and publish the methods it uses to collect Individual identity attributes.

1.	**From a physical identity document** 

If physical identity documents are used as evidence, the CA or RA SHALL accept only government-issued passports or identity cards, and other official identity documents of comparable reliability (such as drivers license or military ID). 

The physical identity document used as evidence SHALL contain a face photo and/or other information that can be compared with the Applicant's physical appearance.

The CA SHALL document and publish information describing the physical or digital identity documents or document types it accepts.

2.	**From a digital identity document** 

If digital identity documents (such as passports or national ID cards including a chip bearing digitally signed information about the holder) are used as evidence, the CA or RA SHALL only accept eMRTD digital identity documents according to ICAO 9303 part 10.

This method does not include "eID" as described in Regulation (EU) 910/2014.

3. **Using electronic identification schemes (eID)**
   
If an eID is used as evidence, the CA or RA SHALL only accept “notified” eID schemes according to Article 9 of the [eIDAS Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2014.257.01.0073.01.ENG) and the eID shall conform to eIDAS LoA “Substantial” or “High”.

The CA SHALL document and publish information describing the eID and associated eID attributes it accepts.

4.	**From a certificate supporting a digital signature applied by the Applicant** 

If a digital signature is to be used as evidence, the CA or RA SHALL have the Applicant digitally sign the Certificate Request using a valid personal Certificate that was issued under an Approved Framework described in this section. 

Identity attributes are evidenced by the signing Certificate, not by the content of the signed document. The CA or RA SHALL only rely upon the signing Certificate as evidence for identity attributes if the digital signature is valid in accordance with the requirements of the relevant Approved Framework.

The CA SHOULD consider requirements to avoid issuance of consecutive Certificates that are issued based on a preceding Certificate, where the original verification of the Subject's identity may have been conducted in the distant past.

  a. Approved Frameworks

  * To be added by subsequent ballot.

  b. Criteria to propose additional frameworks

  The CA/Browser Forum S/MIME Certificate Working Group may consider additional trust service frameworks that provide an equivalent level of security and validation compared to these Requirements. Proposals that evaluate the additional framework against the following criteria MAY be submitted to the questions@cabforum.org mailing list:

  * Legal context: the framework SHALL be subject to regulatory provisions, which describe the requirements imposed on the Certificate issuer/trust service provider, the legal effects of the trust services, and the corresponding Certificate levels;
  * Identity validation: the approved Certificate levels must provide a level of assurance equivalent to that of the identity validation methods described in these Requirements; 
  * Supervision and auditing systems: the framework SHALL include appropriate rules providing for:
    * supervision to ensure that trust service providers meet regulatory-imposed provisions;
    * requirements imposed on auditing bodies when conducting audits; and
    * supervision of the auditing bodies.
  * Best practices and transparency: the requirements of the trust service framework and evidence of supervision of the approved trust service providers SHALL be publicly available. The trust service framework shall require trust service providers to disclose their practices in a publicly available CP and/or CPS.

5.	**From Enterprise RA records** 

In the case of `Sponsor-validated` Certificates approved by an Enterprise RA, records maintained by the Enterprise RA SHALL be accepted as evidence of Individual identity. 

The Enterprise RA SHALL maintain records to satisfy the requirements of [Section 1.3.2](#132-registration-authorities) and [Section 8.8](#88-review-of-delegated-parties).

6. **Affiliation from company attestation**

In the case of `Sponsor-validated` Certificates not approved by an Enterprise RA, the CA or RA MAY verify the authority or affiliation of an Individual to represent an Organization to be included in the `subject:organizationName` of the Certificate using an Attestation provided by the Organization and verified in accordance with [Section 3.2.8](#328-reliability-of-verification-sources). 

The CA or RA SHALL still verify the identity of the Individual in accordance with [Section 3.2.4](#324-authentication-of-individual-identity) and the Organization in accordance with [Section 3.2.3](#323-authentication-of-organization-identity).

7. **From a general attestation** 

Evidence for Individual identity attributes MAY be gathered using an Attestation from a qualified legal practitioner or notary in the Applicant's jurisdiction. 

8. **From authorized reference sources as supplementary evidence** 
   
Evidence for Individual identity attributes SHALL use at least one of the following sources for authoritative evidence:  a physical or digital identity document, digital signature supported by certificate, Enterprise RA records, or suitable Attestation.

The CA or RA MAY additionally gather and verify supplementary evidence using authorized sources such as additional official documents, government or regulatory registers, or national population registers.

Examples of this method include:

* If the Subject presents an ID featuring an Applicant name that has subsequently been changed, the evidence MAY be complemented by inspection of an official document such as a marriage certificate or court order documenting the change.
* If a professional Title of a regulated profession in the`subject:country`, or a corporate Title linked to the `subject:organizationName`, is to be used it SHALL be verified against supporting documentation, a Reliable Data Source, or Attestation.
* In cases where the "role" LEI is included in an extension of a `Sponsor-validated` Certificate, the CA SHALL verify that the LEI is assigned to the Individual and the `subject:organizationName` in the Certificate Subject.
* The CA MAY verify the address (but not the identity) of the Applicant using a utility bill, bank statement, credit card statement, government-issued tax document, or other form of identification that the CA determines to be reliable.

The CA SHALL internally document the accepted reference sources, including a description of the documents or Attestations accepted as supplementary evidence.

#### 3.2.4.2 Validation of individual identity

The CA or RA SHALL validate all identity attributes of the Individual to be included in the Certificate.

If the evidence has an explicit validity period, the CA SHALL verify that the time of the identity validation is within this validity period. In context this can include the `notBefore` and `notAfter` fields of a digital signature Certificate or the date of expiry of an identity document.

The CA or RA MAY reuse existing evidence to validate Individual identity subject to the age restrictions in [Section 4.2.1](#421-performing-identification-and-authentication-functions).

1.	**Validation of a physical identity document** 

The physical identity document SHALL be presented in its original form. The CA SHALL employ procedures to ensure the evidence presented by the Applicant is a genuine identity document that is not counterfeited or falsified/modified.

The CA or RA MAY use manual (in person) or remote procedures. A remote process SHALL ensure that the Applicant has the document in hand and presents the document in real-time in front of a camera.

The CA or RA registration agent SHALL make a visual comparison of the physical appearance of the Applicant and the face photo and/or other information on the physical identity document.

The CA or RA registration agent SHALL have access to authoritative sources of information on document appearance and validation for forms of identity document accepted by the CA.  

The CA or RA SHALL retain information sufficient to evidence the fulfillment of the identity validation process and the verified attributes. In addition to identity attributes, the CA or RA SHALL record the following information: issuer, validity period, and the document's unique identification number.

Automated and manual processes MAY be used in combination, (for example the CA or RA may deploy automated tools to support the work of a registration agent, or an automated process that falls back to a registration agent if the process yields an uncertain result).

2.	**Validation of a digital identity document**

The CA or RA SHALL only accept digital identity documents if the issuer's digital signature on the document is successfully validated according to ICAO 9303 part 11.

The CA or RA SHALL record information obtained from the digital identity document to evidence the identity proofing process. In addition to identity attributes and face photo, the following information SHALL be recorded: issuer, validity period, and the document's unique identification number.

The CA or RA registration agent SHALL make a visual comparison of the physical appearance of the Applicant and the face photo and/or other information on the digital identity document.

Automated and manual processes MAY be used in combination, (for example using automated tools to support the work of a registration agent, or an automated process that falls back to a registration agent if the process yields an uncertain result).

3. **Validation of eID**
   
If authentication using an eID is used as evidence, the CA or RA SHALL confirm that the eID scheme is suitable (i.e., that the eID is accessible via a "notified" eIDAS-Node), and that the individual eID is valid (i.e., not expired, suspended, or revoked).  

The authentication using the eID SHALL be created as part of the identity validation process, and evidence of the validation with the eID's Identity Provider (IdP) SHALL be retained by the CA or RA.

4.	**Validation of digital signature with certificate** 

If a digital signature with Certificate is used as evidence, the signature SHALL be created as part of the identity validation process.

The CA or RA SHALL validate the digital signature and SHALL only use the signing Certificate as evidence for identity attributes if the signature is valid.

If required identity attributes to be collected are not present in the Certificate, the CA or RA SHALL collect these attributes from other sources and validate them accordingly.

5.	**Validation of an Attestation**

If an Attestation is used as evidence for the validation of Individual identity attributes, then the reliability of the Attestation SHALL be verified according to [Section 3.2.8](#328-reliability-of-verification-sources).

6. **Validation using an Enterprise RA record**

An Enterprise RA issuing a Sponsor-validated Certificate SHALL validate all identity attributes of an Individual to be included in the Certificate. The Enterprise RA MAY rely upon existing internal records to validate Individual identity.

### 3.2.5 Validation of authority

If the Applicant for a Certificate containing Subject Identity Information is an organization, the CA SHALL use a Reliable Method of Communication to verify the authenticity of the Applicant Representative's certificate request.

The CA MAY use the sources listed in [Section 3.2.2.1](#3221-identity) to verify the Reliable Method of Communication. Provided that the CA uses a Reliable Method of Communication, the CA MAY establish the authenticity of the certificate request directly with the Applicant Representative or with an authoritative source within the Applicant's organization, such as the Applicant's main business offices, corporate offices, human resource offices, information technology offices, or other department that the CA deems appropriate.

In addition, the CA SHALL establish a process that allows an Applicant to specify the individuals who may request Certificates. If an Applicant specifies, in writing, the individuals who may request a Certificate, then the CA SHALL NOT accept any certificate requests that are outside this specification. The CA SHALL provide an Applicant with a list of its authorized certificate requesters upon the Applicant's verified written request.

### 3.2.5 Non-verified subscriber information

Subscriber information that has not been verified in accordance with these Requirements SHALL NOT be included in Publicly-Trusted S/MIME Certificates.

### 3.2.6 Criteria for Interoperation or Certification

The CA SHALL disclose all Cross-Certified Subordinate CA Certificates that identify the CA as the Subject, provided that the CA arranged for or accepted the establishment of the trust relationship (i.e. the Cross-Certified Subordinate CA Certificate at issue).

### 3.2.6 Validation of authority

Before commencing to issue `Organization-validated` and `Sponsor-validated` Certificates for an Applicant, the CA or RA SHALL use a Reliable Method of Communication to verify the authority and approval of an Applicant Representative to perform one or more of the following:

*  to act as an Enterprise RA;
*  to request issuance or revocation of Certificates; or 
*  to assign responsibilities to others to act in these roles. 

The CA or RA MAY establish a process that allows an Applicant to specify the individuals who may act as Applicant Representatives on an ongoing basis. The CA SHALL provide an Applicant with a list of its authorized Applicant Representatives upon the Applicant's verified written request.

The CA or RA MAY use the sources listed in [Section 3.2.3.2.1](#3231-attribute-collection-of-organization-identity) to verify the Reliable Method of Communication. Provided that the CA or RA uses a Reliable Method of Communication, the CA or RA MAY establish the authenticity of the Certificate Request directly with the Applicant Representative or with an authoritative source within the Applicant's organization, such as the Applicant's main business offices, corporate offices, human resource offices, information technology offices, or other department that the CA or RA deems appropriate. 

### 3.2.7 Criteria for interoperation

The CA SHALL disclose all Cross Certificates that identify the CA as the Subject, provided that the CA arranged for or accepted the establishment of the trust relationship (i.e., the Cross Certificate at issue).

### 3.2.8 Reliability of verification sources

Before relying on a source of verification data to validate Certificate Requests, the CA SHALL verify its suitability as a Reliable Data Source. Enterprise RA records are a Reliable Data Source for Individual Subject attributes included in Sponsor-validated Certificates issued to the Enterprise RA’s Organisation.

The CA or RA MAY rely upon a letter attesting that Subject Information or other fact is correct. The CA or RA SHALL verify that the letter was written by an accountant, lawyer, government official, or other reliable third party in the Applicant’s jurisdiction customarily relied upon for such information. 

An Attestation SHALL include a copy of documentation supporting the fact to be attested. The CA or RA SHALL use a Reliable Method of Communication to contact the sender and to confirm the Attestation is authentic.

## 3.3 Identification and authentication for re-key requests

### 3.3.1 Identification and authentication for routine re-key

### 3.3.2 Identification and authentication for re-key after revocation

## 3.4 Identification and authentication for revocation request

# 4. CERTIFICATE LIFE-CYCLE OPERATIONAL REQUIREMENTS

## 4.1 Certificate Application

### 4.1.1 Who can submit a certificate application


### 4.1.2 Enrollment process and responsibilities

Prior to the issuance of a Certificate, the CA SHALL obtain the following documentation from the Applicant:

1. A certificate request, which may be electronic; and
2. An executed Subscriber Agreement or Terms of Use, which may be electronic.

The CA SHOULD obtain any additional documentation the CA determines necessary to meet these Requirements.

Prior to the issuance of a Certificate, the CA SHALL obtain from the Applicant a certificate request in a form prescribed by the CA and that complies with these Requirements. One certificate request MAY suffice for multiple Certificates to be issued to the same Applicant, subject to the aging and updating requirement in [Section 4.2.1](#421-performing-identification-and-authentication-functions), provided that each Certificate is supported by a valid, current certificate request signed by the appropriate Applicant Representative on behalf of the Applicant. The certificate request MAY be made, submitted and/or signed electronically.

The certificate request MUST contain a request from, or on behalf of, the Applicant for the issuance of a Certificate, and a certification by, or on behalf of, the Applicant that all of the information contained therein is correct.

### 4.1.2 Enrollment process and responsibilities

Prior to the issuance of a Certificate, the CA SHALL obtain the following documentation from the Applicant:

1. A Certificate Request; and
2. An executed Subscriber Agreement and/or Terms of Use.

The Certificate Request and Subscriber Agreement or Terms of Use SHALL be in a form prescribed by the CA and SHALL comply with these Requirements including [Section 9.6.3](#963-subscriber-representations-and-warranties). The CA SHOULD obtain any additional documentation the CA determines necessary to fulfill these Requirements.

The Certificate Request SHALL contain a request from, or on behalf of, the Applicant for the issuance of a Certificate, and a certification by, or on behalf of, the Applicant that all of the information contained therein is correct.

One Certificate Request MAY suffice for multiple Certificates to be issued to the same Applicant, subject to the validation reuse periods described in [Section 4.2.1](#421-performing-identification-and-authentication-functions), provided that each Certificate is supported by a valid, current Certificate Request signed by the appropriate Applicant Representative on behalf of the Applicant. 

A CA may rely on a previously verified Certificate Request to issue a replacement Certificate if:

1. The previous Certificate being referenced was not revoked;
2. The expiration date of the replacement Certificate is the same as the previous Certificate being referenced; and
3. The Subject Information of the Certificate is the same as the previous Certificate being referenced.

## 4.2 Certificate application processing

### 4.2.1 Performing identification and authentication functions

The certificate request MAY include all factual information about the Applicant to be included in the Certificate, and such additional information as is necessary for the CA to obtain from the Applicant in order to comply with these Requirements and the CA's Certificate Policy and/or Certification Practice Statement. In cases where the certificate request does not contain all the necessary information about the Applicant, the CA SHALL obtain the remaining information from the Applicant or, having obtained it from a reliable, independent, third-party data source, confirm it with the Applicant. The CA SHALL establish and follow a documented procedure for verifying all data requested for inclusion in the Certificate by the Applicant.

Applicant information MUST include, but not be limited to, at least one Fully-Qualified Domain Name or IP address to be included in the Certificate's `subjectAltName` extension.

[Section 6.3.2](#632-certificate-operational-periods-and-key-pair-usage-periods) limits the validity period of Subscriber Certificates. The CA MAY use the documents and data provided in [Section 3.2](#32-initial-identity-validation) to verify certificate information, or may reuse previous validations themselves, provided that the CA obtained the data or document from a source specified under [Section 3.2](#32-initial-identity-validation) or completed the validation itself no more than 825 days prior to issuing the Certificate. For validation of Domain Names and IP Addresses according to Section 3.2.2.4 and 3.2.2.5, any reused data, document, or completed validation MUST be obtained no more than 398 days prior to issuing the Certificate.

In no case may a prior validation be reused if any data or document used in the prior validation was obtained more than the maximum time permitted for reuse of the data or document prior to issuing the Certificate.

After the change to any validation method specified in the Baseline Requirements or EV Guidelines, a CA may continue to reuse validation data or documents collected prior to the change, or the validation itself, for the period stated in this BR 4.2.1 unless otherwise specifically provided in a ballot.

The CA SHALL develop, maintain, and implement documented procedures that identify and require additional verification activity for High Risk Certificate Requests prior to the Certificate's approval, as reasonably necessary to ensure that such requests are properly verified under these Requirements.

If a Delegated Third Party fulfills any of the CA's obligations under this section , the CA SHALL verify that the process used by the Delegated Third Party to identify and further verify High Risk Certificate Requests provides at least the same level of assurance as the CA's own processes.

### 4.2.1 Performing identification and authentication functions

Applicant information SHALL include, but not be limited to, at least one Mailbox Field to be included in the Certificate's `subjectAltName` extension.

[Section 6.3.2](#632-certificate-operational-periods-and-key-pair-usage-periods) limits the validity period of Subscriber Certificates. 

The CA MAY reuse completed validations and/or supporting evidence performed in accordance with [Section 3.2](#32-initial-identity-validation) within the following limits:

1. **Validation of mailbox authorization or control**: Completed validation of the control of a mail server in accordance with [Section 3.2.2.1](#3221-validating-authority-over-mailbox-via-domain) or [Section 3.2.2.3](#3223-validating-applicant-as-operator-of-associated-mail-servers) SHALL be obtained no more than 398 days prior to issuing the Certificate. 
   
      In the event of changes to the TLS Baseline Requirements methods specified in [Section 3.2.2.1](#3221-validating-authority-over-mailbox-via-domain), a CA MAY continue to reuse completed validations and/or supporting evidence for the period stated in this section.

      Completed validation of control of a mailbox in accordance with [Section 3.2.2.2](#3222-validating-control-over-mailbox-via-email) SHALL be obtained no more than 30 days prior to issuing the Certificate.

2. **Authentication of organization identity**: Completed validation of organization identity in accordance with [Section 3.2.3](#323-authentication-of-organization-identity) SHALL be obtained no more than 825 days prior to issuing the Certificate. 
 
      Validation of authority in accordance with [Section 3.2.6](#326-validation-of-authority) SHALL be obtained no more than 825 days prior to issuing the Certificate, unless a contract between the CA and the Applicant specifies a different term. For example, the contract MAY include the perpetual assignment of roles until revoked by the Applicant or CA, or until the contract expires or is terminated.

3. **Authentication of individual identity**: Completed validation of Individual identity in accordance with [Section 3.2.4](#324-authentication-of-individual-identity) SHALL be obtained no more than 825 days prior to issuing the Certificate. 

A prior validation SHALL NOT be reused if any data or document used in the prior validation was obtained more than the maximum time permitted for reuse of the data or document prior to issuing the Certificate.

### 4.2.2 Approval or rejection of certificate applications

CAs SHALL NOT issue certificates containing Internal Names or Reserved IP Addresses, as such names cannot be validated according to [Section 3.2.2.4](#3224-validation-of-domain-authorization-or-control) or [Section 3.2.2.5](#3225-authentication-for-an-ip-address).

### 4.2.2 Approval or rejection of certificate applications


### 4.2.3 Time to process certificate applications


## 4.3 Certificate issuance

### 4.3.1 CA actions during certificate issuance

Certificate issuance by the Root CA SHALL require an individual authorized by the CA (i.e. the CA system operator, system officer, or PKI administrator) to deliberately issue a direct command in order for the Root CA to perform a certificate signing operation.

### 4.3.1 CA actions during certificate issuance

Certificate issuance by the Root CA SHALL require at least two individuals authorized by the CA (i.e., the CA system operator, system officer, or PKI administrator) one of whom deliberately issues a direct command in order for the Root CA to perform a Certificate signing operation.

### 4.3.2 Notification to subscriber by the CA of issuance of certificate


## 4.4 Certificate acceptance

### 4.4.1 Conduct constituting certificate acceptance


### 4.4.2 Publication of the certificate by the CA


### 4.4.3 Notification of certificate issuance by the CA to other entities


## 4.5 Key pair and certificate usage

### 4.5.1 Subscriber private key and certificate usage

See [Section 9.6.3](#963-subscriber-representations-and-warranties), provisions 2. and 4.

### 4.5.2 Relying party public key and certificate usage


## 4.6 Certificate renewal

### 4.6.1 Circumstance for certificate renewal


### 4.6.2 Who may request renewal


### 4.6.3 Processing certificate renewal requests


### 4.6.4 Notification of new certificate issuance to subscriber


### 4.6.5 Conduct constituting acceptance of a renewal certificate


### 4.6.6 Publication of the renewal certificate by the CA


### 4.6.7 Notification of certificate issuance by the CA to other entities


## 4.7 Certificate re-key

### 4.7.1 Circumstance for certificate re-key


### 4.7.2 Who may request certification of a new public key


### 4.7.3 Processing certificate re-keying requests


### 4.7.4 Notification of new certificate issuance to subscriber


### 4.7.5 Conduct constituting acceptance of a re-keyed certificate


### 4.7.6 Publication of the re-keyed certificate by the CA


### 4.7.7 Notification of certificate issuance by the CA to other entities


## 4.8 Certificate modification

### 4.8.1 Circumstance for certificate modification


### 4.8.2 Who may request certificate modification


### 4.8.3 Processing certificate modification requests


### 4.8.4 Notification of new certificate issuance to subscriber


### 4.8.5 Conduct constituting acceptance of modified certificate


### 4.8.6 Publication of the modified certificate by the CA


### 4.8.7 Notification of certificate issuance by the CA to other entities


## 4.9 Certificate revocation and suspension

### 4.9.1 Circumstances for revocation

#### 4.9.1.1 Reasons for Revoking a Subscriber Certificate

The CA MAY support revocation of Short-lived Subscriber Certificates.

With the exception of Short-lived Subscriber Certificates, the CA SHALL revoke a Certificate within 24 hours and use the corresponding CRLReason (see Section 7.2.2) if one or more of the following occurs:

1. The Subscriber requests in writing, without specifying a CRLreason, that the CA revoke the Certificate (CRLReason "unspecified (0)" which results in no reasonCode extension being provided in the CRL);
2. The Subscriber notifies the CA that the original certificate request was not authorized and does not retroactively grant authorization (CRLReason #9, privilegeWithdrawn);
3. The CA obtains evidence that the Subscriber's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise (CRLReason #1, keyCompromise);
4. The CA is made aware of a demonstrated or proven method that can easily compute the Subscriber's Private Key based on the Public Key in the Certificate (such as a Debian weak key, see <https://wiki.debian.org/SSLkeys>) (CRLReason #1, keyCompromise);
5. The CA obtains evidence that the validation of domain authorization or control for any Fully-Qualified Domain Name or IP address in the Certificate should not be relied upon (CRLReason #4, superseded).

With the exception of Short-lived Subscriber Certificates, the CA SHOULD revoke a certificate within 24 hours and MUST revoke a Certificate within 5 days and use the corresponding CRLReason (see Section 7.2.2) if one or more of the following occurs:

6. The Certificate no longer complies with the requirements of [Section 6.1.5](#615-key-sizes) and [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking) (CRLReason #4, superseded);
7. The CA obtains evidence that the Certificate was misused (CRLReason #9, privilegeWithdrawn);
8. The CA is made aware that a Subscriber has violated one or more of its material obligations under the Subscriber Agreement or Terms of Use (CRLReason #9, privilegeWithdrawn);
9. The CA is made aware of any circumstance indicating that use of a Fully-Qualified Domain Name or IP address in the Certificate is no longer legally permitted (e.g. a court or arbitrator has revoked a Domain Name Registrant's right to use the Domain Name, a relevant licensing or services agreement between the Domain Name Registrant and the Applicant has terminated, or the Domain Name Registrant has failed to renew the Domain Name) (CRLReason #5, cessationOfOperation);
10. The CA is made aware that a Wildcard Certificate has been used to authenticate a fraudulently misleading subordinate Fully-Qualified Domain Name (CRLReason #9, privilegeWithdrawn);
11. The CA is made aware of a material change in the information contained in the Certificate (CRLReason #9, privilegeWithdrawn);
12. The CA is made aware that the Certificate was not issued in accordance with these Requirements or the CA's Certificate Policy or Certification Practice Statement (CRLReason #4, superseded);
13. The CA determines or is made aware that any of the information appearing in the Certificate is inaccurate (CRLReason #9, privilegeWithdrawn);
14. The CA's right to issue Certificates under these Requirements expires or is revoked or terminated, unless the CA has made arrangements to continue maintaining the CRL/OCSP Repository (CRLReason "unspecified (0)" which results in no reasonCode extension being provided in the CRL);
15. Revocation is required by the CA's Certificate Policy and/or Certification Practice Statement for a reason that is not otherwise required to be specified by this section 4.9.1.1 (CRLReason "unspecified (0)" which results in no reasonCode extension being provided in the CRL); or
16. The CA is made aware of a demonstrated or proven method that exposes the Subscriber's Private Key to compromise or if there is clear evidence that the specific method used to generate the Private Key was flawed (CRLReason #1, keyCompromise).

#### 4.9.1.1 Reasons for revoking a subscriber certificate

The CA SHALL revoke a Certificate within 24 hours if one or more of the following occurs:

1. The Subscriber requests in writing that the CA revoke the Certificate;
2. The Subscriber notifies the CA that the original Certificate Request was not authorized and does not retroactively grant authorization;
3. The CA obtains evidence that the Subscriber's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise;
4. The CA is made aware of a demonstrated or proven method that can easily compute the Subscriber's Private Key based on the Public Key in the Certificate (such as a Debian weak key, see <https://wiki.debian.org/SSLkeys>);
5. The CA obtains evidence that the validation of domain authorization or mailbox control for any Mailbox Address in the Certificate should not be relied upon.

The CA SHOULD revoke a Certificate within 24 hours and SHALL revoke a Certificate within 5 days if one or more of the following occurs:

6. The Certificate no longer complies with the requirements of [Section 6.1.5](#615-key-sizes) and [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
7. The CA obtains evidence that the Certificate was misused;
8. The CA is made aware that a Subscriber has violated one or more of its material obligations under the Subscriber Agreement or Terms of Use;
9. The CA is made aware of any circumstance indicating that use of an email address or Fully-Qualified Domain Name in the Certificate is no longer legally permitted (e.g., a court or arbitrator has revoked the right to use an email address or Domain Name, a relevant licensing or services agreement between the Subscriber has terminated, or the account holder has failed to maintain the active status of the email address or Domain Name);
10. The CA is made aware of a material change in the information contained in the Certificate;
11. The CA is made aware that the Certificate was not issued in accordance with these Requirements or the CA's CP and/or CPS;
12. The CA determines or is made aware that any of the information appearing in the Certificate is inaccurate;
13. The CA's right to issue Certificates under these Requirements expires or is revoked or terminated, unless the CA has made arrangements to continue maintaining the CRL/OCSP Repository;
14. Revocation is required by the CA's CP and/or CPS; or
15. The CA is made aware of a demonstrated or proven method that exposes the Subscriber's Private Key to compromise or if there is clear evidence that the specific method used to generate the Private Key was flawed.

#### 4.9.1.2 Reasons for Revoking a Subordinate CA Certificate

The Issuing CA SHALL revoke a Subordinate CA Certificate within seven (7) days if one or more of the following occurs:

1. The Subordinate CA requests revocation in writing;
2. The Subordinate CA notifies the Issuing CA that the original certificate request was not authorized and does not retroactively grant authorization;
3. The Issuing CA obtains evidence that the Subordinate CA's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise or no longer complies with the requirements of [Section 6.1.5](#615-key-sizes) and [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
4. The Issuing CA obtains evidence that the Certificate was misused;
5. The Issuing CA is made aware that the Certificate was not issued in accordance with or that Subordinate CA has not complied with this document or the applicable Certificate Policy or Certification Practice Statement;
6. The Issuing CA determines that any of the information appearing in the Certificate is inaccurate or misleading;
7. The Issuing CA or Subordinate CA ceases operations for any reason and has not made arrangements for another CA to provide revocation support for the Certificate;
8. The Issuing CA's or Subordinate CA's right to issue Certificates under these Requirements expires or is revoked or terminated, unless the Issuing CA has made arrangements to continue maintaining the CRL/OCSP Repository; or
9. Revocation is required by the Issuing CA's Certificate Policy and/or Certification Practice Statement.

#### 4.9.1.2 Reasons for revoking a subordinate CA certificate

The Issuing CA SHALL revoke a Subordinate CA Certificate within seven (7) days if one or more of the following occurs:

1. The Subordinate CA requests revocation in writing;
2. The Subordinate CA notifies the Issuing CA that the original Certificate Request was not authorized and does not retroactively grant authorization;
3. The Issuing CA obtains evidence that the Subordinate CA's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise or no longer complies with the requirements of [Section 6.1.5](#615-key-sizes) and [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
4. The Issuing CA obtains evidence that the Certificate was misused;
5. The Issuing CA is made aware that the Certificate was not issued in accordance with or that Subordinate CA has not complied with this document or the applicable CP and/or CPS;
6. The Issuing CA determines that any of the information appearing in the Certificate is inaccurate or misleading;
7. The Issuing CA or Subordinate CA ceases operations for any reason and has not made arrangements for another CA to provide revocation support for the Certificate;
8. The Issuing CA's or Subordinate CA's right to issue Certificates under these Requirements expires or is revoked or terminated, unless the Issuing CA has made arrangements to continue maintaining the CRL/OCSP Repository; or
9. Revocation is required by the Issuing CA's CP and/or CPS.

### 4.9.2 Who can request revocation

The Subscriber, RA, or Issuing CA can initiate revocation. Additionally, Subscribers, Relying Parties, Application Software Suppliers, and other third parties may submit Certificate Problem Reports informing the issuing CA of reasonable cause to revoke the certificate.

### 4.9.2 Who can request revocation

The Subscriber, RA, or Issuing CA can initiate revocation. Additionally, Subscribers, Relying Parties, Application Software Suppliers, and other third parties MAY submit Certificate Problem Reports informing the Issuing CA of reasonable cause to revoke a Certificate.

### 4.9.3 Procedure for revocation request

The CA SHALL provide a process for Subscribers to request revocation of their own Certificates. The process MUST be described in the CA's Certificate Policy or Certification Practice Statement. The CA SHALL maintain a continuous 24x7 ability to accept and respond to revocation requests and Certificate Problem Reports.

The CA SHALL provide Subscribers, Relying Parties, Application Software Suppliers, and other third parties with clear instructions for reporting suspected Private Key Compromise, Certificate misuse, or other types of fraud, compromise, misuse, inappropriate conduct, or any other matter related to Certificates. The CA SHALL publicly disclose the instructions through a readily accessible online means and in Section 1.5.2 of their CPS.

### 4.9.3 Procedure for revocation request

The CA SHALL provide a process for Subscribers to request revocation of their own Certificates. The process SHALL be described in the CA's CP and/or CPS. The CA SHALL maintain a continuous 24x7 ability to accept and respond to revocation requests and Certificate Problem Reports.

The CA SHALL provide clear instructions for reporting suspected Private Key Compromise, Certificate misuse, or other types of fraud, compromise, misuse, inappropriate conduct, or any other matter related to Certificates. The CA SHALL publicly disclose the instructions through a readily accessible online means and in Section 1.5.2 of their CPS.

### 4.9.4 Revocation request grace period


### 4.9.5 Time within which CA must process the revocation request

Within 24 hours after receiving a Certificate Problem Report, the CA SHALL investigate the facts and circumstances related to a Certificate Problem Report and provide a preliminary report on its findings to both the Subscriber and the entity who filed the Certificate Problem Report.
After reviewing the facts and circumstances, the CA SHALL work with the Subscriber and any entity reporting the Certificate Problem Report or other revocation-related notice to establish whether or not the certificate will be revoked, and if so, a date which the CA will revoke the certificate. The period from receipt of the Certificate Problem Report or revocation-related notice to published revocation MUST NOT exceed the time frame set forth in [Section 4.9.1.1](#4911-reasons-for-revoking-a-subscriber-certificate). The date selected by the CA SHOULD consider the following criteria:

1. The nature of the alleged problem (scope, context, severity, magnitude, risk of harm);
2. The consequences of revocation (direct and collateral impacts to Subscribers and Relying Parties);
3. The number of Certificate Problem Reports received about a particular Certificate or Subscriber;
4. The entity making the complaint (for example, a complaint from a law enforcement official that a Web site is engaged in illegal activities should carry more weight than a complaint from a consumer alleging that they didn't receive the goods they ordered); and
5. Relevant legislation.

### 4.9.5 Time within which CA must process the revocation request

Within 24 hours after receiving a Certificate Problem Report, the CA SHALL investigate the facts and circumstances related to a Certificate Problem Report and provide a preliminary report on its findings to both the Subscriber and the entity who filed the Certificate Problem Report.

After reviewing the facts and circumstances, the CA SHALL work with the Subscriber and any entity reporting the Certificate Problem Report or other revocation-related notice to establish whether or not the Certificate will be revoked, and if so, a date on which the CA will revoke the Certificate. The period from receipt of the Certificate Problem Report or revocation-related notice to published revocation SHALL NOT exceed the time frame set forth in [Section 4.9.1.1](#4911-reasons-for-revoking-a-subscriber-certificate). The date selected by the CA SHOULD consider the following criteria:

1. The nature of the alleged problem (scope, context, severity, magnitude, risk of harm);
2. The consequences of revocation (direct and collateral impacts to Subscribers and Relying Parties);
3. The number of Certificate Problem Reports received about a particular Certificate or Subscriber;
4. The entity making the complaint (for example, a complaint from a law enforcement official should be addressed with higher priority); and
5. Relevant legislation.
   
### 4.9.6 Revocation checking requirement for relying parties


**Note**: Following certificate issuance, a certificate may be revoked for reasons stated in [Section 4.9](#49-certificate-revocation-and-suspension). Therefore, relying parties should check the revocation status of all certificates that contain a CDP or OCSP pointer.

### 4.9.7 CRL issuance frequency

CRLs must be available via a publicly-accessible HTTP URL (i.e., "published").

Within twenty-four (24) hours of issuing its first Certificate, the CA MUST generate and publish either:
- a full and complete CRL; OR
- partitioned (i.e., "sharded") CRLs that, when aggregated, represent the equivalent of a full and complete CRL.

CAs issuing Subscriber Certificates:  
1. MUST update and publish a new CRL at least every: 
     - seven (7) days if all Certificates include an Authority Information Access extension with an id-ad-ocsp accessMethod (“AIA OCSP pointer”); or
     - four (4) days in all other cases; 
2. MUST update and publish a new CRL within twenty-four (24) hours after recording a Certificate as revoked.

CAs issuing CA Certificates:  
1. MUST update and publish a new CRL at least every twelve (12) months;
2. MUST update and publish a new CRL within twenty-four (24) hours after recording a Certificate as revoked.

CAs MUST continue issuing CRLs until one of the following is true:
- all Subordinate CA Certificates containing the same Subject Public Key are expired or revoked; OR
- the corresponding Subordinate CA Private Key is destroyed.


### 4.9.7 CRL issuance frequency

For the status of Subscriber Certificates: the CA SHALL update and reissue CRLs at least once every seven days, and the value of the `nextUpdate` field SHALL NOT be more than ten days beyond the value of the `thisUpdate` field.

For the status of Subordinate CA Certificates: the CA SHALL update and reissue CRLs at least:

1. once every twelve months; and
2. within 24 hours after revoking a Subordinate CA Certificate.

The value of the `nextUpdate` field SHALL NOT be more than twelve months beyond the value of the `thisUpdate` field.

### 4.9.8 Maximum latency for CRLs (if applicable)


### 4.9.8 Maximum latency for CRLs


### 4.9.9 On-line revocation/status checking availability

The following SHALL apply for communicating the status of Certificates which include an Authority Information Access extension with an id-ad-ocsp accessMethod.

OCSP responses MUST conform to RFC6960 and/or RFC5019. OCSP responses MUST either:

1. Be signed by the CA that issued the Certificates whose revocation status is being checked, or
2. Be signed by an OCSP Responder whose Certificate is signed by the CA that issued the Certificate whose
revocation status is being checked.

In the latter case, the OCSP signing Certificate MUST contain an extension of type `id-pkix-ocsp-nocheck`, as
defined by RFC6960.

### 4.9.9 On-line revocation/status checking availability

When provided, OCSP responses SHALL conform to [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960) and/or [RFC 5019](https://datatracker.ietf.org/doc/html/rfc5019). OCSP responses SHALL either:

1. Be signed by the CA that issued the Certificates whose revocation status is being checked, or
2. Be signed by an OCSP Responder whose Certificate is signed by the CA that issued the Certificate whose revocation status is being checked.
   
In the latter case, the OCSP signing Certificate SHALL contain the ocspSigning EKU (1.3.6.1.5.5.7.3.9) and an extension of type `id-pkix-ocsp-nocheck`, as defined by [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960).

### 4.9.10 On-line revocation checking requirements

The following SHALL apply for communicating the status of Certificates which include an Authority Information Access extension with an id-ad-ocsp accessMethod.

OCSP responders operated by the CA SHALL support the HTTP GET method, as described in RFC 6960 and/or RFC 5019. The CA MAY process the Nonce extension (`1.3.6.1.5.5.7.48.1.2`) in accordance with RFC 8954.

The validity interval of an OCSP response is the difference in time between the `thisUpdate` and `nextUpdate` field, inclusive. For purposes of computing differences, a difference of 3,600 seconds shall be equal to one hour, and a difference of 86,400 seconds shall be equal to one day, ignoring leap-seconds.

For the status of Subscriber Certificates:

1. OCSP responses MUST have a validity interval greater than or equal to eight hours;
2. OCSP responses MUST have a validity interval less than or equal to ten days;
3. For OCSP responses with validity intervals less than sixteen hours, then the CA SHALL update the information provided via an Online Certificate Status Protocol prior to one-half of the validity period before the nextUpdate.
4. For OCSP responses with validity intervals greater than or equal to sixteen hours, then the CA SHALL update the information provided via an Online Certificate Status Protocol at least eight hours prior to the nextUpdate, and no later than four days after the thisUpdate.

For the status of Subordinate CA Certificates:

* The CA SHALL update information provided via an Online Certificate Status Protocol

  i. at least every twelve months; and
  ii. within 24 hours after revoking a Subordinate CA Certificate.

If the OCSP responder receives a request for the status of a certificate serial number that is "unused", then the responder SHOULD NOT respond with a "good" status. If the OCSP responder is for a CA that is not Technically Constrained in line with [Section 7.1.2.3](#7123-technically-constrained-non-tls-subordinate-ca-certificate-profile) or [Section 7.1.2.5](#7125-technically-constrained-tls-subordinate-ca-certificate-profile), the responder MUST NOT respond with a "good" status for such requests.

The CA SHOULD monitor the OCSP responder for requests for "unused" serial numbers as part of its security response procedures.

The OCSP responder MAY provide definitive responses about "reserved" certificate serial numbers, as if there was a corresponding Certificate that matches the Precertificate [RFC6962].

A certificate serial number within an OCSP request is one of the following three options:

1. "assigned" if a Certificate with that serial number has been issued by the Issuing CA, using any current or previous key associated with that CA subject; or
2. "reserved" if a Precertificate [RFC6962] with that serial number has been issued by
   a. the Issuing CA; or
   b. a Precertificate Signing Certificate, as defined in [Section 7.1.2.4](#7124-technically-constrained-precertificate-signing-ca-certificate-profile), associated with the Issuing CA; or
3. "unused" if neither of the previous conditions are met.

### 4.9.10 On-line revocation checking requirements

OCSP responders operated by the CA SHALL support the HTTP GET method, as described in [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960) and/or [RFC 5019](https://datatracker.ietf.org/doc/html/rfc5019).

The validity interval of an OCSP response is the difference in time between the thisUpdate and nextUpdate field, inclusive. For purposes of computing differences, a difference of 3,600 seconds SHALL be equal to one hour, and a difference of 86,400 seconds SHALL be equal to one day, ignoring leap-seconds.

For the status of Subscriber Certificates:

1. OCSP responses SHALL have a validity interval greater than or equal to eight hours;
2. OCSP responses SHALL have a validity interval less than or equal to ten days;
3. For OCSP responses with validity intervals less than sixteen hours, then the CA SHALL update the information provided via an Online Certificate Status Protocol prior to one-half of the validity period before the nextUpdate; and
4. For OCSP responses with validity intervals greater than or equal to sixteen hours, then the CA SHALL update the information provided via an Online Certificate Status Protocol at least eight hours prior to the nextUpdate, and no later than four days after the thisUpdate.
   
For the status of Subordinate CA Certificates, the CA SHALL update information provided via OCSP:

1. at least every twelve months; and
2. within 24 hours after revoking a Subordinate CA Certificate.

If the OCSP responder receives a request for the status of a Certificate serial number that is "unused", then the responder SHOULD NOT respond with a "good" status. If the OCSP responder is for a CA that is not Technically Constrained in line with [Section 7.1.5](#715-name-constraints), the responder SHALL NOT respond with a "good" status for such requests.

The CA SHOULD monitor the OCSP responder for requests for "unused" serial numbers as part of its security response procedures.

A Certificate serial number within an OCSP request is "assigned" if a Certificate with that serial number has been issued by the Issuing CA, using any current or previous key associated with that CA subject, or "unused" if otherwise.

### 4.9.11 Other forms of revocation advertisements available

No Stipulation.

### 4.9.11 Other forms of revocation advertisements available


### 4.9.12 Special requirements re key compromise

See [Section 4.9.1](#491-circumstances-for-revocation).

### 4.9.13 Circumstances for suspension

The Repository MUST NOT include entries that indicate that a Certificate is suspended.

### 4.9.13 Circumstances for suspension

See [Section 7.2.2](#722-crl-and-crl-entry-extensions) for restrictions on use of suspension. The CA SHALL describe its suspension practices in the CA's CP and/or CPS.

### 4.9.14 Who can request suspension

Not applicable.

### 4.9.14 Who can request suspension


### 4.9.15 Procedure for suspension request

Not applicable.

### 4.9.15 Procedure for suspension request


### 4.9.16 Limits on suspension period

Not applicable.

### 4.9.16 Limits on suspension period


## 4.10 Certificate status services

### 4.10.1 Operational characteristics

Revocation entries on a CRL or OCSP Response MUST NOT be removed until after the Expiry Date of the revoked Certificate.

### 4.10.1 Operational characteristics

Revocation entries on a CRL or OCSP Response SHALL NOT be removed until after the Expiry Date of the revoked Certificate.

### 4.10.2 Service availability

The CA SHALL operate and maintain its CRL and optional OCSP capability with resources sufficient to provide a response time of ten seconds or less under normal operating conditions.

The CA SHALL maintain an online 24x7 Repository that application software can use to automatically check the current status of all unexpired Certificates issued by the CA.

The CA SHALL maintain a continuous 24x7 ability to respond internally to a high-priority Certificate Problem Report, and where appropriate, forward such a complaint to law enforcement authorities, and/or revoke a Certificate that is the subject of such a complaint.

### 4.10.2 Service availability

The CA SHALL operate and maintain its CRL and OCSP capability with resources sufficient to provide a response time of ten seconds or less under normal operating conditions.

The CA SHALL maintain an online 24x7 Repository that application software can use to automatically check the current status of all unexpired Certificates issued by the CA.

The CA SHALL maintain a continuous 24x7 ability to respond internally to a high-priority Certificate Problem Report, and where appropriate, forward such a complaint to law enforcement authorities, and/or revoke a Certificate that is the subject of such a complaint.

### 4.10.3 Optional features


## 4.11 End of subscription


## 4.12 Key escrow and recovery

### 4.12.1 Key escrow and recovery policy and practices


### 4.12.1 Key escrow and recovery policy and practices

The CA MAY escrow the Subscriber’s Private Key as specified in the CA's CP and/or CPS. 

The CA SHALL notify Subscribers when their Private Keys are escrowed. Escrowed Private Keys SHALL be stored in encrypted form. The CA SHALL protect escrowed Private Keys from unauthorized disclosure.

The CA SHALL recover Subscriber Private Keys only under the circumstances permitted within the CA's CP and/or CPS.

### 4.12.2 Session key encapsulation and recovery policy and practices

Not applicable.

### 4.12.2 Session key encapsulation and recovery policy and practices


# 5. MANAGEMENT, OPERATIONAL, AND PHYSICAL CONTROLS

The CA/Browser Forum's Network and Certificate System Security Requirements are incorporated by reference as if fully set forth herein.

The CA SHALL develop, implement, and maintain a comprehensive security program designed to:

1. Protect the confidentiality, integrity, and availability of Certificate Data and Certificate Management Processes;
2. Protect against anticipated threats or hazards to the confidentiality, integrity, and availability of the Certificate Data and Certificate Management Processes;
3. Protect against unauthorized or unlawful access, use, disclosure, alteration, or destruction of any Certificate Data or Certificate Management Processes;
4. Protect against accidental loss or destruction of, or damage to, any Certificate Data or Certificate Management Processes; and
5. Comply with all other security requirements applicable to the CA by law.

The Certificate Management Process MUST include:

1. physical security and environmental controls;
2. system integrity controls, including configuration management, integrity maintenance of trusted code, and malware detection/prevention;
3. network security and firewall management, including port restrictions and IP address filtering;
4. user management, separate trusted-role assignments, education, awareness, and training; and
5. logical access controls, activity logging, and inactivity time-outs to provide individual accountability.

The CA's security program MUST include an annual Risk Assessment that:

1. Identifies foreseeable internal and external threats that could result in unauthorized access, disclosure, misuse, alteration, or destruction of any Certificate Data or Certificate Management Processes;
2. Assesses the likelihood and potential damage of these threats, taking into consideration the sensitivity of the Certificate Data and Certificate Management Processes; and
3. Assesses the sufficiency of the policies, procedures, information systems, technology, and other arrangements that the CA has in place to counter such threats.

Based on the Risk Assessment, the CA SHALL develop, implement, and maintain a security plan consisting of security procedures, measures, and products designed to achieve the objectives set forth above and to manage and control the risks identified during the Risk Assessment, commensurate with the sensitivity of the Certificate Data and Certificate Management Processes. The security plan MUST include administrative, organizational, technical, and physical safeguards appropriate to the sensitivity of the Certificate Data and Certificate Management Processes. The security plan MUST also take into account then-available technology and the cost of implementing the specific measures, and SHALL implement a reasonable level of security appropriate to the harm that might result from a breach of security and the nature of the data to be protected.

# 5. FACILITY, MANAGEMENT, AND OPERATIONAL CONTROLS

The CA SHALL develop, implement, and maintain a comprehensive security program designed to:

1. Protect the confidentiality, integrity, and availability of Certificate Data and Certificate Management Processes;
2. Protect against anticipated threats or hazards to the confidentiality, integrity, and availability of the Certificate Data and Certificate Management Processes;
3. Protect against unauthorized or unlawful access, use, disclosure, alteration, or destruction of any Certificate Data or Certificate Management Processes;
4. Protect against accidental loss or destruction of, or damage to, any Certificate Data or Certificate Management Processes; and
5. Comply with all other security requirements applicable to the CA by law.

The Certificate Management Process SHALL include:

1. physical security and environmental controls;
2. system integrity controls, including configuration management, integrity maintenance of trusted code, and malware detection/prevention;
3. network security and firewall management, including port restrictions and IP address filtering;
4. user management, separate trusted-role assignments, education, awareness, and training; and
5. logical access controls, activity logging, and inactivity time-outs to provide individual accountability.

The CA's security program SHALL include an annual Risk Assessment that:

1. Identifies foreseeable internal and external threats that could result in unauthorized access, disclosure, misuse, alteration, or destruction of any Certificate Data or Certificate Management Processes;
2. Assesses the likelihood and potential damage of these threats, taking into consideration the sensitivity of the Certificate Data and Certificate Management Processes; and
3. Assesses the sufficiency of the policies, procedures, information systems, technology, and other arrangements that the CA has in place to counter such threats.

Based on the Risk Assessment, the CA SHALL develop, implement, and maintain a security plan consisting of security procedures, measures, and products designed to achieve the objectives set forth above and to manage and control the risks identified during the Risk Assessment, commensurate with the sensitivity of the Certificate Data and Certificate Management Processes. The security plan SHALL include administrative, organizational, technical, and physical safeguards appropriate to the sensitivity of the Certificate Data and Certificate Management Processes. The security plan SHALL also take into account then-available technology and the cost of implementing the specific measures, and SHALL implement a reasonable level of security appropriate to the harm that might result from a breach of security and the nature of the data to be protected.

## 5.1 PHYSICAL SECURITY CONTROLS

## 5.1 Physical controls

### 5.1.1 Site location and construction

### 5.1.2 Physical access

### 5.1.3 Power and air conditioning

### 5.1.4 Water exposures

### 5.1.5 Fire prevention and protection

### 5.1.6 Media storage

### 5.1.7 Waste disposal

### 5.1.8 Off-site backup

## 5.2 Procedural controls

### 5.2.1 Trusted roles

### 5.2.2 Number of Individuals Required per Task

The CA Private Key SHALL be backed up, stored, and recovered only by personnel in trusted roles using, at least, dual control in a physically secured environment.

### 5.2.2 Number of persons required per task

The CA Private Key SHALL be backed up, stored, and recovered only by personnel in trusted roles using, at least, dual control in a physically secured environment.

### 5.2.3 Identification and authentication for each role

### 5.2.4 Roles requiring separation of duties

## 5.3 Personnel controls

### 5.3.1 Qualifications, experience, and clearance requirements

Prior to the engagement of any person in the Certificate Management Process, whether as an employee, agent, or an independent contractor of the CA, the CA SHALL verify the identity and trustworthiness of such person.

### 5.3.2 Background check procedures

### 5.3.3 Training Requirements and Procedures

The CA SHALL provide all personnel performing information verification duties with skills-training that covers basic Public Key Infrastructure knowledge, authentication and vetting policies and procedures (including the CA's Certificate Policy and/or Certification Practice Statement), common threats to the information verification process (including phishing and other social engineering tactics), and these Requirements.

The CA SHALL maintain records of such training and ensure that personnel entrusted with Validation Specialist duties maintain a skill level that enables them to perform such duties satisfactorily.

The CA SHALL document that each Validation Specialist possesses the skills required by a task before allowing the Validation Specialist to perform that task.

The CA SHALL require all Validation Specialists to pass an examination provided by the CA on the information verification requirements outlined in these Requirements.

### 5.3.3 Training requirements

The CA SHALL provide all personnel performing information verification duties with skills-training that covers basic Public Key Infrastructure knowledge, authentication and vetting policies and procedures (including the CA's CP and/or CPS), common threats to the information verification process (including phishing and other social engineering tactics), and these Requirements.

The CA SHALL maintain records of such training and ensure that personnel entrusted with Validation Specialist duties maintain a skill level that enables them to perform such duties satisfactorily.

The CA SHALL document that each Validation Specialist possesses the skills required by a task before allowing the Validation Specialist to perform that task.

The CA SHALL require all Validation Specialists to pass an examination provided by the CA on the information verification requirements outlined in these Requirements.

### 5.3.4 Retraining frequency and requirements

All personnel in Trusted roles SHALL maintain skill levels consistent with the CA's training and performance programs.

### 5.3.5 Job rotation frequency and sequence

### 5.3.6 Sanctions for unauthorized actions

### 5.3.7 Independent Contractor Controls

The CA SHALL verify that the Delegated Third Party's personnel involved in the issuance of a Certificate meet the training and skills requirements of [Section 5.3.3](#533-training-requirements-and-procedures) and the document retention and event logging requirements of [Section 5.4.1](#541-types-of-events-recorded).

### 5.3.7 Independent contractor requirements

The CA SHALL verify that the Delegated Third Party's personnel involved in the issuance of a Certificate meet the training and skills requirements of [Section 5.3.3](#533-training-requirements) and the document retention and event logging requirements of [Section 5.4.1](#541-types-of-events-recorded).

### 5.3.8 Documentation supplied to personnel

## 5.4 Audit logging procedures

### 5.4.1 Types of events recorded

The CA and each Delegated Third Party SHALL record events related to the security of their Certificate Systems, Certificate Management Systems, Root CA Systems, and Delegated Third Party Systems. The CA and each Delegated Third Party SHALL record events related to their actions taken to process a certificate request and to issue a Certificate, including all information generated and documentation received in connection with the certificate request; the time and date; and the personnel involved. The CA SHALL make these records available to its Qualified Auditor as proof of the CA’s compliance with these Requirements.

The CA SHALL record at least the following events:

1. CA certificate and key lifecycle events, including:
   1. Key generation, backup, storage, recovery, archival, and destruction;
   2. Certificate requests, renewal, and re-key requests, and revocation;
   3. Approval and rejection of certificate requests;
   4. Cryptographic device lifecycle management events;
   5. Generation of Certificate Revocation Lists;
   6. Signing of OCSP Responses (as described in [Section 4.9](#49-certificate-revocation-and-suspension) and [Section 4.10](#410-certificate-status-services)); and
   7. Introduction of new Certificate Profiles and retirement of existing Certificate Profiles.

2. Subscriber Certificate lifecycle management events, including:
   1. Certificate requests, renewal, and re-key requests, and revocation;
   2. All verification activities stipulated in these Requirements and the CA's Certification Practice Statement;
   3. Approval and rejection of certificate requests;
   4. Issuance of Certificates; 
   5. Generation of Certificate Revocation Lists; and 
   6. Signing of OCSP Responses (as described in [Section 4.9](#49-certificate-revocation-and-suspension) and [Section 4.10](#410-certificate-status-services)).

3. Security events, including:
   1. Successful and unsuccessful PKI system access attempts;
   2. PKI and security system actions performed;
   3. Security profile changes;
   4. Installation, update and removal of software on a Certificate System;
   5. System crashes, hardware failures, and other anomalies;
   6. Firewall and router activities; and
   7. Entries to and exits from the CA facility.

Log records MUST include the following elements:

1. Date and time of event;
2. Identity of the person making the journal record; and
3. Description of the event.

### 5.4.1 Types of events recorded

The CA and each Delegated Third Party SHALL record events related to the security of their Certificate Systems, Certificate Management Systems, Root CA Systems, and Delegated Third Party Systems. The CA and each Delegated Third Party SHALL record events related to their actions taken to process a Certificate Request and to issue a Certificate, including all information generated and documentation received in connection with the Certificate Request; the time and date; and the personnel involved. The CA SHALL make these records available to its Qualified Auditor as proof of the CA’s compliance with these Requirements.

The CA SHALL record at least the following events:

1. CA Certificate and key lifecycle events, including:<br>
   i. Key generation, backup, storage, recovery, archival, and destruction;
   ii. Certificate requests, renewal, and re-key requests, and revocation;
   iii. Approval and rejection of Certificate Requests;
   iv. Cryptographic device lifecycle management events;
   v. Generation of Certificate Revocation Lists;
   vi. Signing of OCSP Responses (as described in [Section 4.9](#49-certificate-revocation-and-suspension) and [Section 4.10](#410-certificate-status-services)); and
   vii. Introduction of new Certificate Profiles and retirement of existing Certificate Profiles.

2. Subscriber Certificate lifecycle management events, including:<br>
   i. Certificate requests, renewal, and re-key requests, and revocation;
   ii. All verification activities stipulated in these Requirements and the CA's Certification Practice Statement;
   iii. Approval and rejection of Certificate Requests;
   iv. Issuance of Certificates;
   v. Generation of Certificate Revocation Lists; and
   vi. Signing of OCSP Responses (as described in [Section 4.9](#49-certificate-revocation-and-suspension) and [Section 4.10](#410-certificate-status-services)).

3. Security events, including:<br>
   i. Successful and unsuccessful PKI system access attempts;
   ii. PKI and security system actions performed;
   iii. Security profile changes;
   iv. Installation, update and removal of software on a Certificate System;
   v. System crashes, hardware failures, and other anomalies;
   vi. Firewall and router activities; and
   vii. Entries to and exits from the CA facility.

Log records SHALL include the following elements:

1. Date and time of event;
2. Identity of the person making the journal record; and
3. Description of the event.

### 5.4.2 Frequency of processing audit log

### 5.4.3 Retention period for audit log

The CA and each Delegated Third Party SHALL retain, for at least two (2) years:

  1. CA certificate and key lifecycle management event records (as set forth in [Section 5.4.1](#541-types-of-events-recorded) (1)) after the later occurrence of:
     1. the destruction of the CA Private Key; or
     2. the revocation or expiration of the final CA Certificate in that set of Certificates that have an X.509v3 `basicConstraints` extension with the `cA` field set to true and which share a common Public Key corresponding to the CA Private Key;
  2. Subscriber Certificate lifecycle management event records (as set forth in [Section 5.4.1](#541-types-of-events-recorded) (2)) after the expiration of the Subscriber Certificate;
  3. Any security event records (as set forth in [Section 5.4.1](#541-types-of-events-recorded) (3)) after the event occurred.

Note: While these Requirements set the minimum retention period, the CA MAY choose a greater value as more appropriate in order to be able to investigate possible security or other types of incidents that will require retrospection and examination of past audit log events.

### 5.4.3 Retention period for audit log

The CA and each Delegated Third Party SHALL retain, for at least two (2) years:

  1. CA Certificate and key lifecycle management event records (as set forth in [Section 5.4.1](#541-types-of-events-recorded) (1)) after the later occurrence of:<br>
     i. the destruction of the CA Private Key; or
     ii. the revocation or expiration of the final CA Certificate in that set of Certificates that have an X.509v3 `basicConstraints` extension with the `cA` field set to true and which share a common Public Key corresponding to the CA Private Key;
  2. Subscriber Certificate lifecycle management event records (as set forth in [Section 5.4.1](#541-types-of-events-recorded) (2)) after the expiration of the Subscriber Certificate;
  3. Any security event records (as set forth in [Section 5.4.1](#541-types-of-events-recorded) (3)) after the event occurred.

**Note**: While these Requirements set the minimum retention period, the CA MAY choose a greater value as more appropriate in order to be able to investigate possible security or other types of incidents that will require retrospection and examination of past audit log events.

### 5.4.4 Protection of audit log

### 5.4.5 Audit log backup procedures

### 5.4.6 Audit collection System (internal vs. external)

### 5.4.7 Notification to event-causing subject

### 5.4.8 Vulnerability assessments

Additionally, the CA's security program MUST include an annual Risk Assessment that:

1. Identifies foreseeable internal and external threats that could result in unauthorized access, disclosure, misuse, alteration, or destruction of any Certificate Data or Certificate Management Processes;
2. Assesses the likelihood and potential damage of these threats, taking into consideration the sensitivity of the Certificate Data and Certificate Management Processes; and
3. Assesses the sufficiency of the policies, procedures, information systems, technology, and other arrangements that the CA has in place to counter such threats.

### 5.4.8 Vulnerability assessments

The CA's security program SHALL include an annual Risk Assessment that:

1. Identifies foreseeable internal and external threats that could result in unauthorized access, disclosure, misuse, alteration, or destruction of any Certificate Data or Certificate Management Processes;
2. Assesses the likelihood and potential damage of these threats, taking into consideration the sensitivity of the Certificate Data and Certificate Management Processes; and
3. Assesses the sufficiency of the policies, procedures, information systems, technology, and other arrangements that the CA has in place to counter such threats.

## 5.5 Records archival

### 5.5.1 Types of records archived

The CA and each Delegated Third Party SHALL archive all audit logs (as set forth in [Section 5.4.1](#541-types-of-events-recorded)).

Additionally, the CA and each Delegated Third Party SHALL archive:
1. Documentation related to the security of their Certificate Systems, Certificate Management Systems, Root CA Systems, and Delegated Third Party Systems; and
2. Documentation related to their verification, issuance, and revocation of certificate requests and Certificates.

### 5.5.1 Types of records archived

The CA and each Delegated Third Party SHALL archive all audit logs (as set forth in [Section 5.4.1](#541-types-of-events-recorded)).

Additionally, the CA and each Delegated Third Party SHALL archive:

1. Documentation related to the security of their Certificate Systems, Certificate Management Systems, Root CA Systems, and Delegated Third Party Systems; and
2. Documentation related to their verification, issuance, and revocation of Certificate Requests and Certificates.

### 5.5.2 Retention period for archive

Archived audit logs (as set forth in [Section 5.5.1](#551-types-of-records-archived) SHALL be retained for a period of at least two (2) years from their record creation timestamp, or as long as they are required to be retained per [Section 5.4.3](#543-retention-period-for-audit-log), whichever is longer.

Additionally, the CA and each Delegated Third Party SHALL retain, for at least two (2) years:
1. All archived documentation related to the security of Certificate Systems, Certificate Management Systems, Root CA Systems and Delegated Third Party Systems (as set forth in [Section 5.5.1](#551-types-of-records-archived)); and
2. All archived documentation relating to the verification, issuance, and revocation of certificate requests and Certificates (as set forth in [Section 5.5.1](#551-types-of-records-archived)) after the later occurrence of:
   1. such records and documentation were last relied upon in the verification, issuance, or revocation of certificate requests and Certificates; or
   2. the expiration of the Subscriber Certificates relying upon such records and documentation.

Note: While these Requirements set the minimum retention period, the CA MAY choose a greater value as more appropriate in order to be able to investigate possible security or other types of incidents that will require retrospection and examination of past records archived.

### 5.5.2 Retention period for archive

Archived audit logs (as set forth in [Section 5.5.1](#551-types-of-records-archived) SHALL be retained for a period of at least two (2) years from their record creation timestamp, or as long as they are required to be retained per [Section 5.4.3](#543-retention-period-for-audit-log), whichever is longer.

Additionally, the CA and each Delegated Third Party SHALL retain, for at least two (2) years:

1. All archived documentation related to the security of Certificate Systems, Certificate Management Systems, Root CA Systems and Delegated Third Party Systems (as set forth in [Section 5.5.1](#551-types-of-records-archived)); and
2. All archived documentation relating to the verification, issuance, and revocation of Certificate Requests and Certificates (as set forth in [Section 5.5.1](#551-types-of-records-archived)) after the later occurrence of:
   1. such records and documentation were last relied upon in the verification, issuance, or revocation of Certificate Requests and Certificates; or
   2. the expiration of the Subscriber Certificates relying upon such records and documentation.

**Note**: While these Requirements set the minimum retention period, the CA MAY choose a greater value as more appropriate in order to be able to investigate possible security or other types of incidents that will require retrospection and examination of past records archived.

### 5.5.3 Protection of archive

### 5.5.4 Archive backup procedures

### 5.5.5 Requirements for time-stamping of records

### 5.5.6 Archive collection system (internal or external)

### 5.5.7 Procedures to obtain and verify archive information

## 5.6 Key changeover

## 5.7 Compromise and disaster recovery

### 5.7.1 Incident and compromise handling procedures

CA organizations shall have an Incident Response Plan and a Disaster Recovery Plan.

The CA SHALL document a business continuity and disaster recovery procedures designed to notify and reasonably protect Application Software Suppliers, Subscribers, and Relying Parties in the event of a disaster, security compromise, or business failure. The CA is not required to publicly disclose its business continuity plans but SHALL make its business continuity plan and security plans available to the CA's auditors upon request. The CA SHALL annually test, review, and update these procedures.

The business continuity plan MUST include:

1. The conditions for activating the plan,
2. Emergency procedures,
3. Fallback procedures,
4. Resumption procedures,
5. A maintenance schedule for the plan;
6. Awareness and education requirements;
7. The responsibilities of the individuals;
8. Recovery time objective (RTO);
9. Regular testing of contingency plans.
10. The CA's plan to maintain or restore the CA's business operations in a timely manner following interruption to or failure of critical business processes
11. A requirement to store critical cryptographic materials (i.e., secure cryptographic device and activation materials) at an alternate location;
12. What constitutes an acceptable system outage and recovery time
13. How frequently backup copies of essential business information and software are taken;
14. The distance of recovery facilities to the CA's main site; and
15. Procedures for securing its facility to the extent possible during the period of time following a disaster and prior to restoring a secure environment either at the original or a remote site.

### 5.7.1 Incident and compromise handling procedures

CA operators SHALL have an Incident Response Plan and a Disaster Recovery Plan.

The CA SHALL document a business continuity and disaster recovery procedures designed to notify and reasonably protect Application Software Suppliers, Subscribers, and Relying Parties in the event of a disaster, security compromise, or business failure. The CA is not required to publicly disclose its business continuity plans but SHALL make its business continuity plan and security plans available to the CA's auditors upon request. The CA SHALL annually test, review, and update these procedures.

The business continuity plan SHALL include:

1. The conditions for activating the plan;
2. Emergency procedures;
3. Fallback procedures;
4. Resumption procedures;
5. A maintenance schedule for the plan;
6. Awareness and education requirements;
7. The responsibilities of the individuals;
8. Recovery time objective (RTO);
9. Regular testing of contingency plans;
10. The CA's plan to maintain or restore the CA's business operations in a timely manner following interruption to or failure of critical business processes;
11. A requirement to store critical cryptographic materials (i.e., secure cryptographic device and activation materials) at an alternate location;
12. What constitutes an acceptable system outage and recovery time;
13. How frequently backup copies of essential business information and software are taken;
14. The distance of recovery facilities to the CA's main site; and
15. Procedures for securing its facility to the extent possible during the period of time following a disaster and prior to restoring a secure environment either at the original or a remote site.

### 5.7.2 Recovery Procedures if Computing resources, software, and/or data are corrupted

### 5.7.2 Computing resources, software, and/or data are corrupted


### 5.7.3 Recovery Procedures after Key Compromise

### 5.7.3 Entity private key compromise procedures


### 5.7.4 Business continuity capabilities after a disaster

## 5.8 CA or RA termination

# 6. TECHNICAL SECURITY CONTROLS

## 6.1 Key pair generation and installation

### 6.1.1 Key pair generation

#### 6.1.1.1 CA Key Pair Generation

For CA Key Pairs that are either

  i. used as a CA Key Pair for a Root Certificate or
  ii. used as a CA Key Pair for a Subordinate CA Certificate, where the Subordinate CA is not the operator of the Root CA or an Affiliate of the Root CA,

the CA SHALL:

1. prepare and follow a Key Generation Script,
2. have a Qualified Auditor witness the CA Key Pair generation process or record a video of the entire CA Key Pair generation process, and
3. have a Qualified Auditor issue a report opining that the CA followed its key ceremony during its Key and Certificate generation process and the controls used to ensure the integrity and confidentiality of the Key Pair.

For other CA Key Pairs that are for the operator of the Root CA or an Affiliate of the Root CA, the CA SHOULD:

1. prepare and follow a Key Generation Script and
2. have a Qualified Auditor witness the CA Key Pair generation process or record a video of the entire CA Key Pair generation process.

In all cases, the CA SHALL:

1. generate the CA Key Pair in a physically secured environment as described in the CA's Certificate Policy and/or Certification Practice Statement;
2. generate the CA Key Pair using personnel in Trusted Roles under the principles of multiple person control and split knowledge;
3. generate the CA Key Pair within cryptographic modules meeting the applicable technical and business requirements as disclosed in the CA's Certificate Policy and/or Certification Practice Statement;
4. log its CA Key Pair generation activities; and
5. maintain effective controls to provide reasonable assurance that the Private Key was generated and protected in conformance with the procedures described in its Certificate Policy and/or Certification Practice Statement and (if applicable) its Key Generation Script.

#### 6.1.1.1 CA key pair generation

For CA Key Pairs that are either

1. used as a CA Key Pair for a Root CA Certificate; or
2. used as a CA Key Pair for a Subordinate CA Certificate, where the Subordinate CA is not the operator of the Root CA or an Affiliate of the Root CA,

the CA SHALL:

1. prepare and follow a Key Generation Script;
2. have a Qualified Auditor witness the CA Key Pair generation process or record a video of the entire CA Key Pair generation process; and
3. have a Qualified Auditor issue a report opining that the CA followed its key ceremony during its Key and Certificate generation process and the controls used to ensure the integrity and confidentiality of the Key Pair.

For other CA Key Pairs that are for the operator of the Root CA or an Affiliate of the Root CA, the CA SHOULD:

1. prepare and follow a Key Generation Script; and
2. either (i) have a Qualified Auditor witness the CA Key Pair generation process, or (ii) video-record the entire CA Key Pair generation process for review by its Qualified Auditor.

In all cases, the CA SHALL:

1. generate the CA Key Pair in a physically secured environment as described in the CA's CP and/or CPS;
2. generate the CA Key Pair using personnel in Trusted Roles under the principles of multiple person control and split knowledge;
3. generate the CA Key Pair within cryptographic modules meeting the applicable technical and business requirements as disclosed in the CA's CP and/or CPS;
4. log its CA Key Pair generation activities; and
5. maintain effective controls to provide reasonable assurance that the Private Key was generated and protected in conformance with the procedures described in its CP and/or CPS and (if applicable) its Key Generation Script.

#### 6.1.1.2 RA Key Pair Generation

#### 6.1.1.3 Subscriber Key Pair Generation

The CA SHALL reject a certificate request if one or more of the following conditions are met:

1. The Key Pair does not meet the requirements set forth in [Section 6.1.5](#615-key-sizes) and/or [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
2. There is clear evidence that the specific method used to generate the Private Key was flawed;
3. The CA is aware of a demonstrated or proven method that exposes the Applicant's Private Key to compromise;
4. The CA has previously been made aware that the Applicant's Private Key has suffered a Key Compromise, such as through the provisions of [Section 4.9.1.1](#4911-reasons-for-revoking-a-subscriber-certificate);
5. The CA is aware of a demonstrated or proven method to easily compute the Applicant's Private Key based on the Public Key (such as a Debian weak key, see <https://wiki.debian.org/SSLkeys>).

If the Subscriber Certificate will contain an `extKeyUsage` extension containing either the values `id-kp-serverAuth` [RFC5280] or `anyExtendedKeyUsage` [RFC5280], the CA SHALL NOT generate a Key Pair on behalf of a Subscriber, and SHALL NOT accept a certificate request using a Key Pair previously generated by the CA.

#### 6.1.1.3 Subscriber key pair generation

The CA SHALL reject a Certificate Request if one or more of the following conditions are met:

1. The Key Pair does not meet the requirements set forth in [Section 6.1.5](#615-key-sizes) and/or [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
2. There is clear evidence that the specific method used to generate the Private Key was flawed;
3. The CA is aware of a demonstrated or proven method that exposes the Applicant's Private Key to compromise;
4. The CA has previously been made aware that the Applicant's Private Key has suffered a Key Compromise, such as through the provisions of [Section 4.9.1.1](#4911-reasons-for-revoking-a-subscriber-certificate);
5. The CA is aware of a demonstrated or proven method to easily compute the Applicant's Private Key based on the Public Key (such as a Debian weak key, see <https://wiki.debian.org/SSLkeys>).

The CA or a Delegated Third Party MAY generate the Private Key on behalf of the Subscriber.

### 6.1.2 Private key delivery to subscriber

Parties other than the Subscriber SHALL NOT archive the Subscriber Private Key without authorization by the Subscriber.

If the CA or any of its designated RAs become aware that a Subscriber's Private Key has been communicated to an unauthorized person or an organization not affiliated with the Subscriber, then the CA SHALL revoke all certificates that include the Public Key corresponding to the communicated Private Key.

### 6.1.2 Private key delivery to subscriber

Parties other than the Subscriber SHALL NOT archive the Subscriber Private Key without authorization by the Subscriber.

If the CA or any of its designated RAs become aware that a Subscriber's Private Key has been communicated to a person or organization not authorized by the Subscriber, then the CA SHALL revoke all Certificates that include the Public Key corresponding to the communicated Private Key.

If the CA or a Delegated Third Party generates the Private Key on behalf of the Subscriber where the Private Keys will be transported to the Subscriber, then the entity generating the Private Key SHALL either transport the Private Key in hardware with an activation method that is equivalent to 128 bits of encryption or encrypt the Private Key with at least 128 bits of encryption strength. Example methods include using a 128-bit AES key to wrap the Private Key or storing the key in a PKCS 12 file encrypted with a randomly generated password of more than 16 characters containing uppercase letters, lowercase letters, numbers, and symbols for transport. The CA or Delegated Third Party SHALL NOT store Subscriber Private Keys in clear text.

The material used to activate/protect the Private Key (e.g., a password used to secure a PKCS 12 file) must be delivered to the Subscriber securely and separately from the container holding the Private Key.

### 6.1.3 Public key delivery to certificate issuer

### 6.1.4 CA public key delivery to relying parties

### 6.1.5 Key sizes

For RSA key pairs the CA SHALL:

* Ensure that the modulus size, when encoded, is at least 2048 bits, and;
* Ensure that the modulus size, in bits, is evenly divisible by 8.

For ECDSA key pairs, the CA SHALL:

* Ensure that the key represents a valid point on the NIST P-256, NIST P-384 or NIST P-521 elliptic curve.

No other algorithms or key sizes are permitted.

### 6.1.5 Key sizes

For RSA key pairs the CA SHALL:

* Ensure that the modulus size, when encoded, is at least 2048 bits; and
* Ensure that the modulus size, in bits, is evenly divisible by 8.

For ECDSA key pairs, the CA SHALL:

* Ensure that the key represents a valid point on the NIST P-256, NIST P-384, or NIST P-521 elliptic curve.

For EdDSA key pairs, the CA SHALL:

* Ensure that the key represents a valid point on the curve25519 or curve 448 elliptic curve.
  
No other algorithms or key sizes are permitted.

### 6.1.6 Public key parameters generation and quality checking

RSA: The CA SHALL confirm that the value of the public exponent is an odd number equal to 3 or more. Additionally, the public exponent SHOULD be in the range between 2^16 + 1 and 2^256 - 1. The modulus SHOULD also have the following characteristics: an odd number, not the power of a prime, and have no factors smaller than 752. [Source: Section 5.3.3, NIST SP 800-89]

ECDSA: The CA SHOULD confirm the validity of all keys using either the ECC Full Public Key Validation Routine or the ECC Partial Public Key Validation Routine. [Source: Sections 5.6.2.3.2 and 5.6.2.3.3, respectively, of NIST SP 800-56A: Revision 2]

### 6.1.6 Public key parameters generation and quality checking

For RSA key pairs: the CA SHALL confirm that the value of the public exponent is an odd number equal to 3 or more. Additionally, the public exponent SHOULD be in the range between 2^16 + 1 and 2^256 - 1. The modulus SHOULD also have the following characteristics: an odd number, not the power of a prime, and have no factors smaller than 752. (See NIST SP 800-89, Section 5.3.3.)

For ECDSA key pairs: the CA SHOULD confirm the validity of all keys using either the ECC Full Public Key Validation Routine or the ECC Partial Public Key Validation Routine. (See NIST SP 800-56A: Revision 2, Sections 5.6.2.3.2 and 5.6.2.3.3.)

For EdDSA key pairs: no stipulation.

### 6.1.7 Key usage purposes (as per X.509 v3 key usage field)

Private Keys corresponding to Root Certificates MUST NOT be used to sign Certificates except in the following cases:

1. Self-signed Certificates to represent the Root CA itself;
2. Certificates for Subordinate CAs and Cross-Certified Subordinate CA Certificates;
3. Certificates for infrastructure purposes (administrative role certificates, internal CA operational device certificates); and
4. Certificates for OCSP Response verification.

### 6.1.7 Key usage purposes (as per X.509 v3 key usage field)

Private Keys corresponding to Root CA Certificates SHALL NOT be used to sign Certificates except in the following cases:

1. Self-signed Certificates to represent the Root CA itself;
2. Certificates for Subordinate CAs and Cross Certificates;
3. Certificates for infrastructure purposes (administrative role certificates, internal CA operational device certificates); and
4. Certificates for OCSP Response verification.

## 6.2 Private Key Protection and Cryptographic Module Engineering Controls

The CA SHALL implement physical and logical safeguards to prevent unauthorized certificate issuance. Protection of the CA Private Key outside the validated system or device specified above MUST consist of physical security, encryption, or a combination of both, implemented in a manner that prevents disclosure of the Private Key. The CA SHALL encrypt its Private Key with an algorithm and key-length that, according to the state of the art, are capable of withstanding cryptanalytic attacks for the residual life of the encrypted key or key part.

## 6.2 Private key protection and cryptographic module engineering controls

The CA SHALL implement physical and logical safeguards to prevent unauthorized Certificate issuance. Protection of the CA Private Key outside the validated system or device specified above SHALL consist of physical security, encryption, or a combination of both, implemented in a manner that prevents disclosure of the Private Key. The CA SHALL encrypt its Private Key with an algorithm and key-length that, according to the state of the art, are capable of withstanding cryptanalytic attacks for the residual life of the encrypted key or key part.

### 6.2.1 Cryptographic module standards and controls

### 6.2.2 Private key (n out of m) multi-person control

### 6.2.3 Private key escrow

### 6.2.4 Private key backup

See [Section 5.2.2](#522-number-of-individuals-required-per-task).

### 6.2.4 Private key backup

See [Section 5.2.2](#522-number-of-persons-required-per-task).

### 6.2.5 Private key archival

Parties other than the Subordinate CA SHALL NOT archive the Subordinate CA Private Keys without authorization by the Subordinate CA.

### 6.2.6 Private key transfer into or from a cryptographic module

If the Issuing CA generated the Private Key on behalf of the Subordinate CA, then the Issuing CA SHALL encrypt the Private Key for transport to the Subordinate CA. If the Issuing CA becomes aware that a Subordinate CA's Private Key has been communicated to an unauthorized person or an organization not affiliated with the Subordinate CA, then the Issuing CA SHALL revoke all certificates that include the Public Key corresponding to the communicated Private Key.

### 6.2.7 Private key storage on cryptographic module

The CA SHALL protect its Private Key in a system or device that has been validated as meeting at least FIPS 140-2 level 3, FIPS 140-3 level 3, or an appropriate Common Criteria Protection Profile or Security Target, EAL 4 (or higher), which includes requirements to protect the Private Key and other assets against known threats.

### 6.2.8 Activating Private Keys

### 6.2.8 Method of activating private key


### 6.2.9 Deactivating Private Keys

### 6.2.9 Method of deactivating private key


### 6.2.10 Destroying Private Keys

### 6.2.10 Method of destroying private key


### 6.2.11 Cryptographic Module Rating

## 6.3 Other aspects of key pair management

### 6.3.1 Public key archival

### 6.3.2 Certificate operational periods and key pair usage periods

Subscriber Certificates issued on or after 1 September 2020 SHOULD NOT have a Validity Period greater than 397 days and MUST NOT have a Validity Period greater than 398 days. 

For the purpose of calculations, a day is measured as 86,400 seconds. Any amount of time greater than this, including fractional seconds and/or leap seconds, shall represent an additional day. For this reason, Subscriber Certificates SHOULD NOT be issued for the maximum permissible time by default, in order to account for such adjustments.

### 6.3.2 Certificate operational periods and key pair usage periods

| Generation | Maximum Validity Period      | 
|------|-----------------------|
| Strict and Multipurpose | 825 days |
| Legacy | 1185 days |

For the purpose of calculations, a day is measured as 86,400 seconds. Any amount of time greater than this, including fractional seconds and/or leap seconds, SHALL represent an additional day. For this reason, Subscriber Certificates SHOULD NOT be issued for the maximum permissible time by default, in order to account for such adjustments.

## 6.4 Activation data

### 6.4.1 Activation data generation and installation

### 6.4.2 Activation data protection

### 6.4.3 Other aspects of activation data

## 6.5 Computer security controls

### 6.5.1 Specific computer security technical requirements

The CA SHALL enforce multi-factor authentication for all accounts capable of directly causing certificate issuance.

### 6.5.2 Computer security rating

## 6.6 Life cycle technical controls

### 6.6.1 System development controls

### 6.6.2 Security management controls

### 6.6.3 Life cycle security controls

## 6.7 Network security controls

## 6.7 Network security controls

The CA/Browser Forum's Network and Certificate System Security Requirements are incorporated by reference as if fully set forth herein.

## 6.8 Time-stamping

# 7. CERTIFICATE, CRL, AND OCSP PROFILES

## 7.1 Certificate profile

The CA SHALL meet the technical requirements set forth in [Section 2.2 - Publication of Information](#22-publication-of-information), [Section 6.1.5 - Key Sizes](#615-key-sizes), and [Section 6.1.6 - Public Key Parameters Generation and Quality Checking](#616-public-key-parameters-generation-and-quality-checking).

Prior to 2023-09-15, the CA SHALL issue Certificates in accordance with the profile specified in these Requirements or the profile specified in version 1.8.6 of the Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates. Effective 2023-09-15, the CA SHALL issue Certificates in accordance with the profile specified in these Requirements.

## 7.1 Certificate profile

The CA SHALL meet the technical requirements set forth in [Section 2.2](#22-publication-of-certification-information), [Section 6.1.5](#615-key-sizes), and [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking).

CAs SHALL generate non-sequential Certificate serial numbers greater than zero (0) and less than 2^159 containing at least 64 bits of output from a CSPRNG.

### 7.1.1 Version number(s)

Certificates MUST be of type X.509 v3.

### 7.1.1 Version number(s)

Certificates SHALL be of type X.509 v3.

### 7.1.2 Certificate content and extensions; application of RFC 6818

This section specifies the additional requirements for Certificate content and extensions for Certificates.

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

#### 7.1.2.4 All certificates

All fields and extensions SHALL be set in accordance with [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280). The CA SHALL NOT issue a Certificate that contains a `keyUsage` flag, `extKeyUsage` value, Certificate extension, or other data not specified in [Section 7.1.2.1](#7121-root-ca-certificates), [Section 7.1.2.2](#7122-subordinate-ca-certificates), or [Section 7.1.2.3](#7123-subscriber-certificates) unless the CA is aware of a reason for including the data in the Certificate. If the CA includes fields or extensions in a Certificate that are not specified but are otherwise permitted by these Requirements, then the CA SHALL document the processes and procedures that the CA employs for the validation of information contained in such fields and extensions in its CP and/or CPS.

CAs SHALL NOT issue a Certificate with:

1. Extensions that do not apply in the context of the public Internet (such as an `extKeyUsage` value for a service that is only valid in the context of a privately managed network), unless:<br>
   i. such value falls within an OID arc for which the Applicant demonstrates ownership, or<br>
   ii. the Applicant can otherwise demonstrate the right to assert the data in a public context; or
2. Field or extension values which have not been validated according to the processes and procedures described in these Requirements or the CA's CP and/or CPS.
   
### 7.1.3 Algorithm object identifiers

#### 7.1.3.1 SubjectPublicKeyInfo

The following requirements apply to the `subjectPublicKeyInfo` field within a Certificate or Precertificate. No other encodings are permitted.

#### 7.1.3.1 SubjectPublicKeyInfo

The following requirements apply to the `subjectPublicKeyInfo` field within a Certificate. No other encodings are permitted.

##### 7.1.3.1.1 RSA

The CA SHALL indicate an RSA key using the rsaEncryption (OID: 1.2.840.113549.1.1.1) algorithm identifier. The parameters MUST be present, and MUST be an explicit NULL.
The CA SHALL NOT use a different algorithm, such as the id-RSASSA-PSS (OID: 1.2.840.113549.1.1.10) algorithm identifier, to indicate an RSA key.

When encoded, the `AlgorithmIdentifier` for RSA keys MUST be byte-for-byte identical with the following hex-encoded bytes: `300d06092a864886f70d0101010500`

##### 7.1.3.1.1 RSA

The CA SHALL indicate an RSA key using the rsaEncryption (OID: 1.2.840.113549.1.1.1) algorithm identifier. The parameters SHALL be present, and SHALL be an explicit NULL.

The CA SHALL NOT use a different algorithm, such as the id-RSASSA-PSS (OID: 1.2.840.113549.1.1.10) algorithm identifier, to indicate an RSA key.

When encoded, the `AlgorithmIdentifier` for RSA keys SHALL be byte-for-byte identical with the following hex-encoded bytes: `300d06092a864886f70d0101010500`

##### 7.1.3.1.2 ECDSA

The CA SHALL indicate an ECDSA key using the id-ecPublicKey (OID: 1.2.840.10045.2.1) algorithm identifier. The parameters MUST use the `namedCurve` encoding.

* For P-256 keys, the `namedCurve` MUST be secp256r1 (OID: 1.2.840.10045.3.1.7).
* For P-384 keys, the `namedCurve` MUST be secp384r1 (OID: 1.3.132.0.34).
* For P-521 keys, the `namedCurve` MUST be secp521r1 (OID: 1.3.132.0.35).

When encoded, the `AlgorithmIdentifier` for ECDSA keys MUST be byte-for-byte identical with the following hex-encoded bytes:

* For P-256 keys, `301306072a8648ce3d020106082a8648ce3d030107`.
* For P-384 keys, `301006072a8648ce3d020106052b81040022`.
* For P-521 keys, `301006072a8648ce3d020106052b81040023`.

##### 7.1.3.1.2 ECDSA

The CA SHALL indicate an ECDSA key using the id-ecPublicKey (OID: 1.2.840.10045.2.1) algorithm identifier. The parameters SHALL use the `namedCurve` encoding.

* For P-256 keys, the `namedCurve` SHALL be secp256r1 (OID: 1.2.840.10045.3.1.7).
* For P-384 keys, the `namedCurve` SHALL be secp384r1 (OID: 1.3.132.0.34).
* For P-521 keys, the `namedCurve` SHALL be secp521r1 (OID: 1.3.132.0.35).

When encoded, the `AlgorithmIdentifier` for ECDSA keys SHALL be byte-for-byte identical with the following hex-encoded bytes:

* For P-256 keys, `301306072a8648ce3d020106082a8648ce3d030107`.
* For P-384 keys, `301006072a8648ce3d020106052b81040022`.
* For P-521 keys, `301006072a8648ce3d020106052b81040023`.

##### 7.1.3.1.3 EdDSA

The CA SHALL indicate an EdDSA key using one of the following algorithm identifiers below:

* For curve25519 keys, the `algorithm` SHALL be id-Ed25519 (OID: 1.3.101.112).
* For curve448 keys, the `algorithm` SHALL be id-Ed448 (OID: 1.3.101.113).

The parameters for EdDSA keys SHALL be absent.

When encoded, the `AlgorithmIdentifier` for EdDSA keys SHALL be byte-for-byte identical with the following hex-encoded bytes:

* For Curve25519 keys, `300506032b6570`.
* For Curve448 keys, `300506032b6571`.

#### 7.1.3.2 Signature AlgorithmIdentifier

All objects signed by a CA Private Key MUST conform to these requirements on the use of the `AlgorithmIdentifier` or `AlgorithmIdentifier`-derived type in the context of signatures.

In particular, it applies to all of the following objects and fields:

* The `signatureAlgorithm` field of a Certificate or Precertificate.
* The `signature` field of a TBSCertificate (for example, as used by either a Certificate or Precertificate).
* The `signatureAlgorithm` field of a CertificateList
* The `signature` field of a TBSCertList
* The `signatureAlgorithm` field of a BasicOCSPResponse.

No other encodings are permitted for these fields.

#### 7.1.3.2 Signature AlgorithmIdentifier

All objects signed by a CA Private Key SHALL conform to these requirements on the use of the `AlgorithmIdentifier` or `AlgorithmIdentifier`-derived type in the context of signatures.

In particular, it applies to all of the following objects and fields:

* The `signatureAlgorithm` field of a Certificate.
* The `signature` field of a TBSCertificate (for example, as used by a Certificate).
* The `signatureAlgorithm` field of a CertificateList
* The `signature` field of a TBSCertList
* The `signatureAlgorithm` field of a BasicOCSPResponse.

No other encodings are permitted for these fields.

##### 7.1.3.2.1 RSA

The CA SHALL use one of the following signature algorithms and encodings. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the specified hex-encoded bytes.

* RSASSA-PKCS1-v1_5 with SHA-256:

  Encoding:
  `300d06092a864886f70d01010b0500`.

* RSASSA-PKCS1-v1_5 with SHA-384:

  Encoding:
  `300d06092a864886f70d01010c0500`.

* RSASSA-PKCS1-v1_5 with SHA-512:

  Encoding:
  `300d06092a864886f70d01010d0500`.

* RSASSA-PSS with SHA-256, MGF-1 with SHA-256, and a salt length of 32 bytes:

  Encoding:

  ```hexdump
  304106092a864886f70d01010a3034a00f300d0609608648016503040201
  0500a11c301a06092a864886f70d010108300d0609608648016503040201
  0500a203020120
  ```

* RSASSA-PSS with SHA-384, MGF-1 with SHA-384, and a salt length of 48 bytes:

  Encoding:

  ```hexdump
  304106092a864886f70d01010a3034a00f300d0609608648016503040202
  0500a11c301a06092a864886f70d010108300d0609608648016503040202
  0500a203020130
  ```

* RSASSA-PSS with SHA-512, MGF-1 with SHA-512, and a salt length of 64 bytes:

  Encoding:

  ```hexdump
  304106092a864886f70d01010a3034a00f300d0609608648016503040203
  0500a11c301a06092a864886f70d010108300d0609608648016503040203
  0500a203020140
  ```

In addition, the CA MAY use the following signature algorithm and encoding if all of the following conditions are met:

* If used within a Certificate, such as the `signatureAlgorithm` field of a Certificate or the `signature` field of a TBSCertificate:
  * The new Certificate is a Root CA Certificate or Subordinate CA Certificate that is a Cross-Certificate; and,
  * There is an existing Certificate, issued by the same issuing CA Certificate, using the following encoding for the signature algorithm; and,
  * The existing Certificate has a `serialNumber` that is at least 64-bits long; and,
  * The only differences between the new Certificate and existing Certificate are one of the following:
    * A new `subjectPublicKey` within the `subjectPublicKeyInfo`, using the same algorithm and key size; and/or,
    * A new `serialNumber`, of the same encoded length as the existing Certificate; and/or
    * The new Certificate's `extKeyUsage` extension is present, has at least one key purpose specified, and none of the key purposes specified are the id-kp-serverAuth (OID: 1.3.6.1.5.5.7.3.1) or the anyExtendedKeyUsage (OID: 2.5.29.37.0) key purposes; and/or
    * The new Certificate's `basicConstraints` extension has a pathLenConstraint that is zero.
* If used within an OCSP response, such as the `signatureAlgorithm` of a BasicOCSPResponse:
  * The `producedAt` field value of the ResponseData MUST be earlier than 2022-06-01 00:00:00 UTC; and,
  * All unexpired, un-revoked Certificates that contain the Public Key of the CA Key Pair and that have the same Subject Name MUST also contain an `extKeyUsage` extension with the only key usage present being the id-kp-ocspSigning (OID: 1.3.6.1.5.5.7.3.9) key usage.
* If used within a CRL, such as the `signatureAlgorithm` field of a CertificateList or the `signature` field of a TBSCertList:
  * The CRL is referenced by one or more Root CA or Subordinate CA Certificates; and,
  * The Root CA or Subordinate CA Certificate has issued one or more Certificates using the following encoding for the signature algorithm.

**Note**: The above requirements do not permit a CA to sign a Precertificate with this encoding.

* RSASSA-PKCS1-v1_5 with SHA-1:

  Encoding:
  `300d06092a864886f70d0101050500`

##### 7.1.3.2.1 RSA

The CA SHALL use one of the following signature algorithms and encodings. When encoded, the `AlgorithmIdentifier` SHALL be byte-for-byte identical with the specified hex-encoded bytes.

* RSASSA-PKCS1-v1_5 with SHA-256:

  Encoding:
  `300d06092a864886f70d01010b0500`.

* RSASSA-PKCS1-v1_5 with SHA-384:

  Encoding:
  `300d06092a864886f70d01010c0500`.

* RSASSA-PKCS1-v1_5 with SHA-512:

  Encoding:
  `300d06092a864886f70d01010d0500`.

* RSASSA-PSS with SHA-256, MGF-1 with SHA-256, and a salt length of 32 bytes:

  Encoding:

  ```hexdump
  304106092a864886f70d01010a3034a00f300d0609608648016503040201
  0500a11c301a06092a864886f70d010108300d0609608648016503040201
  0500a203020120
  ```

* RSASSA-PSS with SHA-384, MGF-1 with SHA-384, and a salt length of 48 bytes:

  Encoding:

  ```hexdump
  304106092a864886f70d01010a3034a00f300d0609608648016503040202
  0500a11c301a06092a864886f70d010108300d0609608648016503040202
  0500a203020130
  ```

* RSASSA-PSS with SHA-512, MGF-1 with SHA-512, and a salt length of 64 bytes:

  Encoding:

  ```hexdump
  304106092a864886f70d01010a3034a00f300d0609608648016503040203
  0500a11c301a06092a864886f70d010108300d0609608648016503040203
  0500a203020140
  ```

##### 7.1.3.2.2 ECDSA

The CA SHALL use the appropriate signature algorithm and encoding based upon the signing key used.

If the signing key is P-256, the signature MUST use ECDSA with SHA-256. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040302`.

If the signing key is P-384, the signature MUST use ECDSA with SHA-384. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040303`.

If the signing key is P-521, the signature MUST use ECDSA with SHA-512. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040304`.

##### 7.1.3.2.2 ECDSA

The CA SHALL use the appropriate signature algorithm and encoding based upon the signing key used.

If the signing key is P-256, the signature SHALL use ECDSA with SHA-256. When encoded, the `AlgorithmIdentifier` SHALL be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040302`.

If the signing key is P-384, the signature SHALL use ECDSA with SHA-384. When encoded, the `AlgorithmIdentifier` SHALL be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040303`.

If the signing key is P-521, the signature SHALL use ECDSA with SHA-512. When encoded, the `AlgorithmIdentifier` SHALL be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040304`.

##### 7.1.3.2.3 EdDSA

The CA SHALL use the appropriate signature algorithm and encoding based upon the signing key used.

If the signing key is Curve25519, the signature algorithm SHALL be id-Ed25519 (OID: 1.3.101.112). When encoded, the `AlgorithmIdentifier` SHALL be byte-for-byte identical with the following hex-encoded bytes: `300506032b6570`.

If the signing key is Curve448, the signature algorithm SHALL be id-Ed448 (OID: 1.3.101.113). When encoded, the `AlgorithmIdentifier` SHALL be byte-for-byte identical with the following hex-encoded bytes: `300506032b6571`.

### 7.1.4 Name Forms

This section details encoding rules that apply to all Certificates issued by a CA. Further restrictions may be specified within [Section 7.1.2](#712-certificate-content-and-extensions), but these restrictions do not supersede these requirements.

### 7.1.4 Name forms

Attribute values SHALL be encoded according to [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280).

#### 7.1.4.1 Name Encoding

The following requirements apply to all Certificates listed in [Section 7.1.2](#712-certificate-content-and-extensions). Specifically, this includes Technically Constrained Non-TLS Subordinate CA Certificates, as defined in [Section 7.1.2.3](#7123-technically-constrained-non-tls-subordinate-ca-certificate-profile), but does not include certificates issued by such CA Certificates, as they are out of scope of these Baseline Requirements.

For every valid Certification Path (as defined by [RFC 5280, Section 6](https://tools.ietf.org/html/rfc5280#section-6)):

* For each Certificate in the Certification Path, the encoded content of the Issuer Distinguished Name field of a Certificate SHALL be byte-for-byte identical with the encoded form of the Subject Distinguished Name field of the Issuing CA certificate.
* For each CA Certificate in the Certification Path, the encoded content of the Subject Distinguished Name field of a Certificate SHALL be byte-for-byte identical among all Certificates whose Subject Distinguished Names can be compared as equal according to [RFC 5280, Section 7.1](https://tools.ietf.org/html/rfc5280#section-7.1), and including expired and revoked Certificates.

When encoding a `Name`, the CA SHALL ensure that:

  * Each `Name` MUST contain an `RDNSequence`.
  * Each `RelativeDistinguishedName` MUST contain exactly one `AttributeTypeAndValue`.
  * Each `RelativeDistinguishedName`, if present, is encoded within the `RDNSequence` in the order that it appears in [Section 7.1.4.2](#7142-subject-attribute-encoding).
    * For example, a `RelativeDistinguishedName` that contains a `countryName` `AttributeTypeAndValue` pair MUST be encoded within the `RDNSequence` before a `RelativeDistinguishedName` that contains a `stateOrProvinceName` `AttributeTypeAndValue`.
  * Each `Name` MUST NOT contain more than one instance of a given `AttributeTypeAndValue` across all `RelativeDistinguishedName`s unless explicitly allowed in these Requirements.

**Note**: [Section 7.1.2.2.2](#71222-cross-certified-subordinate-ca-naming) provides an exception to the above `Name` encoding requirements when issuing a [Cross-Certified Subordinate CA Certificate](#7122-cross-certified-subordinate-ca-certificate-profile), as described within that section.

#### 7.1.4.1 Name encoding

For every valid Certification Path (as defined by [RFC 5280, Section 6](https://datatracker.ietf.org/doc/html/rfc5280#section-6)):

* For each Certificate in the Certification Path, the encoded content of the Issuer Distinguished Name field of a Certificate SHALL be byte-for-byte identical with the encoded form of the Subject Distinguished Name field of the Issuing CA Certificate.
* For each CA Certificate in the Certification Path, the encoded content of the Subject Distinguished Name field of a Certificate SHALL be byte-for-byte identical among all Certificates whose Subject Distinguished Names can be compared as equal according to [RFC 5280, Section 7.1](https://datatracker.ietf.org/doc/html/rfc5280#section-7.1), and including expired and revoked Certificates.

#### 7.1.4.2 Subject Attribute Encoding

This document defines requirements for the content and validation of a number of attributes that may appear within the `subject` field of a `tbsCertificate`. CAs SHALL NOT include these attributes unless their content has been validated as specified by, and only if permitted by, the relevant certificate profile specified within [Section 7.1.2](#712-certificate-content-and-extensions).

CAs that include attributes in the Certificate `subject` field that are listed in the table below SHALL encode those attributes in the relative order as they appear in the table and follow the specified encoding requirements for the attribute.

Table: Encoding and Order Requirements for Selected Attributes

| __Attribute__            | __OID__    | __Specification__                               | __Encoding Requirements__                  | __Max Length[^maxlength]__ |
| ----                     | --         | ---                                             | ----                                       | - |
| `domainComponent`        | `0.9.2342.19200300.100.1.25` | [RFC 4519](https://tools.ietf.org/html/rfc4519) | MUST use `IA5String`     | 63 |
| `countryName`            | `2.5.4.6`  | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `PrintableString`                 | 2 |
| `stateOrProvinceName`    | `2.5.4.8`  | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 128 |
| `localityName`           | `2.5.4.7`  | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 128 |
| `postalCode`             | `2.5.4.17` | X.520                                           | MUST use `UTF8String` or `PrintableString` | 40 |
| `streetAddress`          | `2.5.4.9`  | X.520                                           | MUST use `UTF8String` or `PrintableString` | 128 |
| `organizationName`       | `2.5.4.10` | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 64 |
| `surname`                | `2.5.4.4`  | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 64[^surname_givenname] |
| `givenName`              | `2.5.4.42` | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 64[^surname_givenname] |
| `organizationalUnitName` | `2.5.4.11` | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 64 |
| `commonName`             | `2.5.4.3`  | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `UTF8String` or `PrintableString` | 64 |

[^surname_givenname]: **Note**: Although RFC 5280 specifies the upper bound as 32,768 characters, this was a transcription error from X.520 (08/2005). The effective (interoperable) upper bound is 64 characters.

CAs that include attributes in the Certificate `subject` field that are listed in the table below SHALL follow the specified encoding requirements for the attribute.

Table: Encoding Requirements for Selected Attributes

| __Attribute__            | __OID__    | __Specification__                               | __Encoding Requirements__                  | __Max Length[^maxlength]__ |
| ----                     | --         | ---                                             | ----                                       | - |
| `businessCategory`       | `2.5.4.15` | X.520                                           | MUST use `UTF8String` or `PrintableString` | 128 |
| `jurisdictionCountry`    | `1.3.6.1.4.1.311.60.2.1.3` | Guidelines for the Issuance and Management of Extended Validation Certificates | MUST use `PrintableString` | 2 |
| `jurisdictionStateOrProvince`    | `1.3.6.1.4.1.311.60.2.1.2` | Guidelines for the Issuance and Management of Extended Validation Certificates | MUST use `UTF8String` or `PrintableString` | 128 |
| `jurisdictionLocality`    | `1.3.6.1.4.1.311.60.2.1.1` | Guidelines for the Issuance and Management of Extended Validation Certificates | MUST use `UTF8String` or `PrintableString` | 128 |
| `serialNumber`    | `2.5.4.5` | [RFC 5280](https://tools.ietf.org/html/rfc5280) | MUST use `PrintableString` | 64 |
| `organizationIdentifier` | `2.5.4.97` | X.520 | MUST use `UTF8String` or `PrintableString` | None |

[^maxlength]: **Note**: ASN.1 length limits for DirectoryString are expressed as character limits, not byte limits.

#### 7.1.4.2 Subject information - subscriber certificates

By issuing the Certificate, the CA represents that it followed the procedure set forth in its CP and/or CPS to verify that, as of the Certificate's issuance date, all of the Subject Information was accurate. 

CAs SHALL NOT include a Mailbox Address in a Mailbox Field except as verified in accordance with [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control)

Subject attributes SHALL NOT contain only metadata such as '.', '-', and ' ' (i.e., space) characters, and/or any other indication that the value is absent, incomplete, or not applicable. 

##### 7.1.4.2.1 Subject alternative name extension

__Certificate Field:__ `extensions:subjectAltName`  
__Required/Optional:__ SHALL be present  
__Contents:__ This extension SHALL contain at least one `GeneralName` entry of the following types:

* `Rfc822Name` and/or
* `otherName` of type `id-on-SmtpUTF8Mailbox`, encoded in accordance with [RFC 8398](https://datatracker.ietf.org/doc/html/rfc8398)

All Mailbox Addresses in the `subject` field or entries of type `dirName` of this extension SHALL be repeated as `rfc822Name` or `otherName` values of type `id-on-SmtpUTF8Mailbox` in this extension.

The CA MAY include `GeneralName` entries of type `dirName` provided that the information contained in the `Name` complies with the requirements set forth in the appropriate subsection of [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields) according to the Certificate Type. Additionally, information contained in the `Name` SHALL be validated according to [Section 3.1](#31-naming), [Section 3.2.3](#323-authentication-of-organization-identity), and/or [Section 3.2.4](#324-authentication-of-individual-identity), as appropriate for the Certificate Type.

For Legacy and Multipurpose Generation profiles, then the CA MAY include `otherName` entries of any type, provided that the CA has validated the field value according to its CP and/or CPS.

The CA SHALL NOT include `GeneralName` entries that do not conform to the requirements of this section.

##### 7.1.4.2.2 Subject distinguished name fields

a. __Certificate Field:__ `subject:commonName` (OID 2.5.4.3)  
   __Contents:__ If present, this attribute SHALL contain one of the following values verified in accordance with [Section 3.2](#32-initial-identity-validation).

| Certificate Type    | Contents |
|---------|----------|
| `Mailbox-validated` | Mailbox Address |
| `Organization-validated` | `subject:organizationName` or Mailbox Address |
| `Sponsor-validated` | Personal Name, Pseudonym, or Mailbox Address |
| `Individual-validated` | Personal Name, Pseudonym, or Mailbox Address |

If present, the Personal Name SHALL contain a name of the Subject. The Personal Name SHOULD be presented as `subject:givenName` and/or `subject:surname`. The Personal Name MAY be in the Subject's preferred presentation format or a format preferred by the CA or Enterprise RA, but SHALL be a meaningful representation of the Subject’s name as verified under [Section 3.2.4](#324-authentication-of-individual-identity). 

If present, the Mailbox Address SHALL contain a `rfc822Name` or `otherName` value of type `id-on-SmtpUTF8Mailbox` from `extensions:subjectAltName`.

If present, the Pseudonym SHALL contain the `subject:pseudonym` if that Subject attribute is also present.

**Note**: Like all other Certificate attributes, `subject:commonName` and `subject:emailAddress` SHALL comply with the attribute upper bounds defined in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280).

Additional specifications for naming are provided in [Section 3.1](#31-naming).

b. __Certificate Field:__ `subject:organizationName` (OID 2.5.4.10)  
   __Contents:__ If present, the `subject:organizationName` field SHALL contain the Subject's full legal organization name and/or an Assumed Name as verified under [Section 3.2.3](#323-authentication-of-organization-identity). If both are included, the Assumed Name SHALL appear first, followed by the full legal organization name in parentheses. The CA MAY include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations; e.g., if the official record shows "Company Name Incorporated", the CA MAY use "Company Name Inc." or "Company Name". 

c. __Certificate Field:__ `subject:organizationalUnitName` (OID: 2.5.4.11)  
   __Contents:__ If present, the CA SHALL confirm that the `subject:organizationalUnitName` is the full legal organization name of an Affiliate of the `subject:organizationName` in the Certificate and has been verified in accordance with the requirements of [Section 3.2.3](#323-authentication-of-organization-identity). The CA MAY include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations.

d. __Certificate Field:__ `subject:organizationIdentifier` (2.5.4.97)  
   __Contents:__ If present, the `subject:organizationIdentifier` field SHALL contain a Registration Reference for a Legal Entity assigned in accordance to the identified Registration Scheme. 

   The `subject:organizationIdentifier` SHALL be encoded as a PrintableString or UTF8String.

   The Registration Scheme identified in the Certificate SHALL be the result of the verification performed in accordance with [Section 3.2.3](#323-authentication-of-organization-identity). The Registration Scheme SHALL be identified using the following structure in the presented order:

    * 3 character Registration Scheme identifier;
    * 2 character ISO 3166 country code for the nation in which the Registration Scheme is operated, or if the scheme is operated globally ISO 3166 code "XG" SHALL be used;
    * For the NTR Registration Scheme identifier, where registrations are administrated at the subdivision (state or province) level, a plus "+" (0x2B (ASCII), U+002B (UTF-8)) followed by an up-to-three alphanumeric character ISO 3166-2 identifier for the subdivision of the nation in which the Registration Scheme is operated;
    * a hyphen-minus "-" (0x2D (ASCII), U+002D (UTF-8));
    * Registration Reference allocated in accordance with the identified Registration Scheme.

   **Note 1**: Registration References MAY contain hyphens but Registration Schemes, ISO 3166 country codes, and ISO 3166-2 identifiers do not. Therefore if more than one hyphen appears in the structure, the leftmost hyphen is a separator, and the remaining hyphens are part of the Registration Reference. For example:

    * `NTRGB-12345678` (NTR scheme, Great Britain, Unique Identifier at Country level is 12345678).
    * `NTRUS+CA-12345678` (NTR Scheme, United States - California, Unique identifier at State level is 12345678).
    * `VATDE-123456789` (VAT Scheme, Germany, Unique Identifier at Country Level is 12345678).
    * `PSDBE-NBB-1234.567.890` (PSD Scheme, Belgium, NCA's identifier is NBB, Unique Identifier assigned by the NCA is 1234.567.890).

   Registration Schemes listed in [Appendix A](#appendix-a---registration-schemes) are recognized as valid under these Requirements. The CA SHALL:

   1. Confirm that the organization represented by the Registration Reference is the same as the organization named in the `organizationName` field as specified in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields); and
   2. Further verify the Registration Reference matches other information verified in accordance with [Section 3.2.3](#323-authentication-of-organization-identity).

   **Note 2**: For the following types of entities that do not have an identifier from the Registration Schemes listed in [Appendix A](#appendix-a---registration-schemes):

    * For Government Entities, the CA SHALL enter the Registration Scheme identifier ‘GOV’ followed by the 2 character ISO 3166 country code for the nation in which the Government Entity is located.  If the Government Entity is verified at a subdivision (state or province) level, then a plus "+" (0x2B (ASCII), U+002B (UTF-8)) followed by an ISO 3166-2 identifier for the subdivision (up to three alphanumeric characters) is added.
    * For International Organization Entities, the CA SHALL enter the Registration Scheme identifier ‘INT’ followed by the ISO 3166 code "XG". An International Organization Entity is founded by a constituent document, e.g., a charter, treaty, convention or similar document, signed by, or on behalf of, a minimum of two Sovereign State governments.
  
    For example:
    * GOVUS (Government Entity, United States)
    * GOVUS+CA (Government Entity, United States - California)
    * INTXG (International Organization)

e. __Certificate Field:__ `subject:givenName` (2.5.4.42) and/or `subject:surname` (2.5.4.4)  
   __Contents:__ If present, the `subject:givenName` field and `subject:surname` field SHALL contain a Natural Person Subject’s name as verified under [Section 3.2.4](#324-authentication-of-individual-identity). Subjects with a single legal name SHALL provide the name in the `subject:surname` attribute. The `subject:givenName` and/or `subject:surname` SHALL NOT be present if the `subject:pseudonym` is present.

f. __Certificate Field:__ `subject:pseudonym` (2.5.4.65)  
   __Contents:__ The `subject:pseudonym` SHALL NOT be present if the `subject:givenName` and/or `subject:surname` are present. If present, the `subject:pseudonym` field SHALL be verified according to [Section 3.1.3](#313-anonymity-or-pseudonymity-of-subscribers).

g. __Certificate Field:__ `subject:serialNumber` (2.5.4.5)  
   __Contents:__ If present, the `subject:serialNumber` MAY be used to contain an identifier assigned by the CA or RA to identify and/or to disambiguate the Subscriber. 
   
   In addition, the `subject:serialNumber` MAY be used in the `Sponsor-validated` and `Individual-validated` profiles to contain a Natural Person Identifier as described in ETSI EN 319 412-1 Section 5.1.3. Registration Schemes listed in [Appendix A](#appendix-a---registration-schemes) are recognized as valid under these Requirements. The CA SHALL confirm that the Individual represented by the Natural Person Identifier is the same as the Certificate Subject in accordance with [Section 3.2.4](#324-authentication-of-individual-identity). 

h. __Certificate Field:__ `subject:emailAddress` (1.2.840.113549.1.9.1) 
   __Contents:__ If present, the `subject:emailAddress` SHALL contain a single Mailbox Address as verified under [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control).

i. __Certificate Field:__ `subject:title` (2.5.4.12) 
   __Contents:__ If present, the `subject:title` field SHALL contain only a organizational role/title or a regulated professional designation verified according to [Section 3.2.4](#324-authentication-of-individual-identity).

j. __Certificate Field:__ Number and street: `subject:streetAddress` (OID: 2.5.4.9)  
 __Contents:__ If present, the `subject:streetAddress` field SHALL contain the Subject's street address information as verified under [Section 3.2.3](#323-authentication-of-organization-identity) for Organization-validated and Sponsor-validated Certificate Types or [Section 3.2.4](#324-authentication-of-individual-identity) for Individual-validated Certificate Types.

k. __Certificate Field:__ `subject:localityName` (OID: 2.5.4.7)  
   __Contents:__ If present, the `subject:localityName` field SHALL contain the Subject's locality information as verified under [Section 3.2.3](#323-authentication-of-organization-identity) for Organization-validated and Sponsor-validated Certificate Types or [Section 3.2.4](#324-authentication-of-individual-identity) for Individual-validated Certificate Types. If the `subject:countryName` field specifies the ISO 3166-1 user-assigned code of XX in accordance with [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields) (n), the `localityName` field MAY contain the Subject's locality and/or state or province information.

l. __Certificate Field:__ `subject:stateOrProvinceName` (OID: 2.5.4.8)  
   __Contents:__ If present, the `subject:stateOrProvinceName` field SHALL contain the Subject's state or province information as verified under [Section 3.2.3](#323-authentication-of-organization-identity) for Organization-validated and Sponsor-validated Certificate Types or [Section 3.2.4](#324-authentication-of-individual-identity) for Individual-validated Certificate Types. If the `subject:countryName` field specifies the ISO 3166-1 user-assigned code of XX in accordance with [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields) (n), the `subject:stateOrProvinceName` field MAY contain the full name of the Subject's country information.

m. __Certificate Field:__ `subject:postalCode` (OID: 2.5.4.17)  
   __Contents:__ If present, the `subject:postalCode` field SHALL contain the Subject's zip or postal information as verified under [Section 3.2.3](#323-authentication-of-organization-identity) for Organization-validated and Sponsor-validated Certificate Types or [Section 3.2.4](#324-authentication-of-individual-identity) for Individual-validated Certificate Types.

n. __Certificate Field:__ `subject:countryName` (OID: 2.5.4.6)  
   __Contents:__ If present, the `subject:countryName` SHALL contain the two-letter ISO 3166-1 country code associated with the location of the Subject verified under [Section 3.2.3](#323-authentication-of-organization-identity) for Organization-validated and Sponsor-validated Certificate Types or [Section 3.2.4](#324-authentication-of-individual-identity) for Individual-validated Certificate Types. If a Country is not represented by an official ISO 3166-1 country code, the CA MAY specify the ISO 3166-1 user-assigned code of XX indicating that an official ISO 3166-1 alpha-2 code has not been assigned.

##### 7.1.4.2.3 Subject DN attributes for mailbox-validated profile

| Attribute | Legacy | Multipurpose | Strict |
|-----------|--------|--------------|--------|
| `commonName` | MAY  | MAY | MAY |
| `organizationName` | SHALL NOT | SHALL NOT | SHALL NOT |
| `organizationalUnitName` | SHALL NOT | SHALL NOT | SHALL NOT |
| `organizationIdentifier` | SHALL NOT | SHALL NOT | SHALL NOT |
| `givenName` | SHALL NOT | SHALL NOT | SHALL NOT |
| `surname` | SHALL NOT | SHALL NOT | SHALL NOT |
| `pseudonym` | SHALL NOT | SHALL NOT | SHALL NOT |
| `serialNumber` | MAY | MAY | MAY |
| `emailAddress` | MAY | MAY | MAY |
| `title` | SHALL NOT | SHALL NOT | SHALL NOT |
| `streetAddress` | SHALL NOT | SHALL NOT | SHALL NOT |
| `localityName` | SHALL NOT | SHALL NOT | SHALL NOT |
| `stateOrProvinceName` | SHALL NOT | SHALL NOT | SHALL NOT |
| `postalCode` | SHALL NOT | SHALL NOT | SHALL NOT |
| `countryName` | SHALL NOT | SHALL NOT | SHALL NOT |
| Other | SHALL NOT | SHALL NOT | SHALL NOT |

##### 7.1.4.2.4 Subject DN attributes for organization-validated profile

| Attribute | Legacy | Multipurpose | Strict |
|-----------|--------|--------------|--------|
| `commonName` | MAY  | MAY | MAY |
| `organizationName` | SHALL | SHALL | SHALL |
| `organizationalUnitName` | MAY  | MAY | MAY |
| `organizationIdentifier` | SHALL | SHALL | SHALL |
| `givenName` | SHALL NOT | SHALL NOT | SHALL NOT |
| `surname` | SHALL NOT | SHALL NOT | SHALL NOT |
| `pseudonym` | SHALL NOT | SHALL NOT | SHALL NOT |
| `serialNumber` | MAY | MAY | MAY |
| `emailAddress` | MAY | MAY | MAY |
| `title` | SHALL NOT | SHALL NOT | SHALL NOT |
| `streetAddress` | MAY | MAY | SHALL NOT |
| `localityName` | MAY | MAY | MAY |
| `stateOrProvinceName` | MAY | MAY | MAY |
| `postalCode` | MAY | MAY | SHALL NOT |
| `countryName` | MAY | MAY | MAY |
| Other | MAY | SHALL NOT | SHALL NOT |

##### 7.1.4.2.5 Subject DN attributes for sponsor-validated profile

| Attribute | Legacy<br> (See Note 1) | Multipurpose<br> (See Note 2) | Strict<br> (See Note 2) |
|-----------|--------|--------------|--------|
| `commonName` | MAY  | MAY | MAY |
| `organizationName` | SHALL | SHALL | SHALL |
| `organizationalUnitName` | MAY  | MAY | MAY |
| `organizationIdentifier` | SHALL | SHALL | SHALL |
| `givenName` | MAY | MAY | MAY |
| `surname` | MAY | MAY | MAY |
| `pseudonym` | MAY | MAY | MAY |
| `serialNumber` | MAY | MAY | MAY |
| `emailAddress` | MAY | MAY | MAY |
| `title` | MAY  | MAY | MAY |
| `streetAddress` | MAY | MAY | SHALL NOT |
| `localityName` | MAY | MAY | MAY |
| `stateOrProvinceName` | MAY | MAY | MAY |
| `postalCode` | MAY | MAY | SHALL NOT |
| `countryName` | MAY | MAY | MAY |
| Other | MAY | SHALL NOT | SHALL NOT |

**Note**: 

 1. Legacy Generation profiles MAY omit the `subject:givenName`, `subject:surname`, and `subject:pseudonym` attributes and include only the `subject:commonName` as described in [Section 7.1.4.2.2(a)](#71422-subject-distinguished-name-fields).
 2. Multipurpose and Strict Generation profiles SHALL include either `subject:givenName` and/or `subject:surname`, or the `subject:pseudonym`. 


##### 7.1.4.2.6 Subject DN attributes for individual-validated profile

| Attribute | Legacy<br> (See Note 1) | Multipurpose<br> (See Note 2) | Strict<br> (See Note 2) |
|-----------|--------|----------------|--------|
| `commonName` | MAY  | MAY | MAY | 
| `organizationName` | SHALL NOT | SHALL NOT | SHALL NOT |
| `organizationalUnitName` | SHALL NOT | SHALL NOT | SHALL NOT |
| `organizationIdentifier` | SHALL NOT | SHALL NOT | SHALL NOT |
| `givenName` | MAY | MAY | MAY |
| `surname` | MAY | MAY | MAY |
| `pseudonym` | MAY | MAY | MAY |
| `serialNumber` | MAY | MAY | MAY |
| `emailAddress` | MAY | MAY | MAY |
| `title` | MAY  | MAY | MAY |
| `streetAddress` | MAY | MAY | SHALL NOT |
| `localityName` | MAY | MAY | MAY |
| `stateOrProvinceName` | MAY | MAY | MAY |
| `postalCode` | MAY | MAY | SHALL NOT |
| `countryName` | MAY | MAY | MAY |
| Other | MAY | SHALL NOT | SHALL NOT |

**Note**: 

 1. Legacy Generation profiles MAY omit the `subject:givenName`, `subject:surname`, and `subject:pseudonym` attributes and include only the `subject:commonName` as described in [Section 7.1.4.2.2(a)](#71422-subject-distinguished-name-fields).
 2. Strict and Multipurpose Generation profiles SHALL include either `subject:givenName` and/or `subject:surname`, or the `subject:pseudonym`. 

#### 7.1.4.3 Subscriber Certificate Common Name Attribute

If present, this attribute MUST contain exactly one entry that is one of the values contained in the Certificate's `subjectAltName` extension (see [Section 7.1.2.7.12](#712712-subscriber-certificate-subject-alternative-name)). The value of the field MUST be encoded as follows:

  * If the value is an IPv4 address, then the value MUST be encoded as an IPv4Address as specified in RFC 3986, Section 3.2.2.
  * If the value is an IPv6 address, then the value MUST be encoded in the text representation specified in RFC 5952, Section 4.
  * If the value is a Fully-Qualified Domain Name or Wildcard Domain Name, then the value MUST be encoded as a character-for-character copy of the `dNSName` entry value from the `subjectAltName` extension. Specifically, all Domain Labels of the Fully-Qualified Domain Name or FQDN portion of the Wildcard Domain Name must be encoded as LDH Labels, and P-Labels MUST NOT be converted to their Unicode representation.

#### 7.1.4.3 Subject information - root certificates and subordinate CA certificates

By issuing a Subordinate CA Certificate, the CA represents that it followed the procedure set forth in its CP and/or CPS to verify that, as of the Certificate's issuance date, all of the Subject Information was accurate.

##### 7.1.4.3.1 Subject distinguished name fields

a. __Certificate Field:__ `subject:commonName` (OID 2.5.4.3)  
   __Required/Optional:__ SHALL be present  
   __Contents:__ This field SHOULD contain an identifier for the Certificate such that the Certificate's Name is unique across all Certificates issued by the Issuing CA.

b. __Certificate Field:__ `subject:organizationName` (OID 2.5.4.10)  
   __Required/Optional:__ SHALL be present  
   __Contents:__ This field SHALL contain either the Subject CA's name or DBA as verified under [Section 3.2.3.2.2](#32322-verification-of-assumed-name) The CA MAY include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations; e.g., if the official record shows "Company Name Incorporated", the CA MAY use "Company Name Inc." or "Company Name".

c. __Certificate Field:__ `subject:countryName` (OID: 2.5.4.6)  
   __Required/Optional:__ SHALL be present  
   __Contents:__ This field SHALL contain the two‐letter ISO 3166‐1 country code for the country in which the CA's place of business is located.

d. Other Subject Attributes  
   Other attributes MAY be present within the subject field. If present, other attributes SHALL contain information that has been verified by the CA.

#### 7.1.4.4 Other Subject Attributes

When explicitly stated as permitted by the relevant certificate profile specified within [Section 7.1.2](#712-certificate-content-and-extensions), CAs MAY include additional attributes within the `AttributeTypeAndValue` beyond those specified in [Section 7.1.4.2](#7142-subject-attribute-encoding).

Before including such an attribute, the CA SHALL:

  * Document the attributes within Section 7.1.4 of their CP or CPS, along with the applicable validation practices.
  * Ensure that the contents contain information that has been verified by the CA, independent of the Applicant.

### 7.1.5 Name constraints

For a Subordinate CA Certificate to be considered Technically Constrained, the Certificate SHALL include an Extended Key Usage (EKU) extension specifying all extended key usages for which the Subordinate CA Certificate is authorized to issue Certificates. The `anyExtendedKeyUsage` KeyPurposeId SHALL NOT appear within this extension.

If the Subordinate CA Certificate includes the `id-kp-emailProtection` extended key usage, then for the Subordinate CA Certificate to be considered Technically Constrained it SHALL include the `nameConstraints` X.509v3 extension with constraints on `rfc822Name` and `directoryName` as follows:

   1. For each `rfc822Name` in `permittedSubtrees`, each `rfc822Name` SHALL contain either a FQDN or a U+002E FULL STOP (".") character followed by a FQDN. The `rfc822Name` SHALL NOT contain an email address. The CA SHALL confirm that the Applicant has registered the FQDN contained in the `rfc822Name` or has been authorized by the domain registrant to act on the registrant's behalf in line with the verification practices of [Section 3.2.2.3](#3223-validating-applicant-as-operator-of-associated-mail-servers).

   2. For each `directoryName` in `permittedSubtrees`, the CA SHALL confirm the Applicant's and/or Subsidiary's Organizational name and location such that end entity Certificates issued from the Subordinate CA Certificate will be in compliance with [Section 7.1.2.4](#7124-all-certificates).

### 7.1.6 Certificate policy object identifier

### 7.1.6 Certificate policy object identifier

This section describes the content requirements for the Root CA, Subordinate CA, and Subscriber Certificates as they relate to the identification of Certificate Policy.

#### 7.1.6.1 Reserved Certificate Policy Identifiers

The following Certificate Policy identifiers are reserved for use by CAs as an optional means of asserting that a Certificate complies with these Requirements.

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) domain-validated(1)} (2.23.140.1.2.1)`

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) organization-validated(2)} (2.23.140.1.2.2)`

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) individual-validated(3)} (2.23.140.1.2.3)`

`{joint‐iso‐itu‐t(2) international‐organizations(23) ca‐browser‐forum(140) certificate‐policies(1) ev-guidelines(1)} (2.23.140.1.1)`

#### 7.1.6.1 Reserved certificate policy identifiers

The following CA/Browser Forum Certificate Policy identifiers are reserved for use by CAs to assert that a Certificate complies with these Requirements.

| Certificate Type | Generation | Policy Identifier |
| ---------------- | ---------- | ----------------- |
| `Mailbox-validated` | Legacy | `2.23.140.1.5.1.1` |
| `Mailbox-validated` | Multipurpose | `2.23.140.1.5.1.2` |
| `Mailbox-validated` | Strict | `2.23.140.1.5.1.3` |
| `Organization-validated` | Legacy | `2.23.140.1.5.2.1` |
| `Organization-validated` | Multipurpose | `2.23.140.1.5.2.2` |
| `Organization-validated` | Strict | `2.23.140.1.5.2.3` |
| `Sponsor-validated` | Legacy | `2.23.140.1.5.3.1` |
| `Sponsor-validated` | Multipurpose | `2.23.140.1.5.3.2` |
| `Sponsor-validated` | Strict | `2.23.140.1.5.3.3` |
| `Individual-validated` | Legacy | `2.23.140.1.5.4.1` |
| `Individual-validated` | Multipurpose | `2.23.140.1.5.4.2` |
| `Individual-validated` | Strict | `2.23.140.1.5.4.3` |

#### 7.1.6.2 Root CA certificates

A Root CA Certificate SHOULD NOT contain the `certificatePolicies` extension. If present, the extension SHALL conform to the requirements set forth for Certificates issued to Subordinate CAs in [Section 7.1.6.3](#7163-subordinate-ca-certificates).

#### 7.1.6.3 Subordinate CA certificates

A Certificate issued to a Subordinate CA that is not an Affiliate of the Issuing CA:

1. SHALL include one or more explicit policy identifiers defined in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers) that indicate the Subordinate CA's adherence to and compliance with these Requirements and MAY contain one or more identifiers documented by the Subordinate CA in its CP and/or CPS; and
2. SHALL NOT contain the `anyPolicy` identifier (2.5.29.32.0).

A Certificate issued to a Subordinate CA that is an Affiliate of the Issuing CA SHALL include a set of policy identifiers from one of the two options below:

1. One or more explicit policy identifiers defined in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers) that indicate the Subordinate CA's adherence to and compliance with these Requirements and MAY contain one or more identifiers documented by the Subordinate CA in its CP and/or CPS; or
2. The `anyPolicy` identifier (2.5.29.32.0).

The Subordinate CA and the Issuing CA SHALL represent, in their CP and/or CPS, that all Certificates containing a policy identifier indicating compliance with these Requirements are issued and managed in accordance with these Requirements.

#### 7.1.6.4 Subscriber certificates

A Certificate issued to a Subscriber SHALL contain, within the Certificate's `certificatePolicies` extension, a policy identifier that is specified in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers).

The Certificate MAY also contain additional policy identifier(s) defined by the Issuing CA. The Issuing CA SHALL document in its CP and/or CPS that the Certificates it issues containing the specified policy identifier(s) are managed in accordance with these Requirements.

### 7.1.7 Usage of Policy Constraints extension

### 7.1.8 Policy qualifiers syntax and semantics

### 7.1.9 Processing semantics for the critical Certificate Policies extension

## 7.2 CRL profile

Prior to 2024‐03‐15, the CA SHALL issue CRLs in accordance with the profile specified in these Requirements or the profile specified in Version 1.8.7 of the Baseline Requirements for the Issuance and Management of Publicly‐Trusted Certificates. Effective 2024‐03‐15, the CA SHALL issue CRLs in accordance with the profile specified in these Requirements.

If the CA asserts compliance with these Baseline Requirements, all CRLs that it issues MUST comply with the following CRL profile, which incorporates, and is derived from [RFC 5280](https://tools.ietf.org/html/rfc5280). Except as explicitly noted, all normative requirements imposed by RFC 5280 shall apply, in addition to the normative requirements imposed by this document. CAs SHOULD examine [RFC 5280, Appendix B](https://tools.ietf.org/html/rfc5280#appendix-B) for further issues to be aware of.

A full and complete CRL is a CRL whose scope includes all Certificates issued by the CA.

A partitioned CRL (sometimes referred to as a "sharded CRL") is a CRL with a constrained scope, such as all Certificates issued by the CA during a certain period of time ("temporal sharding"). Aside from the presence of the Issuing Distribution Point extension (OID 2.5.29.28) in partitioned CRLs, both CRL formats are syntactically the same from the perspective of this profile.

Minimally, CAs MUST issue either a "full and complete" CRL or a set of "partitioned" CRLs which cover the complete set of Certificates issued by the CA. In other words, if issuing only partitioned CRLs, the combined scope of those CRLs must be equivalent to that of a full and complete CRL. 

CAs MUST NOT issue indirect CRLs (i.e., the issuer of the CRL is not the issuer of all Certificates that are included in the scope of the CRL).

Table: CRL Fields

| __Field__                  | __Presence__    | __Description__ |
| ---                        | ------          | ------          |
| `tbsCertList`              |                 |                 |
|     `version`              | MUST            | MUST be v2(1), see [Section 7.2.1](#721-version-numbers) |
|     `signature`            | MUST            | See [Section 7.1.3.2](#7132-signature-algorithmidentifier) |
|     `issuer`               | MUST            | MUST be byte-for-byte identical to the `subject` field of the Issuing CA. |
|     `thisUpdate`           | MUST            | Indicates the issue date of the CRL. |
|     `nextUpdate`           | MUST            | Indicates the date by which the next CRL will be issued. For CRLs covering Subscriber Certificates, at most 10 days after the `thisUpdate`. For other CRLs, at most 12 months after the `thisUpdate`. |
|     `revokedCertificates`  | *               | MUST be present if the CA has issued a Certificate that has been revoked and the corresponding entry has yet to appear on at least one regularly scheduled CRL beyond the revoked Certificate's validity period. The CA SHOULD remove an entry for a corresponding Certificate after it has appeared on at least one regularly scheduled CRL beyond the revoked Certificate's validity period. See the "revokedCertificates Component" table for additional requirements.  |
|     `extensions`           | MUST            | See the "CRL Extensions" table for additional requirements. |
| `signatureAlgorithm`       | MUST            | Encoded value MUST be byte-for-byte identical to the `tbsCertList.signature`. |
| `signature`                | MUST            | - |
| Any other value            | NOT RECOMMENDED | - |

## 7.2 CRL profile

### 7.2.1 Version number(s)

Certificate Revocation Lists MUST be of type X.509 v2.

### 7.2.1 Version number(s)


### 7.2.2 CRL and CRL entry extensions

Table: CRL Extensions

| __Extension__              | __Presence__    | __Critical__ | __Description__ |
| ----                       | -               | -            | ----- |
| `authorityKeyIdentifier`   | MUST            | N            | See [Section 7.1.2.11.1](#712111-authority-key-identifier) |
| `CRLNumber`                | MUST            | N            | MUST contain an INTEGER greater than or equal to zero (0) and less than 2¹⁵⁹, and convey a strictly increasing sequence. |
| `IssuingDistributionPoint` | *               | Y            | See [Section 7.2.2.1 CRL Issuing Distribution Point](#7221-crl-issuing-distribution-point) |
| Any other extension        | NOT RECOMMENDED | -            | - |

Table: revokedCertificates Component

| __Component__        | __Presence__ | __Description__ |
| ----                 | -            | ----- |
| `serialNumber`       | MUST         | MUST be byte-for-byte identical to the serialNumber contained in the revoked Certificate. |
| `revocationDate`     | MUST         | Normally, the date and time revocation occurred. See the footnote following this table for circumstances where backdating is permitted. | 
| `crlEntryExtensions` | *            | See the "crlEntryExtensions Component" table for additional requirements. |

**Note:** The CA SHOULD update the revocation date in a CRL entry when it is determined that the private key of the Certificate was compromised prior to the revocation date that is indicated in the CRL entry for that Certificate. Backdating the revocationDate field is an exception to best practice described in RFC 5280 (Section 5.3.2); however, these requirements specify the use of the revocationDate field to support TLS implementations that process the revocationDate field as the date when the Certificate is first considered to be compromised.

Table: crlEntryExtensions Component 

| __CRL Entry Extension__   | __Presence__    | __Description__ |
| ---                       | -               | ------          |
| `reasonCode`              | *               | When present (OID 2.5.29.21), MUST NOT be marked critical and MUST indicate the most appropriate reason for revocation of the Certificate. <br><br> MUST be present unless the CRL entry is for a Certificate not technically capable of causing issuance and either 1) the CRL entry is for a Subscriber Certificate subject to these Requirements revoked prior to July 15, 2023 or 2) the reason for revocation (i.e., reasonCode) is unspecified (0). <br><br>See the "CRLReasons" table for additional requirements. |
| Any other value           | NOT RECOMMENDED | - |

Table: CRLReasons

| __RFC 5280 reasonCode__   | __RFC 5280 reasonCode value__ | __Description__ |
| ---                       | -    | ------          |
| unspecified               | 0    | Represented by the omission of a reasonCode. MUST be omitted if the CRL entry is for a Certificate not technically capable of causing issuance unless the CRL entry is for a Subscriber Certificate subject to these Requirements revoked prior to July 15, 2023. 
| keyCompromise             | 1    | Indicates that it is known or suspected that the Subscriber’s Private Key has been compromised. |
| affiliationChanged        | 3    | Indicates that the Subject's name or other Subject Identity Information in the Certificate has changed, but there is no cause to suspect that the Certificate's Private Key has been compromised. |
| superseded                | 4    | Indicates that the Certificate is being replaced because: the Subscriber has requested a new Certificate, the CA has reasonable evidence that the validation of domain authorization or control for any fully‐qualified domain name or IP address in the Certificate should not be relied upon, or the CA has revoked the Certificate for compliance reasons such as the Certificate does not comply with these Baseline Requirements or the CA's CP or CPS. |
| cessationOfOperation      | 5    | Indicates that the website with the Certificate is shut down prior to the expiration of the Certificate, or if the Subscriber no longer owns or controls the Domain Name in the Certificate prior to the expiration of the Certificate.
| certificateHold           | 6    | MUST NOT be included if the CRL entry is for 1) a Certificate subject to these Requirements, or 2) a Certificate not subject to these Requirements and was either A) issued on-or-after 2020-09-30 or B) has a `notBefore` on-or-after 2020-09-30.
| privilegeWithdrawn        | 9    | Indicates that there has been a subscriber-side infraction that has not resulted in keyCompromise, such as the Certificate Subscriber provided misleading information in their Certificate Request or has not upheld their material obligations under the Subscriber Agreement or Terms of Use. |

The Subscriber Agreement, or an online resource referenced therein, MUST inform Subscribers about the revocation reason options listed above and provide explanation about when to choose each option. Tools that the CA provides to the Subscriber MUST allow for these options to be easily specified when the Subscriber requests revocation of their Certificate, with the default value being that no revocation reason is provided (i.e. the default corresponds to the CRLReason “unspecified (0)” which results in no reasonCode extension being provided in the CRL). 

The privilegeWithdrawn reasonCode SHOULD NOT be made available to the Subscriber as a revocation reason option, because the use of this reasonCode is determined by the CA and not the Subscriber.

When a CA obtains verifiable evidence of Key Compromise for a Certificate whose CRL entry does not contain a reasonCode extension or has a reasonCode extension with a non-keyCompromise reason, the CA SHOULD update the CRL entry to enter keyCompromise as the CRLReason in the reasonCode extension. 

### 7.2.2 CRL and CRL entry extensions

If present, the `reasonCode` (OID 2.5.29.21) extension SHALL NOT be marked critical.

If a CRL entry is for a Root CA or Subordinate CA Certificate, including Cross Certificates, this CRL entry extension SHALL be present. The `CRLreason` of certificateHold (6) SHALL NOT be used for Root CA or Subordinate CA Certificates.

If a CRL entry is for a Certificate not technically capable of causing issuance, this CRL entry extension SHOULD be present, but MAY be omitted, subject to the following requirements.

The `CRLReason` indicated SHALL NOT be unspecified (0). If the reason for revocation is unspecified, CAs SHALL omit the `reasonCode` entry extension. 

The Repository MAY include CRL entries that have a `CRLreason` of certificateHold (6) for Certificates that include the Certificate Policy identifiers for the Legacy or Multipurpose Generations. The Repository SHALL NOT include CRL entries that have a `CRLreason` of certificateHold (6) for Certificates that include the Certificate Policy identifiers for the Strict Generation.

If a `reasonCode` CRL entry extension is present, the `CRLReason` SHALL indicate the most appropriate reason for revocation of the Certificate, as defined by the CA within its CP/CPS.

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

## 7.3 OCSP profile

If an OCSP response is for a Root CA or Subordinate CA Certificate, including Cross-Certified Subordinate CA Certificates, and that certificate has been revoked, then the `revocationReason` field within the `RevokedInfo` of the `CertStatus` MUST be present.

The `CRLReason` indicated MUST contain a value permitted for CRLs, as specified in [Section 7.2.2](#722-crl-and-crl-entry-extensions).

## 7.3 OCSP profile

If an OCSP response is for a Root CA or Subordinate CA Certificate, including Cross Certificates, and that Certificate has been revoked, then the `revocationReason` field within the `RevokedInfo` of the `CertStatus` SHALL be present.

The `CRLReason` indicated SHALL contain a value permitted for CRLs, as specified in [Section 7.2.2](#722-crl-and-crl-entry-extensions).

### 7.3.1 Version number(s)

### 7.3.2 OCSP extensions

The `singleExtensions` of an OCSP response MUST NOT contain the `reasonCode` (OID 2.5.29.21) CRL entry extension.

### 7.3.2 OCSP extensions

The `singleExtensions` of an OCSP response SHALL NOT contain the `reasonCode` (OID 2.5.29.21) CRL entry extension.

# 8. COMPLIANCE AUDIT AND OTHER ASSESSMENTS

The CA SHALL at all times:

1. Comply with these Requirements;
2. Comply with the audit requirements set forth in this section; and
3. Be licensed as a CA in each jurisdiction where it operates, if licensing is required by the law of such jurisdiction for the issuance of Certificates.

**Implementers' Note**: Version 1.1.6 of the SSL Baseline Requirements was published on July 29, 2013. Version 2.0 of WebTrust's Principles and Criteria for Certification Authorities - SSL Baseline with Network Security and ETSI's Electronic Signatures and Infrastructures (ESI) 102 042 incorporate version 1.1.6 of these Baseline Requirements and version 1.0 of the Network and Certificate System Security Requirements. The CA/Browser Forum continues to improve the Baseline Requirements while WebTrust and ETSI also continue to update their audit criteria. We encourage all CAs to conform to each revision herein on the date specified without awaiting a corresponding update to an applicable audit criterion. In the event of a conflict between an existing audit criterion and a guideline revision, we will communicate with the audit community and attempt to resolve any uncertainty, and we will respond to implementation questions directed to <questions@cabforum.org>. Our coordination with compliance auditors will continue as we develop guideline revision cycles that harmonize with the revision cycles for audit criteria, the compliance auditing periods and cycles of CAs, and the CA/Browser Forum's guideline implementation dates.

# 8. COMPLIANCE AUDIT AND OTHER ASSESSMENTS

The CA SHALL at all times:

1. Issue Certificates and operate its PKI in accordance with all law applicable to its business and the Certificates it issues in every jurisdiction in which it operates;
2. Comply with these Requirements;
3. Comply with the audit requirements set forth in this section; and
4. Be licensed as a CA in each jurisdiction where it operates, if licensing is required by the law of such jurisdiction for the issuance of Certificates.

**Note**: The CA/Browser Forum continues to improve the S/MIME Baseline Requirements while CPA Canada/WebTrust and ETSI also continue to update their audit criteria. We encourage all CAs to conform to each revision herein on the date specified without awaiting a corresponding update to an applicable audit criterion. In the event of a conflict between an existing audit criterion and a revision to the S/MIME Baseline Requirements, we will communicate with the audit community and attempt to resolve any uncertainty, and we will respond to implementation questions directed to <questions@cabforum.org>. 

## 8.1 Frequency or circumstances of assessment

Certificates that are capable of being used to issue new certificates MUST either be Technically Constrained in line with [Section 7.1.2.3](#7123-technically-constrained-non-tls-subordinate-ca-certificate-profile), [Section 7.1.2.4](#7124-technically-constrained-precertificate-signing-ca-certificate-profile), or [Section 7.1.2.5](#7125-technically-constrained-tls-subordinate-ca-certificate-profile), as well as audited in line with [Section 8.7](#87-self-audits) only, or Unconstrained and fully audited in line with all remaining requirements from this section. A Certificate is deemed as capable of being used to issue new certificates if it contains an X.509v3 `basicConstraints` extension, with the `cA` boolean set to true and is therefore by definition a Root CA Certificate or a Subordinate CA Certificate.

The period during which the CA issues Certificates SHALL be divided into an unbroken sequence of audit periods. An audit period MUST NOT exceed one year in duration.

If the CA has a currently valid Audit Report indicating compliance with an audit scheme listed in [Section 8.4](#84-topics-covered-by-assessment), then no pre-issuance readiness assessment is necessary.

If the CA does not have a currently valid Audit Report indicating compliance with one of the audit schemes listed in [Section 8.4](#84-topics-covered-by-assessment), then, before issuing Publicly-Trusted Certificates, the CA SHALL successfully complete a point-in-time readiness assessment performed in accordance with applicable standards under one of the audit schemes listed in [Section 8.4](#84-topics-covered-by-assessment). The point-in-time readiness assessment SHALL be completed no earlier than twelve (12) months prior to issuing Publicly-Trusted Certificates and SHALL be followed by a complete audit under such scheme within ninety (90) days of issuing the first Publicly-Trusted Certificate.

## 8.1 Frequency or circumstances of assessment

Certificates that are capable of being used to issue new Certificates SHALL either be Technically Constrained in line with [Section 7.1.5](#715-name-constraints) and audited in line with [Section 8.8](#88-review-of-delegated-parties) only, or unconstrained and fully audited in line with all remaining requirements from this section. A Certificate is deemed as capable of being used to issue new Certificates if it contains an X.509v3 `basicConstraints` extension, with the `cA` boolean set to true and is therefore by definition a Root CA Certificate or a Subordinate CA Certificate.

The period during which the CA issues Certificates SHALL be divided into an unbroken sequence of audit periods. An audit period SHALL NOT exceed one year in duration.

If the CA has a currently valid Audit Report indicating compliance with an audit scheme listed in [Section 8.4](#84-topics-covered-by-assessment), then no pre-issuance readiness assessment is necessary.

If the CA does not have a currently valid Audit Report indicating compliance with one of the audit schemes listed in [Section 8.4](#84-topics-covered-by-assessment), then, before issuing Publicly-Trusted S/MIME Certificates, the CA SHALL successfully complete a point-in-time readiness assessment performed in accordance with applicable standards under one of the audit schemes listed in [Section 8.4](#84-topics-covered-by-assessment). The point-in-time readiness assessment SHALL be completed no earlier than twelve (12) months prior to issuing Publicly-Trusted S/MIME Certificates and SHALL be followed by a complete audit under such scheme within ninety (90) days of issuing the first Publicly-Trusted S/MIME Certificate.

## 8.2 Identity/qualifications of assessor

The CA's audit SHALL be performed by a Qualified Auditor. A Qualified Auditor means a natural person, Legal Entity, or group of natural persons or Legal Entities that collectively possess the following qualifications and skills:

1. Independence from the subject of the audit;
2. The ability to conduct an audit that addresses the criteria specified in an Eligible Audit Scheme (see [Section 8.4](#84-topics-covered-by-assessment));
3. Employs individuals who have proficiency in examining Public Key Infrastructure technology, information security tools and techniques, information technology and security auditing, and the third-party attestation function;
4. (For audits conducted in accordance with any one of the ETSI standards) accredited in accordance with ISO 17065 applying the requirements specified in ETSI EN 319 403;
5. (For audits conducted in accordance with the WebTrust standard) licensed by WebTrust;
6. Bound by law, government regulation, or professional code of ethics; and
7. Except in the case of an Internal Government Auditing Agency, maintains Professional Liability/Errors & Omissions insurance with policy limits of at least one million US dollars in coverage

## 8.2 Identity/qualifications of assessor

The CA's audit SHALL be performed by a Qualified Auditor. A Qualified Auditor means a Natural Person, Legal Entity, or group of Natural Persons or Legal Entities that collectively possess the following qualifications and skills:

1. Independence from the subject of the audit;
2. The ability to conduct an audit that addresses the criteria specified in an Eligible Audit Scheme (see [Section 8.4](#84-topics-covered-by-assessment));
3. Employs individuals who have proficiency in examining Public Key Infrastructure technology, information security tools and techniques, information technology and security auditing, and the third-party attestation function;
4. (For audits conducted in accordance with any one of the ETSI standards) accredited in accordance with ISO 17065 applying the requirements specified in ETSI EN 319 403 or ETSI EN 319 403-1;
5. (For audits conducted in accordance with the WebTrust standard) licensed for WebTrust by CPA Canada;
6. Bound by law, government regulation, or professional code of ethics; and
7. Except in the case of an Internal Government Auditing Agency, maintains Professional Liability/Errors & Omissions insurance with policy limits of at least one million US dollars in coverage.
   
## 8.3 Assessor's relationship to assessed entity

## 8.4 Topics covered by assessment

The CA SHALL undergo an audit in accordance with one of the following schemes:

1. “WebTrust for CAs v2.1 or newer” AND “WebTrust for CAs SSL Baseline with Network Security v2.3 or newer”; or
2. ETSI EN 319 411-1 v1.2.2, which includes normative references to ETSI EN 319 401 (the latest version of the referenced ETSI documents should be applied); or
3. If a Government CA is required by its Certificate Policy to use a different internal audit scheme, it MAY use such scheme provided that the audit either
   a. encompasses all requirements of one of the above schemes or
   b. consists of comparable criteria that are available for public review.

Whichever scheme is chosen, it MUST incorporate periodic monitoring and/or accountability procedures to ensure that its audits continue to be conducted in accordance with the requirements of the scheme.

The audit MUST be conducted by a Qualified Auditor, as specified in [Section 8.2](#82-identityqualifications-of-assessor).

For Delegated Third Parties which are not Enterprise RAs, then the CA SHALL obtain an audit report, issued under the auditing standards that underlie the accepted audit schemes found in [Section 8.4](#84-topics-covered-by-assessment), that provides an opinion whether the Delegated Third Party's performance complies with either the Delegated Third Party's practice statement or the CA's Certificate Policy and/or Certification Practice Statement. If the opinion is that the Delegated Third Party does not comply, then the CA SHALL not allow the Delegated Third Party to continue performing delegated functions.

The audit period for the Delegated Third Party SHALL NOT exceed one year (ideally aligned with the CA's audit). However, if the CA or Delegated Third Party is under the operation, control, or supervision of a Government Entity and the audit scheme is completed over multiple years, then the annual audit MUST cover at least the core controls that are required to be audited annually by such scheme plus that portion of all non-core controls that are allowed to be conducted less frequently, but in no case may any non-core control be audited less often than once every three years.

## 8.4 Topics covered by assessment

The CA SHALL undergo an audit in accordance with one of the following schemes:

1. For Audit Periods starting before the Effective Date defined in [Section 1.2.1](#121-revisions) of the first version of these Requirements, “WebTrust for CAs v2.2.2 or newer”; or
2. For Audit Periods starting after the Effective Date defined in [Section 1.2.1](#121-revisions) of the first version of these Requirements, “WebTrust for CAs v2.2.2 or newer” AND “WebTrust for S/MIME Baseline Requirements v1.0.0 or newer”; or
3. ETSI TS 119 411-6 v1.1.1 or newer, which includes normative references to ETSI EN 319 401, ETSI EN 319 411-1 and ETSI EN 319 411-2 (the latest version of the referenced ETSI documents should be applied); or
4. If a Government CA is required by its Certificate Policy to use a different internal audit scheme, it MAY use such scheme provided that the audit either
   a. encompasses all requirements of one of the above schemes; or
   b. consists of comparable criteria that are available for public review.
Whichever scheme is chosen, it SHALL incorporate periodic monitoring and/or accountability procedures to ensure that its audits continue to be conducted in accordance with the requirements of the scheme.

The audit SHALL be conducted by a Qualified Auditor, as specified in [Section 8.2](#82-identityqualifications-of-assessor).

For Delegated Third Parties that are not Enterprise RAs, then the CA SHALL obtain an audit report, issued under the auditing standards that underlie the accepted audit schemes found above in this [Section 8.4](#84-topics-covered-by-assessment), that provides an opinion whether the Delegated Third Party's performance complies with either the Delegated Third Party's practice statement or the CA's CP and/or CPS as described in [Section 1.3.2](#132-registration-authorities). If the opinion is that the Delegated Third Party does not comply, then the CA SHALL not allow the Delegated Third Party to continue performing delegated functions.

The audit period for the Delegated Third Party SHALL NOT exceed one year (ideally aligned with the CA's audit). 

## 8.5 Actions taken as a result of deficiency

## 8.6 Communication of results

The Audit Report SHALL state explicitly that it covers the relevant systems and processes used in the issuance of all Certificates that assert one or more of the policy identifiers listed in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers). The CA SHALL make the Audit Report publicly available.

The CA MUST make its Audit Report publicly available no later than three months after the end of the audit period. In the event of a delay greater than three months, the CA SHALL provide an explanatory letter signed by the Qualified Auditor.

The Audit Report MUST contain at least the following clearly-labelled information:

1. name of the organization being audited;
2. name and address of the organization performing the audit;
3. the SHA-256 fingerprint of all Roots and Subordinate CA Certificates, including Cross-Certified Subordinate CA Certificates, that were in-scope of the audit;
4. audit criteria, with version number(s), that were used to audit each of the certificates (and associated keys);
5. a list of the CA policy documents, with version numbers, referenced during the audit;
6. whether the audit assessed a period of time or a point in time;
7. the start date and end date of the Audit Period, for those that cover a period of time;
8. the point in time date, for those that are for a point in time;
9. the date the report was issued, which will necessarily be after the end date or point in time date; and
10. (for audits conducted in accordance with any of the ETSI standards) a statement to indicate if the audit was a full audit or a surveillance audit, and which portions of the criteria were applied and evaluated, e.g. DVCP, OVCP, NCP, NCP+, LCP, EVCP, EVCP+, QCP-w, Part 1 (General Requirements), and/or Part 2 (Requirements for Trust Service Providers).
11. (for audits conducted in accordance with any of the ETSI standards) a statement to indicate that the auditor referenced the applicable CA/Browser Forum criteria, such as this document, and the version used.

An authoritative English language version of the publicly available audit information MUST be provided by the Qualified Auditor and the CA SHALL ensure it is publicly available.

The Audit Report MUST be available as a PDF, and SHALL be text searchable for all information required. Each SHA-256 fingerprint within the Audit Report MUST be uppercase letters and MUST NOT contain colons, spaces, or line feeds.

## 8.6 Communication of results

The Audit Report SHALL state explicitly that it covers the relevant systems and processes used in the issuance of all Certificates that assert one or more of the policy identifiers listed in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers). The CA SHALL make the Audit Report publicly available.

The CA SHALL make its Audit Report publicly available no later than three months after the end of the audit period. In the event of a delay greater than three months, the CA SHALL provide an explanatory letter signed by the Qualified Auditor.

The Audit Report SHALL contain at least the following clearly-labelled information:

1. Name of the organization being audited;
2. Name and address of the organization performing the audit;
3. The SHA-256 fingerprint of all Roots and Subordinate CA Certificates, including Cross Certificates, that were in-scope of the audit;
4. Audit criteria, with version number(s), that were used to audit each of the Certificates (and associated keys);
5. A list of the CA policy documents, with version numbers, referenced during the audit;
6. Whether the audit assessed a period of time or a point in time;
7. The start date and end date of the Audit Period, for those that cover a period of time;
8. The point in time date, for those that are for a point in time;
9. The date the report was issued, which will necessarily be after the end date or point in time date; 
10. (For audits conducted in accordance with any of the ETSI standards) a statement to indicate if the audit was a full audit or a surveillance audit, and which portions of the criteria were applied and evaluated, e.g., ETSI EN 319 401, ETSI TS 119 411-6, ETSI EN 319 411-1 policy LCP, NCP or NCP+, ETSI EN 319 411-2 policy QCP-n, QCP-n-qscd, QCP-l or QCP-l-qscd; and
11. (For audits conducted in accordance with any of the ETSI standards) a statement to indicate that the auditor referenced the applicable CA/Browser Forum criteria, such as this document, and the version used.

An authoritative English language version of the publicly available audit information SHALL be provided by the Qualified Auditor and the CA SHALL ensure that it is publicly available.

The Audit Report SHALL be available as a PDF, and SHALL be text searchable for all information required. Each SHA-256 fingerprint within the Audit Report SHALL be uppercase letters and SHALL NOT contain colons, spaces, or line feeds. See https://www.ccadb.org/policy#51-audit-statement-content for more information.

## 8.7 Self-Audits

During the period in which the CA issues Certificates, the CA SHALL monitor adherence to its Certificate Policy, Certification Practice Statement and these Requirements and strictly control its service quality by performing self audits on at least a quarterly basis against a randomly selected sample of the greater of one certificate or at least three percent of the Certificates issued by it during the period commencing immediately after the previous self-audit sample was taken. Except for Delegated Third Parties that undergo an annual audit that meets the criteria specified in [Section 8.4](#84-topics-covered-by-assessment), the CA SHALL strictly control the service quality of Certificates issued or containing information verified by a Delegated Third Party by having a Validation Specialist employed by the CA perform ongoing quarterly audits against a randomly selected sample of at least the greater of one certificate or three percent of the Certificates verified by the Delegated Third Party in the period beginning immediately after the last sample was taken. The CA SHALL review each Delegated Third Party's practices and procedures to ensure that the Delegated Third Party is in compliance with these Requirements and the relevant Certificate Policy and/or Certification Practice Statement.

The CA SHALL internally audit each Delegated Third Party's compliance with these Requirements on an annual basis.

During the period in which a Technically Constrained Subordinate CA issues Certificates, the CA which signed the Subordinate CA SHALL monitor adherence to the CA's Certificate Policy and the Subordinate CA's Certification Practice Statement. On at least a quarterly basis, against a randomly selected sample of the greater of one certificate or at least three percent of the Certificates issued by the Subordinate CA, during the period commencing immediately after the previous audit sample was taken, the CA shall ensure all applicable CP are met.

## 8.7 Self audits

During the period in which the CA issues Certificates, the CA SHALL monitor adherence to its CP and/or CPS and these Requirements and control its service quality by performing self audits on at least a quarterly basis against a randomly selected sample including a minimum of the greater of thirty (30) Certificates or three percent (3%) of the Certificates issued by it during the period commencing immediately after the previous self-audit sample was taken. 

## 8.8 Review of delegated parties

Except for Delegated Third Parties, Enterprise RAs, and Technically Constrained Subordinate CAs that undergo an annual audit that meets the criteria specified in [Section 8.4](#84-topics-covered-by-assessment), the CA SHALL ensure the practices and procedures of delegated parties are in compliance with these Requirements and the relevant CP and/or CPS. The CA shall document the obligations of delegated parties and perform monitoring on at least an annual basis of the delegated parties' adherence with those obligations.

# 9. OTHER BUSINESS AND LEGAL MATTERS

## 9.1 Fees

### 9.1.1 Certificate issuance or renewal fees

### 9.1.2 Certificate access fees

### 9.1.3 Revocation or status information access fees

### 9.1.4 Fees for other services

### 9.1.5 Refund policy

## 9.2 Financial responsibility

### 9.2.1 Insurance coverage

### 9.2.2 Other assets

### 9.2.3 Insurance or warranty coverage for end-entities

## 9.3 Confidentiality of business information

### 9.3.1 Scope of confidential information

### 9.3.2 Information not within the scope of confidential information

### 9.3.3 Responsibility to protect confidential information

## 9.4 Privacy of personal information

### 9.4.1 Privacy plan

### 9.4.1 Privacy plan

The CA SHALL publish a Privacy Policy that provides information on the CA's data protection practices. The Privacy Policy SHOULD include information on how the CA collects, uses, shares, store, and deletes or retains data, as well as contact information for the exercise of privacy rights.  The CA SHALL document where to obtain this information within Section 9.4.1 of the CA's CP and/or CPS.  

### 9.4.2 Information treated as private

### 9.4.2 Information treated as private

The CA or RA SHALL treat all personal information about an Individual that is not publicly available in the contents of a Certificate as private information. This includes information that links a Pseudonym to the real identity of the Subject Individual. 

### 9.4.3 Information not deemed private

### 9.4.4 Responsibility to protect private information

### 9.4.4 Responsibility to protect private information

The CA or RA SHALL protect private information using appropriate safeguards and a reasonable degree of care. The CA or RA SHALL require the same from any service providers who handle private information on behalf of the CA or RA.

### 9.4.5 Notice and consent to use private information

### 9.4.5 Notice and consent to use private information

The CA or RA shall provide appropriate notices to, and receive the necessary consent, from Subject Individuals before using private information for any purpose other than providing services related to the issuance and management of Certificates. The CA or RA shall require the same from any service providers who handle private information on behalf of the CA or RA.

### 9.4.6 Disclosure pursuant to judicial or administrative process

### 9.4.7 Other information disclosure circumstances

## 9.5 Intellectual property rights

## 9.6 Representations and warranties

### 9.6.1 CA representations and warranties

By issuing a Certificate, the CA makes the certificate warranties listed herein to the following Certificate Beneficiaries:

1. The Subscriber that is a party to the Subscriber Agreement or Terms of Use for the Certificate;
2. All Application Software Suppliers with whom the Root CA has entered into a contract for inclusion of its Root Certificate in software distributed by such Application Software Supplier; and
3. All Relying Parties who reasonably rely on a Valid Certificate.
The CA represents and warrants to the Certificate Beneficiaries that, during the period when the Certificate is valid, the CA has complied with these Requirements and its Certificate Policy and/or Certification Practice Statement in issuing and managing the Certificate.

The Certificate Warranties specifically include, but are not limited to, the following:

1. **Right to Use Domain Name or IP Address**: That, at the time of issuance, the CA
   i. implemented a procedure for verifying that the Applicant either had the right to use, or had control of, the Domain Name(s) and IP address(es) listed in the Certificate's `subject` field and `subjectAltName` extension (or, only in the case of Domain Names, was delegated such right or control by someone who had such right to use or control);
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's Certificate Policy and/or Certification Practice Statement;
2. **Authorization for Certificate**: That, at the time of issuance, the CA
   i. implemented a procedure for verifying that the Subject authorized the issuance of the Certificate and that the Applicant Representative is authorized to request the Certificate on behalf of the Subject;
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's Certificate Policy and/or Certification Practice Statement;
3. **Accuracy of Information**: That, at the time of issuance, the CA
   i. implemented a procedure for verifying the accuracy of all of the information contained in the Certificate;
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's Certificate Policy and/or Certification Practice Statement;
4. **Identity of Applicant**: That, if the Certificate contains Subject Identity Information, the CA
   i. implemented a procedure to verify the identity of the Applicant in accordance with [Section 3.2](#32-initial-identity-validation) and [Section 7.1.2](#712-certificate-content-and-extensions);
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's Certificate Policy and/or Certification Practice Statement;
5. **Subscriber Agreement**: That, if the CA and Subscriber are not Affiliated, the Subscriber and CA are parties to a legally valid and enforceable Subscriber Agreement that satisfies these Requirements, or, if the CA and Subscriber are the same entity or are Affiliated, the Applicant Representative acknowledged the Terms of Use;
6. **Status**: That the CA maintains a 24 x 7 publicly-accessible Repository with current information regarding the status (valid or revoked) of all unexpired Certificates; and
7. **Revocation**: That the CA will revoke the Certificate for any of the reasons specified in these Requirements.

The Root CA SHALL be responsible for the performance and warranties of the Subordinate CA, for the Subordinate CA's compliance with these Requirements, and for all liabilities and indemnification obligations of the Subordinate CA under these Requirements, as if the Root CA were the Subordinate CA issuing the Certificates

### 9.6.1 CA representations and warranties

By issuing a Certificate, the CA makes the warranties listed herein to the following Certificate Beneficiaries:

1. The Subscriber that is a party to the Subscriber Agreement or Terms of Use for the Certificate;
2. All Application Software Suppliers with whom the Root CA has entered into a contract for inclusion of its Root CA Certificate in software distributed by such Application Software Supplier; and
3. All Relying Parties who reasonably rely on a Valid Certificate. 

The CA represents and warrants to the Certificate Beneficiaries that, during the period when the Certificate is valid, the CA has complied with these Requirements and its CP and/or CPS in issuing and managing the Certificate.

The Certificate Warranties specifically include, but are not limited to, the following:

1. **Right to Use Mailbox Address**: That, at the time of issuance, the CA:<br>
   i. implemented a procedure for verifying that the Applicant either had the right to use, or had control of, the Mailbox Addresses listed in the Certificate's `subject` field and `subjectAltName` extension (or was delegated such right or control by someone who had such right to use or control);
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's CP and/or CPS;
2. **Authorization for Certificate**: That, at the time of issuance, the CA:<br>
   i. implemented a procedure for verifying that the Subject authorized the issuance of the Certificate and that the Applicant Representative is authorized to request the Certificate on behalf of the Subject;
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's CP and/or CPS;
3. **Accuracy of Information**: That, at the time of issuance, the CA:<br>
   i. implemented a procedure for verifying the accuracy of all of the information contained in the Certificate (with the exception of the subject:serialNumber attribute);
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's CP and/or CPS;
4. **Identity of Applicant**: That, if the Certificate contains Subject Identity Information, the CA:<br>
   i. implemented a procedure to verify the identity of the Applicant in accordance with [Section 3.2](#32-initial-identity-validation) and [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields);
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's CP and/or CPS;
5. **Subscriber Agreement**: That, if the CA and Subscriber are not Affiliated, the Subscriber and CA are parties to a legally valid and enforceable Subscriber Agreement that satisfies these Requirements, or, if the CA and Subscriber are the same entity or are Affiliated, the Applicant Representative acknowledged the Terms of Use;
6. **Status**: That the CA maintains a 24 x 7 publicly-accessible Repository with current information regarding the status (Valid or Revoked) of all unexpired Certificates; and
7. **Revocation**: That the CA will revoke the Certificate for any of the reasons specified in these Requirements.

The Root CA SHALL be responsible for the performance and warranties, compliance with these Requirements, and for all liabilities and indemnification obligations of the Subordinate CA under these Requirements, as if the Root CA were the Subordinate CA issuing the Certificates.

### 9.6.2 RA representations and warranties


### 9.6.3 Subscriber representations and warranties

The CA SHALL require, as part of the Subscriber Agreement or Terms of Use, that the Applicant make the commitments and warranties in this section for the benefit of the CA and the Certificate Beneficiaries.

Prior to the issuance of a Certificate, the CA SHALL obtain, for the express benefit of the CA and the Certificate Beneficiaries, either:

1. The Applicant's agreement to the Subscriber Agreement with the CA, or
2. The Applicant's acknowledgement of the Terms of Use.

The CA SHALL implement a process to ensure that each Subscriber Agreement or Terms of Use is legally enforceable against the Applicant. In either case, the Agreement MUST apply to the Certificate to be issued pursuant to the certificate request. The CA MAY use an electronic or "click-through" Agreement provided that the CA has determined that such agreements are legally enforceable. A separate Agreement MAY be used for each certificate request, or a single Agreement MAY be used to cover multiple future certificate requests and the resulting Certificates, so long as each Certificate that the CA issues to the Applicant is clearly covered by that Subscriber Agreement or Terms of Use.

The Subscriber Agreement or Terms of Use MUST contain provisions imposing on the Applicant itself (or made by the Applicant on behalf of its principal or agent under a subcontractor or hosting service relationship) the following obligations and warranties:

1. **Accuracy of Information**: An obligation and warranty to provide accurate and complete information at all times to the CA, both in the certificate request and as otherwise requested by the CA in connection with the issuance of the Certificate(s) to be supplied by the CA;
2. **Protection of Private Key**: An obligation and warranty by the Applicant to take all reasonable measures to assure control of, keep confidential, and properly protect at all times the Private Key that corresponds to the Public Key to be included in the requested Certificate(s) (and any associated activation data or device, e.g. password or token);
3. **Acceptance of Certificate**: An obligation and warranty that the Subscriber will review and verify the Certificate contents for accuracy;
4. **Use of Certificate**: An obligation and warranty to install the Certificate only on servers that are accessible at the `subjectAltName`(s) listed in the Certificate, and to use the Certificate solely in compliance with all applicable laws and solely in accordance with the Subscriber Agreement or Terms of Use;
5. **Reporting and Revocation**: An obligation and warranty to:
   a. promptly request revocation of the Certificate, and cease using it and its associated Private Key, if there is any actual or suspected misuse or compromise of the Subscriber’s Private Key associated with the Public Key included in the Certificate, and
   b. promptly request revocation of the Certificate, and cease using it, if any information in the Certificate is or becomes incorrect or inaccurate;

6. **Termination of Use of Certificate**: An obligation and warranty to promptly cease all use of the Private Key corresponding to the Public Key included in the Certificate upon revocation of that Certificate for reasons of Key Compromise.
7. **Responsiveness**: An obligation to respond to the CA's instructions concerning Key Compromise or Certificate misuse within a specified time period.
8. **Acknowledgment and Acceptance**: An acknowledgment and acceptance that the CA is entitled to revoke the certificate immediately if the Applicant were to violate the terms of the Subscriber Agreement or Terms of Use or if revocation is required by the CA's CP, CPS, or these Baseline Requirements.

### 9.6.3 Subscriber representations and warranties

The CA SHALL require, as part of the Subscriber Agreement or Terms of Use, that the Applicant make the commitments and warranties in this section for the benefit of the CA and the Certificate Beneficiaries.

Prior to the issuance of a Certificate, the CA SHALL obtain, for the express benefit of the CA and the Certificate Beneficiaries, either the Applicant's:

1. Agreement to the Subscriber Agreement with the CA; or
2. Acknowledgement of the Terms of Use.

The CA SHALL implement a process to ensure that each Subscriber Agreement or Terms of Use is legally enforceable against the Applicant. In either case, the Agreement SHALL apply to the Certificate to be issued pursuant to the Certificate Request. The CA MAY use an electronic or "click-through" Agreement provided that the CA has determined that such agreements are legally enforceable. A separate Agreement MAY be used for each Certificate Request, or a single Agreement MAY be used to cover multiple future Certificate Requests and the resulting Certificates, so long as each Certificate that the CA issues to the Applicant is clearly covered by that Subscriber Agreement or Terms of Use.

The Subscriber Agreement or Terms of Use SHALL contain provisions imposing on the Applicant itself (or made by the Applicant on behalf of its principal or agent under a subcontractor or hosting service relationship) the following obligations and warranties:

1. **Accuracy of Information**: An obligation and warranty to provide accurate and complete information at all times to the CA, both in the Certificate Request and as otherwise requested by the CA in connection with the issuance of the Certificate(s) to be supplied by the CA;
2. **Protection of Private Key**: An obligation and warranty by the Applicant to take all reasonable measures to assure control of, keep confidential, and properly protect at all times the Private Key that corresponds to the Public Key to be included in the requested Certificate(s) (and any associated activation data or device such as a password or token);
3. **Acceptance of Certificate**: An obligation and warranty that the Subscriber will review and verify the Certificate contents for accuracy;
4. **Use of Certificate**: An obligation and warranty to use the Certificate only on MailBox Addresses listed in the Certificate, and to use the Certificate solely in compliance with all applicable laws and solely in accordance with the Subscriber Agreement or Terms of Use;
5. **Reporting and Revocation**: An obligation and warranty to:<br>
   i. promptly request revocation of the Certificate, and cease using it and its associated Private Key, if there is any actual or suspected misuse or compromise of the Subscriber’s Private Key associated with the Public Key included in the Certificate, and
   ii. promptly request revocation of the Certificate, and cease using it, if any information in the Certificate is or becomes incorrect or inaccurate;
6. **Termination of Use of Certificate**: An obligation and warranty to promptly cease all use of the Private Key corresponding to the Public Key included in the Certificate upon revocation of that Certificate for reasons of Key Compromise.
7. **Responsiveness**: An obligation to respond to the CA's instructions concerning Key Compromise or Certificate misuse within a specified time period.
8. **Acknowledgment and Acceptance**: An acknowledgment and acceptance that the CA is entitled to revoke the Certificate immediately if the Applicant were to violate the terms of the Subscriber Agreement or Terms of Use, or if revocation is required by the CA's CP and/or CPS, or by these Requirements.


### 9.6.4 Relying party representations and warranties

### 9.6.5 Representations and warranties of other participants

## 9.7 Disclaimers of warranties

## 9.8 Limitations of liability

For delegated tasks, the CA and any Delegated Third Party MAY allocate liability between themselves contractually as they determine, but the CA SHALL remain fully responsible for the performance of all parties in accordance with these Requirements, as if the tasks had not been delegated.

If the CA has issued and managed the Certificate in compliance with these Requirements and its Certificate Policy and/or Certification Practice Statement, the CA MAY disclaim liability to the Certificate Beneficiaries or any other third parties for any losses suffered as a result of use or reliance on such Certificate beyond those specified in the CA's Certificate Policy and/or Certification Practice Statement. If the CA has not issued or managed the Certificate in compliance with these Requirements and its Certificate Policy and/or Certification Practice Statement, the CA MAY seek to limit its liability to the Subscriber and to Relying Parties, regardless of the cause of action or legal theory involved, for any and all claims, losses or damages suffered as a result of the use or reliance on such Certificate by any appropriate means that the CA desires. If the CA chooses to limit its liability for Certificates that are not issued or managed in compliance with these Requirements or its Certificate Policy and/or Certification Practice Statement, then the CA SHALL include the limitations on liability in the CA's Certificate Policy and/or Certification Practice Statement.

## 9.8 Limitations of liability

For delegated tasks, the CA and any Delegated Third Party MAY allocate liability between themselves contractually as they determine, but the CA SHALL remain fully responsible for the performance of all parties in accordance with these Requirements, as if the tasks had not been delegated.

If the CA has issued and managed the Certificate in compliance with these Requirements and its CP and/or CPS, the CA MAY disclaim liability to the Certificate Beneficiaries or any other third parties for any losses suffered as a result of use or reliance on such Certificate beyond those specified in the CA's CP and/or CPS. If the CA has not issued or managed the Certificate in compliance with these Requirements and its CP and/or CPS, the CA MAY seek to limit its liability to the Subscriber and to Relying Parties, regardless of the cause of action or legal theory involved, for any and all claims, losses or damages suffered as a result of the use or reliance on such Certificate by any appropriate means that the CA desires. If the CA chooses to limit its liability for Certificates that are not issued or managed in compliance with these Requirements or its CP and/or CPS, then the CA SHALL include the limitations on liability in the CA's CP and/or CPS.

## 9.9 Indemnities

Notwithstanding any limitations on its liability to Subscribers and Relying Parties, the CA understands and acknowledges that the Application Software Suppliers who have a Root Certificate distribution agreement in place with the Root CA do not assume any obligation or potential liability of the CA under these Requirements or that otherwise might exist because of the issuance or maintenance of Certificates or reliance thereon by Relying Parties or others. Thus, except in the case where the CA is a government entity, the CA SHALL defend, indemnify, and hold harmless each Application Software Supplier for any and all claims, damages, and losses suffered by such Application Software Supplier related to a Certificate issued by the CA, regardless of the cause of action or legal theory involved. This does not apply, however, to any claim, damages, or loss suffered by such Application Software Supplier related to a Certificate issued by the CA where such claim, damage, or loss was directly caused by such Application Software Supplier's software displaying as not trustworthy a Certificate that is still valid, or displaying as trustworthy: (1) a Certificate that has expired, or (2) a Certificate that has been revoked (but only in cases where the revocation status is currently available from the CA online, and the application software either failed to check such status or ignored an indication of revoked status).

## 9.9 Indemnities

Notwithstanding any limitations on its liability to Subscribers and Relying Parties, the CA understands and acknowledges that the Application Software Suppliers who have agreed to distribute the Root CA Certificate do not assume any obligation or potential liability of the CA under these Requirements or that otherwise might exist because of the issuance or maintenance of Certificates or reliance thereon by Relying Parties or others. Thus, except in the case where the CA is a government entity, the CA SHALL defend, indemnify, and hold harmless each Application Software Supplier for any and all claims, damages, and losses suffered by such Application Software Supplier related to a Certificate issued by the CA, regardless of the cause of action or legal theory involved. This does not apply, however, to any claim, damages, or loss suffered by such Application Software Supplier related to a Certificate issued by the CA where such claim, damage, or loss was directly caused by such Application Software Supplier's software displaying as not trustworthy a Certificate that is still valid, or displaying as trustworthy: (1) a Certificate that has expired, or (2) a Certificate that has been revoked (but only in cases where the revocation status is currently available from the CA online, and the application software either failed to check such status or ignored an indication of revoked status).

## 9.10 Term and termination

### 9.10.1 Term

### 9.10.2 Termination

### 9.10.3 Effect of termination and survival

## 9.11 Individual notices and communications with participants

## 9.12 Amendments

### 9.12.1 Procedure for amendment

### 9.12.2 Notification mechanism and period

### 9.12.3 Circumstances under which OID must be changed

## 9.13 Dispute resolution provisions

## 9.14 Governing law

## 9.15 Compliance with applicable law

The CA SHALL issue Certificates and operate its PKI in accordance with all law applicable to its business and the Certificates it issues in every jurisdiction in which it operates.

## 9.15 Compliance with applicable law


## 9.16 Miscellaneous provisions

### 9.16.1 Entire agreement

### 9.16.2 Assignment

### 9.16.3 Severability

In the event of a conflict between these Requirements and a law, regulation or government order (hereinafter 'Law') of any jurisdiction in which a CA operates or issues certificates, a CA MAY modify any conflicting requirement to the minimum extent necessary to make the requirement valid and legal in the jurisdiction. This applies only to operations or certificate issuances that are subject to that Law. In such event, the CA SHALL immediately (and prior to issuing a certificate under the modified requirement) include in Section 9.16.3 of the CA's CPS a detailed reference to the Law requiring a modification of these Requirements under this section, and the specific modification to these Requirements implemented by the CA.

The CA MUST also (prior to issuing a certificate under the modified requirement) notify the CA/Browser Forum of the relevant information newly added to its CPS by sending a message to <questions@cabforum.org> and receiving confirmation that it has been posted to the Public Mailing List and is indexed in the Public Mail Archives available at <https://cabforum.org/pipermail/public/> (or such other email addresses and links as the Forum may designate), so that the CA/Browser Forum may consider possible revisions to these Requirements accordingly.

Any modification to CA practice enabled under this section MUST be discontinued if and when the Law no longer applies, or these Requirements are modified to make it possible to comply with both them and the Law simultaneously. An appropriate change in practice, modification to the CA's CPS and a notice to the CA/Browser Forum, as outlined above, MUST be made within 90 days.

### 9.16.3 Severability

In the event of a conflict between these Requirements and a law, regulation or government order (hereinafter ‘Law’) of any jurisdiction in which a CA operates or issues Certificates, a CA MAY modify any conflicting requirement to the minimum extent necessary to make the requirement valid and legal in the jurisdiction. This applies only to operations or Certificate issuances that are subject to that Law. In such event, the CA SHALL immediately (and prior to issuing a Certificate under the modified requirement) include in Section 9.16.3 of the CA’s CPS a detailed reference to the Law requiring a modification of these Requirements under this section, and the specific modification to these Requirements implemented by the CA.

The CA SHALL also (prior to issuing a Certificate under the modified requirement) notify the CA/Browser Forum of the relevant information newly added to its CPS by sending a message to <public@cabforum.org> and receiving confirmation that it has been posted to the Public Mailing List and is indexed in the Public Mail Archives available at [https://cabforum.org/pipermail/public/](https://cabforum.org/pipermail/public/) (or such other email addresses and links as the Forum may designate), so that the CA/Browser Forum may consider possible revisions to these Requirements accordingly.

Any modification to CA practice enabled under this section SHALL be discontinued if and when the Law no longer applies, or these Requirements are modified to make it possible to comply with both them and the Law simultaneously. An appropriate change in practice, modification to the CA’s CPS and a notice to the CA/Browser Forum, as outlined above, SHALL be made within 90 days.

### 9.16.4 Enforcement (attorneys' fees and waiver of rights)

### 9.16.5 Force Majeure

## 9.17 Other provisions

# Appendix A - Registration schemes

## A.1 organizationIdentifier

The following Registration Schemes are recognized as valid under these Requirements for use in the `subject:organizationIdentifier` attribute described in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields).

The country code used in the Registration Scheme identifier SHALL match that of the `subject:countryName` in the Certificate as specified in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields).

* **NTR**: For an identifier allocated by a national or state trade register to the Legal Entity named in the `subject:organizationName`. 

* **VAT**: For an identifier allocated by the national tax authorities to the Legal Entity named in the `subject:organizationName`. 

* **PSD**: For a national authorization number allocated to the payment service provider named in the `subject:organizationName` under Payments Services Directive (EU) 2015/2366. This shall use the extended structure as defined in ETSI TS 119 495, clause 5.2.1. 

* **LEI**: For a Legal Entity Identifier as specified in ISO 17442 for the entity named in the `subject:organizationName`. The 2 character ISO 3166 country code SHALL be set to 'XG'. 

## A.2 Natural Person Identifier

The following Registration Schemes are recognized as valid for use in the `subject:serialNumber` attribute described in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields).

* **PAS**: For an identifier based on a passport number issued to the Subject Individual. 

* **IDC**: For an identifier based on a national identity card issued to the Subject Individual. 

* **PNO**: For an identifier based on a national personal number (or national civic registration number) issued to the Subject Individual. 

* **TIN**: For an identifier based on Tax Identification Number issued to the Subject Individual. 

# Appendix B - Transition of Extant S/MIME CAs

Following the Effective Date for v 1.0.0 of these Requirements (September 1, 2023) an Extant S/MIME CA MAY continue to issue end entity S/MIME Certificates that are compliant with these Requirements. 

On or after September 15, 2024, all newly-issued Publicly-Trusted end entity S/MIME Certificates SHALL be issued from S/MIME Subordinate CAs that are compliant with these Requirements.

For backwards compatibility, Extant S/MIME CA Certificates that share the same Public Keys with S/MIME Subordinate CAs that are compliant with these Requirements, or are no longer used for signing end entity S/MIME Certificates, are not required to be revoked.