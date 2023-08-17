### 9.6.1 CA representations and warranties

By issuing a Certificate, the CA makes the warranties listed herein to the following Certificate Beneficiaries:

1. The Subscriber that is a party to the Subscriber Agreement or Terms of Use for the Certificate;
2. All Application Software Suppliers with whom the Root CA has entered into a contract for inclusion of its Root CA Certificate in software distributed by such Application Software Supplier; and
3. All Relying Parties who reasonably rely on a Valid Certificate. 

The CA represents and warrants to the Certificate Beneficiaries that, during the period when the Certificate is valid, the CA has complied with these Requirements and its CP and/or CPS in issuing and managing the Certificate.

The Certificate Warranties specifically include, but are not limited to, the following:

1. **Right to Use Mailbox Address**: That, at the time of issuance, the CA:<br>
   i. implemented a procedure for verifying that the Applicant either had the right to use, or had control of, the Mailbox Addresses listed in the Certificate's `subject` field and `subjectAltName` extension (or was delegated such right or control by someone who had such right to use or control);
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's CP and/or CPS;
2. **Authorization for Certificate**: That, at the time of issuance, the CA:<br>
   i. implemented a procedure for verifying that the Subject authorized the issuance of the Certificate and that the Applicant Representative is authorized to request the Certificate on behalf of the Subject;
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's CP and/or CPS;
3. **Accuracy of Information**: That, at the time of issuance, the CA:<br>
   i. implemented a procedure for verifying the accuracy of all of the information contained in the Certificate (with the exception of the subject:serialNumber attribute);
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's CP and/or CPS;
4. **Identity of Applicant**: That, if the Certificate contains Subject Identity Information, the CA:<br>
   i. implemented a procedure to verify the identity of the Applicant in accordance with [Section 3.2](#32-initial-identity-validation) and [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields);
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's CP and/or CPS;
5. **Subscriber Agreement**: That, if the CA and Subscriber are not Affiliated, the Subscriber and CA are parties to a legally valid and enforceable Subscriber Agreement that satisfies these Requirements, or, if the CA and Subscriber are the same entity or are Affiliated, the Applicant Representative acknowledged the Terms of Use;
6. **Status**: That the CA maintains a 24 x 7 publicly-accessible Repository with current information regarding the status (Valid or Revoked) of all unexpired Certificates; and
7. **Revocation**: That the CA will revoke the Certificate for any of the reasons specified in these Requirements.

The Root CA SHALL be responsible for the performance and warranties, compliance with these Requirements, and for all liabilities and indemnification obligations of the Subordinate CA under these Requirements, as if the Root CA were the Subordinate CA issuing the Certificates.

