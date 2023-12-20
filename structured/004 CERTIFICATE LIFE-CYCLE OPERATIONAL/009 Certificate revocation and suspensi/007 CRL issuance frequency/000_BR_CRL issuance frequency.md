### 4.9.7 CRL issuance frequency

CRLs must be available via a publicly-accessible HTTP URL (i.e., "published").

Within twenty-four (24) hours of issuing its first Certificate, the CA MUST generate and publish either:
- a full and complete CRL; OR
- partitioned (i.e., "sharded") CRLs that, when aggregated, represent the equivalent of a full and complete CRL.

CAs issuing Subscriber Certificates:  
1. MUST update and publish a new CRL at least every: 
     - seven (7) days if all Certificates include an Authority Information Access extension with an id-ad-ocsp accessMethod (“AIA OCSP pointer”); or
     - four (4) days in all other cases; 
2. MUST update and publish a new CRL within twenty-four (24) hours after recording a Certificate as revoked.

CAs issuing CA Certificates:  
1. MUST update and publish a new CRL at least every twelve (12) months;
2. MUST update and publish a new CRL within twenty-four (24) hours after recording a Certificate as revoked.

CAs MUST continue issuing CRLs until one of the following is true:
- all Subordinate CA Certificates containing the same Subject Public Key are expired or revoked; OR
- the corresponding Subordinate CA Private Key is destroyed.


