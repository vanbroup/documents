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

