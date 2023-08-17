### 3.2.2 Validation of mailbox authorization or control

This section defines the permitted processes and procedures for confirming the Applicant's control of Mailbox Addresses to be included in issued Certificates. 

The CA SHALL verify that Applicant controls the email accounts associated with all Mailbox Fields referenced in the Certificate or has been authorized by the email account holder to act on the account holder’s behalf. 

The CA SHALL NOT delegate the verification of mailbox authorization or control.

The CA's CP and/or CPS SHALL specify the procedures that the CA employs to perform this verification. CAs SHALL maintain a record of which validation method, including the relevant version number from the TLS Baseline Requirements or S/MIME Baseline Requirements, was used to validate every domain or email address in issued Certificates.

Completed validations of Applicant authority MAY be valid for the issuance of multiple Certificates over time. In all cases, the validation SHALL have been initiated within the time period specified in the relevant requirement (such as [Section 4.2.1](#421-performing-identification-and-authentication-functions)) prior to Certificate issuance.

**Note:** Mailbox Fields MAY be listed in Subscriber Certificates using `rfc822Name` or `otherNames` of `type id-on-SmtpUTF8Mailbox` in the `subjectAltName` extension. Mailbox Fields MAY be listed in Subordinate CA Certificates via `rfc822Name` in permittedSubtrees within the `nameConstraints` extension.

