#### 1.3.2.1 Enterprise registration authorities

The CA MAY delegate to an Enterprise Registration Authority (RA) to verify Certificate Requests for Subjects within the Enterprise RA's own organization. The CA SHALL NOT accept Certificate Requests authorized by an Enterprise RA unless the following requirements are satisfied:

1. If the Certificate Request is for a `Mailbox-validated`, `Organization-validated`, or `Sponsor-validated` profile, the CA SHALL confirm that the Enterprise RA has authorization or control of the requested email domain(s) in accordance with [Section 3.2.2.1](#3221-validating-authority-over-mailbox-via-domain) or [Section 3.2.2.3](#3223-validating-applicant-as-operator-of-associated-mail-servers). 
2. The CA SHALL confirm that the `subject:organizationName` name is either that of the delegated enterprise, or an Affiliate of the delegated enterprise, or that the delegated enterprise is an agent of the named Subject. For example, the CA SHALL NOT issue a Certificate containing the Subject name "XYZ Co." on the authority of Enterprise RA "ABC Co.", unless the two companies are Affiliated as defined in [Section 3.2](#32-initial-identity-validation) or "ABC Co." is the agent of "XYZ Co". This requirement applies regardless of whether the accompanying requested email domain falls within the subdomains of ABC Co.'s Registered Domain Name.

The CA SHALL impose these limitations as a contractual requirement on the Enterprise RA and monitor compliance by the Enterprise RA in accordance with [Section 8.8](#88-review-of-delegated-parties).

An Enterprise RA MAY also submit Certificate Requests using the `Mailbox-validated` profile for users whose email domain(s) are not under the delegated organization’s authorization or control.  In this case, the CA SHALL confirm that the mailbox holder has control of the requested Mailbox Address(es) in accordance with [Section 3.2.2.2](#3222-validating-control-over-mailbox-via-email).


