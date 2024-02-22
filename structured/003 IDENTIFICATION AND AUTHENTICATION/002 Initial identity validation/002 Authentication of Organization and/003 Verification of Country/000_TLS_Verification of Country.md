#### 3.2.2.3 Verification of Country

If the `subject:countryName` field is present, then the CA SHALL verify the country associated with the Subject using one of the following:

  a. the IP Address range assignment by country for either
     i. the web site's IP address, as indicated by the DNS record for the web site or
     ii. the Applicant's IP address;
  b. the ccTLD of the requested Domain Name;
  c. information provided by the Domain Name Registrar; or
  d. a method identified in [Section 3.2.2.1](#3221-identity).

The CA SHOULD implement a process to screen proxy servers in order to prevent reliance upon IP addresses assigned in countries other than where the Applicant is actually located.

