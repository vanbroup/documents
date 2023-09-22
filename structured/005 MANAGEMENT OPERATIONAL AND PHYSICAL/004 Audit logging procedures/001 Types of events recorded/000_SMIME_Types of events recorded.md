### 5.4.1 Types of events recorded

The CA and each Delegated Third Party SHALL record events related to the security of their Certificate Systems, Certificate Management Systems, Root CA Systems, and Delegated Third Party Systems. The CA and each Delegated Third Party SHALL record events related to their actions taken to process a Certificate Request and to issue a Certificate, including all information generated and documentation received in connection with the Certificate Request; the time and date; and the personnel involved. The CA SHALL make these records available to its Qualified Auditor as proof of the CA’s compliance with these Requirements.

The CA SHALL record at least the following events:

1. CA Certificate and key lifecycle events, including:<br>
   i. Key generation, backup, storage, recovery, archival, and destruction;
   ii. Certificate requests, renewal, and re-key requests, and revocation;
   iii. Approval and rejection of Certificate Requests;
   iv. Cryptographic device lifecycle management events;
   v. Generation of Certificate Revocation Lists;
   vi. Signing of OCSP Responses (as described in [Section 4.9](#49-certificate-revocation-and-suspension) and [Section 4.10](#410-certificate-status-services)); and
   vii. Introduction of new Certificate Profiles and retirement of existing Certificate Profiles.

2. Subscriber Certificate lifecycle management events, including:<br>
   i. Certificate requests, renewal, and re-key requests, and revocation;
   ii. All verification activities stipulated in these Requirements and the CA's Certification Practice Statement;
   iii. Approval and rejection of Certificate Requests;
   iv. Issuance of Certificates;
   v. Generation of Certificate Revocation Lists; and
   vi. Signing of OCSP Responses (as described in [Section 4.9](#49-certificate-revocation-and-suspension) and [Section 4.10](#410-certificate-status-services)).

3. Security events, including:<br>
   i. Successful and unsuccessful PKI system access attempts;
   ii. PKI and security system actions performed;
   iii. Security profile changes;
   iv. Installation, update and removal of software on a Certificate System;
   v. System crashes, hardware failures, and other anomalies;
   vi. Firewall and router activities; and
   vii. Entries to and exits from the CA facility.

Log records SHALL include the following elements:

1. Date and time of event;
2. Identity of the person making the journal record; and
3. Description of the event.

