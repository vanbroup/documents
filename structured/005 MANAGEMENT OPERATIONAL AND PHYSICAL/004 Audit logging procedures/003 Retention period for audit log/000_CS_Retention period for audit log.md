### 5.4.3 Retention period for audit log

The CA, Delegated Third Parties, and Timestamp Authority MUST retain, for at least two (2) years:

1.	CA certificate and key lifecycle management event records (as set forth in [Section 5.4.1.1](#5411-types-of-events-recorded-for-cas))(1) after the later occurrence of:
   a.	the destruction of the CA Private Key; or
   b.	the revocation or expiration of the final CA Certificate in that set of Certificates that have an X.509v3 basicConstraints extension with the cA field set to true and which share a common Public Key corresponding to the CA Private Key;
2.	Subscriber Certificate lifecycle management event records (as set forth in [Section 5.4.1.2](#5412-types-of-events-recorded-for-timestamp-authorities))(2) after the revocation or expiration of the Subscriber Certificate;
3.	Timestamp Authority data records (as set forth in [Section 5.4.1.2](#5412-types-of-events-recorded-for-timestamp-authorities)) after the revocation or renewal of the Timestamp Certificate private key (as set forth in [Section 6.3.2](#632-certificate-operational-periods-and-key-pair-usage-periods));
4.	Any security event records (as set forth in [Section 5.4.1.1](#5412-types-of-events-recorded-for-timestamp-authorities)(3) and for Timestamp Authority security event records set forth in [Section 5.4.1.2](#5412-types-of-events-recorded-for-timestamp-authorities)(3)) after the event occurred

**Note**: While these Requirements set the minimum retention period, the CA, Delegated Third Parties, and Timestamp Authority may choose a greater value as more appropriate in order to be able to investigate possible security or other types of incidents that will require retrospection and examination of past events.

