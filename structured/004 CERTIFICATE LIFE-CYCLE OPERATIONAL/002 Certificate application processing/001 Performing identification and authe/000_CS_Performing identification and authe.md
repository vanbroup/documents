### 4.2.1 Performing identification and authentication functions

The certificate request or signing request MAY include all factual information about the Applicant necessary to issue the Certificate or sign the Code, and such additional information as is necessary for the CA or Signing Service to obtain from the Applicant in order to comply with these Requirements and the CA's Certificate Policy and/or Certification Practice Statement. In cases where the certificate request or signing request does not contain all the necessary information about the Applicant, the CA or Signing Service MUST obtain the remaining information from the Applicant or, having obtained it from a reliable, independent, third-party data source, confirm it with the Applicant. The CA or Signing Service MUST establish and follow a documented procedure for verifying all data requested for inclusion in the Certificate by the Applicant.

Prior to issuing a Code Signing Certificate, each CA SHOULD check at least one database containing information about known or suspected producers, publishers, or distributors of Suspect Code, as identified or indicated by an Anti-Malware Organization and any database of deceptive names maintained by an Application Software Provider. The CA MUST determine whether the entity is identified as requesting a Code Signing Certificate from a High Risk Region of Concern. The CA MUST also maintain and check an internal database listing Certificates revoked due to Code Signatures on Suspect Code and previous certificate requests rejected by the CA.

A CA identifying a high risk application under this section MUST follow the additional procedures defined in [Section 4.2.2](#422-approval-or-rejection-of-certificate-applications) of this document to ensure that the applicant will protect its Private Keys and not sign Suspect Code.

\[These requirements do not specify a particular database and leave the decision of qualifying databases to the implementers.\]

Prior to issuing Code Signing Certificates, the CA SHALL perform "due diligence" verification as specified in EV Guidelines 11.13.

Methods 4, 5 and 7 of [Section 6.2.7.4.1](#62741-subscriber-private-key-protection) may be reused if Subscriber Private Key protection has been validated no more than 13 months prior to issuing the Code Signing Certificate. 

For Non-EV Code Signing Certificates, the CA MAY use the documents and data provided in [Section 3.2](#32-initial-identity-validation) to verify certificate information, or may reuse previous validations themselves, provided that the CA obtained the data or document from a source specified under [Section 3.2](#32-initial-identity-validation) or completed the validation itself no more than 825 days prior to issuing the Certificate.

For EV Code Signing Certificates, use of documents, data, and previous validations performed per [Section 3.2](#32-initial-identity-validation) SHALL be governed by the usage periods as defined in EV Guidelines Section 11.14.

