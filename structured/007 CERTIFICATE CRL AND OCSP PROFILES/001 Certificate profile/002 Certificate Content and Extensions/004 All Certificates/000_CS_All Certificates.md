#### 7.1.2.4 All Certificates

All other fields and extensions MUST be set in accordance with RFC 5280. The CA SHALL NOT issue a Certificate that contains a `keyUsage` flag, `extKeyUsage` value, Certificate extension, or other data not specified in [Section 7.1.2.1](#7121-root-ca-certificate), [Section 7.1.2.2](#7122-subordinate-ca-certificate), or [Section 7.1.2.3](#7123-code-signing-and-timestamp-certificate) unless the CA is aware of a reason for including the data in the Certificate.

CAs SHALL NOT issue a Certificate with:

a. Extensions that do not apply in the context of the public Internet (such as an extKeyUsage value for a service that is only valid in the context of a privately managed network), unless:
   i. such value falls within an OID arc for which the Applicant demonstrates ownership, or
   ii. the Applicant can otherwise demonstrate the right to assert the data in a public context; or
b. semantics that, if included, will mislead a Relying Party about the certificate information verified by the CA (such as including an `extKeyUsage` value for a smart card, where the CA is not able to verify that the corresponding Private Key is confined to such hardware due to remote issuance).


