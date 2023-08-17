#### 7.1.6.3 Subordinate CA Certificates

A Certificate issued to a Subordinate CA that is not an Affiliate of the Issuing CA:

1. MUST include one or more explicit policy identifiers that indicate the Subordinate CA's adherence to and compliance with these Requirements (i.e. either the CA/Browser Forum Reserved Certificate Policy Identifiers or identifiers documented by the Subordinate CA in its Certificate Policy and/or Certification Practice Statement) and
2. MAY contain one or more identifiers documented by the Subordinate CA in its Certificate Policy and/or Certification Practice Statement and
3. MUST NOT contain the `anyPolicy` identifier (2.5.29.32.0).

A Certificate issued to a Subordinate CA that is an affiliate of the Issuing CA:

1. MAY include one or more explicit policy identifiers that indicate the Subordinate CA's adherence to and compliance with these Requirements (i.e. either the CA/Browser Forum Reserved Certificate Policy Identifiers or identifiers documented by the Subordinate CA in its Certificate Policy and/or Certification Practice Statement) and
2. MAY contain one or more identifiers documented by the Subordinate CA in its Certificate Policy and/or Certification Practice Statement and
3. MAY contain the `anyPolicy` identifier (2.5.29.32.0) in place of an explicit policy identifier.

The Subordinate CA and the Issuing CA SHALL represent, in their Certificate Policy and/or Certification Practice Statement, that all Certificates containing a policy identifier indicating compliance with these Requirements are issued and managed in accordance with these Requirements.

