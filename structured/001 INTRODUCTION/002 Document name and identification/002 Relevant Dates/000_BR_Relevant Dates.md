### 1.2.2 Relevant Dates

| **Compliance** | **Section(s)** | **Summary Description (See Full Text for Details)** |
|--|--|----------|
| 2013-01-01 | 6.1.6 | For RSA public keys, CAs SHALL confirm that the value of the public exponent is an odd number equal to 3 or more. |
| 2013-01-01 | 4.9.10 | CAs SHALL support an OCSP capability using the GET method. |
| 2013-01-01 | 5 | CAs SHALL comply with the Network and Certificate System Security Requirements. |
| 2013-08-01 | 4.9.10 | OCSP Responders SHALL NOT respond "Good" for Unissued Certificates. |
| 2013-09-01 | 3.2.2.6 | CAs SHALL revoke any certificate where wildcard character occurs in the first label position immediately to the left of a "registry-controlled" label or "public suffix". |
| 2013-12-31 | 6.1.5 | CAs SHALL confirm that the RSA Public Key is at least 2048 bits or that one of the following ECC curves is used: P-256, P-384, or P-521. A Root CA Certificate issued prior to 31 Dec. 2010 with an RSA key size less than 2048 bits MAY still serve as a trust anchor. |
| 2015-01-16 | 7.1.3 | CAs SHOULD NOT issue Subscriber Certificates utilizing the SHA-1 algorithm with an Expiry Date greater than 1 January 2017. |
| 2015-04-01 | 6.3.2 | CAs SHALL NOT issue certificates with validity periods longer than 39 months, except under certain circumstances. |
| 2015-04-15 | 2.2 | A CA's CPS must state whether it reviews CAA Records, and if so, its policy or practice on processing CAA records for Fully-Qualified Domain Names. |
| 2015-11-01 | 7.1.4.2.1 | Issuance of Certificates with Reserved IP Address or Internal Name prohibited. |
| 2016-01-01 | 7.1.3 | CAs MUST NOT issue any new Subscriber certificates or Subordinate CA certificates using the SHA-1 hash algorithm. |
| 2016-06-30 | 6.1.7 | CAs MUST NOT issue Subscriber Certificates directly from Root CAs. |
| 2016-06-30 | 6.3.2 | CAs MUST NOT issue Subscriber Certificates with validity periods longer than 39 months, regardless of circumstance. |
| 2016‐09‐30 | 7.1 | CAs SHALL generate Certificate serial numbers greater than zero (0) containing at least 64 bits of output from a CSPRNG |
| 2016-10-01 | 7.1.4.2.1 | All Certificates with Reserved IP Address or Internal Name must be revoked. |
| 2016-12-03 | 1 and 2 | Ballot 156 amendments to sections 1.5.2, 2.3, and 2.4 are applicable |
| 2017-01-01 | 7.1.3 | CAs MUST NOT issue OCSP responder certificates using SHA-1 (inferred). |
| 2017-03-01 | 3.2.2.4 | CAs MUST follow revised validation requirements in Section 3.2.2.4. |
| 2017-09-08 | 3.2.2.8 | CAs MUST check and process CAA records |
| 2018-03-01 | 4.2.1 and 6.3.2 | Certificates issued MUST have a Validity Period no greater than 825 days and re-use of validation information limited to 825 days |
| 2018-05-31 | 2.2 | CP and CPS must follow RFC 3647 format |
| 2018-08-01 | 3.2.2.4.1 and .5 | CAs must stop using domain validation methods BR 3.2.2.4.1 and 3.2.2.4.5, stop reusing validation data from those methods |
| 2019-01-15 | 7.1.4.2.1 | All certificates containing an underscore character in any dNSName entry and having a validity period of more than 30 days MUST be revoked prior to January 15, 2019 |
| 2019-05-01 | 7.1.4.2.1 | underscore characters (“_”) MUST NOT be present in dNSName entries |
| 2019-06-01 | 3.2.2.4.3 | CAs SHALL NOT perform validations using this method after May 31, 2019. Completed validations using this method SHALL continue to be valid for subsequent issuance per the applicable certificate data reuse periods.
| 2019-08-01 | 3.2.2.5 | CAs SHALL maintain a record of which IP validation method, including the relevant BR version number, was used to validate every IP Address |
| 2019-08-01 | 3.2.2.5.4 | CAs SHALL NOT perform validations using this method after July 31, 2019. Completed validations using this method SHALL NOT be re-used for certificate issuance after July 31, 2019. Any certificate issued prior to August 1, 2019 containing an IP Address that was validated using any method that was permitted under the prior version of this Section 3.2.2.5 MAY continue to be used without revalidation until such certificate naturally expires |
| 2020-06-03 | 3.2.2.4.6 | CAs MUST NOT perform validation using this method after 3 months from the IPR review date of Ballot SC25 |
| 2020-08-01 | 8.6 | Audit Reports for periods on-or-after 2020-08-01 MUST be structured as defined. |
| 2020-09-01 | 6.3.2 | Certificates issued SHOULD NOT have a Validity Period greater than 397 days and MUST NOT have a Validity Period greater than 398 days. |
| 2020-09-30 | 4.9.10 | OCSP responses MUST conform to the validity period requirements specified. |
| 2020-09-30 | 7.1.4.1 | Subject and Issuer Names for all possible certification paths MUST be byte-for-byte identical. |
| 2020-09-30 | 7.1.6.4 | Subscriber Certificates MUST include a CA/Browser Forum Reserved Policy Identifier in the Certificate Policies extension. |
| 2020-09-30 | 7.2 and 7.3 | All OCSP and CRL responses for Subordinate CA Certificates MUST include a meaningful reason code. |
| 2021-07-01 | 3.2.2.8 | CAA checking is no longer optional if the CA is the DNS Operator or an Affiliate. |
| 2021-07-01 | 3.2.2.4.18 and 3.2.2.4.19 | Redirects MUST be the result of one of the HTTP status code responses defined.  |
| 2021-10-01 | 7.1.4.2.1 | Fully-Qualified Domain Names MUST consist solely of P-Labels and Non-Reserved LDH Labels. |
| 2021-12-01 | 3.2.2.4 | CAs MUST NOT use methods 3.2.2.4.6, 3.2.2.4.18, or 3.2.2.4.19 to issue wildcard certificates or with Authorization Domain Names other than the FQDN. |
| 2022-06-01 | 7.1.3.2.1 | CAs MUST NOT sign OCSP responses using the SHA-1 hash algorithm. |
| 2022-09-01 | 7.1.4.2.2 | CAs MUST NOT include the organizationalUnitName field in the Subject |
| 2023-01-15 | 7.2.2 | Sharded or partitioned CRLs MUST have a distributionPoint |

