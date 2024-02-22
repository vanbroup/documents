---
title: Guidelines for the Issuance and Management of Extended Validation Certificates
subtitle: Version 2.0.0
author:
  - CA/Browser Forum
date: 8 June, 2023
copyright: |
  Copyright 2023 CA/Browser Forum

  This work is licensed under the Creative Commons Attribution 4.0 International license.
---

# 1. INTRODUCTION

# 1. INTRODUCTION
The Guidelines describe an integrated set of technologies, protocols, identity proofing, lifecycle management, and auditing practices specifying the minimum requirements that must be met in order to issue and maintain Extended Validation Certificates ("EV Certificates") concerning an organization.  Subject Organization information from valid EV Certificates can then be used in a special manner by certain relying-party software applications (e.g., browser software) in order to provide users with a trustworthy confirmation of the identity of the entity that controls the Web site or other services they are accessing.  Although initially intended for use in establishing Web-based data communication conduits via TLS/SSL protocols, extensions are envisioned for S/MIME, time-stamping, VoIP, IM, Web services, etc.

The primary purposes of Extended Validation Certificates are to: 1) identify the legal entity that controls a Web or service site, and 2) enable encrypted communications with that site.  The secondary purposes include significantly enhancing cybersecurity by helping establish the legitimacy of an organization claiming to operate a Web site, and providing a vehicle that can be used to assist in addressing problems related to distributing malware, phishing, identity theft, and diverse forms of online fraud.

**Notice to Readers**

The Guidelines for the Issuance and Management of Extended Validation Certificates present criteria established by the CA/Browser Forum for use by certification authorities when issuing, maintaining, and revoking certain digital certificates for use in Internet Web site commerce.  These Guidelines may be revised from time to time, as appropriate, in accordance with procedures adopted by the CA/Browser Forum.  Questions or suggestions concerning these guidelines may be directed to the CA/Browser Forum at <questions@cabforum.org>.

**The CA/Browser Forum**

The CA/Browser Forum is a voluntary open organization of certification authorities and suppliers of Internet browsers and other relying-party software applications.  Membership is listed at <https://cabforum.org/members/>.
## 1.1 Overview

This document describes an integrated set of technologies, protocols, identity-proofing, lifecycle management, and auditing requirements that are necessary (but not sufficient) for the issuance and management of Publicly-Trusted Certificates; Certificates that are trusted by virtue of the fact that their corresponding Root Certificate is distributed in widely-available application software. The requirements are not mandatory for Certification Authorities unless and until they become adopted and enforced by relying-party Application Software Suppliers.

**Notice to Readers**

The CP for the Issuance and Management of Publicly-Trusted Certificates describe a subset of the requirements that a Certification Authority must meet in order to issue Publicly Trusted Certificates. This document serves two purposes: to specify Baseline Requirements and to provide guidance and requirements for what a CA should include in its CPS. Except where explicitly stated otherwise, these Requirements apply only to relevant events that occur on or after 1 July 2012 (the original effective date of these requirements).

These Requirements do not address all of the issues relevant to the issuance and management of Publicly-Trusted Certificates. In accordance with RFC 3647 and to facilitate a comparison of other certificate policies and CPSs (e.g. for policy mapping), this document includes all sections of the RFC 3647 framework. However, rather than beginning with a "no stipulation" comment in all empty sections, the CA/Browser Forum is leaving such sections initially blank until a decision of "no stipulation" is made. The CA/Browser Forum may update these Requirements from time to time, in order to address both existing and emerging threats to online security. In particular, it is expected that a future version will contain more formal and comprehensive audit requirements for delegated functions.

These Requirements only address Certificates intended to be used for authenticating servers accessible through the Internet. Similar requirements for code signing, S/MIME, time-stamping, VoIP, IM, Web services, etc. may be covered in future versions.

These Requirements do not address the issuance, or management of Certificates by enterprises that operate their own Public Key Infrastructure for internal purposes only, and for which the Root Certificate is not distributed by any Application Software Supplier.

These Requirements are applicable to all Certification Authorities within a chain of trust. They are to be flowed down from the Root Certification Authority through successive Subordinate Certification Authorities.

## 1.1 Overview
These Guidelines for the issuance and management of Extended Validation Certificates describe certain of the minimum requirements that a Certification Authority must meet in order to issue Extended Validation Certificates.   Subject Organization information from Valid EV Certificates may be displayed in a special manner by certain relying-party software applications (e.g., browser software) in order to provide users with a trustworthy confirmation of the identity of the entity that controls the Web site they are accessing. These Guidelines incorporate the Baseline Requirements established by the CA/Browser Forum by reference.  A copy of the Baseline Requirements is available on the CA/Browser Forum's website at <https://www.cabforum.org/>.

These Guidelines address the basic issue of validating Subject identity information in EV Certificates and some related matters.   They do not address all of the related matters, such as certain technical and operational ones. This version of the Guidelines addresses only requirements for EV Certificates intended to be used for SSL/TLS authentication on the Internet and for code signing.  Similar requirements for S/MIME, time-stamping, VoIP, IM, Web services, etc. may be covered in future versions.

These Guidelines do not address the verification of information, or the issuance, use, maintenance, or revocation of EV Certificates by enterprises that operate their own Public Key Infrastructure for internal purposes only, where its Root CA Certificate is not distributed by any Application Software Supplier.

## 1.2 Document name and identification

This certificate policy (CP) contains the requirements for the issuance and management of publicly-trusted SSL certificates, as adopted by the CA/Browser Forum.

The following Certificate Policy identifiers are reserved for use by CAs to assert compliance with this document (OID arc 2.23.140.1.2) as follows:

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) domain-validated(1)} (2.23.140.1.2.1);` and

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) organization-validated(2)} (2.23.140.1.2.2);` and

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) individual-validated(3)} (2.23.140.1.2.3)`.

## 1.2 Document name and identification
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
| **Ver.** | **Ballot** | **Description** | **Adopted** | **Effective\*** |
|-|-|-----|--|--|
| 1.4.0 | 72 | Reorganize EV Documents | 29 May 2012 | 29 May 2012 |
| 1.4.1 | 75 | NameConstraints Criticality Flag | 8 June 2012 | 8 June 2012 |
| 1.4.2 | 101 | EV 11.10.2 Accountants | 31 May 2013 | 31 May 2013 |
| 1.4.3 | 104 | Domain verification for EV Certificates | 9 July 2013 | 9 July 2013 |
| 1.4.4 | 113 | Revision to QIIS in EV Guidelines | 13 Jan 2014 | 13 Jan 2014 |
| 1.4.5 | 114 | Improvements to the EV Definitions | 28 Jan 2014 | 28 Jan 2014 |
| 1.4.6 | 119 | Remove "OfIncorporation" from OID descriptions in EVG 9.2.5 | 24 Mar 2014 | 24 Mar 2014 |
| 1.4.7 | 120 | Affiliate Authority to Verify Domain | 5 June 2014 | 5 June 2014 |
| 1.4.8 | 124 | Business Entity Clarification | 5 June 2014 | 5 June 2014 |
| 1.4.9 | 127 | Verification of Name, Title and Agency | 17 July 2014 | 17 July 2014 |
| 1.5.0 | 126 | Operational Existence | 24 July 2014 | 24 July 2014 |
| 1.5.1 | 131 | Verified Method of Communication | 12 Sept 2014 | 12 Sept 2014 |
| 1.5.2 | 123 | Reuse of Information | 16 Oct. 2014 | 16 Oct. 2014 |
| 1.5.3 | 144 | Validation rules for .onion names | 18 Feb. 2015 | 18 Feb. 2015 |
| 1.5.4 | 146 | Convert Baseline Requirements to RFC 3647 Framework | 16 Apr. 2015 | 16 Apr. 2015 |
| 1.5.5 | 145 | Operational Existence for Government Entities | 5 Mar. 2015 | 5 Mar. 2015 |
| 1.5.6 | 147 | Attorney-Accountant Letter Changes | 25 June 2015 | 25 June 2015 |
| 1.5.7 | 151 | Addition of Optional OIDs for Indicating Level of Validation | 28 Sept 2015 | 28 Sept 2015 |
| 1.5.8 | 162 | Sunset of Exceptions | 15 Mar 2016 | 15 Mar 2016 |
| 1.5.9 | 163 | Fix Errata in EV Guidelines 11.2.1 | 18 Mar 2016 | 18 Mar 2016 |
| 1.6.0 | 171 | Updating ETSI Standards | 1 July 2016  | 1 July 2016   |
| 1.6.1 | 180 | In EV 11.7.1, removed outdated cross-reference to BR 3.2.2.4(7)  | 7 Jan. 2017  | 7 Jan. 2017   |
| 1.6.2 | 103 | 825-day Certificate Lifetimes | 17 Mar. 2017 | 17 Mar. 2017 |
| 1.6.3 | 198 | .Onion Revisions (declared invalid) | 7 May 2017 | 8 June 2017 |
| 1.6.4 | 191 | Clarify Place of Business Information | 23 May 2017 | 23 June 2017 |
| 1.6.5 | 201 | .onion Revisions | 8 June 2017 | 8 July 2017 |
| 1.6.6 | 192 | Notary revision | 28 June 2017 | 28 July 2017 |
| 1.6.7 | 207 | ASN.1 Jurisdiction | 23 October 2017 | 23 November 2017 |
| 1.6.8 | 217 | Sunset RFC 2527 | 21 Dec 2017 | 9 Mar 2018 |
| 1.6.9 | SC16 | Other Subject Attributes | 15 Mar 2019 | 16 Apr 2019 |
| 1.7.0 | SC17 | Alternative registration numbers for EV certificates | 21 May 2019 | 21 June 2019 |
| 1.7.1 | SC24 | Fall cleanup v2 | 12 Nov 2019 | 19 Dec 2019 |
| 1.7.2 | SC27 | Version 3 Onion Certificates | 19-Feb-2020 | 27-Mar-2020 |
| 1.7.3 | SC30 | Disclosure of Registration / Incorporating Agency | 13-Jul-2020 | 20-Aug-2020 |
| 1.7.3 | SC31 | Browser Alignment | 16-Jul-2020 | 20-Aug-2020 |
| 1.7.4 | SC35 | Cleanups and Clarifications | 9-Sep-2020 | 19-Oct-2020 |
| 1.7.5 | SC41 | Reformatting the BRs, EVGs, and NCSSRs | 24-Feb-2021 | 5-Apr-2021 |
| 1.7.6 | SC42 | 398-day Re-use Period | 22-Apr-2021 | 2-Jun-2021 |
| 1.7.7 | SC47 | Sunset subject:organizationalUnitName | 30-Jun-2021 | 16-Aug-2021 |
| 1.7.8 | SC48 | Domain Name and IP Address Encoding | 22-Jul-2021 | 25-Aug-2021 |
| 1.7.9 | SC54 | Onion Cleanup | 24-Mar-2022 | 23-Apr-2022 |
| 1.8.0 | SC56 | 2022 Cleanup | 25-Oct-2022 | 30-Nov-2022 |

\* Effective Date and Additionally Relevant Compliance Date(s)

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

I do also participate :-)

This is a description of a requirement.

	[EVG-1.3-001] This is the actual requirement

::: layer-800
The layers 800 to 899 are reserved for Auditors and Assessors.

:::

::: layer-900
CA's can use the layers 900 to 999 to write control statements or additional information to automatically construct their CP/CPS.
:::

### 1.3.1 Certification Authorities

Certification Authority (CA) is defined in [Section 1.6](#16-definitions-and-acronyms). Current CA Members of the CA/Browser Forum are listed here: <https://cabforum.org/members>.

### 1.3.1 Certification authorities

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
The CA MAY delegate the performance of all or any part of a requirement of these Guidelines to an Affiliate or a Registration Authority (RA) or subcontractor, provided that the process employed by the CA fulfills all of the requirements of [Section 3.2.2.13](#32213-final-cross-correlation-and-due-diligence).
Affiliates and/or RAs must comply with the qualification requirements of [Section 5.3.2](#532-background-check-procedures).

The CA SHALL verify that the Delegated Third Party's personnel involved in the issuance of a Certificate meet the training and skills requirements of [Section 5.3](#53-personnel-controls) and the document retention and event logging requirements of [Section 5.4](#54-audit-logging-procedures).

In all cases, the CA MUST contractually obligate each Affiliate, RA, subcontractor, and Enterprise RA to comply with all applicable requirements in these Guidelines and to perform them as required of the CA itself.  The CA SHALL enforce these obligations and internally audit each Affiliate's, RA's, subcontractor's, and Enterprise RA's compliance with these Requirements on an annual basis.

#### 1.3.2.1 Enterprise Registration authorities
The CA MAY contractually authorize a Subscriber to perform the RA function and authorize the CA to issue additional EV Certificates.  In such case, the Subscriber SHALL be considered an Enterprise RA, and the following requirements SHALL apply:

1. In all cases, the Subscriber MUST be an organization verified by the CA in accordance with these Guidelines;
2. The CA MUST impose these limitations as a contractual requirement with the Enterprise RA and monitor compliance by the Enterprise RA; and
3. The Final Cross-Correlation and Due Diligence requirements of [Section 3.2.2.13](#32213-final-cross-correlation-and-due-diligence) MAY be performed by a single person representing the Enterprise RA.

Enterprise RAs that authorize the issuance of EV Certificates solely for its own organization are exempted from the audit requirements of [Section 8](#8-compliance-audit-and-other-assessments). In all other cases, the requirements of [Section 8](#8-compliance-audit-and-other-assessments) SHALL apply.

### 1.3.3 Subscribers

As defined in [Section 1.6.1](#161-definitions).

### 1.3.3 Subscribers
### 1.3.4 Relying Parties

"Relying Party" and "Application Software Supplier" are defined in [Section 1.6.1](#161-definitions). Current Members of the CA/Browser Forum who are Application Software Suppliers are listed here:  
<https://cabforum.org/members>.

### 1.3.4 Relying parties
### 1.3.5 Other Participants

Other groups that have participated in the development of these Requirements include the AICPA/CICA WebTrust for Certification Authorities task force and ETSI ESI. Participation by such groups does not imply their endorsement, recommendation, or approval of the final product.

### 1.3.5 Other participants
## 1.4 Certificate Usage

### 1.4.1 Appropriate Certificate Uses

The primary goal of these Requirements is to enable efficient and secure electronic communication, while addressing user concerns about the trustworthiness of Certificates. These Requirements also serve to inform users and help them to make informed decisions when relying on Certificates.

### 1.4.1 Appropriate certificate uses
EV Certificates are intended for establishing Web-based data communication conduits via the TLS/SSL protocols and for verifying the authenticity of executable code.

#### 1.4.1.1 Primary Purposes

The primary purposes of an EV Certificate are to:

1. **Identify the legal entity that controls a Web site**: Provide a reasonable assurance to the user of an Internet browser that the Web site the user is accessing is controlled by a specific legal entity identified in the EV Certificate by name, address of Place of Business, Jurisdiction of Incorporation or Registration and Registration Number or other disambiguating information; and

2. **Enable encrypted communications with a Web site**: Facilitate the exchange of encryption keys in order to enable the encrypted communication of information over the Internet between the user of an Internet browser and a Web site.

#### 1.4.1.2 Secondary Purposes

The secondary purposes of an EV Certificate are to help establish the legitimacy of a business claiming to operate a Web site or distribute executable code, and to provide a vehicle that can be used to assist in addressing problems related to phishing, malware, and other forms of online identity fraud.  By providing more reliable third-party verified identity and address information regarding the business, EV Certificates may help to:

1. Make it more difficult to mount phishing and other online identity fraud attacks using Certificates;
2. Assist companies that may be the target of phishing attacks or online identity fraud by providing them with a tool to better identify themselves to users; and
3. Assist law enforcement organizations in their investigations of phishing and other online identity fraud, including where appropriate, contacting, investigating, or taking legal action against the Subject.

### 1.4.2 Prohibited Certificate Uses


### 1.4.2 Prohibited certificate uses
EV Certificates focus only on the identity of the Subject named in the Certificate, and not on the behavior of the Subject.  As such, an EV Certificate is **not** intended to provide any assurances, or otherwise represent or warrant:

1. That the Subject named in the EV Certificate is actively engaged in doing business;
2. That the Subject named in the EV Certificate complies with applicable laws;
3. That the Subject named in the EV Certificate is trustworthy, honest, or reputable in its business dealings; or
4. That it is "safe" to do business with the Subject named in the EV Certificate.
   
## 1.5 Policy administration

The Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates present criteria established by the CA/Browser Forum for use by Certification Authorities when issuing, maintaining, and revoking publicly-trusted Certificates. This document may be revised from time to time, as appropriate, in accordance with procedures adopted by the CA/Browser Forum. Because one of the primary beneficiaries of this document is the end user, the Forum openly invites anyone to make recommendations and suggestions by email to the CA/Browser Forum at <questions@cabforum.org>. The Forum members value all input, regardless of source, and will seriously consider all such input.

## 1.5 Policy administration
### 1.5.1 Organization Administering the Document


### 1.5.2 Contact Person

Contact information for the CA/Browser Forum is available here: <https://cabforum.org/leadership/>. In this section of a CA's CPS, the CA shall provide a link to a web page or an email address for contacting the person or persons responsible for operation of the CA.

### 1.5.2 Contact person
### 1.5.3 Person Determining CPS suitability for the policy


### 1.5.4 CPS approval procedures


## 1.6 Definitions and Acronyms

The Definitions found in the CA/Browser Forum's Network and Certificate System Security Requirements are incorporated by reference as if fully set forth herein.

## 1.6 Definitions and acronyms

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
Capitalized Terms are defined in the Baseline Requirements except where provided below:

**Accounting Practitioner**: A certified public accountant, chartered accountant, or a person with an equivalent license within the country of the Applicant's Jurisdiction of Incorporation or Registration or any jurisdiction where the Applicant maintains an office or physical facility; provided that an accounting standards body in the jurisdiction maintains full (not "suspended" or "associate") membership status with the International Federation of Accountants.

**Baseline Requirements**: The Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates as published by the CA/Browser Forum and any amendments to such document.

**Business Entity**: Any entity that is not a Private Organization, Government Entity, or Non-Commercial Entity as defined herein. Examples include, but are not limited to, general partnerships, unincorporated associations, sole proprietorships, etc.

**Certificate Approver**: A natural person who is either the Applicant, employed by the Applicant, or an authorized agent who has express authority to represent the Applicant to

  i. act as a Certificate Requester and to authorize other employees or third parties to act as a Certificate Requester, and
  ii. to approve EV Certificate Requests submitted by other Certificate Requesters.

**Certificate Requester**: A natural person who is either the Applicant, employed by the Applicant, an authorized agent who has express authority to represent the Applicant, or a third party (such as an ISP or hosting company) that completes and submits an EV Certificate Request on behalf of the Applicant.

**Confirmation Request**: An appropriate out-of-band communication requesting verification or confirmation of the particular fact at issue.

**Confirming Person**: A position within an Applicant's organization that confirms the particular fact at issue.

**Contract Signer**: A natural person who is either the Applicant, employed by the Applicant, or an authorized agent who has express authority to represent the Applicant, and who has authority on behalf of the Applicant to sign Subscriber Agreements.

**Demand Deposit Account**: A deposit account held at a bank or other financial institution, the funds deposited in which are payable on demand.  The primary purpose of demand accounts is to facilitate cashless payments by means of check, bank draft, direct debit, electronic funds transfer, etc.  Usage varies among countries, but a demand deposit account is commonly known as a share draft account, a current account, or a checking account.

**EV Authority**: A source other than the Certificate Approver, through which verification occurs that the Certificate Approver is expressly authorized by the Applicant, as of the date of the EV Certificate Request, to take the Request actions described in these Guidelines.

**EV Certificate**: A certificate that contains subject information specified in these Guidelines and that has been validated in accordance with these Guidelines.

**EV Certificate Beneficiaries**: Persons to whom the CA and its Root CA make specified EV Certificate Warranties.

**EV Certificate Renewal**: The process whereby an Applicant who has a valid unexpired and non-revoked EV Certificate makes an application, to the CA that issued the original certificate, for a newly issued EV Certificate for the same organizational name and Domain Name prior to the expiration of the Applicant's existing EV Certificate but with a new 'valid to' date beyond the expiry of the current EV Certificate.

**EV Certificate Reissuance**: The process whereby an Applicant who has a valid unexpired and non-revoked EV Certificate makes an application, to the CA that issued the original certificate, for a newly issued EV Certificate for the same organizational name and Domain Name prior to the expiration of the Applicant's existing EV Certificate but with a 'valid to' date that matches that of the current EV Certificate.

**EV Certificate Request**: A request from an Applicant to the CA requesting that the CA issue an EV Certificate to the Applicant, which request is validly authorized by the Applicant and signed by the Applicant Representative.

**EV Certificate Warranties**: In conjunction with the CA issuing an EV Certificate, the CA and its Root CA, during the period when the EV Certificate is Valid, promise that the CA has followed the requirements of these Guidelines and the CA's EV Policies in issuing the EV Certificate and in verifying the accuracy of the information contained in the EV Certificate.

**EV OID**: An identifying number, in the form of an "object identifier," that is included in the `certificatePolicies` field of a certificate that:

  i. indicates which CA policy statement relates to that certificate, and
  ii. is either the CA/Browser Forum EV policy identifier or a policy identifier that, by pre-agreement with one or more Application Software Supplier, marks the certificate as being an EV Certificate.

**EV Policies**: Auditable EV Certificate practices, policies and procedures, such as a certification practice statement  and certificate policy, that are developed, implemented, and enforced by the CA and its Root CA.

**EV Processes**: The keys, software, processes, and procedures by which the CA verifies Certificate Data under this Guideline, issues EV Certificates, maintains a Repository, and revokes EV Certificates.

**Extended Validation Certificate**: See EV Certificate.

**Government Agency**: In the context of a Private Organization, the government agency in the Jurisdiction of Incorporation under whose authority the legal existence of Private Organizations is established (e.g., the government agency that issued the Certificate of Incorporation).  In the context of Business Entities, the government agency in the jurisdiction of operation that registers business entities.  In the case of a Government Entity, the entity that enacts law, regulations, or decrees establishing the legal existence of Government Entities.

**Guidelines**: This document.

**Incorporating Agency**: In the context of a Private Organization, the government agency in the Jurisdiction of Incorporation under whose authority the legal existence of the entity is registered (e.g., the government agency that issues certificates of formation or incorporation).  In the context of a Government Entity, the entity that enacts law, regulations, or decrees establishing the legal existence of Government Entities.

**Independent Confirmation From Applicant**: Confirmation of a particular fact received by the CA pursuant to the provisions of the Guidelines or binding upon the Applicant.

**Individual**: A natural person.

**International Organization**: An organization founded by a constituent document, e.g., a charter, treaty, convention or similar document, signed by, or on behalf of, a minimum of two Sovereign State governments.

**Jurisdiction of Incorporation**: In the context of a Private Organization, the country and (where applicable) the state or province or locality where the organization's legal existence was established by a filing with (or an act of) an appropriate government agency or entity (e.g., where it was incorporated).  In the context of a Government Entity, the country and (where applicable) the state or province where the Entity's legal existence was created by law.

**Jurisdiction of Registration**: In the case of a Business Entity, the state, province, or locality where the organization has registered its business presence by means of filings by a Principal Individual involved in the business.

**Latin Notary**: A person with legal training whose commission under applicable law not only includes authority to authenticate the execution of a signature on a document but also responsibility for the correctness and content of the document. A Latin Notary is sometimes referred to as a Civil Law Notary.

**Legal Entity**: A Private Organization, Government Entity, Business Entity, or Non-Commercial Entity.

**Legal Existence**: A Private Organization, Government Entity, or Business Entity has Legal Existence if it has been validly formed and not otherwise terminated, dissolved, or abandoned.

**Legal Practitioner**: A person who is either a lawyer or a Latin Notary as described in these Guidelines and competent to render an opinion on factual claims of the Applicant.

**Maximum Validity Period**:

  1. The maximum time period for which the issued EV Certificate is valid.
  2. The maximum period after validation by the CA that certain Applicant information may be relied upon in issuing an EV Certificate pursuant to these Guidelines.

**Notary**: A person whose commission under applicable law includes authority to authenticate the execution of a signature on a document.

**Place of Business**: The location of any facility (such as a factory, retail store, warehouse, etc) where the Applicant's business is conducted.

**Principal Individual**: An individual of a Private Organization, Government Entity, or Business Entity that is either an owner, partner, managing member, director, or officer, as identified by their title of employment, or an employee, contractor or agent authorized by such entity or organization to conduct business related to the request, issuance, and use of EV Certificates.

**Private Organization**: A non-governmental legal entity (whether ownership interests are privately held or publicly traded) whose existence was created by a filing with (or an act of) the Incorporating Agency or equivalent in its Jurisdiction of Incorporation.

**Qualified Auditor**: An independent public accounting firm that meets the auditing qualification requirements specified in [Section 8.2](#82-identityqualifications-of-assessor).

**Qualified Government Information Source**: A database maintained by a Government Entity (e.g. SEC filings) that meets the requirements of [Section 3.2.2.11.6](#322116-qualified-government-information-source).

**Qualified Government Tax Information Source**: A Qualified Governmental Information Source that specifically contains tax information relating to Private Organizations, Business Entities, or Individuals.

**Qualified Independent Information Source**: A regularly-updated and current, publicly available, database designed for the purpose of accurately providing the information for which it is consulted, and which is generally recognized as a dependable source of such information.

**Registration Agency**: A Governmental Agency that registers business information in connection with an entity's business formation or authorization to conduct business under a license, charter or other certification.  A Registration Agency MAY include, but is not limited to

  i. a State Department of Corporations or a Secretary of State;
  ii. a licensing agency, such as a State Department of Insurance; or
  iii. a chartering agency, such as a state office or department of financial regulation, banking or finance, or a federal agency such as the Office of the Comptroller of the Currency or Office of Thrift Supervision.

**Registration Reference**: A unique identifier assigned to a Legal Entity.

**Registration Scheme**: A scheme for assigning a Registration Reference meeting the requirements identified in [Appendix H](#appendix-h--registration-schemes).

**Registered Agent**: An individual or entity that is:

  i. authorized by the Applicant to receive service of process and business communications on behalf of the Applicant; and
  ii. listed in the official records of the Applicant's Jurisdiction of Incorporation as acting in the role specified in (i) above.

**Registered Office**: The official address of a company, as recorded with the Incorporating Agency, to which official documents are sent and at which legal notices are received.

**Registration Number**: The unique number assigned to a Private Organization by the Incorporating Agency in such entity's Jurisdiction of Incorporation.

**Regulated Financial Institution**: A financial institution that is regulated, supervised, and examined by governmental, national, state or provincial, or local authorities.

**Root Key Generation Script**: A documented plan of procedures to be performed for the generation of the Root CA Key Pair.

**Signing Authority**: One or more Certificate Approvers designated to act on behalf of the Applicant.

**Superior Government Entity**: Based on the structure of government in a political subdivision, the Government Entity or Entities that have the ability to manage, direct and control the activities of the Applicant.

**Suspect code**: Code that contains malicious functionality or serious vulnerabilities, including spyware, malware and other code that installs without the user's consent and/or resists its own removal, and code that can be exploited in ways not intended by its designers to compromise the trustworthiness of the platforms on which it executes.

**Translator**: An individual or Business Entity that possesses the requisite knowledge and expertise to accurately translate the words of a document written in one language to the native language of the CA.

**Verified Accountant Letter**: A document meeting the requirements specified in [Section 3.2.2.11.2](#322112-verified-accountant-letter).

**Verified Legal Opinion**: A document meeting the requirements specified in [Section 3.2.2.11.1](#322111-verified-legal-opinion).

**Verified Method of Communication**: The use of a telephone number, a fax number, an email address, or postal delivery address, confirmed by the CA in accordance with [Section 3.2.2.5](#3225-verified-method-of-communication) as a reliable way of communicating with the Applicant.

**Verified Professional Letter**: A Verified Accountant Letter or Verified Legal Opinion.

**WebTrust EV Program**: The additional audit procedures specified for CAs that issue EV Certificates by the AICPA/CICA to be used in conjunction with its WebTrust Program for Certification Authorities.

**WebTrust Program for CAs**: The then-current version of the AICPA/CICA WebTrust Program for Certification Authorities.

**WebTrust Seal of Assurance**: An affirmation of compliance resulting from the WebTrust Program for CAs.

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
Abbreviations and Acronyms are defined in the Baseline Requirements except as otherwise defined herein:

| **Acronym** | **Meaning** |
| --- | --- |
| BIPM | International Bureau of Weights and Measures |
| BIS | (US Government) Bureau of Industry and Security |
| CEO | Chief Executive Officer |
| CFO | Chief Financial Officer |
| CIO | Chief Information Officer |
| CISO | Chief Information Security Officer |
| COO | Chief Operating Officer |
| CPA | Chartered Professional Accountant |
| CSO | Chief Security Officer |
| EV | Extended Validation |
| gTLD | Generic Top-Level Domain |
| IFAC | International Federation of Accountants |
| IRS | Internal Revenue Service |
| ISP | Internet Service Provider |
| QGIS | Qualified Government Information Source |
| QTIS | Qualified Government Tax Information Source |
| QIIS | Qualified Independent Information Source |
| SEC | (US Government) Securities and Exchange Commission |
| UTC(k) | National realization of Coordinated Universal Time |

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
See Baseline Requirements, which are available at <https://www.cabforum.org/>.

### 1.6.4 Conventions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in these Requirements shall be interpreted in accordance with RFC 2119.

By convention, this document omits time and timezones when listing effective requirements such as dates. Except when explicitly specified, the associated time with a date shall be 00:00:00 UTC.

### 1.6.4 Conventions
Terms not otherwise defined in these Guidelines shall be as defined in applicable agreements, user manuals, certification practice statements (CPS), and certificate policies (CP) of the CA issuing EV Certificates.

The key words "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in these Guidelines shall be interpreted in accordance with RFC 2119.

By convention, this document omits time and timezones when listing effective requirements such as dates. Except when explicitly specified, the associated time with a date shall be 00:00:00 UTC.

# 2. PUBLICATION AND REPOSITORY RESPONSIBILITIES

The CA SHALL develop, implement, enforce, and annually update a Certificate Policy and/or Certification Practice Statement that describes in detail how the CA implements the latest version of these Requirements.

# 2. PUBLICATION AND REPOSITORY RESPONSIBILITIES
Each CA must develop, implement, enforce, display prominently on its Web site, and periodically update as necessary its own auditable EV Certificate practices, policies and procedures, such as a Certification Practice Statement (CPS) and Certificate Policy (CP) that:

A.  Implement the requirements of these Guidelines as they are revised from time-to-time;

B.  Implement the requirements of

    i. the then-current WebTrust Program for CAs, and
    ii. the then-current WebTrust EV Program or ETSI TS 102 042 for EVCP or ETSI EN 319 411-1 for EVCP policy; and

C.  Specify the CA's and its Root CA's entire root certificate hierarchy including all roots that its EV Certificates depend on for proof of those EV Certificates' authenticity.

## 2.1 Repositories

The CA SHALL make revocation information for Subordinate Certificates and Subscriber Certificates available in accordance with this Policy.

## 2.1 Repositories
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
Each CA MUST publicly disclose its Certificate Policy and/or Certification Practice Statement through an appropriate and readily accessible online means that is available on a 24x7 basis. The CA SHALL publicly disclose its CA business practices to the extent required by the CA's selected audit scheme (see [Section 8](#8-compliance-audit-and-other-assessments)).

The CA's Certificate Policy and/or Certification Practice Statement MUST be structured in accordance with RFC 3647. The Certificate Policy and/or Certification Practice Statement MUST include all material required by RFC 3647.

Each CA SHALL publicly give effect to these Guidelines and represent that they will adhere to the latest published version by incorporating them into their respective EV Policies, using a clause such as the following (which must include a link to the official version of these Guidelines):

> [Name of CA] conforms to the current version of the CA/Browser Forum Guidelines for Issuance and Management of Extended Validation Certificates published at <https://www.cabforum.org>.  In the event of any inconsistency between this document and those Guidelines, those Guidelines take precedence over this document.

In addition, the CA MUST include (directly or by reference) the applicable requirements of these Guidelines in all contracts with Subordinate CAs, RAs, Enterprise RAs, and subcontractors that involve or relate to the issuance or maintenance of EV Certificates.  The CA MUST enforce compliance with such terms.

## 2.3 Time or frequency of publication

The CA SHALL develop, implement, enforce, and annually update a Certificate Policy and/or Certification Practice Statement that describes in detail how the CA implements the latest version of these Requirements. The CA SHALL indicate conformance with this requirement by incrementing the version number and adding a dated changelog entry, even if no other changes are made to the document.

## 2.3 Time or frequency of publication
## 2.4 Access controls on repositories

The CA shall make its Repository publicly available in a read-only manner.

## 2.4 Access controls on repositories
# 3. IDENTIFICATION AND AUTHENTICATION

## 3.1 Naming

### 3.1.1 Types of names

### 3.1.2 Need for names to be meaningful

### 3.1.3 Anonymity or pseudonymity of subscribers

### 3.1.4 Rules for interpreting various name forms

### 3.1.5 Uniqueness of names

### 3.1.6 Recognition, authentication, and role of trademarks

## 3.2 Initial identity validation

### 3.2.1 Method to prove possession of private key

### 3.2.2 Authentication of Organization and Domain Identity

If the Applicant requests a Certificate that will contain Subject Identity Information comprised only of the `countryName` field, then the CA SHALL verify the country associated with the Subject using a verification process meeting the requirements of [Section 3.2.2.3](#3223-verification-of-country) and that is described in the CA's Certificate Policy and/or Certification Practice Statement. If the Applicant requests a Certificate that will contain the countryName field and other Subject Identity Information, then the CA SHALL verify the identity of the Applicant, and the authenticity of the Applicant Representative's certificate request using a verification process meeting the requirements of this [Section 3.2.2.1](#3221-identity) and that is described in the CA's Certificate Policy and/or Certification Practice Statement. The CA SHALL inspect any document relied upon under this Section for alteration or falsification.

### 3.2.2 Authentication of organization identity

#### 3.2.2.1 Identity

If the Subject Identity Information is to include the name or address of an organization, the CA SHALL verify the identity and address of the organization and that the address is the Applicant's address of existence or operation. The CA SHALL verify the identity and address of the Applicant using documentation provided by, or through communication with, at least one of the following:

1. A government agency in the jurisdiction of the Applicant's legal creation, existence, or recognition;
2. A third party database that is periodically updated and considered a Reliable Data Source;
3. A site visit by the CA or a third party who is acting as an agent for the CA; or
4. An Attestation Letter.

The CA MAY use the same documentation or communication described in 1 through 4 above to verify both the Applicant's identity and address.

Alternatively, the CA MAY verify the address of the Applicant (but not the identity of the Applicant) using a utility bill, bank statement, credit card statement, government-issued tax document, or other form of identification that the CA determines to be reliable.

#### 3.2.2.1 Overview

This part of the Guidelines sets forth Verification Requirements and Acceptable Methods of Verification for each such Requirement.

##### 3.2.2.1.1 Verification Requirements – Overview

Before issuing an EV Certificate, the CA MUST ensure that all Subject organization information to be included in the EV Certificate conforms to the requirements of, and is verified in accordance with, these Guidelines and matches the information confirmed and documented by the CA pursuant to its verification processes.  Such verification processes are intended to accomplish the following:

1. Verify Applicant's existence and identity, including;

   A.  Verify the Applicant's legal existence and identity (as more fully set forth in [Section 3.2.2.2](#3222-verification-of-applicants-legal-existence-and-identity)),

   B.  Verify the Applicant's physical existence (business presence at a physical address), and

   C.  Verify the Applicant's operational existence (business activity).

2. Verify the Applicant is a registered holder, or has control, of the Domain Name(s) to be included in the EV Certificate;

3. Verify a reliable means of communication with the entity to be named as the Subject in the Certificate;

4. Verify the Applicant's authorization for the EV Certificate, including;

   A.  Verify the name, title, and authority of the Contract Signer, Certificate Approver, and Certificate Requester,

   B.  Verify that a Contract Signer signed the Subscriber Agreement or that a duly authorized Applicant Representative acknowledged and agreed to the Terms of Use; and

   C.  Verify that a Certificate Approver has signed or otherwise approved the EV Certificate Request.

##### 3.2.2.1.2 Acceptable Methods of Verification – Overview

As a general rule, the CA is responsible for taking all verification steps reasonably necessary to satisfy each of the Verification Requirements set forth in the subsections below.  The Acceptable Methods of Verification set forth in each of Sections 3.2.2 through 3.2.14 (which usually include alternatives) are considered to be the minimum acceptable level of verification required of the CA.  In all cases, however, the CA is responsible for taking any additional verification steps that may be reasonably necessary under the circumstances to satisfy the applicable Verification Requirement.

##### 3.2.2.1.3 Disclosure of Verification Sources

Effective as of 1 October 2020, prior to the use of an Incorporating Agency or Registration Agency to fulfill these verification requirements, the CA MUST publicly disclose Agency Information about the Incorporating Agency or Registration Agency. This disclosure SHALL be through an appropriate and readily accessible online means.

This Agency Information SHALL include at least the following:

* Sufficient information to unambiguously identify the Incorporating Agency or Registration Agency (such as a name, jurisdiction, and website); and,
* The accepted value or values for each of the `subject:jurisdictionLocalityName` (OID: 1.3.6.1.4.1.311.60.2.1.1), `subject:jurisdictionStateOrProvinceName` (OID: 1.3.6.1.4.1.311.60.2.1.2), and `subject:jurisdictionCountryName` (OID: 1.3.6.1.4.1.311.60.2.1.3) fields, when a certificate is issued using information from that Incorporating Agency or Registration Agency, indicating the jurisdiction(s) that the Agency is appropriate for; and,
* The acceptable form or syntax of Registration Numbers used by the Incorporating Agency or Registration Agency, if the CA restricts such Numbers to an acceptable form or syntax; and,
* A revision history that includes a unique version number and date of publication for any additions, modifications, and/or removals from this list.

The CA MUST document where to obtain this information within Section 3.2 of the CA's Certificate Policy and/or Certification Practice Statement.

#### 3.2.2.2 DBA/Tradename

If the Subject Identity Information is to include a DBA or tradename, the CA SHALL verify the Applicant's right to use the DBA/tradename using at least one of the following:

1. Documentation provided by, or communication with, a government agency in the jurisdiction of the Applicant's legal creation, existence, or recognition;
2. A Reliable Data Source;
3. Communication with a government agency responsible for the management of such DBAs or trade names;
4. An Attestation Letter accompanied by documentary support; or
5. A utility bill, bank statement, credit card statement, government-issued tax document, or other form of identification that the CA determines to be reliable.

#### 3.2.2.2 Verification of Applicant's Legal Existence and Identity

##### 3.2.2.2.1 Verification Requirements

To verify the Applicant's legal existence and identity, the CA MUST do the following.

1. **Private Organization Subjects**

   A.  **Legal Existence**: Verify that the Applicant is a legally recognized entity, in existence and validly formed (e.g., incorporated) with the Incorporating or Registration Agency in the Applicant's Jurisdiction of Incorporation or Registration, and not designated on the records of the Incorporating or Registration Agency by labels such as "inactive", "invalid", "not current", or the equivalent.
   B.  **Organization Name**: Verify that the Applicant's formal legal name as recorded with the Incorporating or Registration Agency in the Applicant's Jurisdiction of Incorporation or Registration matches the Applicant's name in the EV Certificate Request.
   C.  **Registration Number**: Obtain the specific Registration Number assigned to the Applicant by the Incorporating or Registration Agency in the Applicant's Jurisdiction of Incorporation or Registration.  Where the Incorporating or Registration Agency does not assign a Registration Number, the CA SHALL obtain the Applicant's date of Incorporation or Registration.
   D.  **Registered Agent**: Obtain the identity and address of the Applicant's Registered Agent or Registered Office (as applicable in the Applicant's Jurisdiction of Incorporation or Registration).

2. **Government Entity Subjects**

   A.  **Legal Existence**: Verify that the Applicant is a legally recognized Government Entity, in existence in the political subdivision in which such Government Entity operates.
   B.  **Entity Name**: Verify that the Applicant's formal legal name matches the Applicant's name in the EV Certificate Request.
   C.  **Registration Number**: The CA MUST attempt to obtain the Applicant's date of incorporation, registration, or formation, or the identifier for the legislative act that created the Government Entity.  In circumstances where this information is not available, the CA MUST enter appropriate language to indicate that the Subject is a Government Entity.

3. **Business Entity Subjects**

   A.  **Legal Existence**: Verify that the Applicant is engaged in business under the name submitted by the Applicant in the Application.
   B.  **Organization Name**: Verify that the Applicant's formal legal name as recognized by the Registration Agency in the Applicant's Jurisdiction of Registration matches the Applicant's name in the EV Certificate Request.
   C.  **Registration Number**: Attempt to obtain the specific unique Registration Number assigned to the Applicant by the Registration Agency in the Applicant's Jurisdiction of Registration.  Where the Registration Agency does not assign a Registration Number, the CA SHALL obtain the Applicant's date of Registration.
   D.  **Principal Individual**: Verify the identity of the identified Principal Individual.

4. **Non-Commercial Entity Subjects (International Organizations)**

   A.  **Legal Existence**: Verify that the Applicant is a legally recognized International Organization Entity.
   B.  **Entity Name**: Verify that the Applicant's formal legal name matches the Applicant's name in the EV Certificate Request.
   C.  **Registration Number**: The CA MUST attempt to obtain the Applicant's date of formation, or the identifier for the legislative act that created the International Organization Entity.  In circumstances where this information is not available, the CA MUST enter appropriate language to indicate that the Subject is an International Organization Entity.

##### 3.2.2.2.2 Acceptable Method of Verification

1. **Private Organization Subjects**: Unless verified under subsection (6), all items listed in [Section 3.2.2.2.1](#32221-verification-requirements) (1) MUST be verified directly with, or obtained directly from, the Incorporating or Registration Agency in the Applicant's Jurisdiction of Incorporation or Registration. Such verification MAY be through use of a Qualified Government Information Source operated by, or on behalf of, the Incorporating or Registration Agency, or by direct contact with the Incorporating or Registration Agency in person or via mail, e-mail, Web address, or telephone, using an address or phone number obtained directly from the Qualified Government Information Source, Incorporating or Registration Agency, or from a Qualified Independent Information Source.

2. **Government Entity Subjects**: Unless verified under subsection (6), all items listed in [Section 3.2.2.2.1](#32221-verification-requirements) (2) MUST either be verified directly with, or obtained directly from, one of the following:
   i. a Qualified Government Information Source in the political subdivision in which such Government Entity operates;
   ii. a superior governing Government Entity in the same political subdivision as the Applicant (e.g. a Secretary of State may verify the legal existence of a specific State Department), or
   iii. from a judge that is an active member of the federal, state or local judiciary within that political subdivision.

   Any communication from a judge SHALL be verified in the same manner as is used for verifying factual assertions that are asserted by an Attorney as set forth in [Section 3.2.2.11.1](#322111-verified-legal-opinion).

   Such verification MAY be by direct contact with the appropriate Government Entity in person or via mail, e-mail, Web address, or telephone, using an address or phone number obtained from a Qualified Independent Information Source.

3. **Business Entity Subjects**: Unless verified under subsection (6), Items listed in [Section 3.2.2.2.1](#32221-verification-requirements) (3) (A) through (C) above, MUST be verified directly with, or obtained directly from, the Registration Agency in the Applicant's Jurisdiction of Registration. Such verification MAY be performed by means of a Qualified Government Information Source, a Qualified Governmental Tax Information Source, or by direct contact with the Registration Agency in person or via mail, e-mail, Web address, or telephone, using an address or phone number obtained directly from the Qualified Government Information Source, Qualified Governmental Tax Information Source or Registration Agency, or from a Qualified Independent Information Source. In addition, the CA MUST validate a Principal Individual associated with the Business Entity pursuant to the requirements in subsection (4), below.

4. **Principal Individual**: A Principal Individual associated with the Business Entity MUST be validated in a face-to-face setting.  The CA MAY rely upon a face-to-face validation of the Principal Individual performed by the Registration Agency, provided that the CA has evaluated the validation procedure and concluded that it satisfies the requirements of the Guidelines for face-to-face validation procedures.  Where no face-to-face validation was conducted by the Registration Agency, or the Registration Agency's face-to-face validation procedure does not satisfy the requirements of the Guidelines, the CA SHALL perform face-to-face validation.

   A.  **Face-To-Face Validation**: The face-to-face validation MUST be conducted before either an employee of the CA, a Latin Notary, a Notary (or equivalent in the Applicant's jurisdiction), a Lawyer, or Accountant (Third-Party Validator).  The Principal Individual(s) MUST present the following documentation (Vetting Documents) directly to the Third-Party Validator:

       i. A Personal Statement that includes the following information:

          1. Full name or names by which a person is, or has been, known (including all other names used);
          2. Residential Address at which he/she can be located;
          3. Date of birth; and
          4. An affirmation that all of the information contained in the Certificate Request is true and correct.

       ii. A current signed government-issued identification document that includes a photo of the Individual and is signed by the Individual such as:

           1. A passport;
           2. A driver's license;
           3. A personal identification card;
           4. A concealed weapons permit; or
           5. A military ID.

       iii. At least two secondary documentary evidences to establish his/her identity that include the name of the Individual, one of which MUST be from a financial institution.

            1. Acceptable financial institution documents include:

               a. A major credit card, provided that it contains an expiration date and it has not expired'
               b. A debit card from a regulated financial institution, provided that it contains an expiration date and it has not expired,
               c. A mortgage statement from a recognizable lender that is less than six months old,
               d. A bank statement from a regulated financial institution that is less than six months old.

            2. Acceptable non-financial documents include:

               a. Recent original utility bills or certificates from a utility company confirming the arrangement to pay for the services at a fixed address (not a mobile/cellular telephone bill),
               b. A copy of a statement for payment of a lease, provided that the statement is dated within the past six months,
               c. A certified copy of a birth certificate,
               d. A local authority tax bill for the current year,
               e. A certified copy of a court order, such as a divorce certificate, annulment papers, or adoption papers.

       The Third-Party Validator performing the face-to-face validation MUST:

         i. Attest to the signing of the Personal Statement and the identity of the signer; and
         ii. Identify the original Vetting Documents used to perform the identification.  In addition, the Third-Party Validator MUST attest on a copy of the current signed government-issued photo identification document that it is a full, true, and accurate reproduction of the original.

   B.  **Verification of Third-Party Validator**: The CA MUST independently verify that the Third-Party Validator is a legally-qualified Latin Notary or Notary (or legal equivalent in the Applicant's jurisdiction), lawyer, or accountant in the jurisdiction of the Individual's residency, and that the Third-Party Validator actually did perform the services and did attest to the signature of the Individual.

   C.  **Cross-checking of Information**: The CA MUST obtain the signed and attested Personal Statement together with the attested copy of the current signed government-issued photo identification document.  The CA MUST review the documentation to determine that the information is consistent, matches the information in the application, and identifies the Individual.  The CA MAY rely on electronic copies of this documentation, provided that:

       i. the CA confirms their authenticity (not improperly modified when compared with the underlying original) with the Third-Party Validator; and
       ii. electronic copies of similar kinds of documents are recognized as legal substitutes for originals under the laws of the CA's jurisdiction.

5. **Non-Commercial Entity Subjects (International Organization)**: Unless verified under subsection (6), all items listed in [Section 3.2.2.2.1](#32221-verification-requirements) (4) MUST be verified either:

   A.  With reference to the constituent document under which the International Organization was formed; or
   B.  Directly with a signatory country's government in which the CA is permitted to do business.  Such verification may be obtained from an appropriate government agency or from the laws of that country, or by verifying that the country's government has a mission to represent it at the International Organization; or
   C.  Directly against any current list of qualified entities that the CA/Browser Forum may maintain at www.cabforum.org.
   D.  In cases where the International Organization applying for the EV Certificate is an organ or agency - including a non-governmental organization of a verified International Organization, then the CA may verify the International Organization Applicant directly with the verified umbrella International Organization of which the Applicant is an organ or agency.

6. The CA may rely on a Verified Professional Letter to establish the Applicant's information listed in (1)-(5) above if:

   i. the Verified Professional Letter includes a copy of supporting documentation used to establish the Applicant's legal existence, such as a certificate of registration, articles of incorporation, operating agreement, statute, or regulatory act, and
   ii. the CA confirms the Applicant's organization name specified in the Verified Professional Letter with a QIIS or QGIS.

#### 3.2.2.3 Verification of Country

If the `subject:countryName` field is present, then the CA SHALL verify the country associated with the Subject using one of the following:

  a. the IP Address range assignment by country for either
     i. the web site's IP address, as indicated by the DNS record for the web site or
     ii. the Applicant's IP address;
  b. the ccTLD of the requested Domain Name;
  c. information provided by the Domain Name Registrar; or
  d. a method identified in [Section 3.2.2.1](#3221-identity).

The CA SHOULD implement a process to screen proxy servers in order to prevent reliance upon IP addresses assigned in countries other than where the Applicant is actually located.

#### 3.2.2.3 Verification of Applicant's Legal Existence and Identity – Assumed Name

##### 3.2.2.3.1 Verification Requirements

If, in addition to the Applicant's formal legal name, as recorded with the applicable Incorporating Agency or Registration Agency in the Applicant's Jurisdiction of Incorporation or Registration, the Applicant's identity, as asserted in the EV Certificate, is to contain any assumed name (also known as "doing business as", "DBA", or "d/b/a" in the US, and "trading as" in the UK) under which the Applicant conducts business, the CA MUST verify that:

   i. the Applicant has registered its use of the assumed name with the appropriate government agency for such filings in the jurisdiction of its Place of Business (as verified in accordance with these Guidelines), and
   ii. that such filing continues to be valid.

##### 3.2.2.3.2 Acceptable Method of Verification

To verify any assumed name under which the Applicant conducts business:

1. The CA MAY verify the assumed name through use of a Qualified Government Information Source operated by, or on behalf of, an appropriate government agency in the jurisdiction of the Applicant's Place of Business, or by direct contact with such government agency in person or via mail, e-mail, Web address, or telephone; or
2. The CA MAY verify the assumed name through use of a Qualified Independent Information Source provided that the QIIS has verified the assumed name with the appropriate government agency.
3. The CA MAY rely on a Verified Professional Letter  that indicates the assumed name under which the Applicant conducts business, the government agency with which the assumed name is registered, and that such filing continues to be valid.

#### 3.2.2.4 Verification of Applicant's Physical Existence

##### 3.2.2.4.1 Address of Applicant's Place of Business

1. **Verification Requirements**: To verify the Applicant's physical existence and business presence, the CA MUST verify that the physical address provided by the Applicant is an address where the Applicant or a Parent/Subsidiary Company conducts business operations (not, for example, a mail drop or P.O. box, or 'care of' (C/O) address, such as an address for an agent of the Organization), and is the address of the Applicant's Place of Business.

2. **Acceptable Methods of Verification**

   A.  **Place of Business in the Country of Incorporation or Registration**

       i. For Applicants whose Place of Business is in the same country as the Applicant's Jurisdiction of Incorporation or Registration and whose Place of Business is NOT the same as that indicated in the relevant Qualified Government Information Source used in [Section 3.2.2.2](#3222-verification-of-applicants-legal-existence-and-identity) to verify legal existence:

          1. For Applicants listed at the same Place of Business address in the current version of either at least one QGIS (other than that used to verify legal existence), QIIS or QTIS, the CA MUST confirm that the Applicant's address, as listed in the EV Certificate Request, is a valid business address for the Applicant or a Parent/Subsidiary Company by reference to such QGIS, QIIS, or QTIS, and MAY rely on the Applicant's representation that such address is its Place of Business;

          2. For Applicants who are not listed at the same Place of Business address in the current version of either at least one QIIS or QTIS, the CA MUST confirm that the address provided by the Applicant in the EV Certificate Request is the Applicant's or a Parent/Subsidiary Company's business address, by obtaining documentation of a site visit to the business address, which MUST be performed by a reliable individual or firm.  The documentation of the site visit MUST:

             a. Verify that the Applicant's business is located at the exact address stated in the EV Certificate Request (e.g., via permanent signage, employee confirmation, etc.),
             b. Identify the type of facility (e.g., office in a commercial building, private residence, storefront, etc.) and whether it appears to be a permanent business location,
             c. Indicate whether there is a permanent sign (that cannot be moved) that identifies the Applicant,
             d. Indicate whether there is evidence that the Applicant is conducting ongoing business activities at the site (not that it is just, for example, a mail drop, P.O. box, etc.), and
             e. Include one or more photos of
                i. the exterior of the site (showing signage indicating the Applicant's name, if present, and showing the street address if possible), and
                ii. the interior reception area or workspace.

       ii. For all Applicants, the CA MAY alternatively rely on a Verified Professional Letter that indicates the address of the Applicant's or a Parent/Subsidiary Company's Place of Business and that business operations are conducted there.
       iii. For Government Entity Applicants, the CA MAY rely on the address contained in the records of the QGIS in the Applicant's jurisdiction.
       iv. For Applicants whose Place of Business is in the same country as the Applicant's Jurisdiction of Incorporation or Registration and where the QGIS used in [Section 3.2.2.2](#3222-verification-of-applicants-legal-existence-and-identity) to verify legal existence contains a business address for the Applicant, the CA MAY rely on the address in the QGIS to confirm the Applicant's or a Parent/Subsidiary Company's address as listed in the EV Certificate Request, and MAY rely on the Applicant's representation that such address is its Place of Business.

   B.  **Place of Business not in the Country of Incorporation or Registration**: The CA MUST rely on a Verified Professional Letter that indicates the address of the Applicant's Place of Business and that business operations are conducted there.

#### 3.2.2.5 Verified Method of Communication

##### 3.2.2.5.1 Verification Requirements

To assist in communicating with the Applicant and confirming that the Applicant is aware of and approves issuance, the CA MUST verify a telephone number, fax number, email address, or postal delivery address as a Verified Method of Communication with the Applicant.

##### 3.2.2.5.2 Acceptable Methods of Verification

To verify a Verified Method of Communication with the Applicant, the CA MUST:

A.  Verify that the Verified Method of Communication belongs to the Applicant, or a Parent/Subsidiary or Affiliate of the Applicant, by matching it with one of the Applicant's Parent/Subsidiary or Affiliate's Places of Business in:

  i. records provided by the applicable phone company;
  ii. a QGIS, QTIS, or QIIS; or
  iii. a Verified Professional Letter; and

B.  Confirm the Verified Method of Communication by using it to obtain an affirmative response sufficient to enable a reasonable person to conclude that the Applicant, or a Parent/Subsidiary or Affiliate of Applicant, can be contacted reliably by using the Verified Method of Communication.

#### 3.2.2.6 Verification of Applicant's Operational Existence

##### 3.2.2.6.1 Verification Requirements

The CA MUST verify that the Applicant has the ability to engage in business by verifying the Applicant's, or Affiliate/Parent/Subsidiary Company's, operational existence.  The CA MAY rely on its verification of a Government Entity's legal existence under [Section 3.2.2.2](#3222-verification-of-applicants-legal-existence-and-identity) as verification of a Government Entity's operational existence.

##### 3.2.2.6.2 Acceptable Methods of Verification

To verify the Applicant's ability to engage in business, the CA MUST verify the operational existence of the Applicant, or its Affiliate/Parent/Subsidiary Company, by:

1. Verifying that the Applicant, Affiliate, Parent Company, or Subsidiary Company has been in existence for at least three years, as indicated by the records of an Incorporating Agency or Registration Agency;

2. Verifying that the Applicant, Affiliate, Parent Company, or Subsidiary Company is listed in either a current QIIS or QTIS;

3. Verifying that the Applicant, Affiliate, Parent Company, or Subsidiary Company has an active current Demand Deposit Account with a Regulated Financial Institution by receiving authenticated documentation of the Applicant's, Affiliate's, Parent Company's, or Subsidiary Company's Demand Deposit Account directly from a Regulated Financial Institution; or

4. Relying on a Verified Professional Letter to the effect that the Applicant has an active current Demand Deposit Account with a Regulated Financial Institution.

##### 3.2.2.7 Verification of Applicant's Domain Name

##### 3.2.2.7.1 Verification Requirements

1. For each Fully-Qualified Domain Name listed in a Certificate which is not an Onion Domain Name, the CA SHALL confirm that, as of the date the Certificate was issued, the Applicant (or the Applicant's Parent Company, Subsidiary Company, or Affiliate, collectively referred to as "Applicant" for the purposes of this section) either is the Domain Name Registrant or has control over the FQDN using a procedure specified in Section 3.2.2.4 of the Baseline Requirements. For a Certificate issued to an Onion Domain Name, the CA SHALL confirm that, as of the date the Certificate was issued, the Applicant's control over the Onion Domain Name in accordance with Appendix B of the Baseline Requirements.

2. **Mixed Character Set Domain Names**: EV Certificates MAY include Domain Names containing mixed character sets only in compliance with the rules set forth by the domain registrar.  The CA MUST visually compare any Domain Names with mixed character sets with known high risk domains.  If a similarity is found, then the EV Certificate Request MUST be flagged as High Risk.  The CA must perform reasonably appropriate additional authentication and verification to be certain beyond reasonable doubt that the Applicant and the target in question are the same organization.

#### 3.2.2.8 Verification of Name, Title, and Authority of Contract Signer and Certificate Approver

##### 3.2.2.8.1 Verification Requirements

For both the Contract Signer and the Certificate Approver, the CA MUST verify the following.

1. **Name, Title and Agency**: The CA MUST verify the name and title of the Contract Signer and the Certificate Approver, as applicable.  The CA MUST also verify that the Contract Signer and the Certificate Approver are agents representing the Applicant.
2. **Signing Authority of Contract Signer**: The CA MUST verify that the Contract Signer is authorized by the Applicant to enter into the Subscriber Agreement (and any other relevant contractual obligations) on behalf of the Applicant, including a contract that designates one or more Certificate Approvers on behalf of the Applicant.
3. **EV Authority of Certificate Approver**: The CA MUST verify, through a source other than the Certificate Approver him- or herself, that the Certificate Approver is expressly authorized by the Applicant to do the following, as of the date of the EV Certificate Request:

   A.  Submit, and, if applicable, authorize a Certificate Requester to submit, the EV Certificate Request on behalf of the Applicant; and
   B.  Provide, and, if applicable, authorize a Certificate Requester to provide, the information requested from the Applicant by the CA for issuance of the EV Certificate; and
   C.  Approve EV Certificate Requests submitted by a Certificate Requester.

##### 3.2.2.8.2 Acceptable Methods of Verification – Name, Title and Agency

Acceptable methods of verification of the name, title, and agency status of the Contract Signer and the Certificate Approver include the following.

1. **Name and Title**: The CA MAY verify the name and title of the Contract Signer and the Certificate Approver by any appropriate method designed to provide reasonable assurance that a person claiming to act in such a role is in fact the named person designated to act in such role.

2. **Agency**: The CA MAY verify the agency of the Contract Signer and the Certificate Approver by:

   A.  Contacting the Applicant using a Verified Method of Communication for the Applicant, and obtaining confirmation that the Contract Signer and/or the Certificate Approver, as applicable, is an employee;
   B.  Obtaining an Independent Confirmation From the Applicant (as described in [Section 3.2.2.11.4](#322114-independent-confirmation-from-applicant)), or a Verified Professional Letter verifying that the Contract Signer and/or the Certificate Approver, as applicable, is either an employee or has otherwise been appointed as an agent of the Applicant; or
   C.  Obtaining confirmation from a QIIS or QGIS that the Contract Signer and/or Certificate Approver is an employee of the Applicant.

   The CA MAY also verify the agency of the Certificate Approver via a certification from the Contract Signer (including in a contract between the CA and the Applicant signed by the Contract Signer), provided that the employment or agency status and Signing Authority of the Contract Signer has been verified.

##### 3.2.2.8.3 Acceptable Methods of Verification – Authority

Acceptable methods of verification of the Signing Authority of the Contract Signer, and the EV Authority of the Certificate Approver, as applicable, include:

1. **Verified Professional Letter**: The Signing Authority of the Contract Signer, and/or the EV Authority of the Certificate Approver, MAY be verified by reliance on a Verified Professional Letter;
2. **Corporate Resolution**: The Signing Authority of the Contract Signer, and/or the EV Authority of the Certificate Approver, MAY be verified by reliance on a properly authenticated corporate resolution that confirms that the person has been granted such Signing Authority, provided that such resolution is

   i. certified by the appropriate corporate officer (e.g., secretary), and
   ii. the CA can reliably verify that the certification was validly signed by such person, and that such person does have the requisite authority to provide such certification;

3. **Independent Confirmation from Applicant**: The Signing Authority of the Contract Signer, and/or the EV Authority of the Certificate Approver, MAY be verified by obtaining an Independent Confirmation from the Applicant (as described in [Section 3.2.2.11.4](#322114-independent-confirmation-from-applicant));
4. **Contract between CA and Applicant**: The EV Authority of the Certificate Approver MAY be verified by reliance on a contract between the CA and the Applicant that designates the Certificate Approver with such EV Authority, provided that the contract is signed by the Contract Signer and provided that the agency and Signing Authority of the Contract Signer have been verified;
5. **Prior Equivalent Authority**: The signing authority of the Contract Signer, and/or the EV authority of the Certificate Approver, MAY be verified by relying on a demonstration of Prior Equivalent Authority.

   A.  Prior Equivalent Authority of a Contract Signer MAY be relied upon for confirmation or verification of the signing authority of the Contract Signer when the Contract Signer has executed a binding contract between the CA and the Applicant with a legally valid and enforceable seal or handwritten signature and only when the contract was executed more than 90 days prior to the EV Certificate application.  The CA MUST record sufficient details of the previous agreement to correctly identify it and associate it with the EV application.  Such details MAY include any of the following:

       i. Agreement title,
       ii. Date of Contract Signer's signature,
       iii. Contract reference number, and
       iv. Filing location.

   B.  Prior Equivalent Authority of a Certificate Approver MAY be relied upon for confirmation or verification of the EV Authority of the Certificate Approver when the Certificate Approver has performed one or more of the following:

       i. Under contract to the CA, has served (or is serving) as an Enterprise RA for the Applicant, or
       ii. Has participated in the approval of one or more certificate requests, for certificates issued by the CA and which are currently and verifiably in use by the Applicant.  In this case the CA MUST have contacted the Certificate Approver by phone at a previously validated phone number or have accepted a signed and notarized letter approving the certificate request.

6. **QIIS or QGIS**: The Signing Authority of the Contract Signer, and/or the EV Authority of the Certificate Approver, MAY be verified by a QIIS or QGIS that identifies the Contract Signer and/or the Certificate Approver as a corporate officer, sole proprietor, or other senior official of the Applicant.

7. **Contract Signer's Representation/Warranty**: Provided that the CA verifies that the Contract Signer is an employee or agent of the Applicant, the CA MAY rely on the signing authority of the Contract Signer by obtaining a duly executed representation or warranty from the Contract Signer that includes the following acknowledgments:

   A.  That the Applicant authorizes the Contract Signer to sign the Subscriber Agreement on the Applicant's behalf,
   B.  That the Subscriber Agreement is a legally valid and enforceable agreement,
   C.  That, upon execution of the Subscriber Agreement, the Applicant will be bound by all of its terms and conditions,
   D.  That serious consequences attach to the misuse of an EV certificate, and
   E.  The contract signer has the authority to obtain the digital equivalent of a corporate seal, stamp or officer's signature to establish the authenticity of the company's Web site.

Note: An example of an acceptable representation/warranty appears in [Appendix E](#appendix-e---sample-contract-signers-representationwarranty-informative).

##### 3.2.2.8.4 Pre-Authorized Certificate Approver

Where the CA and Applicant contemplate the submission of multiple future EV Certificate Requests, then, after the CA:

1. Has verified the name and title of the Contract Signer and that he/she is an employee or agent of the Applicant; and

2. Has verified the Signing Authority of such Contract Signer in accordance with one of the procedures in [Section 3.2.2.8.3](#32283-acceptable-methods-of-verification--authority).

The CA and the Applicant MAY enter into a written agreement, signed by the Contract Signer on behalf of the Applicant, whereby, for a specified term, the Applicant expressly authorizes one or more Certificate Approver(s) designated in such agreement to exercise EV Authority with respect to each future EV Certificate Request submitted on behalf of the Applicant and properly authenticated as originating with, or otherwise being approved by, such Certificate Approver(s).

Such an agreement MUST provide that the Applicant shall be obligated under the Subscriber Agreement for all EV Certificates issued at the request of, or approved by, such Certificate Approver(s) until such EV Authority is revoked, and MUST include mutually agreed-upon provisions for:

   i. authenticating the Certificate Approver when EV Certificate Requests are approved,
   ii. periodic re-confirmation of the EV Authority of the Certificate Approver,
   iii. secure procedures by which the Applicant can notify the CA that the EV Authority of any such Certificate Approver is revoked, and
   iv. such other appropriate precautions as are reasonably necessary.

#### 3.2.2.9 Verification of Signature on Subscriber Agreement and EV Certificate Requests

Both the Subscriber Agreement and each non-pre-authorized EV Certificate Request MUST be signed.  The Subscriber Agreement MUST be signed by an authorized Contract Signer.  The EV Certificate Request MUST be signed by the Certificate Requester submitting the document, unless the Certificate Request has been pre-authorized in line with [Section 3.2.2.8.4](#32284-pre-authorized-certificate-approver).  If the Certificate Requester is not also an authorized Certificate Approver, then an authorized Certificate Approver MUST independently approve the EV Certificate Request.  In all cases, applicable signatures MUST be a legally valid and contain an enforceable seal or handwritten signature (for a paper Subscriber Agreement and/or EV Certificate Request), or a legally valid and enforceable electronic signature (for an electronic Subscriber Agreement and/or EV Certificate Request), that binds the Applicant to the terms of each respective document.

##### 3.2.2.9.1 Verification Requirements

1. **Signature**: The CA MUST authenticate the signature of the Contract Signer on the Subscriber Agreement and the signature of the Certificate Requester on each EV Certificate Request in a manner that makes it reasonably certain that the person named as the signer in the applicable document is, in fact, the person who signed the document on behalf of the Applicant.

2. **Approval Alternative**: In cases where an EV Certificate Request is signed and submitted by a Certificate Requester who does not also function as a Certificate Approver, approval and adoption of the EV Certificate Request by a Certificate Approver in accordance with the requirements of [Section 3.2.2.10](#32210-verification-of-approval-of-ev-certificate-request) can substitute for authentication of the signature of the Certificate Requester on such EV Certificate Request.

##### 3.2.2.9.2 Acceptable Methods of Signature Verification

Acceptable methods of authenticating the signature of the Certificate Requester or Contract Signer include the following:

1. Contacting the Applicant using a Verified Method of Communication for the Applicant, for the attention of the Certificate Requester or Contract Signer, as applicable, followed by a response from someone who identifies themselves as such person confirming that he/she did sign the applicable document on behalf of the Applicant;

2. A letter mailed to the Applicant's or Agent's address, as verified through independent means in accordance with these Guidelines, for the attention of the Certificate Requester or Contract Signer, as applicable, followed by a response through a Verified Method of Communication from someone who identifies themselves as such person confirming that he/she did sign the applicable document on behalf of the Applicant;

3. Use of a signature process that establishes the name and title of the signer in a secure manner, such as through use of an appropriately secure login process that identifies the signer before signing, or through use of a digital signature made with reference to an appropriately verified certificate; or

4. Notarization by a notary, provided that the CA independently verifies that such notary is a legally qualified notary in the jurisdiction of the Certificate Requester or Contract Signer.

#### 3.2.2.10 Verification of Approval of EV Certificate Request

##### 3.2.2.10.1 Verification Requirements

In cases where an EV Certificate Request is submitted by a Certificate Requester, before the CA issues the requested EV Certificate, the CA MUST verify that an authorized Certificate Approver reviewed and approved the EV Certificate Request.

##### 3.2.2.10.2 Acceptable Methods of Verification

Acceptable methods of verifying the Certificate Approver's approval of an EV Certificate Request include:

1. Contacting the Certificate Approver using a Verified Method of Communication for the Applicant and obtaining oral or written confirmation that the Certificate Approver has reviewed and approved the EV Certificate Request;
2. Notifying the Certificate Approver that one or more new EV Certificate Requests are available for review and approval at a designated access-controlled and secure Web site, followed by a login by, and an indication of approval from, the Certificate Approver in the manner required by the Web site; or
3. Verifying the signature of the Certificate Approver on the EV Certificate Request in accordance with [Section 3.2.2.9](#3229-verification-of-signature-on-subscriber-agreement-and-ev-certificate-requests).

#### 3.2.2.11 Verification of Certain Information Sources

##### 3.2.2.11.1 Verified Legal Opinion

1. **Verification Requirements**: Before relying on a legal opinion submitted to the CA, the CA MUST verify that such legal opinion meets the following requirements:

   A.  **Status of Author**: The CA MUST verify that the legal opinion is authored by an independent legal practitioner retained by and representing the Applicant (or an in-house legal practitioner employed by the Applicant) (Legal Practitioner) who is either:

       i. A lawyer (or solicitor, barrister, advocate, or equivalent) licensed to practice law in the country of the Applicant's Jurisdiction of Incorporation or Registration or any jurisdiction where the Applicant maintains an office or physical facility, or
       ii. A Latin Notary who is currently commissioned or licensed to practice in the country of the Applicant's Jurisdiction of Incorporation or Registration or any jurisdiction where the Applicant maintains an office or physical facility (and that such jurisdiction recognizes the role of the Latin Notary);

   B.  **Basis of Opinion**: The CA MUST verify that the Legal Practitioner is acting on behalf of the Applicant and that the conclusions of the Verified Legal Opinion are based on the Legal Practitioner's stated familiarity with the relevant facts and the exercise of the Legal Practitioner's professional judgment and expertise;
   C.  **Authenticity**: The CA MUST confirm the authenticity of the Verified Legal Opinion.

2. **Acceptable Methods of Verification**: Acceptable methods of establishing the foregoing requirements for a Verified Legal Opinion are:

   A.  **Status of Author**: The CA MUST verify the professional status of the author of the legal opinion by directly contacting the authority responsible for registering or licensing such Legal Practitioner(s) in the applicable jurisdiction;
   B.  **Basis of Opinion**: The text of the legal opinion MUST make it clear that the Legal Practitioner is acting on behalf of the Applicant and that the conclusions of the legal opinion are based on the Legal Practitioner's stated familiarity with the relevant facts and the exercise of the practitioner's professional judgment and expertise.  The legal opinion MAY also include disclaimers and other limitations customary in the Legal Practitioner's jurisdiction, provided that the scope of the disclaimed responsibility is not so great as to eliminate any substantial risk (financial, professional, and/or reputational) to the Legal Practitioner, should the legal opinion prove to be erroneous.  An acceptable form of legal opinion is attached as [Appendix B](#appendix-b---sample-attorney-opinions-confirming-specified-information);
   C.  **Authenticity**: To confirm the authenticity of the legal opinion, the CA MUST make a telephone call or send a copy of the legal opinion back to the Legal Practitioner at the address, phone number, facsimile, or (if available) e-mail address for the Legal Practitioner listed with the authority responsible for registering or licensing such Legal Practitioner, and obtain confirmation from the Legal Practitioner or the Legal Practitioner's assistant that the legal opinion is authentic.  If a phone number is not available from the licensing authority, the CA MAY use the number listed for the Legal Practitioner in records provided by the applicable phone company, QGIS, or QIIS.

       In circumstances where the opinion is digitally signed, in a manner that confirms the authenticity of the document and the identity of the signer, as verified by the CA in [Section 3.2.2.11.1](#322111-verified-legal-opinion) (2)(A), no further verification of authenticity is required.

##### 3.2.2.11.2 Verified Accountant Letter

1. **Verification Requirements**: Before relying on an accountant letter submitted to the CA, the CA MUST verify that such accountant letter meets the following requirements:

   A.  **Status of Author**: The CA MUST verify that the accountant letter is authored by an Accounting Practitioner retained or employed by the Applicant and licensed within the country of the Applicant's Jurisdiction of Incorporation, Jurisdiction of Registration, or country where the Applicant maintains an office or physical facility.  Verification of license MUST be  through the member organization or regulatory organization in the Accounting Practitioner's country or jurisdiction that is appropriate to contact when verifying an accountant's license to practice in that country or jurisdiction.  Such country or jurisdiction must have an accounting standards body that maintains full membership status with the International Federation of Accountants.
   B.  **Basis of Opinion**: The CA MUST verify that the Accounting Practitioner is acting on behalf of the Applicant and that the conclusions of the Verified Accountant Letter are based on the Accounting Practitioner's stated familiarity with the relevant facts and the exercise of the Accounting Practitioner's professional judgment and expertise;
   C.  **Authenticity**: The CA MUST confirm the authenticity of the Verified Accountant Letter.

2. **Acceptable Methods of Verification**: Acceptable methods of establishing the foregoing requirements for a Verified Accountant Letter are listed here.

   A.  **Status of Author**: The CA MUST verify the professional status of the author of the accountant letter by directly contacting the authority responsible for registering or licensing such Accounting Practitioners in the applicable jurisdiction.
   B.  **Basis of Opinion**: The text of the Verified Accountant Letter MUST make clear that the Accounting Practitioner is acting on behalf of the Applicant and that the information in the letter is based on the Accounting Practitioner's stated familiarity with the relevant facts and the exercise of the practitioner's professional judgment and expertise.  The Verified Accountant Letter MAY also include disclaimers and other limitations customary in the Accounting Practitioner's jurisdiction, provided that the scope of the disclaimed responsibility is not so great as to eliminate any substantial risk (financial, professional, and/or reputational) to the Accounting Practitioner, should the Verified Accountant Letter prove to be erroneous.  Acceptable forms of Verified Accountant Letter are attached as [Appendix C](#appendix-c---sample-accountant-letters-confirming-specified-information).
   C.  **Authenticity**: To confirm the authenticity of the accountant's opinion, the CA MUST make a telephone call or send a copy of the Verified Accountant Letter back to the Accounting Practitioner at the address, phone number, facsimile, or (if available) e-mail address for the Accounting Practitioner listed with the authority responsible for registering or licensing such Accounting Practitioners and obtain confirmation from the Accounting Practitioner or the Accounting Practitioner's assistant that the accountant letter is authentic.  If a phone number is not available from the licensing authority, the CA MAY use the number listed for the Accountant in records provided by the applicable phone company, QGIS, or QIIS.

      In circumstances where the opinion is digitally signed, in a manner that confirms the authenticity of the document and the identity of the signer, as verified by the CA in [Section 3.2.2.11.2](#322112-verified-accountant-letter) (2)(A), no further verification of authenticity is required.

##### 3.2.2.11.3 Face-to-Face Validation

1. **Verification Requirements**: Before relying on face-to-face vetting documents submitted to the CA, the CA MUST verify that the Third-Party Validator meets the following requirements:

   A.  **Qualification of Third-Party Validator**: The CA MUST independently verify that the Third-Party Validator is a legally-qualified Latin Notary or Notary (or legal equivalent in the Applicant's jurisdiction), Lawyer, or Accountant in the jurisdiction of the individual's residency;
   B.  **Document Chain of Custody**: The CA MUST verify that the Third-Party Validator viewed the Vetting Documents in a face-to-face meeting with the individual being validated;
   C.  **Verification of Attestation**: If the Third-Party Validator is not a Latin Notary, then the CA MUST confirm the authenticity of the attestation and vetting documents.

2. **Acceptable Methods of Verification**: Acceptable methods of establishing the foregoing requirements for vetting documents are:

   A.  **Qualification of Third-Party Validator**: The CA MUST verify the professional status of the Third-Party Validator by directly contacting the authority responsible for registering or licensing such Third-Party Validators in the applicable jurisdiction;
   B.  **Document Chain of Custody**: The Third-Party Validator MUST submit a statement to the CA which attests that they obtained the Vetting Documents submitted to the CA for the individual during a face-to-face meeting with the individual;
   C.  **Verification of Attestation**: If the Third-Party Validator is not a Latin Notary, then the CA MUST confirm the authenticity of the vetting documents received from the Third-Party Validator.  The CA MUST make a telephone call to the Third-Party Validator and obtain confirmation from them or their assistant that they performed the face-to-face validation.  The CA MAY rely upon self-reported information obtained from the Third-Party Validator for the sole purpose of performing this verification process.  In circumstances where the attestation is digitally signed, in a manner that confirms the authenticity of the documents, and the identity of the signer as verified by the CA in [Section 3.2.2.11.3](#322113-face-to-face-validation) (1)(A), no further verification of authenticity is required.

##### 3.2.2.11.4 Independent Confirmation From Applicant

An Independent Confirmation from the Applicant is a confirmation of a particular fact (e.g., confirmation of the employee or agency status of a Contract Signer or Certificate Approver, confirmation of the EV Authority of a Certificate Approver, etc.) that is:

A.  Received by the CA from a Confirming Person (someone other than the person who is the subject of the inquiry) that has the appropriate authority to confirm such a fact, and who represents that he/she has confirmed such fact;
B.  Received by the CA in a manner that authenticates and verifies the source of the confirmation; and
C.  Binding on the Applicant.

An Independent Confirmation from the Applicant MAY be obtained via the following procedure:

1. **Confirmation Request**: The CA MUST initiate a Confirmation Request via an appropriate out-of-band communication, requesting verification or confirmation of the particular fact at issue as follows:

   A.  **Addressee**: The Confirmation Request MUST be directed to:

       i. A position within the Applicant's organization that qualifies as a Confirming Person (e.g., Secretary, President, CEO, CFO, COO, CIO, CSO, Director, etc.) and is identified by name and title in a current QGIS, QIIS, QTIS, Verified Legal Opinion, Verified Accountant Letter, or by contacting the Applicant using a Verified Method of Communication; or
       ii. The Applicant's Registered Agent or Registered Office in the Jurisdiction of Incorporation as listed in the official records of the Incorporating Agency, with instructions that it be forwarded to an appropriate Confirming Person; or
       iii. A named individual verified to be in the direct line of management above the Contract Signer or Certificate Approver by contacting the Applicant's Human Resources Department by phone or mail (at the phone number or address for the Applicant's Place of Business, verified in accordance with these Guidelines).

   B.  **Means of Communication**: The Confirmation Request MUST be directed to the Confirming Person in a manner reasonably likely to reach such person.  The following options are acceptable:

       i. By paper mail addressed to the Confirming Person at:

          1. The address of the Applicant's Place of Business as verified by the CA in accordance with these Guidelines, or
          2. The business address for such Confirming Person specified in a current QGIS, QTIS, QIIS, Verified Professional Letter, or
          3. The address of the Applicant's Registered Agent or Registered Office listed in the official records of the Jurisdiction of Incorporation, or

       ii. By e-mail addressed to the Confirming Person at the business e-mail address for such person listed in a current QGIS, QTIS, QIIS, Verified Legal Opinion, or Verified Accountant Letter; or
       iii. By telephone call to the Confirming Person, where such person is contacted by calling the main phone number of the Applicant's Place of Business (verified in accordance with these Guidelines) and asking to speak to such person, and a person taking the call identifies him- or herself as such person; or
       iv. By facsimile to the Confirming Person at the Place of Business.  The facsimile number must be listed in a current QGIS, QTIS, QIIS, Verified Legal Opinion, or Verified Accountant Letter.  The cover page must be clearly addressed to the Confirming Person.

2. **Confirmation Response**: The CA MUST receive a response to the Confirmation Request from a Confirming Person that confirms the particular fact at issue.  Such response MAY be provided to the CA by telephone, by e-mail, or by paper mail, so long as the CA can reliably verify that it was provided by a Confirming Person in response to the Confirmation Request.

3. The CA MAY rely on a verified Confirming Person to confirm their own contact information: email address, telephone number, and facsimile number.  The CA MAY rely on this verified contact information for future correspondence with the Confirming Person if:

   A.  The domain of the e-mail address is owned by the Applicant and is the Confirming Person's own e-mail address and not a group e-mail alias;
   B.  The Confirming Person's telephone/fax number is verified by the CA to be a telephone number that is part of the organization's telephone system, and is not the personal phone number for the person.

##### 3.2.2.11.5 Qualified Independent Information Source

A Qualified Independent Information Source (QIIS) is a regularly-updated and publicly available database that is generally recognized as a dependable source for certain information.  A database qualifies as a QIIS if the CA determines that:

1. Industries other than the certificate industry rely on the database for accurate location, contact, or other information; and

2. The database provider updates its data on at least an annual basis.

The CA SHALL use a documented process to check the accuracy of the database and ensure its data is acceptable, including reviewing the database provider's terms of use. The CA SHALL NOT use any data in a QIIS that the CA knows is

  i. self-reported and
  ii. not verified by the QIIS as accurate.

Databases in which the CA or its owners or affiliated companies maintain a controlling interest, or in which any Registration Authorities or subcontractors to whom the CA has outsourced any portion of the vetting process (or their owners or affiliated companies) maintain any ownership or beneficial interest, do not qualify as a QIIS.

##### 3.2.2.11.6 Qualified Government Information Source

A Qualified Government Information Source (QGIS) is a regularly-updated and current, publicly available, database designed for the purpose of accurately providing the information for which it is consulted, and which is generally recognized as a dependable source of such information provided that it is maintained by a Government Entity, the reporting of data is required by law, and false or misleading reporting is punishable with criminal or civil penalties. Nothing in these Guidelines shall prohibit the use of third-party vendors to obtain the information from the Government Entity provided that the third party obtains the information directly from the Government Entity.

##### 3.2.2.11.7 Qualified Government Tax Information Source

A Qualified Government Tax Information Source is a Qualified Government Information Source that specifically contains tax information relating to Private Organizations, Business Entities or Individuals (e.g., the IRS in the United States).

#### 3.2.2.12 Other Verification Requirements

##### 3.2.2.12.1 High Risk Status

The High Risk Certificate requirements of Section 4.2.1 of the Baseline Requirements apply equally to EV Certificates.

##### 3.2.2.12.2 Denied Lists and Other Legal Block Lists

1. **Verification Requirements**: The CA MUST verify whether the Applicant, the Contract Signer, the Certificate Approver, the Applicant's Jurisdiction of Incorporation, Registration, or Place of Business:

   A.  Is identified on any government denied list, list of prohibited persons, or other list that prohibits doing business with such organization or person under the laws of the country of the CA's jurisdiction(s) of operation; or
   B.  Has its Jurisdiction of Incorporation, Registration, or Place of Business in any country with which the laws of the CA's jurisdiction prohibit doing business.

   The CA MUST NOT issue any EV Certificate to the Applicant if either the Applicant, the Contract Signer, or Certificate Approver or if the Applicant's Jurisdiction of Incorporation or Registration or Place of Business is on any such list.

2. **Acceptable Methods of Verification**  The CA MUST take reasonable steps to verify with the following lists and regulations:

   A.  If the CA has operations in the U.S., the CA MUST take reasonable steps to verify with the following US Government denied lists and regulations:

       i. BIS Denied Persons List - [https://www.bis.doc.gov/index.php/the-denied-persons-list](https://www.bis.doc.gov/index.php/the-denied-persons-list)
       ii. BIS Denied Entities List - [https://www.bis.doc.gov/index.php/policy-guidance/lists-of-parties-of-concern/entity-list](https://www.bis.doc.gov/index.php/policy-guidance/lists-of-parties-of-concern/entity-list)
       iii. US Treasury Department List of Specially Designated Nationals and Blocked Persons - [https://www.treasury.gov/resource-center/sanctions/sdn-list/pages/default.aspx](https://www.treasury.gov/resource-center/sanctions/sdn-list/pages/default.aspx)
       iv. US Government export regulations

   B.  If the CA has operations in any other country, the CA MUST take reasonable steps to verify with all equivalent denied lists and export regulations (if any) in such other country.

##### 3.2.2.12.3 Parent/Subsidiary/Affiliate Relationship

A CA verifying an Applicant using information of the Applicant's Parent, Subsidiary, or Affiliate, when allowed under [Section 3.2.2.4.1](#32241-address-of-applicants-place-of-business), [Section 3.2.2.5](#3225-verified-method-of-communication), [Section 3.2.2.6.1](#32261-verification-requirements), or [Section 3.2.2.7.1](#32271-verification-requirements), MUST verify the Applicant's relationship to the Parent, Subsidiary, or Affiliate. Acceptable methods of verifying the Applicant's relationship to the Parent, Subsidiary, or Affiliate include the following:

1. QIIS or QGIS: The relationship between the Applicant and the Parent, Subsidiary, or Affiliate is identified in a QIIS or QGIS;
2. Independent Confirmation from the Parent, Subsidiary, or Affiliate: A CA MAY verify the relationship between an Applicant and a Parent, Subsidiary, or Affiliate by obtaining an Independent Confirmation from the appropriate Parent, Subsidiary, or Affiliate (as described in [Section 3.2.2.11.4](#322114-independent-confirmation-from-applicant));
3. Contract between CA and Parent, Subsidiary, or Affiliate: A CA MAY verify the relationship between an Applicant and a Parent, Subsidiary, or Affiliate by relying on a contract between the CA and the Parent, Subsidiary, or Affiliate that designates the Certificate Approver with such EV Authority, provided that the contract is signed by the Contract Signer and provided that the agency and Signing Authority of the Contract Signer have been verified;
4. Verified Professional Letter: A CA MAY verify the relationship between an Applicant and a Parent, Subsidiary, or Affiliate by relying on a Verified Professional Letter; or
5. Corporate Resolution: A CA MAY verify the relationship between an Applicant and a Subsidiary by relying on a properly authenticated corporate resolution that approves creation of the Subsidiary or the Applicant, provided that such resolution is:

   i. certified by the appropriate corporate officer (e.g., secretary), and
   ii. the CA can reliably verify that the certification was validly signed by such person, and that such person does have the requisite authority to provide such certification.

#### 3.2.2.13 Final Cross-Correlation and Due Diligence

1. The results of the verification processes and procedures outlined in these Guidelines are intended to be viewed both individually and as a group.  Thus, after all of the verification processes and procedures are completed, the CA MUST have a person who is not responsible for the collection of information review all of the information and documentation assembled in support of the EV Certificate application and look for discrepancies or other details requiring further explanation.
2. The CA MUST obtain and document further explanation or clarification from the Applicant, Certificate Approver, Certificate Requester, Qualified Independent Information Sources, and/or other sources of information, as necessary, to resolve those discrepancies or details that require further explanation.
3. The CA MUST refrain from issuing an EV Certificate until the entire corpus of information and documentation assembled in support of the EV Certificate Request is such that issuance of the EV Certificate will not communicate factual information that the CA knows, or the exercise of due diligence should discover from the assembled information and documentation, to be inaccurate,.  If satisfactory explanation and/or additional documentation are not received within a reasonable time, the CA MUST decline the EV Certificate Request and SHOULD notify the Applicant accordingly.
4. In the case where some or all of the documentation used to support the application is in a language other than the CA's normal operating language, the CA or its Affiliate MUST perform the requirements of this Final Cross-Correlation and Due Diligence section using employees under its control and having appropriate training, experience, and judgment in confirming organizational identification and authorization and fulfilling all qualification requirements contained in [Section 5.3.2](#532-background-check-procedures).  When employees under the control of the CA do not possess the language skills necessary to perform the Final Cross-Correlation and Due Diligence a CA MAY:

   A.  Rely on language translations of the relevant portions of the documentation, provided that the translations are received from a Translator; or
   B.  When the CA has utilized the services of an RA, the CA MAY rely on the language skills of the RA to perform the Final Cross-Correlation and Due Diligence, provided that the RA complies with [Section 3.2.2.13](#32213-final-cross-correlation-and-due-diligence), Subsections (1), (2) and (3).  Notwithstanding the foregoing, prior to issuing the EV Certificate, the CA MUST review the work completed by the RA and determine that all requirements have been met; or
   C.  When the CA has utilized the services of an RA, the CA MAY rely on the RA to perform the Final Cross-Correlation and Due Diligence, provided that the RA complies with this section and is subjected to the Audit Requirements of [Section 8.1.1](#811-self-audits) and [Section 8.2](#82-identityqualifications-of-assessor).

In the case of EV Certificates to be issued in compliance with the requirements of [Section 1.3.2](#132-registration-authorities), the Enterprise RA MAY perform the requirements of this Final Cross-Correlation and Due Diligence section.

#### 3.2.2.14 Requirements for Re-use of Existing Documentation

For each EV Certificate Request, including requests to renew existing EV Certificates, the CA MUST perform all authentication and verification tasks required by these Guidelines to ensure that the request is properly authorized by the Applicant and that the information in the EV Certificate is still accurate and valid. This section sets forth the age limitations on for the use of documentation collected by the CA.

##### 3.2.2.14.1 Validation For Existing Subscribers

If an Applicant has a currently valid EV Certificate issued by the CA, a CA MAY rely on its prior authentication and verification of:

1. The Principal Individual verified under [Section 3.2.2.2.2](#32222-acceptable-method-of-verification) (4) if the individual is the same person as verified by the CA in connection with the Applicant's previously issued and currently valid EV Certificate;
2. The Applicant's Place of Business under [Section 3.2.2.4.1](#32241-address-of-applicants-place-of-business);
3. The Applicant's Verified Method of Communication required by [Section 3.2.2.5](#3225-verified-method-of-communication) but still MUST perform the verification required by [Section 3.2.2.5.2](#32252-acceptable-methods-of-verification) (B);
4. The Applicant's Operational Existence under [Section 3.2.2.6](#3226-verification-of-applicants-operational-existence);
5. The Name, Title, Agency and Authority of the Contract Signer, and Certificate Approver, under [Section 3.2.2.8](#3228-verification-of-name-title-and-authority-of-contract-signer-and-certificate-approver); and
6. The Applicant's right to use the specified Domain Name under [Section 3.2.2.7](#3227-verification-of-applicants-domain-name), provided that the CA verifies that the WHOIS record still shows the same registrant as when the CA verified the specified Domain Name for the initial EV Certificate.

##### 3.2.2.14.2 Re-issuance Requests

A CA may rely on a previously verified certificate request to issue a replacement certificate, so long as the certificate being referenced was not revoked due to fraud or other illegal conduct, if:

1. The expiration date of the replacement certificate is the same as the expiration date of the  EV Certificate that is being replaced, and
2. The Subject Information of the Certificate is the same as the Subject in the EV Certificate that is being replaced.

##### 3.2.2.14.3 Age of Validated Data

1. Except for reissuance of an EV Certificate under [Section 3.2.2.14.2](#322142-re-issuance-requests) and except when permitted otherwise in [Section 3.2.2.14.1](#322141-validation-for-existing-subscribers), the age of all data used to support issuance of an EV Certificate (before revalidation is required) SHALL NOT exceed the following limits:

   A.  Legal existence and identity – 398 days;
   B.  Assumed name – 398 days;
   C.  Address of Place of Business – 398 days;
   D.  Verified Method of Communication – 398 days;
   E.  Operational existence – 398 days;
   F.  Domain Name – 398 days;
   G.  Name, Title, Agency, and Authority – 398 days, unless a contract between the CA and the Applicant specifies a different term, in which case, the term specified in such contract controls.  For example, the contract MAY include the perpetual assignment of EV roles until revoked by the Applicant or CA, or until the contract expires or is terminated.

2. The 398-day period set forth above SHALL begin to run on the date the information was collected by the CA.
3. The CA MAY reuse a previously submitted EV Certificate Request, Subscriber Agreement, or Terms of Use, including use of a single EV Certificate Request in support of multiple EV Certificates containing the same Subject to the extent permitted under [Section 3.2.2.9](#3229-verification-of-signature-on-subscriber-agreement-and-ev-certificate-requests) and [Section 3.2.2.10](#32210-verification-of-approval-of-ev-certificate-request).
4. The CA MUST repeat the verification process required in these Guidelines for any information obtained outside the time limits specified above except when permitted otherwise under [Section 3.2.2.14.1](#322141-validation-for-existing-subscribers).

### 3.2.3 Authentication of individual identity

If an Applicant subject to this [Section 3.2.3](#323-authentication-of-individual-identity) is a natural person, then the CA SHALL verify the Applicant's name, Applicant's address, and the authenticity of the certificate request.

The CA SHALL verify the Applicant's name using a legible copy, which discernibly shows the Applicant's face, of at least one currently valid government-issued photo ID (passport, drivers license, military ID, national ID, or equivalent document type). The CA SHALL inspect the copy for any indication of alteration or falsification.

The CA SHALL verify the Applicant's address using a form of identification that the CA determines to be reliable, such as a government ID, utility bill, or bank or credit card statement. The CA MAY rely on the same government-issued ID that was used to verify the Applicant's name.

The CA SHALL verify the certificate request with the Applicant using a Reliable Method of Communication.

### 3.2.3 Authentication of individual identity
### 3.2.4 Non-verified subscriber information

### 3.2.5 Validation of authority

If the Applicant for a Certificate containing Subject Identity Information is an organization, the CA SHALL use a Reliable Method of Communication to verify the authenticity of the Applicant Representative's certificate request.

The CA MAY use the sources listed in [Section 3.2.2.1](#3221-identity) to verify the Reliable Method of Communication. Provided that the CA uses a Reliable Method of Communication, the CA MAY establish the authenticity of the certificate request directly with the Applicant Representative or with an authoritative source within the Applicant's organization, such as the Applicant's main business offices, corporate offices, human resource offices, information technology offices, or other department that the CA deems appropriate.

In addition, the CA SHALL establish a process that allows an Applicant to specify the individuals who may request Certificates. If an Applicant specifies, in writing, the individuals who may request a Certificate, then the CA SHALL NOT accept any certificate requests that are outside this specification. The CA SHALL provide an Applicant with a list of its authorized certificate requesters upon the Applicant's verified written request.

### 3.2.5 Validation of authority
### 3.2.6 Criteria for Interoperation or Certification

The CA SHALL disclose all Cross-Certified Subordinate CA Certificates that identify the CA as the Subject, provided that the CA arranged for or accepted the establishment of the trust relationship (i.e. the Cross-Certified Subordinate CA Certificate at issue).

### 3.2.6 Criteria for interoperation

## 3.3 Identification and authentication for re-key requests

### 3.3.1 Identification and authentication for routine re-key

### 3.3.2 Identification and authentication for re-key after revocation

## 3.4 Identification and authentication for revocation request

# 4. CERTIFICATE LIFE-CYCLE OPERATIONAL REQUIREMENTS

## 4.1 Certificate Application

### 4.1.1 Who can submit a certificate application


### 4.1.1 Who can submit a certificate application
The CA MAY only issue EV Certificates to Applicants that meet the Private Organization, Government Entity, Business Entity and Non-Commercial Entity requirements specified below.

#### 4.1.1.1 Private Organization Subjects

An Applicant qualifies as a Private Organization if:

1. The entity's legal existence is created or recognized by a by a filing with (or an act of) the Incorporating or Registration Agency in its Jurisdiction of Incorporation or Registration (e.g., by issuance of a certificate of incorporation, registration number, etc.) or created or recognized by a Government Agency (e.g. under a charter, treaty, convention, or equivalent recognition instrument);

2. The entity designated with the Incorporating or Registration Agency a Registered Agent, a Registered Office (as required under the laws of the Jurisdiction of Incorporation or Registration), or an equivalent facility;

3. The entity is not designated on the records of the Incorporating or Registration Agency by labels such as "inactive," "invalid," "not current," or the equivalent;

4. The entity has a verifiable physical existence and business presence;

5. The entity's Jurisdiction of Incorporation, Registration, Charter, or License, and/or its Place of Business is not in any country where the CA is prohibited from doing business or issuing a certificate by the laws of the CA's jurisdiction; and

6. The entity is not listed on any government denial list or prohibited list (e.g., trade embargo) under the laws of the CA's jurisdiction.

#### 4.1.1.2 Government Entity Subjects

An Applicant qualifies as a Government Entity if:

1. The entity's legal existence was established by the political subdivision in which the entity operates;

2. The entity is not in any country where the CA is prohibited from doing business or issuing a certificate by the laws of the CA's jurisdiction; and

3. The entity is not listed on any government denial list or prohibited list (e.g., trade embargo) under the laws of the CA's jurisdiction.

#### 4.1.1.3 Business Entity Subjects

An Applicant qualifies as a Business Entity if:

1. The entity is a legally recognized entity that filed certain forms with a Registration Agency in its jurisdiction, the Registration Agency issued or approved the entity's charter, certificate, or license, and the entity's existence can be verified with that Registration Agency;

2. The entity has a verifiable physical existence and business presence;

3. At least one Principal Individual associated with the entity is identified and validated by the CA;

4. The identified Principal Individual attests to the representations made in the Subscriber Agreement;

5. The CA verifies the entity's use of any assumed name used to represent the entity pursuant to the requirements of [Section 3.2.2.3](#3223-verification-of-applicants-legal-existence-and-identity--assumed-name);

6. The entity and the identified Principal Individual associated with the entity are not located or residing in any country where the CA is prohibited from doing business or issuing a certificate by the laws of the CA's jurisdiction; and

7. The entity and the identified Principal Individual associated with the entity are not listed on any government denial list or prohibited list (e.g., trade embargo) under the laws of the CA's jurisdiction.

#### 4.1.1.4 Non-Commercial Entity Subjects

An Applicant qualifies as a Non-Commercial Entity if:

1. The Applicant is an International Organization Entity, created under a charter, treaty, convention or equivalent instrument that was signed by, or on behalf of, more than one country's government.  The CA/Browser Forum may publish a listing of Applicants who qualify as an International Organization for EV eligibility; and

2. The Applicant is not headquartered in any country where the CA is prohibited from doing business or issuing a certificate by the laws of the CA's jurisdiction; and

3. The Applicant is not listed on any government denial list or prohibited list (e.g., trade embargo) under the laws of the CA's jurisdiction.

Subsidiary organizations or agencies of an entity that qualifies as a Non-Commercial Entity also qualifies for EV Certificates as a Non-Commercial Entity.

### 4.1.2 Enrollment process and responsibilities

Prior to the issuance of a Certificate, the CA SHALL obtain the following documentation from the Applicant:

1. A certificate request, which may be electronic; and
2. An executed Subscriber Agreement or Terms of Use, which may be electronic.

The CA SHOULD obtain any additional documentation the CA determines necessary to meet these Requirements.

Prior to the issuance of a Certificate, the CA SHALL obtain from the Applicant a certificate request in a form prescribed by the CA and that complies with these Requirements. One certificate request MAY suffice for multiple Certificates to be issued to the same Applicant, subject to the aging and updating requirement in [Section 4.2.1](#421-performing-identification-and-authentication-functions), provided that each Certificate is supported by a valid, current certificate request signed by the appropriate Applicant Representative on behalf of the Applicant. The certificate request MAY be made, submitted and/or signed electronically.

The certificate request MUST contain a request from, or on behalf of, the Applicant for the issuance of a Certificate, and a certification by, or on behalf of, the Applicant that all of the information contained therein is correct.

### 4.1.2 Enrollment process and responsibilities
The documentation requirements in Section 4.1.2 of the Baseline Requirements apply equally to EV Certificates.
The Certificate Request requirements in Section 4.1.2 of the Baseline Requirements apply equally to EV Certificates subject to the additional more stringent ageing and updating requirement of [Section 3.2.2.14](#32214-requirements-for-re-use-of-existing-documentation).

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
The following Applicant roles are required for the issuance of an EV Certificate.

1. **Certificate Requester**: The EV Certificate Request MUST be submitted by an authorized Certificate Requester.  A Certificate Requester is a natural person who is either the Applicant, employed by the Applicant, an authorized agent who has express authority to represent the Applicant, or a third party (such as an ISP or hosting company) that completes and submits an EV Certificate Request on behalf of the Applicant.

2. **Certificate Approver**: The EV Certificate Request MUST be approved by an authorized Certificate Approver.  A Certificate Approver is a natural person who is either the Applicant, employed by the Applicant, or an authorized agent who has express authority to represent the Applicant to

   i. act as a Certificate Requester and to authorize other employees or third parties to act as a Certificate Requester, and
   ii. to approve EV Certificate Requests submitted by other Certificate Requesters.

3. **Contract Signer**: A Subscriber Agreement applicable to the requested EV Certificate MUST be signed by an authorized Contract Signer.  A Contract Signer is a natural person who is either the Applicant, employed by the Applicant, or an authorized agent who has express authority to represent the Applicant, and who has authority on behalf of the Applicant to sign Subscriber Agreements.

4. **Applicant Representative**: In the case where the CA and the Subscriber are affiliated, Terms of Use applicable to the requested EV Certificate MUST be acknowledged and agreed to by an authorized Applicant Representative.  An Applicant Representative is a natural person who is either the Applicant, employed by the Applicant, or an authorized agent who has express authority to represent the Applicant, and who has authority on behalf of the Applicant to acknowledge and agree to the Terms of Use.

The Applicant MAY authorize one individual to occupy two or more of these roles. The Applicant MAY authorize more than one individual to occupy any of these roles.

### 4.2.2 Approval or rejection of certificate applications

CAs SHALL NOT issue certificates containing Internal Names or Reserved IP Addresses, as such names cannot be validated according to [Section 3.2.2.4](#3224-validation-of-domain-authorization-or-control) or [Section 3.2.2.5](#3225-authentication-for-an-ip-address).

### 4.2.2 Approval or rejection of certificate applications
### 4.2.3 Time to process certificate applications


## 4.3 Certificate issuance

### 4.3.1 CA actions during certificate issuance

Certificate issuance by the Root CA SHALL require an individual authorized by the CA (i.e. the CA system operator, system officer, or PKI administrator) to deliberately issue a direct command in order for the Root CA to perform a certificate signing operation.

### 4.3.1 CA actions during certificate issuance
Certificate issuance by the Root CA SHALL require an individual authorized by the CA (i.e. the CA system operator, system officer, or PKI administrator) to deliberately issue a direct command in order for the Root CA to perform a certificate signing operation.

Root CA Private Keys MUST NOT be used to sign EV Certificates.

### 4.3.2 Notification to subscriber by the CA of issuance of certificate


## 4.4 Certificate acceptance

### 4.4.1 Conduct constituting certificate acceptance


### 4.4.2 Publication of the certificate by the CA


### 4.4.3 Notification of certificate issuance by the CA to other entities


## 4.5 Key pair and certificate usage

### 4.5.1 Subscriber private key and certificate usage

See [Section 9.6.3](#963-subscriber-representations-and-warranties), provisions 2. and 4.

### 4.5.1 Subscriber private key and certificate usage
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

### 4.9.2 Who can request revocation

The Subscriber, RA, or Issuing CA can initiate revocation. Additionally, Subscribers, Relying Parties, Application Software Suppliers, and other third parties may submit Certificate Problem Reports informing the issuing CA of reasonable cause to revoke the certificate.

### 4.9.2 Who can request revocation
### 4.9.3 Procedure for revocation request

The CA SHALL provide a process for Subscribers to request revocation of their own Certificates. The process MUST be described in the CA's Certificate Policy or Certification Practice Statement. The CA SHALL maintain a continuous 24x7 ability to accept and respond to revocation requests and Certificate Problem Reports.

The CA SHALL provide Subscribers, Relying Parties, Application Software Suppliers, and other third parties with clear instructions for reporting suspected Private Key Compromise, Certificate misuse, or other types of fraud, compromise, misuse, inappropriate conduct, or any other matter related to Certificates. The CA SHALL publicly disclose the instructions through a readily accessible online means and in Section 1.5.2 of their CPS.

### 4.9.3 Procedure for revocation request
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
### 4.9.6 Revocation checking requirement for relying parties


**Note**: Following certificate issuance, a certificate may be revoked for reasons stated in [Section 4.9](#49-certificate-revocation-and-suspension). Therefore, relying parties should check the revocation status of all certificates that contain a CDP or OCSP pointer.

### 4.9.6 Revocation checking requirement for relying parties
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


### 4.9.7 CRL issuance frequency (if applicable)
### 4.9.8 Maximum latency for CRLs (if applicable)


### 4.9.9 On-line revocation/status checking availability

The following SHALL apply for communicating the status of Certificates which include an Authority Information Access extension with an id-ad-ocsp accessMethod.

OCSP responses MUST conform to RFC6960 and/or RFC5019. OCSP responses MUST either:

1. Be signed by the CA that issued the Certificates whose revocation status is being checked, or
2. Be signed by an OCSP Responder whose Certificate is signed by the CA that issued the Certificate whose
revocation status is being checked.

In the latter case, the OCSP signing Certificate MUST contain an extension of type `id-pkix-ocsp-nocheck`, as
defined by RFC6960.

### 4.9.9 On-line revocation/status checking availability
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
### 4.9.11 Other forms of revocation advertisements available

No Stipulation.

### 4.9.11 Other forms of revocation advertisements available
### 4.9.12 Special requirements re key compromise

See [Section 4.9.1](#491-circumstances-for-revocation).

### 4.9.12 Special requirements re key compromise
### 4.9.13 Circumstances for suspension

The Repository MUST NOT include entries that indicate that a Certificate is suspended.

### 4.9.13 Circumstances for suspension
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
### 4.10.2 Service availability

The CA SHALL operate and maintain its CRL and optional OCSP capability with resources sufficient to provide a response time of ten seconds or less under normal operating conditions.

The CA SHALL maintain an online 24x7 Repository that application software can use to automatically check the current status of all unexpired Certificates issued by the CA.

The CA SHALL maintain a continuous 24x7 ability to respond internally to a high-priority Certificate Problem Report, and where appropriate, forward such a complaint to law enforcement authorities, and/or revoke a Certificate that is the subject of such a complaint.

### 4.10.2 Service availability
### 4.10.3 Optional features


## 4.11 End of subscription


## 4.12 Key escrow and recovery

### 4.12.1 Key escrow and recovery policy and practices


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
As specified in Section 5 of the Baseline Requirements. In addition, systems used to process and approve EV Certificate Requests MUST require actions by at least two trusted persons before creating an EV Certificate.

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
### 5.2.3 Identification and authentication for each role

### 5.2.4 Roles requiring separation of duties

### 5.2.4 Roles requiring separation of duties
1. The CA MUST enforce rigorous control procedures for the separation of validation duties to ensure that no one person can single-handedly validate and authorize the issuance of an EV Certificate.  The Final Cross-Correlation and Due Diligence steps, as outlined in [Section 3.2.2.13](#32213-final-cross-correlation-and-due-diligence), MAY be performed by one of the persons.  For example, one Validation Specialist MAY review and verify all the Applicant information and a second Validation Specialist MAY approve issuance of the EV Certificate.
2. Such controls MUST be auditable.
   
## 5.3 Personnel controls

### 5.3.1 Qualifications, experience, and clearance requirements

Prior to the engagement of any person in the Certificate Management Process, whether as an employee, agent, or an independent contractor of the CA, the CA SHALL verify the identity and trustworthiness of such person.

### 5.3.1 Qualifications, experience, and clearance requirements

### 5.3.2 Background check procedures

### 5.3.2 Background check procedures
Prior to the commencement of employment of any person by the CA for engagement in the EV Processes, whether as an employee, agent, or an independent contractor of the CA, the CA MUST:

1. **Verify the Identity of Such Person**: Verification of identity MUST be performed through:

   A.  The personal (physical) presence of such person before trusted persons who perform human resource or security functions, and
   B.  The verification of well-recognized forms of government-issued photo identification (e.g., passports and/or drivers licenses);

   and

2. **Verify the Trustworthiness of Such Person**: Verification of trustworthiness SHALL include background checks, which address at least the following, or their equivalent:

   A.  Confirmation of previous employment,
   B.  Check of professional references;
   C.  Confirmation of the highest or most-relevant educational qualification obtained;
   D.  Search of criminal records (local, state or provincial, and national) where allowed by the jurisdiction in which the person will be employed;

   and

3. In the case of employees already in the employ of the CA at the time of adoption of these Guidelines whose identity and background has not previously been verified as set forth above, the CA SHALL conduct such verification within three months of the date of adoption of these Guidelines.

### 5.3.3 Training Requirements and Procedures

The CA SHALL provide all personnel performing information verification duties with skills-training that covers basic Public Key Infrastructure knowledge, authentication and vetting policies and procedures (including the CA's Certificate Policy and/or Certification Practice Statement), common threats to the information verification process (including phishing and other social engineering tactics), and these Requirements.

The CA SHALL maintain records of such training and ensure that personnel entrusted with Validation Specialist duties maintain a skill level that enables them to perform such duties satisfactorily.

The CA SHALL document that each Validation Specialist possesses the skills required by a task before allowing the Validation Specialist to perform that task.

The CA SHALL require all Validation Specialists to pass an examination provided by the CA on the information verification requirements outlined in these Requirements.

### 5.3.3 Training requirements
The requirements in Section 5.3.3 of the Baseline Requirements apply equally to EV Certificates and these Guidelines.  The required internal examination must relate to the EV Certificate validation criteria outlined in these Guidelines.

### 5.3.4 Retraining frequency and requirements

All personnel in Trusted roles SHALL maintain skill levels consistent with the CA's training and performance programs.

### 5.3.4 Retraining frequency and requirements

### 5.3.5 Job rotation frequency and sequence

### 5.3.6 Sanctions for unauthorized actions

### 5.3.7 Independent Contractor Controls

The CA SHALL verify that the Delegated Third Party's personnel involved in the issuance of a Certificate meet the training and skills requirements of [Section 5.3.3](#533-training-requirements-and-procedures) and the document retention and event logging requirements of [Section 5.4.1](#541-types-of-events-recorded).

### 5.3.7 Independent contractor requirements

### 5.3.8 Documentation supplied to personnel

## 5.4 Audit logging procedures

## 5.4 Audit logging procedures
As specified in Section 5.4 of the Baseline Requirements.

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
### 5.4.2 Frequency of processing audit log

### 5.4.2 Frequency of processing log
### 5.4.3 Retention period for audit log

The CA and each Delegated Third Party SHALL retain, for at least two (2) years:

  1. CA certificate and key lifecycle management event records (as set forth in [Section 5.4.1](#541-types-of-events-recorded) (1)) after the later occurrence of:
     1. the destruction of the CA Private Key; or
     2. the revocation or expiration of the final CA Certificate in that set of Certificates that have an X.509v3 `basicConstraints` extension with the `cA` field set to true and which share a common Public Key corresponding to the CA Private Key;
  2. Subscriber Certificate lifecycle management event records (as set forth in [Section 5.4.1](#541-types-of-events-recorded) (2)) after the expiration of the Subscriber Certificate;
  3. Any security event records (as set forth in [Section 5.4.1](#541-types-of-events-recorded) (3)) after the event occurred.

Note: While these Requirements set the minimum retention period, the CA MAY choose a greater value as more appropriate in order to be able to investigate possible security or other types of incidents that will require retrospection and examination of past audit log events.

### 5.4.3 Retention period for audit log
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

## 5.5 Records archival

### 5.5.1 Types of records archived

The CA and each Delegated Third Party SHALL archive all audit logs (as set forth in [Section 5.4.1](#541-types-of-events-recorded)).

Additionally, the CA and each Delegated Third Party SHALL archive:
1. Documentation related to the security of their Certificate Systems, Certificate Management Systems, Root CA Systems, and Delegated Third Party Systems; and
2. Documentation related to their verification, issuance, and revocation of certificate requests and Certificates.

### 5.5.1 Types of records archived
### 5.5.2 Retention period for archive

Archived audit logs (as set forth in [Section 5.5.1](#551-types-of-records-archived) SHALL be retained for a period of at least two (2) years from their record creation timestamp, or as long as they are required to be retained per [Section 5.4.3](#543-retention-period-for-audit-log), whichever is longer.

Additionally, the CA and each Delegated Third Party SHALL retain, for at least two (2) years:
1. All archived documentation related to the security of Certificate Systems, Certificate Management Systems, Root CA Systems and Delegated Third Party Systems (as set forth in [Section 5.5.1](#551-types-of-records-archived)); and
2. All archived documentation relating to the verification, issuance, and revocation of certificate requests and Certificates (as set forth in [Section 5.5.1](#551-types-of-records-archived)) after the later occurrence of:
   1. such records and documentation were last relied upon in the verification, issuance, or revocation of certificate requests and Certificates; or
   2. the expiration of the Subscriber Certificates relying upon such records and documentation.

Note: While these Requirements set the minimum retention period, the CA MAY choose a greater value as more appropriate in order to be able to investigate possible security or other types of incidents that will require retrospection and examination of past records archived.

### 5.5.2 Retention period for archive
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
### 5.7.2 Recovery Procedures if Computing resources, software, and/or data are corrupted

### 5.7.2 Computing resources, software, and/or data are corrupted
### 5.7.3 Recovery Procedures after Key Compromise

### 5.7.3 Entity private key compromise procedures
### 5.7.4 Business continuity capabilities after a disaster

## 5.8 CA or RA termination

# 6. TECHNICAL SECURITY CONTROLS

## 6.1 Key pair generation and installation

### 6.1.1 Key pair generation

### 6.1.1 Key pair generation
All requirements in Section 6.1.1.1 of the Baseline Requirements apply equally to EV Certificates. However, for Root CA Key Pairs generated after the release of these Guidelines, the Root CA Key Pair generation ceremony MUST be witnessed by the CA's Qualified Auditor in order to observe the process and the controls over the integrity and confidentiality of the Root CA Key Pairs produced.  The Qualified Auditor MUST then issue a report opining that the CA, during its Root CA Key Pair and Certificate generation process:

  1. Documented its Root CA key generation and protection procedures in its Certificate Policy, and its Certification Practices Statement;
  2. Included appropriate detail in its Root Key Generation Script;
  3. Maintained effective controls to provide reasonable assurance that the Root CA key pair was generated and protected in conformity with the procedures described in its CP/CPS and with its Root Key Generation Script;
  4. Performed, during the Root CA key generation process, all the procedures required by its Root Key Generation Script.

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

#### 6.1.1.2 RA Key Pair Generation

#### 6.1.1.3 Subscriber Key Pair Generation

The CA SHALL reject a certificate request if one or more of the following conditions are met:

1. The Key Pair does not meet the requirements set forth in [Section 6.1.5](#615-key-sizes) and/or [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
2. There is clear evidence that the specific method used to generate the Private Key was flawed;
3. The CA is aware of a demonstrated or proven method that exposes the Applicant's Private Key to compromise;
4. The CA has previously been made aware that the Applicant's Private Key has suffered a Key Compromise, such as through the provisions of [Section 4.9.1.1](#4911-reasons-for-revoking-a-subscriber-certificate);
5. The CA is aware of a demonstrated or proven method to easily compute the Applicant's Private Key based on the Public Key (such as a Debian weak key, see <https://wiki.debian.org/SSLkeys>).

If the Subscriber Certificate will contain an `extKeyUsage` extension containing either the values `id-kp-serverAuth` [RFC5280] or `anyExtendedKeyUsage` [RFC5280], the CA SHALL NOT generate a Key Pair on behalf of a Subscriber, and SHALL NOT accept a certificate request using a Key Pair previously generated by the CA.

### 6.1.2 Private key delivery to subscriber

Parties other than the Subscriber SHALL NOT archive the Subscriber Private Key without authorization by the Subscriber.

If the CA or any of its designated RAs become aware that a Subscriber's Private Key has been communicated to an unauthorized person or an organization not affiliated with the Subscriber, then the CA SHALL revoke all certificates that include the Public Key corresponding to the communicated Private Key.

### 6.1.2 Private key delivery to subscriber
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
### 6.1.6 Public key parameters generation and quality checking

RSA: The CA SHALL confirm that the value of the public exponent is an odd number equal to 3 or more. Additionally, the public exponent SHOULD be in the range between 2^16 + 1 and 2^256 - 1. The modulus SHOULD also have the following characteristics: an odd number, not the power of a prime, and have no factors smaller than 752. [Source: Section 5.3.3, NIST SP 800-89]

ECDSA: The CA SHOULD confirm the validity of all keys using either the ECC Full Public Key Validation Routine or the ECC Partial Public Key Validation Routine. [Source: Sections 5.6.2.3.2 and 5.6.2.3.3, respectively, of NIST SP 800-56A: Revision 2]

### 6.1.6 Public key parameters generation and quality checking
### 6.1.7 Key usage purposes (as per X.509 v3 key usage field)

Private Keys corresponding to Root Certificates MUST NOT be used to sign Certificates except in the following cases:

1. Self-signed Certificates to represent the Root CA itself;
2. Certificates for Subordinate CAs and Cross-Certified Subordinate CA Certificates;
3. Certificates for infrastructure purposes (administrative role certificates, internal CA operational device certificates); and
4. Certificates for OCSP Response verification.

### 6.1.7 Key usage purposes (as per X.509 v3 key usage field)

## 6.2 Private Key Protection and Cryptographic Module Engineering Controls

The CA SHALL implement physical and logical safeguards to prevent unauthorized certificate issuance. Protection of the CA Private Key outside the validated system or device specified above MUST consist of physical security, encryption, or a combination of both, implemented in a manner that prevents disclosure of the Private Key. The CA SHALL encrypt its Private Key with an algorithm and key-length that, according to the state of the art, are capable of withstanding cryptanalytic attacks for the residual life of the encrypted key or key part.

## 6.2 Private Key Protection and Cryptographic Module Engineering Controls
### 6.2.1 Cryptographic module standards and controls

### 6.2.2 Private key (n out of m) multi-person control

### 6.2.3 Private key escrow

### 6.2.4 Private key backup

See [Section 5.2.2](#522-number-of-individuals-required-per-task).

### 6.2.4 Private key backup
### 6.2.5 Private key archival

Parties other than the Subordinate CA SHALL NOT archive the Subordinate CA Private Keys without authorization by the Subordinate CA.

### 6.2.5 Private key archival
### 6.2.6 Private key transfer into or from a cryptographic module

If the Issuing CA generated the Private Key on behalf of the Subordinate CA, then the Issuing CA SHALL encrypt the Private Key for transport to the Subordinate CA. If the Issuing CA becomes aware that a Subordinate CA's Private Key has been communicated to an unauthorized person or an organization not affiliated with the Subordinate CA, then the Issuing CA SHALL revoke all certificates that include the Public Key corresponding to the communicated Private Key.

### 6.2.6 Private key transfer into or from a cryptographic module
### 6.2.7 Private key storage on cryptographic module

The CA SHALL protect its Private Key in a system or device that has been validated as meeting at least FIPS 140-2 level 3, FIPS 140-3 level 3, or an appropriate Common Criteria Protection Profile or Security Target, EAL 4 (or higher), which includes requirements to protect the Private Key and other assets against known threats.

### 6.2.7 Private key storage on cryptographic module
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
The Validity Period for an EV Certificate SHALL NOT exceed 398 days.

It is RECOMMENDED that EV Subscriber Certificates have a Maximum Validity Period of twelve months.

## 6.4 Activation data

### 6.4.1 Activation data generation and installation

### 6.4.2 Activation data protection

### 6.4.3 Other aspects of activation data

## 6.5 Computer security controls

### 6.5.1 Specific computer security technical requirements

The CA SHALL enforce multi-factor authentication for all accounts capable of directly causing certificate issuance.

### 6.5.1 Specific computer security technical requirements
### 6.5.2 Computer security rating

## 6.6 Life cycle technical controls

### 6.6.1 System development controls

### 6.6.2 Security management controls

### 6.6.3 Life cycle security controls

## 6.7 Network security controls

## 6.8 Time-stamping

# 7. CERTIFICATE, CRL, AND OCSP PROFILES

## 7.1 Certificate profile

The CA SHALL meet the technical requirements set forth in [Section 2.2 - Publication of Information](#22-publication-of-information), [Section 6.1.5 - Key Sizes](#615-key-sizes), and [Section 6.1.6 - Public Key Parameters Generation and Quality Checking](#616-public-key-parameters-generation-and-quality-checking).

Prior to 2023-09-15, the CA SHALL issue Certificates in accordance with the profile specified in these Requirements or the profile specified in version 1.8.6 of the Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates. Effective 2023-09-15, the CA SHALL issue Certificates in accordance with the profile specified in these Requirements.

## 7.1 Certificate profile
This section sets forth minimum requirements for the content of the EV Certificate as they relate to the identity of the CA and the Subject of the EV Certificate.

### 7.1.1 Version number(s)

Certificates MUST be of type X.509 v3.

### 7.1.1 Version number(s)

### 7.1.2 Certificate extensions
The extensions listed in [Section 7.1.2](#712-certificate-extensions) are recommended for maximum interoperability between certificates and browsers / applications, but are not mandatory on the CAs except where indicated as “Required”.  CAs may use other extensions that are not listed in [Section 7.1.2](#712-certificate-extensions), but are encouraged to add them to this section by ballot from time to time to help increase extension standardization across the industry.

If a CA includes an extension in a certificate that has a Certificate field which is named in [Section 7.1.2](#712-certificate-extensions), the CA must follow the format specified in that subsection.  However, no extension or extension format shall be mandatory on a CA unless specifically stated as “Required” in the subsection that describes the extension.

#### 7.1.2.1 Subject Alternative Name Extension

__Certificate Field__: `subjectAltName:dNSName`  
__Required/Optional__: __Required__  
__Contents__: This extension MUST contain one or more host Domain Name(s) owned or controlled by the Subject and to be associated with the Subject's server.  Such server MAY be owned and operated by the Subject or another entity (e.g., a hosting service). This extension MUST NOT contain a Wildcard Domain Name unless the FQDN portion of the Wildcard Domain Name is an Onion Domain Name verified in accordance with Appendix B of the Baseline Requirements.

#### 7.1.2.2 CA/Browser Forum Organization Identifier Extension

__Extension Name__: `cabfOrganizationIdentifier` (OID: 2.23.140.3.1)  
__Verbose OID__: `{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-extensions(3) cabf-organization-identifier(1) }`  
__Required/Optional__: __Optional (but see below)__  
__Contents__: If the subject:organizationIdentifier is present, this field MUST be present.

If present, this extension MUST contain a Registration Reference for a Legal Entity assigned in accordance to the identified Registration Scheme.

The Registration Scheme MUST be encoded as described by the following ASN.1 grammar:

```ASN.1
id-CABFOrganizationIdentifier OBJECT IDENTIFIER ::= {
    joint-iso-itu-t(2) international-organizations(23)
    ca-browser-forum(140) certificate-extensions(3)
    cabf-organizationIdentifier(1) 
}

ext-CABFOrganizationIdentifier EXTENSION ::= {
    SYNTAX CABFOrganizationIdentifier
    IDENTIFIED BY id-CABFOrganizationIdentifier
}

CABFOrganizationIdentifier ::= SEQUENCE {
    registrationSchemeIdentifier PrintableString (SIZE(3)),
    registrationCountry          PrintableString (SIZE(2)),
    registrationStateOrProvince  [0] IMPLICIT PrintableString
                                  (SIZE(0..128)) OPTIONAL,
    registrationReference        UTF8String
}
```

where the subfields have the same values, meanings, and restrictions described in [Section 7.1.4.2.1](#71428-subject-organization-identifier-field). The CA SHALL validate the contents using the requirements in [Section 7.1.4.2.1](#71428-subject-organization-identifier-field).

### 7.1.3 Algorithm object identifiers

#### 7.1.3.1 SubjectPublicKeyInfo

The following requirements apply to the `subjectPublicKeyInfo` field within a Certificate or Precertificate. No other encodings are permitted.

##### 7.1.3.1.1 RSA

The CA SHALL indicate an RSA key using the rsaEncryption (OID: 1.2.840.113549.1.1.1) algorithm identifier. The parameters MUST be present, and MUST be an explicit NULL.
The CA SHALL NOT use a different algorithm, such as the id-RSASSA-PSS (OID: 1.2.840.113549.1.1.10) algorithm identifier, to indicate an RSA key.

When encoded, the `AlgorithmIdentifier` for RSA keys MUST be byte-for-byte identical with the following hex-encoded bytes: `300d06092a864886f70d0101010500`

##### 7.1.3.1.2 ECDSA

The CA SHALL indicate an ECDSA key using the id-ecPublicKey (OID: 1.2.840.10045.2.1) algorithm identifier. The parameters MUST use the `namedCurve` encoding.

* For P-256 keys, the `namedCurve` MUST be secp256r1 (OID: 1.2.840.10045.3.1.7).
* For P-384 keys, the `namedCurve` MUST be secp384r1 (OID: 1.3.132.0.34).
* For P-521 keys, the `namedCurve` MUST be secp521r1 (OID: 1.3.132.0.35).

When encoded, the `AlgorithmIdentifier` for ECDSA keys MUST be byte-for-byte identical with the following hex-encoded bytes:

* For P-256 keys, `301306072a8648ce3d020106082a8648ce3d030107`.
* For P-384 keys, `301006072a8648ce3d020106052b81040022`.
* For P-521 keys, `301006072a8648ce3d020106052b81040023`.

#### 7.1.3.2 Signature AlgorithmIdentifier

All objects signed by a CA Private Key MUST conform to these requirements on the use of the `AlgorithmIdentifier` or `AlgorithmIdentifier`-derived type in the context of signatures.

In particular, it applies to all of the following objects and fields:

* The `signatureAlgorithm` field of a Certificate or Precertificate.
* The `signature` field of a TBSCertificate (for example, as used by either a Certificate or Precertificate).
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

##### 7.1.3.2.2 ECDSA

The CA SHALL use the appropriate signature algorithm and encoding based upon the signing key used.

If the signing key is P-256, the signature MUST use ECDSA with SHA-256. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040302`.

If the signing key is P-384, the signature MUST use ECDSA with SHA-384. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040303`.

If the signing key is P-521, the signature MUST use ECDSA with SHA-512. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040304`.

### 7.1.4 Name Forms

This section details encoding rules that apply to all Certificates issued by a CA. Further restrictions may be specified within [Section 7.1.2](#712-certificate-content-and-extensions), but these restrictions do not supersede these requirements.

### 7.1.4 Name forms
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

#### 7.1.4.1 Issuer Information

Issuer Information listed in an EV Certificate MUST comply with Section 7.1.4.1 of the Baseline Requirements.

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

#### 7.1.4.2 Subject Distinguished Name Fields

Subject to the requirements of these Guidelines, the EV Certificate and certificates issued to Subordinate CAs that are not controlled by the same entity as the CA MUST include the following information about the Subject organization in the fields listed:

##### 7.1.4.2.1 Subject Organization Name Field

__Certificate Field__: `subject:organizationName` (OID 2.5.4.10)  
__Required/Optional__: Required  
__Contents__: This field MUST contain the Subject's full legal organization name as listed in the official records of the Incorporating or Registration Agency in the Subject's Jurisdiction of Incorporation or Registration or as otherwise verified by the CA as provided herein. A CA MAY abbreviate the organization prefixes or suffixes in the organization name, e.g., if the official record shows "Company Name Incorporated" the CA MAY include "Company Name, Inc."

When abbreviating a Subject's full legal name as allowed by this subsection, the CA MUST use abbreviations that are not misleading in the Jurisdiction of Incorporation or Registration.

In addition, an assumed name or DBA name used by the Subject MAY be included at the beginning of this field, provided that it is followed by the full legal organization name in parenthesis.

If the combination of names or the organization name by itself exceeds 64 characters, the CA MAY abbreviate parts of the organization name, and/or omit non-material words in the organization name in such a way that the text in this field does not exceed the 64-character limit; provided that the CA checks this field in accordance with [Section 3.2.2.12.1](#322121-high-risk-status) and a Relying Party will not be misled into thinking that they are dealing with a different organization. In cases where this is not possible, the CA MUST NOT issue the EV Certificate.

##### 7.1.4.2.2 Subject Common Name Field

__Certificate Field__: `subject:commonName` (OID: 2.5.4.3)  
__Required/Optional__: Deprecated (Discouraged, but not prohibited)  
__Contents__: If present, this field MUST contain a single Domain Name(s) owned or controlled by the Subject and to be associated with the Subject's server.  Such server MAY be owned and operated by the Subject or another entity (e.g., a hosting service). This field MUST NOT contain a Wildcard Domain Name unless the FQDN portion of the Wildcard Domain Name is an Onion Domain Name verified in accordance with Appendix B of the Baseline Requirements.

##### 7.1.4.2.3 Subject Business Category Field

__Certificate Field__: `subject:businessCategory` (OID: 2.5.4.15)  
__Required/Optional__: Required  
__Contents__: This field MUST contain one of the following strings: "Private Organization", "Government Entity", "Business Entity", or "Non-Commercial Entity" depending upon whether the Subject qualifies under the terms of [Section 4.1.1.1](#4111-private-organization-subjects), [Section 4.1.1.2](#4112-government-entity-subjects), [Section 4.1.1.3](#4113-business-entity-subjects) or [Section 4.1.1.4](#4114-non-commercial-entity-subjects), respectively.

##### 7.1.4.2.4 Subject Jurisdiction of Incorporation or Registration Field

__Certificate Fields__:

Locality (if required):  
  `subject:jurisdictionLocalityName` (OID: 1.3.6.1.4.1.311.60.2.1.1)

State or province (if required):  
  `subject:jurisdictionStateOrProvinceName` (OID: 1.3.6.1.4.1.311.60.2.1.2)

Country:  
  `subject:jurisdictionCountryName` (OID: 1.3.6.1.4.1.311.60.2.1.3)

__Required/Optional__: Required  
__Contents__: These fields MUST NOT contain information that is not relevant to the level of the Incorporating Agency or Registration Agency.  For example, the Jurisdiction of Incorporation for an Incorporating Agency or Jurisdiction of Registration for a Registration Agency that operates at the country level MUST include the country information but MUST NOT include the state or province or locality information.  Similarly, the jurisdiction for the applicable Incorporating Agency or Registration Agency at the state or province level MUST include both country and state or province information, but MUST NOT include locality information.  And, the jurisdiction for the applicable Incorporating Agency or Registration Agency at the locality level MUST include the country and state or province information, where the state or province regulates the registration of the entities at the locality level, as well as the locality information.  Country information MUST be specified using the applicable ISO country code.  State or province or locality information (where applicable) for the Subject's Jurisdiction of Incorporation or Registration MUST be specified using the full name of the applicable jurisdiction.

Effective as of 1 October 2020, the CA SHALL ensure that, at time of issuance, the values within these fields have been disclosed within the latest publicly-available disclosure, as described in [Section 3.2.2.1.3](#32213-disclosure-of-verification-sources), as acceptable values for the applicable Incorporating Agency or Registration Agency.

##### 7.1.4.2.5 Subject Registration Number Field

__Certificate Field__: `subject:serialNumber` (OID: 2.5.4.5)  
__Required/Optional__: __Required__  
__Contents__: For Private Organizations, this field MUST contain the Registration (or similar) Number assigned to the Subject by the Incorporating or Registration Agency in its Jurisdiction of Incorporation or Registration, as appropriate.  If the Jurisdiction of Incorporation or Registration does not provide a Registration Number, then the date of Incorporation or Registration SHALL be entered into this field in any one of the common date formats.

For Government Entities that do not have a Registration Number or readily verifiable date of creation, the CA SHALL enter appropriate language to indicate that the Subject is a Government Entity.

For Business Entities, the Registration Number that was received by the Business Entity upon government registration SHALL be entered in this field.  For those Business Entities that register with an Incorporating Agency or Registration Agency in a jurisdiction that does not issue numbers pursuant to government registration, the date of the registration SHALL be entered into this field in any one of the common date formats.

Effective as of 1 October 2020, if the CA has disclosed a set of acceptable format or formats for Registration Numbers for the applicable Registration Agency or Incorporating Agency, as described in [Section 3.2.2.1.3](#32213-disclosure-of-verification-sources), the CA MUST ensure, prior to issuance, that the Registration Number is valid according to at least one currently disclosed format for that applicable Registration Agency or Incorporating agency.

##### 7.1.4.2.6 Subject Physical Address of Place of Business Field

__Certificate Fields__:  
    Number and street: `subject:streetAddress` (OID: 2.5.4.9)  
    City or town: `subject:localityName` (OID: 2.5.4.7)  
    State or province (where applicable): `subject:stateOrProvinceName` (OID: 2.5.4.8)  
    Country: `subject:countryName` (OID: 2.5.4.6)  
    Postal code: `subject:postalCode` (OID: 2.5.4.17)  
__Required/Optional__: As stated in Section 7.1.4.2.2 d, e, f, g and h of the Baseline Requirements.  
__Contents__: This field MUST contain the address of the physical location of the Subject's Place of Business.

##### 7.1.4.2.7 Subject Organizational Unit Name Field

__Certificate Field__: `subject:organizationalUnitName` (OID: 2.5.4.11)  
__Required/Optional/Prohibited:__ __Prohibited__. 

##### 7.1.4.2.8 Subject Organization Identifier Field

__Certificate Field__: `subject:organizationIdentifier` (OID: 2.5.4.97)  
__Required/Optional__: Optional  
__Contents__: If present, this field MUST contain a Registration Reference for a Legal Entity assigned in accordance to the identified Registration Scheme.

The organizationIdentifier MUST be encoded as a PrintableString or UTF8String.

The Registration Scheme MUST be identified using the using the following structure in the presented order:

* 3 character Registration Scheme identifier;
* 2 character ISO 3166 country code for the nation in which the Registration Scheme is operated, or if the scheme is operated globally ISO 3166 code "XG" shall be used;
* For the NTR Registration Scheme identifier, if required under [Section 7.1.4.2.4](#71424-subject-jurisdiction-of-incorporation-or-registration-field), a 2 character ISO 3166-2 identifier for the subdivision (state or province) of the nation in which the Registration Scheme is operated, preceded by plus "+" (0x2B (ASCII), U+002B (UTF-8));
* a hyphen-minus "-" (0x2D (ASCII), U+002D (UTF-8));
* Registration Reference allocated in accordance with the identified Registration Scheme

Note: Registration References MAY contain hyphens, but Registration Schemes, ISO 3166 country codes, and ISO 3166-2 identifiers do not.  Therefore if more than one hyphen appears in the structure, the leftmost hyphen is a separator, and the remaining hyphens are part of the Registration Reference.

As in [Section 7.1.4.2.4](#71424-subject-jurisdiction-of-incorporation-or-registration-field), the specified location information MUST match the scope of the registration being referenced.

Examples:

* `NTRGB-12345678` (NTR scheme, Great Britain, Unique Identifier at Country level is 12345678)
* `NTRUS+CA-12345678` (NTR Scheme, United States - California, Unique identifier at State level is 12345678)
* `VATDE-123456789` (VAT Scheme, Germany, Unique Identifier at Country Level is 12345678)
* `PSDBE-NBB-1234.567.890` (PSD Scheme, Belgium, NCA's identifier is NBB, Subject Unique Identifier assigned by the NCA is 1234.567.890)

Registration Schemes listed in [Appendix H](#appendix-h--registration-schemes) are currently recognized as valid under these guidelines.

The CA SHALL:

1. confirm that the organization represented by the Registration Reference is the same as the organization named in the `organizationName` field as specified in [Section 7.1.4.2.1](#71421-subject-organization-name-field) within the context of the subject’s jurisdiction as specified in [Section 7.1.4.2.4](#71424-subject-jurisdiction-of-incorporation-or-registration-field);
2. further verify the Registration Reference matches other information verified in accordance with [Section 3.2](#32-initial-identity-validation);
3. take appropriate measures to disambiguate between different organizations as described in [Appendix H](#appendix-h--registration-schemes) for each Registration Scheme;
4. Apply the validation rules relevant to the Registration Scheme as specified in [Appendix H](#appendix-h--registration-schemes).

##### 7.1.4.2.9 Other Subject Attributes

CAs SHALL NOT include any Subject Distinguished Name attributes except as specified in [Section 7.1.4.2](#7142-subject-distinguished-name-fields).

#### 7.1.4.3 Subscriber Certificate Common Name Attribute

If present, this attribute MUST contain exactly one entry that is one of the values contained in the Certificate's `subjectAltName` extension (see [Section 7.1.2.7.12](#712712-subscriber-certificate-subject-alternative-name)). The value of the field MUST be encoded as follows:

  * If the value is an IPv4 address, then the value MUST be encoded as an IPv4Address as specified in RFC 3986, Section 3.2.2.
  * If the value is an IPv6 address, then the value MUST be encoded in the text representation specified in RFC 5952, Section 4.
  * If the value is a Fully-Qualified Domain Name or Wildcard Domain Name, then the value MUST be encoded as a character-for-character copy of the `dNSName` entry value from the `subjectAltName` extension. Specifically, all Domain Labels of the Fully-Qualified Domain Name or FQDN portion of the Wildcard Domain Name must be encoded as LDH Labels, and P-Labels MUST NOT be converted to their Unicode representation.

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


#### 7.1.4.4 Other Subject Attributes

When explicitly stated as permitted by the relevant certificate profile specified within [Section 7.1.2](#712-certificate-content-and-extensions), CAs MAY include additional attributes within the `AttributeTypeAndValue` beyond those specified in [Section 7.1.4.2](#7142-subject-attribute-encoding).

Before including such an attribute, the CA SHALL:

  * Document the attributes within Section 7.1.4 of their CP or CPS, along with the applicable validation practices.
  * Ensure that the contents contain information that has been verified by the CA, independent of the Applicant.

### 7.1.5 Name constraints

### 7.1.6 Certificate policy object identifier

### 7.1.6 Certificate policy object identifier
This section sets forth minimum requirements for the contents of EV Certificates as they relate to the identification of EV Certificate Policy.

#### 7.1.6.1 Reserved Certificate Policy Identifiers

The following Certificate Policy identifiers are reserved for use by CAs as an optional means of asserting that a Certificate complies with these Requirements.

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) domain-validated(1)} (2.23.140.1.2.1)`

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) organization-validated(2)} (2.23.140.1.2.2)`

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) individual-validated(3)} (2.23.140.1.2.3)`

`{joint‐iso‐itu‐t(2) international‐organizations(23) ca‐browser‐forum(140) certificate‐policies(1) ev-guidelines(1)} (2.23.140.1.1)`

#### 7.1.6.1 EV Subscriber Certificates

Each EV Certificate issued by the CA to a Subscriber MUST contain a policy identifier that is either defined by these Guidelines or the CA in the certificate's `certificatePolicies` extension that:

1. indicates which CA policy statement relates to that Certificate,
2. asserts the CA's adherence to and compliance with these Guidelines, and
3. is either the CA/Browser Forum’s EV policy identifier or a policy identifier that, by pre-agreement with the Application Software Supplier, marks the Certificate as being an EV Certificate.

The following Certificate Policy identifier is the CA/Browser Forum’s EV policy identifier:
`{joint‐iso‐itu‐t(2) international‐organizations(23) ca‐browser‐forum(140) certificate‐policies(1) ev-guidelines (1) } (2.23.140.1.1)`, if the Certificate complies with these Guidelines.

#### 7.1.6.2 Root CA Certificates

The Application Software Supplier identifies Root CAs that are approved to issue EV Certificates by storing EV policy identifiers in metadata associated with Root CA Certificates.

#### 7.1.6.3 EV Subordinate CA Certificates

1. Certificates issued to Subordinate CAs that are not controlled by the issuing CA MUST contain one or more policy identifiers defined by the issuing CA that explicitly identify the EV Policies that are implemented by the Subordinate CA.
2. Certificates issued to Subordinate CAs that are controlled by the Root CA MAY contain the special `anyPolicy` identifier (OID: 2.5.29.32.0).

#### 7.1.6.4 Subscriber Certificates

A Certificate issued to a Subscriber MUST contain one or more policy identifier(s), defined by the Issuing CA, in the Certificate's `certificatePolicies` extension that indicates adherence to and compliance with these Guidelines.  Each CA SHALL document in its Certificate Policy or Certification Practice Statement that the Certificates it issues containing the specified policy identifier(s) are managed in accordance with these Guidelines.

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
### 7.3.1 Version number(s)

### 7.3.2 OCSP extensions

The `singleExtensions` of an OCSP response MUST NOT contain the `reasonCode` (OID 2.5.29.21) CRL entry extension.

### 7.3.2 OCSP extensions

# 8. COMPLIANCE AUDIT AND OTHER ASSESSMENTS

The CA SHALL at all times:

1. Comply with these Requirements;
2. Comply with the audit requirements set forth in this section; and
3. Be licensed as a CA in each jurisdiction where it operates, if licensing is required by the law of such jurisdiction for the issuance of Certificates.

**Implementers' Note**: Version 1.1.6 of the SSL Baseline Requirements was published on July 29, 2013. Version 2.0 of WebTrust's Principles and Criteria for Certification Authorities - SSL Baseline with Network Security and ETSI's Electronic Signatures and Infrastructures (ESI) 102 042 incorporate version 1.1.6 of these Baseline Requirements and version 1.0 of the Network and Certificate System Security Requirements. The CA/Browser Forum continues to improve the Baseline Requirements while WebTrust and ETSI also continue to update their audit criteria. We encourage all CAs to conform to each revision herein on the date specified without awaiting a corresponding update to an applicable audit criterion. In the event of a conflict between an existing audit criterion and a guideline revision, we will communicate with the audit community and attempt to resolve any uncertainty, and we will respond to implementation questions directed to <questions@cabforum.org>. Our coordination with compliance auditors will continue as we develop guideline revision cycles that harmonize with the revision cycles for audit criteria, the compliance auditing periods and cycles of CAs, and the CA/Browser Forum's guideline implementation dates.

# 8. COMPLIANCE AUDIT AND OTHER ASSESSMENTS

A CA issuing EV Certificates SHALL undergo an audit in accordance with one of the following schemes:

i. WebTrust Program for CAs audit and WebTrust EV Program audit,
ii. ETSI TS 102 042 audit for EVCP, or
iii. ETSI EN 319 411-1 audit for EVCP policy.

If the CA is a Government Entity, an audit of the CA by the appropriate internal government auditing agency is acceptable in lieu of the audits specified above, provided that such internal government auditing agency publicly certifies in writing that its audit addresses the criteria specified in one of the above audit schemes and certifies that the government CA has successfully passed the audit.

## 8.1 Frequency or circumstances of assessment

Certificates that are capable of being used to issue new certificates MUST either be Technically Constrained in line with [Section 7.1.2.3](#7123-technically-constrained-non-tls-subordinate-ca-certificate-profile), [Section 7.1.2.4](#7124-technically-constrained-precertificate-signing-ca-certificate-profile), or [Section 7.1.2.5](#7125-technically-constrained-tls-subordinate-ca-certificate-profile), as well as audited in line with [Section 8.7](#87-self-audits) only, or Unconstrained and fully audited in line with all remaining requirements from this section. A Certificate is deemed as capable of being used to issue new certificates if it contains an X.509v3 `basicConstraints` extension, with the `cA` boolean set to true and is therefore by definition a Root CA Certificate or a Subordinate CA Certificate.

The period during which the CA issues Certificates SHALL be divided into an unbroken sequence of audit periods. An audit period MUST NOT exceed one year in duration.

If the CA has a currently valid Audit Report indicating compliance with an audit scheme listed in [Section 8.4](#84-topics-covered-by-assessment), then no pre-issuance readiness assessment is necessary.

If the CA does not have a currently valid Audit Report indicating compliance with one of the audit schemes listed in [Section 8.4](#84-topics-covered-by-assessment), then, before issuing Publicly-Trusted Certificates, the CA SHALL successfully complete a point-in-time readiness assessment performed in accordance with applicable standards under one of the audit schemes listed in [Section 8.4](#84-topics-covered-by-assessment). The point-in-time readiness assessment SHALL be completed no earlier than twelve (12) months prior to issuing Publicly-Trusted Certificates and SHALL be followed by a complete audit under such scheme within ninety (90) days of issuing the first Publicly-Trusted Certificate.

## 8.1 Frequency or circumstances of assessment
CAs issuing EV Certificates MUST undergo an annual audit that meets the criteria of [Section 8](#8-compliance-audit-and-other-assessments).

### 8.1.1 Self audits
During the period in which it issues EV Certificates, the CA MUST strictly control its service quality by performing ongoing self audits against a randomly selected sample of at least three percent of the EV Certificates it has issued in the period beginning immediately after the last sample was taken.  For all EV Certificates where the Final Cross-Correlation and Due Diligence requirements of [Section 3.2.2.13](#32213-final-cross-correlation-and-due-diligence) is performed by an RA, the CA MUST strictly control its service quality by performing ongoing self audits against a randomly selected sample of at least six percent of the EV Certificates it has issued in the period beginning immediately after the last sample was taken.

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
A Qualified Auditor (as defined in Section 8.2 of the Baseline Requirements) MUST perform the CA's audit.

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
CAs SHOULD make its audit report publicly available no later than three months after the end of the audit period.  If there is a delay greater than three months and if so requested by an Application Software Supplier, the CA MUST provide an explanatory letter signed by its auditor.

## 8.7 Self-Audits

During the period in which the CA issues Certificates, the CA SHALL monitor adherence to its Certificate Policy, Certification Practice Statement and these Requirements and strictly control its service quality by performing self audits on at least a quarterly basis against a randomly selected sample of the greater of one certificate or at least three percent of the Certificates issued by it during the period commencing immediately after the previous self-audit sample was taken. Except for Delegated Third Parties that undergo an annual audit that meets the criteria specified in [Section 8.4](#84-topics-covered-by-assessment), the CA SHALL strictly control the service quality of Certificates issued or containing information verified by a Delegated Third Party by having a Validation Specialist employed by the CA perform ongoing quarterly audits against a randomly selected sample of at least the greater of one certificate or three percent of the Certificates verified by the Delegated Third Party in the period beginning immediately after the last sample was taken. The CA SHALL review each Delegated Third Party's practices and procedures to ensure that the Delegated Third Party is in compliance with these Requirements and the relevant Certificate Policy and/or Certification Practice Statement.

The CA SHALL internally audit each Delegated Third Party's compliance with these Requirements on an annual basis.

During the period in which a Technically Constrained Subordinate CA issues Certificates, the CA which signed the Subordinate CA SHALL monitor adherence to the CA's Certificate Policy and the Subordinate CA's Certification Practice Statement. On at least a quarterly basis, against a randomly selected sample of the greater of one certificate or at least three percent of the Certificates issued by the Subordinate CA, during the period commencing immediately after the previous audit sample was taken, the CA shall ensure all applicable CP are met.

## 8.7 Pre-issuance Readiness Audit

1. If the CA has a currently valid WebTrust Seal of Assurance for CAs, then, before issuing EV Certificates, the CA and its Root CA MUST successfully complete a point-in-time readiness assessment audit against the WebTrust EV Program.
2. If the CA has a currently valid ETSI 102 042 audit, then, before issuing EV Certificates, the CA and its Root CA MUST successfully complete a point-in-time readiness assessment audit against ETSI TS 102 042.
3. If the CA has a currently valid ETSI EN 319 411-1 audit for EVCP policy, then, before issuing EV Certificates, the CA and its Root CA MUST successfully complete a point-in-time readiness assessment audit against ETSI EN 319 411-1 for EVCP.
4. If the CA does not have a currently valid WebTrust Seal of Assurance for CAs or an ETSI TS 102 042 EVCP audit or an ETSI EN 319 411-1 audit for EVCP policy, then, before issuing EV Certificates, the CA and its Root CA MUST successfully complete either:
   i. a point-in-time readiness assessment audit against the WebTrust for CA Program, or
   ii. a point-in-time readiness assessment audit against the WebTrust EV Program, the ETSI TS 102 042 EVCP, or the ETSI EN 319 411-1 for EVCP policy.

The CA MUST complete any required point-in-time readiness assessment no earlier than twelve (12) months prior to issuing an EV Certificate.  The CA MUST undergo a complete audit under such scheme within ninety (90) days of issuing the first EV Certificate.

# 9. OTHER BUSINESS AND LEGAL MATTERS

## 9.1 Fees

### 9.1.1 Certificate issuance or renewal fees

### 9.1.2 Certificate access fees

### 9.1.3 Revocation or status information access fees

### 9.1.4 Fees for other services

### 9.1.5 Refund policy

## 9.2 Financial responsibility

### 9.2.1 Insurance coverage

### 9.2.1 Insurance coverage
Each CA SHALL maintain the following insurance related to their respective performance and obligations under these Guidelines:

A.  Commercial General Liability insurance (occurrence form) with policy limits of at least two million US dollars in coverage; and

B.  Professional Liability/Errors and Omissions insurance, with policy limits of at least five million US dollars in coverage, and including coverage for:
    i. claims for damages arising out of an act, error, or omission, unintentional breach of contract, or neglect in issuing or maintaining EV Certificates, and;
    ii. claims for damages arising out of infringement of the proprietary rights of any third party (excluding copyright, and trademark infringement), and invasion of privacy and advertising injury.

Such insurance must be with a company rated no less than A- as to Policy Holder's Rating in the current edition of Best's Insurance Guide (or with an association of companies each of the members of which are so rated).

A CA MAY self-insure for liabilities that arise from such party's performance and obligations under these Guidelines provided that it has at least five hundred million US dollars in liquid assets based on audited financial statements in the past twelve months, and a quick ratio (ratio of liquid assets to current liabilities) of not less than 1.0.

### 9.2.2 Other assets

### 9.2.3 Insurance or warranty coverage for end-entities

## 9.3 Confidentiality of business information

### 9.3.1 Scope of confidential information

### 9.3.2 Information not within the scope of confidential information

### 9.3.3 Responsibility to protect confidential information

## 9.4 Privacy of personal information

### 9.4.1 Privacy plan

### 9.4.2 Information treated as private

### 9.4.3 Information not deemed private

### 9.4.4 Responsibility to protect private information

### 9.4.5 Notice and consent to use private information

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
When the CA issues an EV Certificate, the CA and its Root CA represent and warrant to the Certificate Beneficiaries listed in Section 9.6.1 of the Baseline Requirements, during the period when the EV Certificate is Valid, that the CA has followed the requirements of these Guidelines and its EV Policies in issuing and managing the EV Certificate and in verifying the accuracy of the information contained in the EV Certificate.  The EV Certificate Warranties specifically include, but are not limited to, the following:

A.  **Legal Existence**: The CA has confirmed with the Incorporating or Registration Agency in the Subject's Jurisdiction of Incorporation or Registration that, as of the date the EV Certificate was issued, the Subject named in the EV Certificate legally exists as a valid organization or entity in the Jurisdiction of Incorporation or Registration;

B.  **Identity**: The CA has confirmed that, as of the date the EV Certificate was issued, the legal name of the Subject named in the EV Certificate matches the name on the official government records of the Incorporating or Registration Agency in the Subject's Jurisdiction of Incorporation or Registration, and if an assumed name is also included, that the assumed name is properly registered by the Subject in the jurisdiction of its Place of Business;

C.  **Right to Use Domain Name**: The CA has taken all steps reasonably necessary to verify that, as of the date the EV Certificate was issued, the Subject named in the EV Certificate has the right to use all the Domain Name(s) listed in the EV Certificate;

D.  **Authorization for EV Certificate**: The CA has taken all steps reasonably necessary to verify that the Subject named in the EV Certificate has authorized the issuance of the EV Certificate;

E.  **Accuracy of Information**: The CA has taken all steps reasonably necessary to verify that all of the other information in the EV Certificate is accurate, as of the date the EV Certificate was issued;

F.  **Subscriber Agreement**: The Subject named in the EV Certificate has entered into a legally valid and enforceable Subscriber Agreement with the CA that satisfies the requirements of these Guidelines or, if they are affiliated, the Applicant Representative has acknowledged and accepted the Terms of Use;

G.  **Status**: The CA will follow the requirements of these Guidelines and maintain a 24 x 7 online-accessible Repository with current information regarding the status of the EV Certificate as Valid or revoked; and

H.  **Revocation**: The CA will follow the requirements of these Guidelines and revoke the EV Certificate for any of the revocation reasons specified in these Guidelines.

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
Section 9.6.3 of the Baseline Requirements applies equally to EV Certificates.  In cases where the Certificate Request does not contain all necessary information about the Applicant, the CA MUST additionally confirm the data with the Certificate Approver or Contract Signer rather than the Certificate Requester.

EV Certificate Applicants make the commitments and warranties set forth in Section 9.6.3 of the Baseline Requirements for the benefit of the CA and Certificate Beneficiaries.
### 9.6.4 Relying party representations and warranties

### 9.6.5 Representations and warranties of other participants

## 9.7 Disclaimers of warranties

## 9.8 Limitations of liability

For delegated tasks, the CA and any Delegated Third Party MAY allocate liability between themselves contractually as they determine, but the CA SHALL remain fully responsible for the performance of all parties in accordance with these Requirements, as if the tasks had not been delegated.

If the CA has issued and managed the Certificate in compliance with these Requirements and its Certificate Policy and/or Certification Practice Statement, the CA MAY disclaim liability to the Certificate Beneficiaries or any other third parties for any losses suffered as a result of use or reliance on such Certificate beyond those specified in the CA's Certificate Policy and/or Certification Practice Statement. If the CA has not issued or managed the Certificate in compliance with these Requirements and its Certificate Policy and/or Certification Practice Statement, the CA MAY seek to limit its liability to the Subscriber and to Relying Parties, regardless of the cause of action or legal theory involved, for any and all claims, losses or damages suffered as a result of the use or reliance on such Certificate by any appropriate means that the CA desires. If the CA chooses to limit its liability for Certificates that are not issued or managed in compliance with these Requirements or its Certificate Policy and/or Certification Practice Statement, then the CA SHALL include the limitations on liability in the CA's Certificate Policy and/or Certification Practice Statement.

## 9.8 Limitations of liability
CAs MAY limit their liability as described in Section 9.8 of the Baseline Requirements except that a CA MUST NOT limit its liability to Subscribers or Relying Parties for legally recognized and provable claims to a monetary amount less than two thousand US dollars per Subscriber or Relying Party per EV Certificate.

## 9.9 Indemnities

Notwithstanding any limitations on its liability to Subscribers and Relying Parties, the CA understands and acknowledges that the Application Software Suppliers who have a Root Certificate distribution agreement in place with the Root CA do not assume any obligation or potential liability of the CA under these Requirements or that otherwise might exist because of the issuance or maintenance of Certificates or reliance thereon by Relying Parties or others. Thus, except in the case where the CA is a government entity, the CA SHALL defend, indemnify, and hold harmless each Application Software Supplier for any and all claims, damages, and losses suffered by such Application Software Supplier related to a Certificate issued by the CA, regardless of the cause of action or legal theory involved. This does not apply, however, to any claim, damages, or loss suffered by such Application Software Supplier related to a Certificate issued by the CA where such claim, damage, or loss was directly caused by such Application Software Supplier's software displaying as not trustworthy a Certificate that is still valid, or displaying as trustworthy: (1) a Certificate that has expired, or (2) a Certificate that has been revoked (but only in cases where the revocation status is currently available from the CA online, and the application software either failed to check such status or ignored an indication of revoked status).

## 9.9 Indemnities
A CA's indemnification obligations and a Root CA's obligations with respect to subordinate CAs are set forth in Section 9.9 of the Baseline Requirements.

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
The CA MAY issue EV Certificates, provided that the CA and its Root CA satisfy the requirements in these Guidelines and the Baseline Requirements.

If a court or government body with jurisdiction over the activities covered by these Guidelines determines that the performance of any mandatory requirement is illegal, then such requirement is considered reformed to the minimum extent necessary to make the requirement valid and legal.  This applies only to operations or certificate issuances that are subject to the laws of that jurisdiction.  The parties involved SHALL notify the CA/Browser Forum of the facts, circumstances, and law(s) involved, so that the CA/Browser Forum may revise these Guidelines accordingly.

### 9.16.4 Enforcement (attorneys' fees and waiver of rights)

### 9.16.5 Force Majeure

## 9.17 Other provisions

# Appendix A - User Agent Verification (Normative)
The CA MUST host test Web pages that allow Application Software Suppliers to test their software with EV Certificates that chain up to each EV Root Certificate.  At a minimum, the CA MUST host separate Web pages using certificates that are:

  i. valid;
  ii. revoked; and
  iii. expired.

# Appendix B - Sample Attorney Opinions Confirming Specified Information

**(Informative)**

[Law Firm Letterhead]

[Date]

| To: | **(Name of Issuing Certification Authority)(Address / fax number of Issuing CA – may be sent by fax or email attachment)** |
| --- | --- |
| Re: | **EV Certificate Request No. (CA Reference Number)** |
| Client: | **(Exact company name of Client – see footnote 1)** |
| Client Representative: | **(Exact name of Client Representative who signed the Application – see footnote 2)** |
| Application Date: | **(Insert date of Client's Application to the Issuing CA)** |

This firm represents _[__exact__ company name of Client]_ [^1] ("Client"), who has submitted the Application to you dated as of the Application Date shown above ("Application").  We have been asked by our Client to present you with our opinion as stated in this letter.

[Insert customary preliminary matters for opinion letters in your jurisdiction.]

On this basis, we hereby offer the following opinion:

1. That [exact company name of Client] ("Company") is a duly formed [corporation, LLC, etc.] that is "active," "valid," "current," or the equivalent under the laws of the state/province of [name of governing jurisdiction where Client is incorporated or registered] and is not under any legal disability known to the author of this letter.

2. That Company conducts business under the assumed name or "DBA"_[assumed name of the Applicant]_ and has registered such name with the appropriate government agency in the jurisdiction of its place of business below.

3. That _[name of Client's Representative]_[^2]  has authority to act on behalf of Company to: [_select as appropriate_] (a) provide the information about Company required for issuance of the EV Certificates as contained in the attached Application, (b) request one or more EV Certificates and to designate other persons to request EV Certificates, and (c) agree to the relevant contractual obligations contained in the Subscriber Agreement on behalf of Company.

4. That Company has a physical presence and its place of business is at the following location:

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5. That Company can be contacted at its stated place of business at the following telephone number:

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

6. That Company has an active current Demand Deposit Account with a regulated financial institution.

7. That Company has the right to use the following Domain Name in identifying itself on the Internet:

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Insert customary limitations and disclaimers for opinion letters in your jurisdiction.

(Name and signature)

_[Jurisdiction(s) in which attorney / Latin notary is admitted to practice]_[^3]

cc: [Send copy to Client_]_

[^1]: This must be the Client's exact corporate name, as registered with the relevant Incorporating Agency in the Client's Jurisdiction of Incorporation.  This is the name that will be included in the EV Certificate.

[^2]: If necessary to establish the Client Representative's actual authority, you may rely on a Power of Attorney from an officer of Client who has authority to delegate the authority to the Client Representative.

[^3]: This letter may be issued by in-house counsel for the Client so long as permitted by the rules of your jurisdiction.

# Appendix C - Sample Accountant Letters Confirming Specified Information

**(Informative)**

It is acceptable for professional accountants to provide letters that address specified matters.  The letters would be provided in accordance with the professional standards in the jurisdiction in which the accountant practices.

Two examples of the letter that might be prepared by an accountant in the United States and in Canada follow:

## CANADA

To: [Name of Certification Authority]

Re: Client Limited [Applicant]

As specifically agreed, I/we have performed the following procedures in connection with the above company's application for an Extended Validation (EV) Certificate, dated ......................., 20....  with respect to the following specified information contained in the application

| Specified Information: | Procedure:(Note 1: These are illustrative of the procedures that would be undertaken and are designed to meet the needs of the Certification Authorities issuing Extended Validation Certificates) | Results: (Note 2: If you are unavailable to perform any of the stated procedure, this should be noted in this column.  Any exceptions should be noted in a separate paragraph below) |
| --- | --- | --- |
|   |   |   |
| Legal Name - 123456 Ontario limited | Agree legal name to permanent audit file information (If audit has been completed) | Legal name on the application agrees with the information contained in our permanent file with respect to Client.(If there is no permanent file, state this fact) |
|   |   |   |
| Doing business as - "Name" | Agree name to government data base of business names | The name "Name" is registered with the (name of database to which the name was agreed) |
|   |   |   |
| Physical location - "Address Information" | Visit the location at the address | Site visit completed at Address |
|   |   |   |
| Business Phone Number - 555 999 9999 | Phone the number provided and confirm that it was answered by the named organization  | Phoned Business Number and noted that it was answered with the Doing Business As name.  This would provided by the receptionist |
|   |   |   |
| Bank Account – "Bank Name", "Account Number" | Request a letter directly from "the Bank" confirming the existence of the account for the benefit of "the Client" | Received letter directly from "the Bank" confirming the existence of the account for the benefit of "the Client" |
|   |   |   |
| The corporate officers are "NAMED" (verified officer) | Agree Names to annual shareholders meeting minutes (Note - not required to personally know the officers) | Agreed Names listed as corporate officers on the application to minute books maintained by the Client |
|   |   |   |
| Name of application signer and approver | Obtain letter from verified Officer confirming the names of the application signer and approver | Obtained letter from the President confirming the names of the duly authorized names of the application signer and approver as they appear in the application |

As a result of applying the above procedures, I/we found [no / the following] exceptions [list of exceptions].  However, these procedures do not constitute an audit of the company's application for an EV Certificate, and therefore I express no opinion on the application dated ......................., 20.....

This letter is for use solely in connection with the application for an Extended Validation Certificate by [Client] dated ......................., 20......

City

(signed) ......................................

## UNITED STATES

To the [Certification Authority] and Management of [Client]:

We have performed the procedures enumerated below, which were agreed to by the Managements of Client, solely to assist you in evaluating the company's application for an Extended Validation (EV) Certificate, dated......................., 20......  This agreed-upon procedures engagement was conducted in accordance with attestation standards established by the American Institute of Certified Public Accountants.  The sufficiency of these procedures is solely the responsibility of those parties specified in this report.  Consequently, we make no representation regarding the sufficiency of the procedures described below either for the purpose for which this report has been requested or for any other purpose.

| Specified Information: | Procedure:(Note 1: These are illustrative of the procedures that would be undertaken and are designed to meet the needs of the Certification Authorities issuing Extended Validation Certificates) | Results: (Note 2: If you are unavailable to perform any of the stated procedure, this should be noted in this column.  Any exceptions should be noted in a separate paragraph below) |
| --- | --- | --- |
|   |   |   |
| Legal Name - 123456 Delaware corporation | Agree legal name to permanent audit file information (If audit has been completed). | Legal name on the application agrees with the information contained in our permanent file with respect to Client.(If there is no permanent file, state this fact) |
|   |   |   |
| Doing business as - "Name" | Agree name to government data base of business names | The name "Name" is registered with the (name of database to which the name was agreed) |
|   |   |   |
| Physical location - "Address Information" | Visit the location at the address | Site visit completed at Address |
|   |   |   |
| Business Phone Number - 555 999 9999 | Phone the number provided and confirm that it was answered by the named organization  | Phoned Business Number and noted that it was answered with the Doing Business As name.  This would provided by the receptionist |
|   |   |   |
| Bank Account – "Bank Name", "Account Number" | Request a letter directly from "the Bank" confirming the existence of the account for the benefit of "the Client" | Received letter directly from "the Bank" confirming the existence of the account for the benefit of "the Client" |
|   |   |   |
| The corporate officers are "NAMED" (verified officer) | Agree Names to annual shareholders meeting minutes (Note - not required to personally know the officers) | Agreed Names listed as corporate officers on the application to minute books maintained by the Client |
|   |   |   |
| Name of application signer and approver | Obtain letter from verified Officer confirming the names of the application signer and approver | Obtained letter from the President confirming the names of the duly authorized names of the application signer and approver as they appear in the application |

We were not engaged to and did not conduct an examination, the objective of which would be the expression of an opinion on the Application for Extended Validation Certificate.  Accordingly, we do not express such an opinion.  Had we performed additional procedures, other matters might have come to our attention that would have been reported to you.

This report is intended solely for the information and use of the Certification Authority and managements of Client, and is not intended to be and should not be used by anyone other than these specified parties.

[Signature]

[Date]

# Appendix D - Country-Specific Interpretative Guidelines (Normative)

NOTE: This appendix provides alternative interpretations of the EV Guidelines for countries that have a language, cultural, technical, or legal reason for deviating from a strict interpretation of the EV Guidelines.  More specific information for particular countries may be added to this appendix in the future.

## 1. Organization Names

1. Non-Latin Organization Name

   Where an EV Applicant's organization name is not registered with a QGIS in _Latin_ characters and the Applicant's foreign character organization name and registration have been verified with a QGIS in accordance with these Guidelines, a CA MAY include a Latin character organization name in the EV Certificate.  In such a case, the CA MUST follow the procedures laid down in this section.

2. Romanized Names

   In order to include a transliteration/Romanization of the registered name, the Romanization MUST be verified by the CA using a system officially recognized by the Government in the Applicant's Jurisdiction of Incorporation.

   If the CA can not rely on a transliteration/Romanization of the registered name using a system officially recognized by the Government in the Applicant's Jurisdiction of Incorporation, then it MUST rely on one of the options below, in order of preference:

   A.  A system recognized by the International Organization for Standardization (ISO);
   B.  A system recognized by the United Nations; or
   C.  A Lawyer's Opinion or Accountant's Letter confirming the proper Romanization of the registered name.

3. Translated Name

   In order to include a Latin character name in the EV certificate that is not a direct Romanization of the registered name (e.g. an English Name)  the CA MUST verify that the Latin character name is:

   A.  Included in the Articles of Incorporation (or equivalent document) filed as part of the organization registration; or
   B.  Recognized by a QTIS in the Applicant's Jurisdiction of Incorporation as the Applicant's recognized name for tax filings; or
   C.  Confirmed with a QIIS to be the name associated with the registered organization; or
   D.  Confirmed by a Verified Legal Opinion or Accountant's Letter to be a translated trading name associated with the registered organization.

### Country-Specific Procedures

#### D-1. Japan

As interpretation of the procedures set out above:

1. Organization Names

   A.  The Revised Hepburn method of Romanization, as well as Kunrei-shiki and Nihon-shiki methods described in ISO 3602, are acceptable for Japanese Romanizations.
   B.  The CA MAY verify the Romanized transliteration, language translation (e.g. English name), or other recognized Roman-letter substitute of the Applicant's formal legal name with either a QIIS, Verified Legal Opinion, or Verified Accountant Letter.
   C.  The CA MAY use the Financial Services Agency to verify a Romanized, translated, or other recognized Roman-letter substitute name.  When used, the CA MUST verify that the translated English is recorded in the audited Financial Statements.
   D.  When relying on Articles of Incorporation to verify a Romanized, translated, or other recognized Roman-letter substitute name, the Articles of Incorporation MUST be accompanied either: by a document, signed with the original Japanese Corporate Stamp, that proves that the Articles of Incorporation are authentic and current, or by a Verified Legal Opinion or a Verified Accountant Letter.  The CA MUST verify the authenticity of the Corporate Stamp.
   E.  A Romanized, translated, or other recognized Roman-lettered substitute name confirmed in accordance with this [Appendix D-1](#d-1-japan) stored in the ROBINS database operated by JIPDEC MAY be relied upon by a CA for determining the allowed organization name during any issuance or renewal process of an EV Certificate without the need to re-perform the above procedures.

2. Accounting Practitioner

   In Japan:

   A.  Accounting Practitioner includes either a certified public accountant (公認会計士 - Konin-kaikei-shi) or a licensed tax accountant (税理士 – Zei-ri-shi).
   B.  The CA MUST verify the professional status of the Accounting Practitioner through direct contact with the relevant local member association that is affiliated with either the Japanese Institute of Certified Public Accountants ([http://www.hp.jicpa.or.jp](http://www.hp.jicpa.or.jp/)), the Japan Federation of Certified Tax Accountant's Associations ([http://www.nichizeiren.or.jp](http://www.nichizeiren.or.jp/)), or any other authoritative source recognized by the Japanese Ministry of Finance ([http://www.mof.go.jp](http://www.mof.go.jp/)) as providing the current registration status of such professionals.

3. Legal Practitioner

   In Japan:

   A.  Legal Practitioner includes any of the following:

       - a licensed lawyer (弁護士 - Ben-go-shi),
       - a judicial scrivener (司法書士 - Shiho-sho-shi lawyer),
       - an administrative solicitor (行政書士 - Gyosei-sho-shi Lawyer),
       - or a notary public (公証人 - Ko-sho-nin).

       For purposes of the EV Guidelines, a Japanese Notary Public is considered equivalent to a Latin Notary.

   B.  The CA MUST verify the professional status of the Legal Practitioner by direct contact through the relevant local member association that is affiliated with one of the following national associations:

       - the Japan Federation of Bar Associations ([http://www.nichibenren.or.jp](http://www.nichibenren.or.jp/)),
       - the Japan Federation of Shiho-Shoshi Lawyer's Associations ([http://www.shiho-shoshi.or.jp](http://www.shiho-shoshi.or.jp/)),
       - the Japan Federation of Administrative Solicitors ([http://www.gyosei.or.jp](http://www.gyosei.or.jp/)),
       - the Japan National Notaries Association ([http://www.koshonin.gr.jp](http://www.koshonin.gr.jp/)), or
       - any other authoritative source recognized by the Japanese Ministry of Justice ([http://www.moj.go.jp](http://www.moj.go.jp/)) as providing the current registration status of such professionals.

# Appendix E - Sample Contract Signer's Representation/Warranty (Informative)

A CA may rely on the Contract Signer's authority to enter into the Subscriber Agreement using a representation/warranty executed by the Contract Signer.  An example of an acceptable warranty is as follows:

[CA] and Applicant are entering into a legally valid and enforceable Subscriber Agreement that creates extensive obligations on Applicant.  An EV Certificate serves as a form of digital identity for Applicant.  The loss or misuse of this identity can result in great harm to the Applicant.  By signing this Subscriber Agreement, the contract signer acknowledges that they have the authority to obtain the digital equivalent of a company stamp, seal, or (where applicable) officer's signature to establish the authenticity of the company's website, and that [Applicant name] is responsible for all uses of its EV Certificate.  By signing this Agreement on behalf of [Applicant name], the contract signer represents that the contract signer

   i. is acting as an authorized representative of [Applicant name],
   ii. is expressly authorized by [Applicant name] to sign Subscriber Agreements and approve EV Certificate requests on Applicant's behalf, and
   iii. has confirmed Applicant's right to use the domain(s) to be included in EV Certificates.

# Appendix F – Unused

This appendix is intentionally left blank.

# Appendix G – Abstract Syntax Notation One module for EV certificates

```ASN.1
CABFSelectedAttributeTypes {
    joint‐iso‐itu‐t(2) international‐organizations(23)
    ca‐browser‐forum(140) module(4)
    cabfSelectedAttributeTypes(1) 1 }
DEFINITIONS ::=
BEGIN
-- EXPORTS All
IMPORTS
  -- from Rec. ITU-T X.501 | ISO/IEC 9594-2
  selectedAttributeTypes, ID, ldap-enterprise
    FROM UsefulDefinitions {joint-iso-itu-t ds(5) module(1)
    usefulDefinitions(0) 7}

  -- from the X.500 series
  ub-locality-name, ub-state-name
    FROM UpperBounds {joint-iso-itu-t ds(5) module(1) upperBounds(10) 7}

  -- from Rec. ITU-T X.520 | ISO/IEC 9594-6
  DirectoryString{}, CountryName
    FROM SelectedAttributeTypes selectedAttributeTypes;

id-evat-jurisdiction ID ::= {ldap-enterprise 311 ev(60) 2 1}
id-evat-jurisdiction-localityName ID ::= {id-evat-jurisdiction 1}
id-evat-jurisdiction-stateOrProvinceName ID ::= {id-evat-jurisdiction 2}
id-evat-jurisdiction-countryName ID ::= {id-evat-jurisdiction 3}

jurisdictionLocalityName ATTRIBUTE ::= {
  SUBTYPE OF    name
  WITH SYNTAX   DirectoryString{ub-locality-name}
  LDAP-SYNTAX   directoryString.&id
  LDAP-NAME     {"jurisdictionL"}
  ID            id-evat-jurisdiction-localityName }

jurisdictionStateOrProvinceName ATTRIBUTE ::= {
  SUBTYPE OF    name
  WITH SYNTAX   DirectoryString{ub-state-name}
  LDAP-SYNTAX   directoryString.&id
  LDAP-NAME     {"jurisdictionST"}
  ID            id-evat-jurisdiction-stateOrProvinceName }

jurisdictionCountryName ATTRIBUTE ::= {
  SUBTYPE OF    name
  WITH SYNTAX   CountryName
  SINGLE VALUE  TRUE
  LDAP-SYNTAX   countryString.&id
  LDAP-NAME     {"jurisdictionC"}
  ID            id-evat-jurisdiction-countryName }

END
```

# Appendix H – Registration Schemes

The following Registration Schemes are currently recognized as valid under these
guidelines:

* **NTR**:

  The information carried in this field shall be the same as held in
  Subject Registration Number Field as specified in
  [Section 7.1.4.2.5](#71425-subject-registration-number-field) and the country code
  used in the Registration Scheme identifier shall match that of the
  subject’s jurisdiction as specified in
  [Section 7.1.4.2.4](#71424-subject-jurisdiction-of-incorporation-or-registration-field).

  Where the Subject Jurisdiction of Incorporation or Registration Field in 9.2.4
  includes more than the country code, the additional locality information shall
  be included as specified in [Section 7.1.4.2.8](#71428-subject-organization-identifier-field)
  and/or [Section 7.1.2.2](#7122-cabrowser-forum-organization-identifier-extension).

* **VAT**:

  Reference allocated by the national tax authorities to a Legal Entity. This
  information shall be validated using information provided by the national tax
  authority against the organization as identified by the Subject Organization
  Name Field (see [Section 7.1.4.2.1](#71421-subject-organization-name-field)) and
  Subject Registration Number Field (see
  Section 7.1.4.2.5](#71425-subject-registration-number-field)) within the context of
  the subject’s jurisdiction as specified in
  [Section 7.1.4.2.4](#71424-subject-jurisdiction-of-incorporation-or-registration-field).

* **PSD**:

  Authorization number as specified in ETSI TS 119 495 clause 4.4
  allocated to a payment service provider and containing the information as
  specified in ETSI TS 119 495 clause 5.2.1.  This information SHALL be
  obtained directly from the national competent authority register for
  payment services or from an information source approved by a government
  agency, regulatory body, or legislation for this purpose.  This information
  SHALL be validated by being matched directly or indirectly (for example, by
  matching a globally unique registration number) against the organization as
  identified by the Subject Organization Name Field (see
  [Section 7.1.4.2.1](#71421-subject-organization-name-field)) and
  Subject Registration Number Field (see
  [Section 7.1.4.2.5](#71425-subject-registration-number-field)) within the context of
  the subject’s jurisdiction as specified in
  [Section 7.1.4.2.4](#71424-subject-jurisdiction-of-incorporation-or-registration-field).
  The stated address of the organization combined with the organization name
  SHALL NOT be the only information used to disambiguate the organization.## Relevant Dates

| **Compliance** | **Section(s)** | **Summary Description (See Full Text for Details)** |
|--|--|----------|
| 2020-01-31 | [9.2.8] | If subject:organizationIdentifier is present, the CA/Browser Forum Organization Identifier Extension MUST be present |
| 2020-09-01 | [9.4] & Appendix F | Certificates issued MUST NOT have a Validity Period greater than 398 days. |
| 2020-10-01 | [11.1.3] | Prior to using an Incorporating Agency or Registration Agency, the CA MUST ensure the agency has been publicly disclosed |
| 2022-09-01 | [9.2.7] | CAs MUST NOT include the organizationalUnitName field in the Subject |

**Implementers' Note**: Version 1.3 of these EV Guidelines was published on 20 November 2010 and supplemented through May 2012 when version 1.4 was published.  ETSI TS 102 042 and ETSI TR 101 564 Technical Report: Guidance on ETSI TS 102 042 for Issuing Extended Validation Certificates for Auditors and CSPs reference version 1.3 of these EV Guidelines, and ETSI Draft EN 319 411-1 references version 1.4.  Version 1.4.5 of Webtrust(r) for Certification Authorities – Extended Validation Audit Criteria references version 1.4.5 of these EV Guidelines.  As illustrated in the Document History table above, the CA/Browser Forum continues to improve relevant industry guidelines, including this document, the Baseline Requirements, and the Network and Certificate System Security Requirements.  We encourage all CAs to conform to each revision on the date specified without awaiting a corresponding update to an applicable audit criterion.  In the event of a conflict between an existing audit criterion and a guideline revision, we will communicate with the audit community and attempt to resolve any uncertainty. We will respond to implementation questions directed to questions@cabforum.org.  Our coordination with compliance auditors will continue as we develop guideline revision cycles that harmonize with the revision cycles for audit criteria, the compliance auditing periods and cycles of CAs, and the CA/Browser Forum's guideline implementation dates.

