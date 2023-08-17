### 3.2.3.2 Authenticity of Certificate requests for Individual Applicants

The CA MUST verify the authenticity of the Certificate Request using one of the following:

1.  Having the Certificate Requester provide a photo of the Certificate Requester holding the submitted government-issued photo ID where the photo is of sufficient quality to read both the name listed on the photo ID and the issuing authority; OR
2.  Having the CA perform an in-person or web camera-based verification of the Certificate Requester where an employee or contractor of the CA can see the Certificate Requester, review the Certificate Requester's photo ID, and confirm that the Certificate Requester is the individual identified in the submitted photo ID; OR
3.  Having the CA obtain an executed Declaration of Identity of the Certificate Requester that includes at least one unique biometric identifier (such as a fingerprint or handwritten signature). The CA MUST confirm the document's authenticity directly with the Verifying Person using contact information confirmed with a QIIS or QGIS; OR
4.  Verifying that the digital signature used to sign the Request under item (2) of [Section 3.2.3.1](#3231-individual-identity-verification) is a valid signature and originated from a Certificate issued at the appropriate level of assurance as evidenced by the certificate chain. Acceptable verification under this section includes validation that the Certificate was issued by a CA qualified by the entity responsible for adopting, enforcing, or maintaining the adopted standard and chains to an intermediate certificate or root certificate designated as complying with such standard.

