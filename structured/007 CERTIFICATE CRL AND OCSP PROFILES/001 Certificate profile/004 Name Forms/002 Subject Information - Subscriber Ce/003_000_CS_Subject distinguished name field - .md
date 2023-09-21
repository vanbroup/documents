##### 7.1.4.2.3 Subject distinguished name field - Non-EV Code Signing Certificates

a. __Certificate Field:__ `subject:organizationName` (OID 2.5.4.10)  
   __Required/Optional:__ Required  
   __Contents:__ The `subject:organizationName` field MUST contain either the Subject's name or DBA as verified under BR Section 3.2. The CA MAY include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations; e.g., if the official record shows "Company Name Incorporated", the CA MAY use "Company Name Inc." or "Company Name". Because subject name attributes for individuals (e.g. `subject:givenName` (2.5.4.42) and `subject:surname` (2.5.4.4)) are not broadly supported by application software, the CA MAY use the `subject:organizationName` field to convey a natural person Subject's name or DBA. The CA MUST have a documented process for verifying that the information included in the `subject:organizationName` field is not misleading to a Relying Party.

b. __Certificate Field:__ `subject:streetAddress` (OID: 2.5.4.9)  
   __Required/Optional:__ Optional  
   __Contents:__ If present, the subject:streetAddress field MUST contain the Subject's street address information as verified under BR Section 3.2.2.1 or 3.2.3.

c. __Certificate Field:__ `subject:localityName` (OID: 2.5.4.7)  
   __Required/Optional:__ Required if the `subject:stateOrProvinceName` field is absent. Optional if the `subject:stateOrProvinceName` field is present.  
   __Contents:__ If present, the `subject:localityName` field MUST contain the Subject's locality information as verified under BR Section 3.2. If the `subject:countryName` field specifies the ISO 3166-1 user-assigned code of XX in accordance with BR Section 7.1.4.2.2.h., the `subject:localityName` field MAY contain the Subject's locality and/or state or province information as verified under BR Section 3.2.2.1 or 3.2.3.

d. __Certificate Field:__ `subject:stateOrProvinceName` (OID: 2.5.4.8)  
   __Required/Optional:__ Required if the `subject:localityName` field is absent. Optional if the `subject:localityName` field is present.  
   __Contents:__ If present, the `subject:stateOrProvinceName` field MUST contain the Subject's state or province information as verified under BR Section 3.2.2.1 or 3.2.3. If the `subject:countryName` field specifies the ISO 3166-1 user-assigned code of `XX` in accordance with BR Section 7.1.4.2.2.h., the `subject:stateOrProvinceName` field MAY contain the full name of the Subject's country information as verified under BR Section 3.2.2.1 or 3.2.3.

e. __Certificate Field:__ `subject:postalCode` (OID: 2.5.4.17)  
   __Required/Optional:__ Optional  
   __Contents:__ If present, the `subject:postalCode` field MUST contain the Subject's zip or postal information as verified under BR Section 3.2.2.1 or 3.2.3.

f. __Certificate Field:__ `subject:countryName` (OID: 2.5.4.6)  
   __Required/Optional:__ Required  
   __Contents:__ The `subject:countryName` MUST contain the two-letter ISO 3166-1 country code associated with the location of the Subject verified under BR Section 3.2.2.3. If a Country is not represented by an official ISO 3166-1 country code, the CA MAY specify the ISO 3166-1 user-assigned code of `XX` indicating that an official ISO 3166-1 alpha-2 code has not been assigned.

