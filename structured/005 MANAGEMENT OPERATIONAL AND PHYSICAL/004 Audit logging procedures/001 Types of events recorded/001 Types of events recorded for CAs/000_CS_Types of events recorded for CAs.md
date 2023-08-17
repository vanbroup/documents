#### 5.4.1.1 Types of events recorded for CAs

The CA and each Delegated Third Party SHALL record details of the actions taken to process a certificate request and to issue a certificate, including all information generated and documentation received in connection with the certificate request; the time and date; and the personnel involved. The CA SHALL make these records available to its Qualified Auditor as proof of the CA’s compliance with these Requirements.

The CA SHALL record at least the following events:
1. CA certificate and key lifecycle management events, including:
   
   1. Key generation, backup, storage, recovery, archival, and destruction;
   2. Certificate requests, renewal, and re-key requests, and revocation;
   3. Approval and rejection of certificate requests ;
   4. Cryptographic device lifecycle management events;
   5. Generation of Certificate Revocation Lists
   6. Signing of OCSP Responses (as described in [Section 4.9](#49-certificate-revocation-and-suspension) and [Section 4.10](#410-certificate-status-services)); and 
   7. Introduction of new Certificate Profiles and retirement of existing Certificate Profiles

2. CA and Subscriber lifecycle management events, including:
   
   1. Certificate requests, renewals, re-key requests, and revocation;
   2. All verification activities stipulated in these Requirements and the CA’s Certification Practice Statement (CPS);
   3. Acceptance and rejection of certificate requests;
   4. Issuance of Certificates;
   5. Generation of Certificate Revocation Lists and OCSP entries; and
   6. Signing of OCSP Responses (as described in [Section 4.9](#49-certificate-revocation-and-suspension) and [Section 4.10](#410-certificate-status-services)).

3.	Security events, including:

   1. Successful and unsuccessful PKI system access attempts;
   2. PKI and security system actions performed;
   3. Security profile changes;
   4. System crashes, hardware failures, and other anomalies;
   5. Firewall and router activities; and
   6. Entries to and exits from the CA facility.

Log records MUST include the following elements:

1. Date and time of event;
2. Identity of the person making the journal record; and 
3. Description of the event.

