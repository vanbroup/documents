#### 7.1.6.3 Subordinate CA certificates

A Certificate issued to a Subordinate CA that is not an Affiliate of the Issuing CA:

1. SHALL include one or more explicit policy identifiers defined in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers) that indicate the Subordinate CA's adherence to and compliance with these Requirements and MAY contain one or more identifiers documented by the Subordinate CA in its CP and/or CPS; and
2. SHALL NOT contain the `anyPolicy` identifier (2.5.29.32.0).

A Certificate issued to a Subordinate CA that is an Affiliate of the Issuing CA SHALL include a set of policy identifiers from one of the two options below:

1. One or more explicit policy identifiers defined in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers) that indicate the Subordinate CA's adherence to and compliance with these Requirements and MAY contain one or more identifiers documented by the Subordinate CA in its CP and/or CPS; or
2. The `anyPolicy` identifier (2.5.29.32.0).

The Subordinate CA and the Issuing CA SHALL represent, in their CP and/or CPS, that all Certificates containing a policy identifier indicating compliance with these Requirements are issued and managed in accordance with these Requirements.

