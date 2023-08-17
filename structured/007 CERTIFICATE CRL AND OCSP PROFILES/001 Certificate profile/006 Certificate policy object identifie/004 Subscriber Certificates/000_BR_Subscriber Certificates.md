#### 7.1.6.4 Subscriber Certificates

A Certificate issued to a Subscriber MUST contain, within the Certificate's `certificatePolicies` extension, one or more policy identifier(s) that are specified beneath the CA/Browser Forum's reserved policy OID arc of `{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1)} (2.23.140.1)`.

The certificate MAY also contain additional policy identifier(s) defined by the Issuing CA. The issuing CA SHALL document in its Certificate Policy or Certification Practice Statement that the Certificates it issues containing the specified policy identifier(s) are managed in accordance with these requirements.

Prior to including a Reserved Certificate Policy Identifier, the CA MUST ensure the following requirements are met:

* __Certificate Policy Identifier:__ `2.23.140.1.2.1`

  If the Certificate complies with these requirements and lacks Subject identity information that has been verified in accordance with [Section 3.2.2.1](#3221-identity) or [Section 3.2.3](#323-authentication-of-individual-identity).

  Such Certificates MUST NOT include `organizationName`, `givenName`, `surname`, `streetAddress`, `localityName`, `stateOrProvinceName`, or `postalCode` in the Subject field.

* __Certificate Policy Identifier:__ `2.23.140.1.2.2`

  If the Certificate complies with these Requirements and includes Subject Identity Information that is verified in accordance with [Section 3.2.2.1](#3221-identity).

  Such Certificates MUST also include `organizationName`, `localityName` (to the extent such field is required under [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields)), `stateOrProvinceName` (to the extent such field is required under [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields)), and `countryName` in the Subject field.

* __Certificate Policy Identifier:__ `2.23.140.1.2.3`

  If the Certificate complies with these Requirements and includes Subject Identity Information that is verified in accordance with [Section 3.2.3](#323-authentication-of-individual-identity).

  Such Certificates MUST also include either `organizationName` or both `givenName` and `surname`, `localityName` (to the extent such field is required under [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields)), `stateOrProvinceName` (to the extent required under [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields)), and `countryName` in the Subject field.

* __Certificate Policy Identifier:__ `2.23.140.1.1`

  If the Certificate complies with these Requirements and has been issued and operated in accordance with the CA/Browser Forum Guidelines for the Issuance and Management of Extended Validation Certificates ("EV Guidelines").

  Such Certificates MUST also include Subject Identity Information as required and verified according to the EV Guidelines.

