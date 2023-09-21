## 3.2 Initial identity validation

The CA SHALL authenticate the identity attributes of the Subject and their control over the Mailbox Addresses to be included in the S/MIME Certificate according to the requirements of the following sections:

| Certificate Type    | Mailbox Control | Organization Identity | Individual Identity | 
|---------|----------|----------|----------|
| `Mailbox-validated` | [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control)  | NA | NA | 
| `Organization-validated` |  [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control)  | [Section 3.2.3](#323-authentication-of-organization-identity) | NA |
| `Sponsor-validated` | [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control) | [Section 3.2.3](#323-authentication-of-organization-identity) | [Section 3.2.4](#324-authentication-of-individual-identity) | 
| `Individual-validated` | [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control) | NA | [Section 3.2.4](#324-authentication-of-individual-identity) | 

