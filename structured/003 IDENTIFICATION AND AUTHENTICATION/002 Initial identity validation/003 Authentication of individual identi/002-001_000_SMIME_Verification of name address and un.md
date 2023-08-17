##### 3.2.3.2.1 Verification of name, address, and unique identifier

The CA or RA SHALL verify the full legal name and an address (if included in the Certificate Subject) of the Legal Entity Applicant using documentation provided by, or through communication with, at least one of the following:

1.	A government agency in the jurisdiction of the Legal Entity’s creation, existence, or recognition; 
2.	A Legal Entity Identifier (LEI) data reference;
3.	A site visit by the CA or a third party who is acting as an agent for the CA; or
4.	An Attestation which includes a copy of supporting documentation used to establish the Applicant's legal existence, such as a certificate of registration, articles of incorporation, operating agreement, statute, or regulatory act.

The CA or RA MAY use the same documentation or communication described in 1 through 4 above to verify both the Applicant's identity and address.

If an LEI data reference is used, the CA or RA SHALL verify that the RegistrationStatus is ISSUED and the EntityStatus is ACTIVE. The CA SHALL only allow use of an LEI if the ValidationSources entry is FULLY_CORROBORATED. An LEI SHALL NOT be used if ValidationSources entry is PARTIALLY_CORROBORATED, PENDING, or ENTITY_SUPPLIED_ONLY.

