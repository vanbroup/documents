##### 7.1.2.2.3 Cross-Certified Subordinate CA Extensions

| __Extension__                     | __Presence__    | __Critical__          | __Description__ |
| ----                              | -               | -                     | ----- |
| `authorityKeyIdentifier`          | MUST            | N                     | See [Section 7.1.2.11.1](#712111-authority-key-identifier) |
| `basicConstraints`                | MUST            | Y                     | See [Section 7.1.2.10.4](#712104-ca-certificate-basic-constraints) |
| `certificatePolicies`             | MUST            | N                     | See [Section 7.1.2.10.5](#712105-ca-certificate-certificate-policies) |
| `crlDistributionPoints`           | MUST            | N                     | See [Section 7.1.2.11.2](#712112-crl-distribution-points) |
| `keyUsage`                        | MUST            | Y                     | See [Section 7.1.2.10.7](#712107-ca-certificate-key-usage) |
| `subjectKeyIdentifier`            | MUST            | N                     | See [Section 7.1.2.11.4](#712114-subject-key-identifier) |
| `authorityInformationAccess`      | SHOULD          | N                     | See [Section 7.1.2.10.3](#712103-ca-certificate-authority-information-access) |
| `nameConstraints`                 | MAY             | \*[^name_constraints] | See [Section 7.1.2.10.8](#712108-ca-certificate-name-constraints) |
| Signed Certificate Timestamp List | MAY             | N                     | See [Section 7.1.2.11.3](#712113-signed-certificate-timestamp-list) |
| Any other extension               | NOT RECOMMENDED | -                     | See [Section 7.1.2.11.5](#712115-other-extensions) |

In addition to the above, extKeyUsage extension requirements vary based on the relationship between the Issuer and Subject organizations represented in the Cross-Certificate.

The extKeyUsage extension MAY be "unrestricted" as described in the following table if:
- the organizationName represented in the Issuer and Subject names of the corresponding certificate are either:
   - the same, or
   - the organizationName represented in the Subject name is an affiliate of the organizationName represented in the Issuer name
- the corresponding CA represented by the Subject of the Cross-Certificate is operated by the same organization as the Issuing CA or an Affiliate of the Issuing CA organization. 

Table: Cross-Certified Subordinate CA with Unrestricted EKU

| __Extension__                     | __Presence__    | __Critical__          | __Description__ |
| ----                              | -               | -                     | ----- |
| `extKeyUsage`                     | SHOULD[^eku_ca] | N                     | See [Section 7.1.2.2.4](#71224-cross-certified-subordinate-ca-extended-key-usage---unrestricted) |

In all other cases, the extKeyUsage extension MUST be "restricted" as described in the following table:

Table: Cross-Certified Subordinate CA with Restricted EKU

| __Extension__                     | __Presence__    | __Critical__          | __Description__ |
| ----                              | -               | -                     | ----- |
| `extKeyUsage`                     | MUST[^eku_ca]   | N                     | See [Section 7.1.2.2.5](#71225-cross-certified-subordinate-ca-extended-key-usage---restricted) |

[^eku_ca]: While [RFC 5280, Section 4.2.1.12](https://tools.ietf.org/html/rfc5280#section-4.2.1.13) notes that this extension will generally only appear within end-entity certificates, these Requirements make use of this extension to further protect relying parties by limiting the scope of CA Certificates, as implemented by a number of Application Software Suppliers.

[^name_constraints]: See [Section 7.1.2.10.8](#712108-ca-certificate-name-constraints) for further requirements, including regarding criticality of this extension.

