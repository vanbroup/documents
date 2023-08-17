##### 7.1.4.3.1 Subject Distinguished Name Fields

a. __Certificate Field:__ `subject:commonName` (OID 2.5.4.3)  
   __Required/Optional:__ Required  
   __Contents:__ This field MUST be present and the contents SHOULD be an identifier for the certificate such that the certificate's Name is unique across all certificates issued by the issuing certificate.

b. __Certificate Field:__ `subject:organizationName` (OID 2.5.4.10)  
   __Required/Optional:__ Required  
   __Contents:__ This field MUST be present and the contents MUST contain either the Subject CA's name or DBA as verified under [Section 3.2.2.2](#3222-dbatradename). The CA may include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations; e.g., if the official record shows "Company Name Incorporated", the CA MAY use "Company Name Inc." or "Company Name".

c. __Certificate Field:__ `subject:countryName` (OID: 2.5.4.6)  
   __Required/Optional:__ Required  
   __Contents:__ This field MUST contain the two‐letter ISO 3166‐1 country code for the country in which the CA's place of business is located.

