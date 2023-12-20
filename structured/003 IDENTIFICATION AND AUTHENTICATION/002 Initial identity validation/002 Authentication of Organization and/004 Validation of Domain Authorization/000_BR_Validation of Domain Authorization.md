#### 3.2.2.4 Validation of Domain Authorization or Control

This section defines the permitted processes and procedures for validating the Applicant's ownership or control of the domain.

The CA SHALL confirm that prior to issuance, the CA has validated each Fully-Qualified Domain Name (FQDN) listed in the Certificate as follows:

1. When the FQDN is not an Onion Domain Name, the CA SHALL validate the FQDN using at least one of the methods listed below; and
2. When the FQDN is an Onion Domain Name, the CA SHALL validate the FQDN in accordance with Appendix B.

Completed validations of Applicant authority may be valid for the issuance of multiple Certificates over time. In all cases, the validation must have been initiated within the time period specified in the relevant requirement (such as [Section 4.2.1](#421-performing-identification-and-authentication-functions) of this document) prior to Certificate issuance. For purposes of domain validation, the term Applicant includes the Applicant's Parent Company, Subsidiary Company, or Affiliate.

CAs SHALL maintain a record of which domain validation method, including relevant BR version number, they used to validate every domain.

**Note**: FQDNs may be listed in Subscriber Certificates using `dNSName`s in the `subjectAltName` extension or in Subordinate CA Certificates via `dNSName`s in `permittedSubtrees` within the Name Constraints extension.

