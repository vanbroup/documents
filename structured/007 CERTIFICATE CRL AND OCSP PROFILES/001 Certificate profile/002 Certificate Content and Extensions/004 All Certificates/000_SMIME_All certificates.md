#### 7.1.2.4 All certificates

All fields and extensions SHALL be set in accordance with [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280). The CA SHALL NOT issue a Certificate that contains a `keyUsage` flag, `extKeyUsage` value, Certificate extension, or other data not specified in [Section 7.1.2.1](#7121-root-ca-certificates), [Section 7.1.2.2](#7122-subordinate-ca-certificates), or [Section 7.1.2.3](#7123-subscriber-certificates) unless the CA is aware of a reason for including the data in the Certificate. If the CA includes fields or extensions in a Certificate that are not specified but are otherwise permitted by these Requirements, then the CA SHALL document the processes and procedures that the CA employs for the validation of information contained in such fields and extensions in its CP and/or CPS.

CAs SHALL NOT issue a Certificate with:

1. Extensions that do not apply in the context of the public Internet (such as an `extKeyUsage` value for a service that is only valid in the context of a privately managed network), unless:<br>
   i. such value falls within an OID arc for which the Applicant demonstrates ownership, or<br>
   ii. the Applicant can otherwise demonstrate the right to assert the data in a public context; or
2. Field or extension values which have not been validated according to the processes and procedures described in these Requirements or the CA's CP and/or CPS.
   
