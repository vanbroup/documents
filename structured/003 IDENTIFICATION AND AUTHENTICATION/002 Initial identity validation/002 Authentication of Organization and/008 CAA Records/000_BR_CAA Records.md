#### 3.2.2.8 CAA Records

As part of the Certificate issuance process, the CA MUST retrieve and process CAA records in accordance with RFC 8659 for each `dNSName` in the `subjectAltName` extension that does not contain an Onion Domain Name. If the CA issues, they MUST do so within the TTL of the CAA record, or 8 hours, whichever is greater.

This stipulation does not prevent the CA from checking CAA records at any other time.

When processing CAA records, CAs MUST process the issue, issuewild, and iodef property tags as specified in RFC 8659, although they are not required to act on the contents of the iodef property tag. Additional property tags MAY be supported, but MUST NOT conflict with or supersede the mandatory property tags set out in this document. CAs MUST respect the critical flag and not issue a certificate if they encounter an unrecognized property tag with this flag set.

RFC 8659 requires that CAs "MUST NOT issue a certificate unless the CA determines that either (1) the certificate request is consistent with the applicable CAA RRset or (2) an exception specified in the relevant CP or CPS applies." For issuances conforming to these Baseline Requirements, CAs MUST NOT rely on any exceptions specified in their CP or CPS unless they are one of the following:

* CAA checking is optional for certificates for which a Certificate Transparency Precertificate (see [Section 7.1.2.9](#7129-precertificate-profile)) was created and logged in at least two public logs, and for which CAA was checked at time of Precertificate issuance.
* CAA checking is optional for certificates issued by a Technically Constrained Subordinate CA Certificate as set out in [Section 7.1.2.3](#7123-technically-constrained-non-tls-subordinate-ca-certificate-profile) or [Section 7.1.2.5](#7125-technically-constrained-tls-subordinate-ca-certificate-profile), where the lack of CAA checking is an explicit contractual provision in the contract with the Applicant.
* For certificates issued prior to July 1, 2021, CAA checking is optional if the CA or an Affiliate of the CA is the DNS Operator (as defined in RFC 7719) of the domain's DNS.

CAs are permitted to treat a record lookup failure as permission to issue if:

* the failure is outside the CA's infrastructure; and
* the lookup has been retried at least once; and
* the domain's zone does not have a DNSSEC validation chain to the ICANN root.

CAs MUST document potential issuances that were prevented by a CAA record in sufficient detail to provide feedback to the CAB Forum on the circumstances, and SHOULD dispatch reports of such issuance requests to the contact(s) stipulated in the CAA iodef record(s), if present. CAs are not expected to support URL schemes in the iodef record other than mailto: or https:.

