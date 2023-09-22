#### 3.2.2.1 Validating authority over mailbox via domain

The CA MAY confirm the Applicant, such as an Enterprise RA, has been authorized by the email account holder to act on the account holder’s behalf by verifying the entity's control over the domain portion of the Mailbox Address to be used in the Certificate.

The CA SHALL use only the approved methods in [Section 3.2.2.4 of the TLS Baseline Requirements](https://github.com/cabforum/servercert/blob/main/docs/BR.md#3224-validation-of-domain-authorization-or-control) to perform this verification.

For purposes of domain validation, the term Applicant includes the Applicant's Parent Company, Subsidiary Company, or Affiliate.

