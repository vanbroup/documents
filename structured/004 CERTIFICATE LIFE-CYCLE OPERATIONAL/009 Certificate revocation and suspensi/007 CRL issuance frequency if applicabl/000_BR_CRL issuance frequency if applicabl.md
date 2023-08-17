### 4.9.7 CRL issuance frequency (if applicable)

For the status of Subscriber Certificates:

If the CA publishes a CRL, then the CA SHALL update and reissue CRLs at least once every seven days, and the value of the `nextUpdate` field MUST NOT be more than ten days beyond the value of the `thisUpdate` field.

For the status of Subordinate CA Certificates:

The CA SHALL update and reissue CRLs at least:

  i. once every twelve months; and
  ii. within 24 hours after revoking a Subordinate CA Certificate.

The value of the `nextUpdate` field MUST NOT be more than twelve months beyond the value of the `thisUpdate` field.

