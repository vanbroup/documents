##### 7.1.4.2.5 Subject DN attributes for sponsor-validated profile

| Attribute | Legacy<br> (See Note 1) | Multipurpose<br> (See Note 2) | Strict<br> (See Note 2) |
|-----------|--------|--------------|--------|
| `commonName` | MAY  | MAY | MAY |
| `organizationName` | SHALL | SHALL | SHALL |
| `organizationalUnitName` | MAY  | MAY | MAY |
| `organizationIdentifier` | SHALL | SHALL | SHALL |
| `givenName` | MAY | MAY | MAY |
| `surname` | MAY | MAY | MAY |
| `pseudonym` | MAY | MAY | MAY |
| `serialNumber` | MAY | MAY | MAY |
| `emailAddress` | MAY | MAY | MAY |
| `title` | MAY  | MAY | MAY |
| `streetAddress` | MAY | MAY | SHALL NOT |
| `localityName` | MAY | MAY | MAY |
| `stateOrProvinceName` | MAY | MAY | MAY |
| `postalCode` | MAY | MAY | SHALL NOT |
| `countryName` | MAY | MAY | MAY |
| Other | MAY | SHALL NOT | SHALL NOT |

**Note**: 

 1. Legacy Generation profiles MAY omit the `subject:givenName`, `subject:surname`, and `subject:pseudonym` attributes and include only the `subject:commonName` as described in [Section 7.1.4.2.2(a)](#71422-subject-distinguished-name-fields).
 2. Multipurpose and Strict Generation profiles SHALL include either `subject:givenName` and/or `subject:surname`, or the `subject:pseudonym`. 


