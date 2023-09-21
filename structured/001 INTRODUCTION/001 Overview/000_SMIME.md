## 1.1 Overview

This S/MIME Baseline Requirements document describes an integrated set of technologies, protocols, identity-proofing, lifecycle management, and auditing requirements that are necessary for the issuance and management of Publicly-Trusted S/MIME Certificates.

An S/MIME Certificate for the purposes of this document can be identified by the existence of an Extended Key Usage (EKU) for `id-kp-emailProtection` (OID: 1.3.6.1.5.5.7.3.4) and the inclusion of a `rfc822Name` or an `otherName` of type `id-on-SmtpUTF8Mailbox` in the `subjectAltName` extension.

**Notice for Readers**

An S/MIME Certificate contains a Public Key bound to a Mailbox Address and MAY also contain the identity of a Natural Person or Legal Entity that controls such email address. The Key Pair can then be used to sign, verify, encrypt, and decrypt email. 

This Certificate Policy (CP) describes a subset of the requirements that a CA SHALL meet in order to issue Publicly-Trusted S/MIME Certificates. This document serves two purposes: to specify Baseline Requirements and to provide guidance and requirements for what a Certification Authority (CA) should include in its Certification Practice Statement (CPS). These Requirements apply only to relevant events that occur on or after the relevant Effective Date described in [Section 1.2.1](#121-revisions) of these Requirements.

These Requirements do not address all of the issues relevant to the issuance and management of Publicly-Trusted S/MIME Certificates. To facilitate a comparison of other CP and/or CPS (e.g., for policy mapping), this document includes all sections of the [RFC 3647](https://datatracker.ietf.org/doc/html/rfc3647) framework. The CA/Browser Forum MAY update these Requirements from time to time.

These Requirements do not address the issuance or management of Certificates by enterprises that operate their own Public Key Infrastructure for internal purposes only, and for which the Root CA Certificate is not distributed by any Application Software Supplier. 

These Requirements are applicable to all CAs within a Publicly-Trusted chain of trust. They are to be flowed down from the Root CA through successive Subordinate CAs.

