##### 7.1.4.2.1 Subject alternative name extension

__Certificate Field:__ `extensions:subjectAltName`  
__Required/Optional:__ SHALL be present  
__Contents:__ This extension SHALL contain at least one `GeneralName` entry of the following types:

* `Rfc822Name` and/or
* `otherName` of type `id-on-SmtpUTF8Mailbox`, encoded in accordance with [RFC 8398](https://datatracker.ietf.org/doc/html/rfc8398)

All Mailbox Addresses in the `subject` field or entries of type `dirName` of this extension SHALL be repeated as `rfc822Name` or `otherName` values of type `id-on-SmtpUTF8Mailbox` in this extension.

The CA MAY include `GeneralName` entries of type `dirName` provided that the information contained in the `Name` complies with the requirements set forth in the appropriate subsection of [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields) according to the Certificate Type. Additionally, information contained in the `Name` SHALL be validated according to [Section 3.1](#31-naming), [Section 3.2.3](#323-authentication-of-organization-identity), and/or [Section 3.2.4](#324-authentication-of-individual-identity), as appropriate for the Certificate Type.

For Legacy and Multipurpose Generation profiles, then the CA MAY include `otherName` entries of any type, provided that the CA has validated the field value according to its CP and/or CPS.

The CA SHALL NOT include `GeneralName` entries that do not conform to the requirements of this section.

