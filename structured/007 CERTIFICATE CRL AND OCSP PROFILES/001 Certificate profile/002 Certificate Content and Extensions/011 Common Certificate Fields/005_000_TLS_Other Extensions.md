##### 7.1.2.11.5 Other Extensions

All extensions and extension values not directly addressed by the applicable certificate profile:

  1. MUST apply in the context of the public Internet, unless:
     a. the extension OID falls within an OID arc for which the Applicant demonstrates ownership, or,
     b. the Applicant can otherwise demonstrate the right to assert the data in a public context.
  2. MUST NOT include semantics that will mislead the Relying Party about certificate information verified by the CA (such as including an extension that indicates a Private Key is stored on a smart card, where the CA is not able to verify that the corresponding Private Key is confined to such hardware due to remote issuance).
  3. MUST be DER encoded according to the relevant ASN.1 module defining the extension and extension values.

CAs SHALL NOT include additional extensions or values unless the CA is aware of a reason for including the data in the Certificate.

