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

