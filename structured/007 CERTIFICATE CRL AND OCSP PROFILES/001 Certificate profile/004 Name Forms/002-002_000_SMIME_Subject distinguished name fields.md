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

