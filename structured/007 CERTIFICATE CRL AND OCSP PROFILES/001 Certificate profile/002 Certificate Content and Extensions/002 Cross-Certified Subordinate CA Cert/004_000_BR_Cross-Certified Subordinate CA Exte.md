##### 7.1.2.2.4 Cross-Certified Subordinate CA Extended Key Usage - Unrestricted

Table: Unrestricted Extended Key Usage Purposes (Affiliated Cross-Certified CA)

| __Key Purpose__        | __Description__ |
| ---                    | -------         |
| `anyExtendedKeyUsage`  | The special extended key usage to indicate there are no restrictions applied. If present, this MUST be the only key usage present. |
| Any other value        | CAs MUST NOT include any other key usage with the `anyExtendedKeyUsage` key usage present. |

Alternatively, if the Issuing CA does not use this form, then the Extended Key Usage extension, if present, MUST be encoded as specified in [Section 7.1.2.2.5](#71225-cross-certified-subordinate-ca-extended-key-usage---restricted).

