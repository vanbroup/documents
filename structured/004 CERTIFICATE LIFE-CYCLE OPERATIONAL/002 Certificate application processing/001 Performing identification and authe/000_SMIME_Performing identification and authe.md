### 4.2.1 Performing identification and authentication functions

Applicant information SHALL include, but not be limited to, at least one Mailbox Field to be included in the Certificate's `subjectAltName` extension.

[Section 6.3.2](#632-certificate-operational-periods-and-key-pair-usage-periods) limits the validity period of Subscriber Certificates. 

The CA MAY reuse completed validations and/or supporting evidence performed in accordance with [Section 3.2](#32-initial-identity-validation) within the following limits:

1. **Validation of mailbox authorization or control**: Completed validation of the control of a mail server in accordance with [Section 3.2.2.1](#3221-validating-authority-over-mailbox-via-domain) or [Section 3.2.2.3](#3223-validating-applicant-as-operator-of-associated-mail-servers) SHALL be obtained no more than 398 days prior to issuing the Certificate. 
   
      In the event of changes to the TLS Baseline Requirements methods specified in [Section 3.2.2.1](#3221-validating-authority-over-mailbox-via-domain), a CA MAY continue to reuse completed validations and/or supporting evidence for the period stated in this section.

      Completed validation of control of a mailbox in accordance with [Section 3.2.2.2](#3222-validating-control-over-mailbox-via-email) SHALL be obtained no more than 30 days prior to issuing the Certificate.

2. **Authentication of organization identity**: Completed validation of organization identity in accordance with [Section 3.2.3](#323-authentication-of-organization-identity) SHALL be obtained no more than 825 days prior to issuing the Certificate. 
 
      Validation of authority in accordance with [Section 3.2.6](#326-validation-of-authority) SHALL be obtained no more than 825 days prior to issuing the Certificate, unless a contract between the CA and the Applicant specifies a different term. For example, the contract MAY include the perpetual assignment of roles until revoked by the Applicant or CA, or until the contract expires or is terminated.

3. **Authentication of individual identity**: Completed validation of Individual identity in accordance with [Section 3.2.4](#324-authentication-of-individual-identity) SHALL be obtained no more than 825 days prior to issuing the Certificate. 

A prior validation SHALL NOT be reused if any data or document used in the prior validation was obtained more than the maximum time permitted for reuse of the data or document prior to issuing the Certificate.

