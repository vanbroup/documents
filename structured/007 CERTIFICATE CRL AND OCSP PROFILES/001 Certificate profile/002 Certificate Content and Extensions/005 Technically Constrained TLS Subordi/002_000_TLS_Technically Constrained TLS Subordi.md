##### 7.1.2.5.2 Technically Constrained TLS Subordinate CA Name Constraints

For a TLS Subordinate CA to be Technically Constrained, Name Constraints extension MUST be encoded as follows. As an explicit exception from RFC 5280, this extension SHOULD be marked critical, but MAY be marked non-critical if compatibility with certain legacy applications that do not support Name Constraints is necessary.

Table: `nameConstraints` requirements

| __Field__             | __Description__ |
| --                    | -------         |
| `permittedSubtrees`   | The `permittedSubtrees` MUST contain at least one `GeneralSubtree` for both of the `dNSName` and `iPAddress` `GeneralName` name types, UNLESS the specified `GeneralName` name type appears within the `excludedSubtrees` to exclude all names of that name type. Additionally, the `permittedSubtrees` MUST contain at least one `GeneralSubtree` of the `directoryName` `GeneralName` name type. |
|     `GeneralSubtree`  | The requirements for a `GeneralSubtree` that appears within a `permittedSubtrees`. |
|         `base`        | See following table. |
|         `minimum`     | MUST NOT be present. |
|         `maximum`     | MUST NOT be present. |
| `excludedSubtrees`    | The `excludedSubtrees` MUST contain at least one `GeneralSubtree` for each of the `dNSName` and `iPAddress` `GeneralName` name types, unless there is an instance present of that name type in the `permittedSubtrees`. The `directoryName` name type is NOT RECOMMENDED. |
|     `GeneralSubtree`  | The requirements for a `GeneralSubtree` that appears within a `permittedSubtrees`. |
|         `base`        | See following table. |
|         `minimum`     | MUST NOT be present. |
|         `maximum`     | MUST NOT be present. |

The following table contains the requirements for the `GeneralName` that appears within the `base` of a `GeneralSubtree` in either the `permittedSubtrees` or `excludedSubtrees`.

Table: `GeneralName` requirements for the `base` field

| __Name Type__   | __Presence__    |  __Permitted Subtrees__ | __Excluded Subtrees__ | __Entire Namespace Exclusion__ |
| ---             | --              | ----                    | ----                  | ----                           |
| `dNSName`       | MUST            | The CA MUST confirm that the Applicant has registered the `dNSName` or has been authorized by the domain registrant to act on the registrant's behalf. See [Section 3.2.2.4](#3224-validation-of-domain-authorization-or-control). | If at least one `dNSName` instance is present in the `permittedSubtrees`, the CA MAY indicate one or more subordinate domains to be excluded. | If no `dNSName` instance is present in the `permittedSubtrees`, then the CA MUST include a zero-length `dNSName` to indicate no domain names are permitted. |
| `iPAddress`     | MUST            | The CA MUST confirm that the Applicant has been assigned the `iPAddress` range or has been authorized by the assigner to act on the asignee's behalf. See [Section 3.2.2.5](#3225-authentication-for-an-ip-address). | If at least one `iPAddress` instance is present in the `permittedSubtrees`, the CA MAY indicate one or more subdivisions of those ranges to be excluded. | If no IPv4 `iPAddress` is present in the `permittedSubtrees`, the CA MUST include an `iPAddress` of 8 zero octets, indicating the IPv4 range of 0.0.0.0/0 being excluded. If no IPv6 `iPAddress` is present in the `permittedSubtrees`, the CA MUST include an `iPAddress` of 32 zero octets, indicating the IPv6 range of ::0/0 being excluded. |
| `directoryName` | MUST            | The CA MUST confirm the Applicant's and/or Subsidiary's name attributes such that all certificates issued will comply with the relevant Certificate Profile (see [Section 7.1.2](#712-certificate-content-and-extensions)), including Name Forms (See [Section 7.1.4](#714-name-forms)). | It is NOT RECOMMENDED to include values within `excludedSubtrees`. | The CA MUST include a value within `permittedSubtrees`, and as such, this does not apply. See the Excluded Subtrees requirements for more. |
| `otherName`     | NOT RECOMMENDED | See below           | See below             | See below                      |
| Any other value | MUST NOT        | -                   | -                     | -                              |

Any `otherName`, if present:

  1. MUST apply in the context of the public Internet, unless:
     a. the `type-id` falls within an OID arc for which the Applicant demonstrates ownership, or,
     b. the Applicant can otherwise demonstrate the right to assert the data in a public context.
  2. MUST NOT include semantics that will mislead the Relying Party about certificate information verified by the CA.
  3. MUST be DER encoded according to the relevant ASN.1 module defining the `otherName` `type-id` and `value`.

CAs SHALL NOT include additional names unless the CA is aware of a reason for including the data in the Certificate.

