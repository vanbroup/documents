#### 7.1.6.3 Subordinate CA Certificates

A Certificate issued to a Subordinate CA that is not an Affiliate of the Issuing CA:

1. MUST include the policy identifier that indicates the Subordinate CA's adherence to and compliance with these Requirements (i.e. either the CA/Browser Forum reserved identifiers as specified in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers) or identifiers defined by the CA in its Certificate Policy and/or Certification Practice Statement), and
2. MUST NOT contain the "anyPolicy" identifier (`2.5.29.32.0`).

A Certificate issued to a Subordinate CA that issues Code Signing Certificates and is an Affiliate of the Issuing CA:

1. MUST include the CA/Browser Forum reserved identifier specified in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers) to indicate the Subordinate CA's compliance with these Requirements, and
2. MAY contain the "anyPolicy" identifier (`2.5.29.32.0`) in place of an explicit policy identifier.

A Certificate issued after 31 March 2022 to a Subordinate CA that issues Timestamp Certificates and is an Affiliate of the Issuing CA:

1. MUST include the CA/Browser Forum reserved identifier specified in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers) to 
indicate the Subordinate CA’s compliance with these Requirements, and  
2. MAY contain the “anyPolicy” identifier (`2.5.29.32.0`) in place of an explicit policy identifier. 

A Subordinate CA MUST represent, in its Certificate Policy and/or Certification Practice Statement, that all Certificates containing a policy identifier indicating compliance with these Requirements are issued and managed in accordance with these Requirements.

