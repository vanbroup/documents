#### 7.1.2.2 CA/Browser Forum Organization Identifier Extension

__Extension Name__: `cabfOrganizationIdentifier` (OID: 2.23.140.3.1)  
__Verbose OID__: `{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-extensions(3) cabf-organization-identifier(1) }`  
__Required/Optional__: __Optional (but see below)__  
__Contents__: If the subject:organizationIdentifier is present, this field MUST be present.

If present, this extension MUST contain a Registration Reference for a Legal Entity assigned in accordance to the identified Registration Scheme.

The Registration Scheme MUST be encoded as described by the following ASN.1 grammar:

```ASN.1
id-CABFOrganizationIdentifier OBJECT IDENTIFIER ::= {
    joint-iso-itu-t(2) international-organizations(23)
    ca-browser-forum(140) certificate-extensions(3)
    cabf-organizationIdentifier(1) 
}

ext-CABFOrganizationIdentifier EXTENSION ::= {
    SYNTAX CABFOrganizationIdentifier
    IDENTIFIED BY id-CABFOrganizationIdentifier
}

CABFOrganizationIdentifier ::= SEQUENCE {
    registrationSchemeIdentifier PrintableString (SIZE(3)),
    registrationCountry          PrintableString (SIZE(2)),
    registrationStateOrProvince  [0] IMPLICIT PrintableString
                                  (SIZE(0..128)) OPTIONAL,
    registrationReference        UTF8String
}
```

where the subfields have the same values, meanings, and restrictions described in [Section 7.1.4.2.8](#71428-subject-organization-identifier-field). The CA SHALL validate the contents using the requirements in [Section 7.1.4.2.8](#71428-subject-organization-identifier-field).

