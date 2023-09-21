### 4.9.7 CRL issuance frequency

For the status of Subscriber Certificates: the CA SHALL update and reissue CRLs at least once every seven days, and the value of the `nextUpdate` field SHALL NOT be more than ten days beyond the value of the `thisUpdate` field.

For the status of Subordinate CA Certificates: the CA SHALL update and reissue CRLs at least:

1. once every twelve months; and
2. within 24 hours after revoking a Subordinate CA Certificate.

The value of the `nextUpdate` field SHALL NOT be more than twelve months beyond the value of the `thisUpdate` field.

