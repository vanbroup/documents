#### 3.2.2.3 Validating applicant as operator of associated mail server(s)

The CA MAY confirm the Applicant's control over each Mailbox Field to be included in the Certificate by confirming control of the SMTP FQDN to which a message delivered to the Mailbox Address should be directed. The SMTP FQDN SHALL be identified using the address resolution algorithm defined in [RFC 5321 Section 5.1](https://datatracker.ietf.org/doc/html/rfc5321#section-5.1) which determines which SMTP FQDNs are authoritative for a given Mailbox Address. If more than one SMTP FQDN has been discovered, the CA SHALL verify control of an SMTP FQDN following the selection process at [RFC 5321 Section 5.1](https://datatracker.ietf.org/doc/html/rfc5321#section-5.1). Aliases in MX record RDATA SHALL NOT be used for this validation method.

To confirm the Applicant's control of the SMTP FQDN, the CA SHALL use only the currently-approved methods in [Section 3.2.2.4](https://github.com/cabforum/servercert/blob/main/docs/BR.md#3224-validation-of-domain-authorization-or-control) of the TLS Baseline Requirements.

