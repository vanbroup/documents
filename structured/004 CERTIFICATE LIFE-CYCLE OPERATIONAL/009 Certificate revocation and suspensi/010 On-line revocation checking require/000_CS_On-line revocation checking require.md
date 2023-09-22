### 4.9.10 On-line revocation checking requirements

Effective 2023-09-15, OCSP responders operated by the CA SHALL support the HTTP GET method, as described in RFC 6960 and/or RFC 5019.

Effective 2023-09-15, the validity interval of an OCSP response is the difference in time between the `thisUpdate` and `nextUpdate` field, inclusive. For purposes of computing differences, a difference of 3,600 seconds shall be equal to one hour, and a difference of 86,400 seconds shall be equal to one day, ignoring leap-seconds.

CAs MAY provide OCSP responses for Code Signing Certificates and Timestamp Certificates for the time period specified in their CPS, which MAY be at least 10 years after the expiration of the certificate.

If the CA provides OCSP responses, the CA SHALL support an OCSP capability using the GET method for Certificates issued in accordance with these Requirements.

For the status of Subordinate CA Certificates:

  * If the Issuing CA provides OCSP responses, the Issuing CA SHALL update information provided via an OCSP response at least every twelve months and within 24 hours after revoking a Subordinate CA Certificate.

For the status of Code Signing Certificates:

  * If the Subordinate CA provides OCSP responses, the CA SHALL update information provided via an OCSP response at least every four days. OCSP responses from this service MUST have a maximum expiration time of ten days.

For the status of Timestamp Certificates:

  * If the Subordinate CA provides OCSP responses, the Subordinate CA SHALL update information provided via an OCSP response at least every twelve months and within 24 hours after revoking a Timestamp Certificate.

A certificate serial number within an OCSP request is "assigned" if a Certificate with that serial number has been issued by the Issuing CA, using any current or previous key associated with that CA subject.

If the OCSP responder receives a request for the status of a certificate serial number that is not "assigned", then the responder MUST NOT respond with a "good" status.

