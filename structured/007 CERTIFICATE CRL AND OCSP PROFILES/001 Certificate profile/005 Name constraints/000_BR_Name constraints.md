### 7.1.5 Name constraints

For a Subordinate CA Certificate to be considered Technically Constrained, the certificate MUST include an Extended Key Usage (EKU) extension specifying all extended key usages that the Subordinate CA Certificate is authorized to issue certificates for. The `anyExtendedKeyUsage` KeyPurposeId MUST NOT appear within this extension.

If the Subordinate CA Certificate includes the id-kp-serverAuth extended key usage, then the Subordinate CA Certificate MUST include the Name Constraints X.509v3 extension with constraints on `dNSName`, `iPAddress` and `DirectoryName` as follows:

a. For each `dNSName` in `permittedSubtrees`, the CA MUST confirm that the Applicant has registered the `dNSName` or has been authorized by the domain registrant to act on the registrant's behalf in line with the verification practices of [Section 3.2.2.4](#3224-validation-of-domain-authorization-or-control).
b. For each `iPAddress` range in `permittedSubtrees`, the CA MUST confirm that the Applicant has been assigned the IP Address range or has been authorized by the assigner to act on the assignee's behalf.
c. For each `DirectoryName` in `permittedSubtrees`, the CA MUST confirm the Applicant's and/or Subsidiary's Organizational name and location such that end entity certificates issued from the subordinate CA Certificate will be in compliance with [Section 7.1.2.4](#7124-all-certificates) and [Section 7.1.2.5](#7125-application-of-rfc-5280).

If the Subordinate CA Certificate is not allowed to issue certificates with an IP Address, then the Subordinate CA Certificate MUST specify the entire IPv4 and IPv6 address ranges in `excludedSubtrees`. The Subordinate CA Certificate MUST include within `excludedSubtrees` an `iPAddress` `GeneralName` of 8 zero octets (covering the IPv4 address range of 0.0.0.0/0). The Subordinate CA Certificate MUST also include within `excludedSubtrees` an `iPAddress` `GeneralName` of 32 zero octets (covering the IPv6 address range of ::0/0). Otherwise, the Subordinate CA Certificate MUST include at least one `iPAddress` in `permittedSubtrees`.

A decoded example for issuance to the domain and sub domains of `example.com` by organization `Example LLC, Boston, Massachusetts, US` would be:

```text
X509v3 Name Constraints:
  Permitted:
    DNS:example.com
    DirName: C=US, ST=MA, L=Boston, O=Example LLC
  Excluded:
    IP:0.0.0.0/0.0.0.0
    IP:0:0:0:0:0:0:0:0/0:0:0:0:0:0:0:0
```

If the Subordinate CA is not allowed to issue certificates with `dNSName`s, then the Subordinate CA Certificate MUST include a zero-length `dNSName` in `excludedSubtrees`. Otherwise, the Subordinate CA Certificate MUST include at least one `dNSName` in `permittedSubtrees`.

