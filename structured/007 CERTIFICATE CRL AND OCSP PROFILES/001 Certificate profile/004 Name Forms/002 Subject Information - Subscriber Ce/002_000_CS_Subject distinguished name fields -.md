##### 7.1.4.2.2 Subject distinguished name fields - EV and Non-EV Code Signing Certificates

a. __Certificate Field:__ `subject:commonName` (OID 2.5.4.3)  
   __Required/Optional:__ Required  
   __Contents:__ This field MUST contain the Subject's legal name as verified under [Section 3.2.2](#322-authentication-of-organization-identity) or [3.2.3](#323-authentication-of-individual-identity).

b. __Certificate Field:__ `subject:organizationalUnitName` (OID 2.5.4.11)  
   __Required/Optional:__ Optional  
   __Contents:__ The CA MUST implement a process that prevents an OU attribute from including a name, DBA, tradename, trademark, address, location, or other text that refers to a specific natural person or Legal Entity unless the CA has verified this information in accordance with [Section 3.2](#32-initial-identity-validation).

c. __Certificate Field:__ `subject:domainComponent` (OID 0.9.2342.19200300.100.1.25)  
   __Required/Optional:__ Prohibited  
   __Contents:__ This field MUST not be present in a Code Signing Certificate.

d. __Certificate Field:__ Other subject attributes  
   __Required/Optional:__ Optional
   __Contents:__ Other attributes MAY be present within the subject field. If present, other attributes MUST contain information that has been verified by the CA. Subject attributes MUST NOT contain only metadata such as '.', '-', and ' ' (i.e. space) characters, and/or any other indication that the value is absent, incomplete, or not applicable.

