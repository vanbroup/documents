#### 3.2.2.5 Authentication for an IP Address

This section defines the permitted processes and procedures for validating the Applicant’s ownership or control of an IP Address listed in a Certificate.

The CA SHALL confirm that prior to issuance, the CA has validated each IP Address listed in the Certificate using at least one of the methods specified in this section.

Completed validations of Applicant authority may be valid for the issuance of multiple Certificates over time. In all cases, the validation must have been initiated within the time period specified in the relevant requirement (such as [Section 4.2.1](#421-performing-identification-and-authentication-functions) of this document) prior to Certificate issuance. For purposes of IP Address validation, the term Applicant includes the Applicant's Parent Company, Subsidiary Company, or Affiliate.

After July 31, 2019, CAs SHALL maintain a record of which IP validation method, including the relevant BR version number, was used to validate every IP Address.

**Note**: IP Addresses verified in accordance with this [Section 3.2.2.5](#3225-authentication-for-an-ip-address) may be listed in Subscriber Certificates as defined in [Section 7.1.4.2](#7142-subject-information---subscriber-certificates) or in Subordinate CA Certificates via iPAddress in permittedSubtrees within the Name Constraints extension. CAs are not required to verify IP Addresses listed in Subordinate CA Certificates via iPAddress in excludedSubtrees in the Name Constraints extension prior to inclusion in the Subordinate CA Certificate.

