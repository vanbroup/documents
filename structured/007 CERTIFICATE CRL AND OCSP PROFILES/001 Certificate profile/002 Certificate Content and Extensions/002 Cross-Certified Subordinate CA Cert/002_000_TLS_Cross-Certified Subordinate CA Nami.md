##### 7.1.2.2.2 Cross-Certified Subordinate CA Naming

The `subject` MUST comply with the requirements of [Section 7.1.4](#714-name-forms), or, if the existing CA Certificate was issued in compliance with the then-current version of the Baseline Requirements, the encoded `subject` name MUST be byte-for-byte identical to the encoded `subject` name of the existing CA Certificate.

**Note**: The above exception allows the CAs to issue Cross-Certified Subordinate CA Certificates, provided that the existing CA Certificate complied with the Baseline Requirements in force at time of issuance. This allows the requirements of [Section 7.1.4](#714-name-forms) to be improved over time, while still permitting Cross-Certification. If the existing CA Certificate did not comply, issuing a Cross-Certificate is not permitted.

