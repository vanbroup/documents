### 3.1.3 Anonymity or pseudonymity of subscribers

The purpose of a Pseudonym is to provide a unique identifier linked to an Individual in a pseudonymized manner when certain privacy conditions are required. For example, a Pseudonym may be used if a government agency requires officials to sign certain decisions via S/MIME so those decisions trace back to individuals, but emphasize the importance of the role over Individual identity in the Certificate. The CA SHALL disclose in its CP and/or CPS if it allows the use of Pseudonyms.

For `Sponsor-validated` certificates, the CA MAY use a `subject:pseudonym` attribute in the Certificate if the associated Subject has been verified according to [Section 3.2.4](#324-authentication-of-individual-identity). If present, the `subject:pseudonym` attribute SHALL be:

  1. either a unique identifier selected by the CA for the Subject of the Certificate; or
  2. an identifier selected by the Enterprise RA which uniquely identifies the Subject of the Certificate within the Organization included in the `subject:organizationName` attribute.

For `Individual-validated` certificates, the CA MAY use the `subject:pseudonym` attribute if the associated Subject has been verified according to [Section 3.2.4](#324-authentication-of-individual-identity). If present, the `subject:pseudonym` attribute SHALL be:

  1. either a unique identifier selected by the CA for the Subject of the Certificate; or
  2. an identifier verified based on government-issued identity documents.

Pseudonym Certificates are not anonymous. CAs and Enterprise RAs SHALL treat Individual identity information relating to a Pseudonym as private in accordance with [Section 9.4.2](#942-information-treated-as-private).

