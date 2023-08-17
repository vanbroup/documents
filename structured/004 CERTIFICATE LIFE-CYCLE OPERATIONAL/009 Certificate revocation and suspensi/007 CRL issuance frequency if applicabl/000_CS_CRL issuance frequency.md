### 4.9.7 CRL issuance frequency

For the status of Subordinate CA Certificates: 

  * The Issuing CA SHALL publish a CRL, then update and reissue a CRL at least once every twelve months and within 24 hours after revoking a Subordinate CA Certificate. The `nextUpdate` field MUST NOT be more than twelve months beyond the value of the `thisUpdate` field.

For the status of Code Signing Certificates:

  * The Subordinate CA SHALL publish a CRL, then update and reissue a CRL at least once every seven days, and the value of the `nextUpdate` field MUST NOT be more than ten days beyond the value of the `thisUpdate` field.

For the status of Timestamp Certificates:

  * The Subordinate CA SHALL update and reissue CRLs at least once every twelve months and within 24 hours after revoking a Timestamp Certificate, and the value of the `nextUpdate` field MUST NOT be more than twelve months beyond the value of the `thisUpdate` field.

