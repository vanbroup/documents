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

