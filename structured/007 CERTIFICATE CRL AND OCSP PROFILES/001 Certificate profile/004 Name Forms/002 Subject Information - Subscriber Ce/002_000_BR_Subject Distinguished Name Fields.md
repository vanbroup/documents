##### 7.1.4.2.2 Subject Distinguished Name Fields

a. __Certificate Field:__ `subject:commonName` (OID 2.5.4.3)  
   __Required/Optional:__ __Deprecated__ (Discouraged, but not prohibited)  
   __Contents:__ If present, this field MUST contain exactly one entry that is one of the values contained in the Certificate's `subjectAltName` extension (see [Section 7.1.4.2.1](#71421-subject-alternative-name-extension)). The value of the field MUST be encoded as follows:

   * If the value is an IPv4 address, then the value MUST be encoded as an IPv4Address as specified in RFC 3986, Section 3.2.2.
   * If the value is an IPv6 address, then the value MUST be encoded in the text representation specified in RFC 5952, Section 4.
   * If the value is a Fully-Qualified Domain Name or Wildcard Domain Name, then the value MUST be encoded as a character-for-character copy of the `dNSName` entry value from the `subjectAltName` extension. Specifically, all Domain Labels of the Fully-Qualified Domain Name or FQDN portion of the Wildcard Domain Name must be encoded as LDH Labels, and P-Labels MUST NOT be converted to their Unicode representation.

b. __Certificate Field:__ `subject:organizationName` (OID 2.5.4.10)  
   __Required/Optional:__ __Optional__.  
   __Contents:__ If present, the `subject:organizationName` field MUST contain either the Subject's name or DBA as verified under [Section 3.2.2.2](#3222-dbatradename). The CA may include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations; e.g., if the official record shows "Company Name Incorporated", the CA MAY use "Company Name Inc." or "Company Name". Because Subject name attributes for individuals (e.g. givenName (2.5.4.42) and surname (2.5.4.4)) are not broadly supported by application software, the CA MAY use the `subject:organizationName` field to convey a natural person Subject's name or DBA.

c. __Certificate Field:__ `subject:givenName` (2.5.4.42) and `subject:surname` (2.5.4.4)  
   __Required/Optional:__ __Optional__.  
   __Contents:__ If present, the `subject:givenName` field and `subject:surname` field MUST contain a natural person Subject’s name as verified under [Section 3.2.3](#323-authentication-of-individual-identity). A Certificate containing a `subject:givenName` field or `subject:surname` field MUST contain the (2.23.140.1.2.3) Certificate Policy OID.

d. __Certificate Field:__ Number and street: `subject:streetAddress` (OID: 2.5.4.9)  
   __Required/Optional:__  
   __Optional__ if the `subject:organizationName` field, `subject:givenName` field, or `subject:surname` field are present.  
   __Prohibited__ if the `subject:organizationName` field, `subject:givenName`, and `subject:surname` field are absent.  
   __Contents:__ If present, the `subject:streetAddress` field MUST contain the Subject's street address information as verified under [Section 3.2.2.1](#3221-identity).

e. __Certificate Field:__ `subject:localityName` (OID: 2.5.4.7)  
   __Required/Optional:__  
   __Required__ if the `subject:organizationName` field, `subject:givenName` field, or `subject:surname` field are present and the `subject:stateOrProvinceName` field is absent.  
   __Optional__ if the `subject:stateOrProvinceName` field and the `subject:organizationName` field, `subject:givenName` field, or `subject:surname` field are present.  
   __Prohibited__ if the `subject:organizationName` field, `subject:givenName`, and `subject:surname` field are absent.  
   __Contents:__ If present, the `subject:localityName` field MUST contain the Subject's locality information as verified under [Section 3.2.2.1](#3221-identity). If the `subject:countryName` field specifies the ISO 3166-1 user-assigned code of XX in accordance with [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields) (h), the `localityName` field MAY contain the Subject's locality and/or state or province information as verified under [Section 3.2.2.1](#3221-identity).

f. __Certificate Field:__ `subject:stateOrProvinceName` (OID: 2.5.4.8)  
   __Required/Optional:__  
   __Required__ if the `subject:organizationName` field, `subject:givenName` field, or `subject:surname` field are present and `subject:localityName` field is absent.  
   __Optional__ if the `subject:localityName` field and the `subject:organizationName` field, the `subject:givenName` field, or the `subject:surname` field are present.  
   __Prohibited__ if the `subject:organizationName` field, the `subject:givenName` field, or `subject:surname` field are absent.  
   __Contents:__ If present, the `subject:stateOrProvinceName` field MUST contain the Subject's state or province information as verified under [Section 3.2.2.1](#3221-identity). If the `subject:countryName` field specifies the ISO 3166-1 user-assigned code of XX in accordance with [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields) (h), the `subject:stateOrProvinceName` field MAY contain the full name of the Subject's country information as verified under [Section 3.2.2.1](#3221-identity).

g. __Certificate Field:__ `subject:postalCode` (OID: 2.5.4.17)  
   __Required/Optional:__  
   __Optional__ if the `subject:organizationName`, `subject:givenName` field, or `subject:surname` fields are present.  
   __Prohibited__ if the `subject:organizationName` field, `subject:givenName` field, or `subject:surname` field are absent.  
   __Contents:__ If present, the `subject:postalCode` field MUST contain the Subject's zip or postal information as verified under [Section 3.2.2.1](#3221-identity).

h. __Certificate Field:__ `subject:countryName` (OID: 2.5.4.6)  
   __Required/Optional:__  
   __Required__ if the `subject:organizationName` field, `subject:givenName`, or `subject:surname` field are present.  
   __Optional__ if the `subject:organizationName` field, `subject:givenName` field, and `subject:surname` field are absent.  
   __Contents:__ If the `subject:organizationName` field is present, the `subject:countryName` MUST contain the two-letter ISO 3166-1 country code associated with the location of the Subject verified under [Section 3.2.2.1](#3221-identity). If the `subject:organizationName` field is absent, the `subject:countryName` field MAY contain the two-letter ISO 3166-1 country code associated with the Subject as verified in accordance with [Section 3.2.2.3](#3223-verification-of-country). If a Country is not represented by an official ISO 3166-1 country code, the CA MAY specify the ISO 3166-1 user-assigned code of XX indicating that an official ISO 3166-1 alpha-2 code has not been assigned.

i. __Certificate Field:__ `subject:organizationalUnitName` (OID: 2.5.4.11)  
   __Required/Optional:__ __Prohibited__. 

j. Other Subject Attributes  
   Other attributes MAY be present within the subject field. If present, other attributes MUST contain information that has been verified by the CA.

