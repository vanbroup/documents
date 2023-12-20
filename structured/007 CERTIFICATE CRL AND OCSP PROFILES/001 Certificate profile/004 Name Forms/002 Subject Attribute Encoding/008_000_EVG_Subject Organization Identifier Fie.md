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

