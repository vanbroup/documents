##### 7.1.4.3.1 Subject distinguished name fields

a. __Certificate Field:__ `subject:commonName` (OID 2.5.4.3)  
   __Required/Optional:__ SHALL be present  
   __Contents:__ This field SHOULD contain an identifier for the Certificate such that the Certificate's Name is unique across all Certificates issued by the Issuing CA.

b. __Certificate Field:__ `subject:organizationName` (OID 2.5.4.10)  
   __Required/Optional:__ SHALL be present  
   __Contents:__ This field SHALL contain either the Subject CA's name or DBA as verified under [Section 3.2.3.2.2](#32322-verification-of-assumed-name) The CA MAY include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations; e.g., if the official record shows "Company Name Incorporated", the CA MAY use "Company Name Inc." or "Company Name".

c. __Certificate Field:__ `subject:countryName` (OID: 2.5.4.6)  
   __Required/Optional:__ SHALL be present  
   __Contents:__ This field SHALL contain the two‐letter ISO 3166‐1 country code for the country in which the CA's place of business is located.

d. Other Subject Attributes  
   Other attributes MAY be present within the subject field. If present, other attributes SHALL contain information that has been verified by the CA.

