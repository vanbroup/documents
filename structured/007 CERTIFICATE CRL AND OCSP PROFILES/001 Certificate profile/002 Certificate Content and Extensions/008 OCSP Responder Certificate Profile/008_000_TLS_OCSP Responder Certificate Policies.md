##### 7.1.2.8.8 OCSP Responder Certificate Policies

If present, the Certificate Policies extension MUST contain at least one `PolicyInformation`. Each `PolicyInformation` MUST match the following profile:

| __Field__                | __Presence__    | __Contents__ |
| ---                      | -               | ------       |
| `policyIdentifier`       | MUST            | One of the following policy identifiers: |
|     A [Reserved Certificate Policy Identifier](#7161-reserved-certificate-policy-identifiers) | NOT RECOMMENDED | |
|     `anyPolicy`          | NOT RECOMMENDED | |
|     Any other identifier | NOT RECOMMENDED | If present, MUST be defined by the CA and documented by the CA in its Certificate Policy and/or Certification Practice Statement. |
| `policyQualifiers`       | NOT RECOMMENDED | If present, MUST contain only permitted `policyQualifiers` from the table below. |


Table: Permitted `policyQualifiers`

| __Qualifier ID__                     | __Presence__ | __Field Type__ |  __Contents__ |
| ---                                  | -            | -              | -----         |
| `id-qt-cps` (OID: 1.3.6.1.5.5.7.2.1) | MAY          | `IA5String`    | The HTTP or HTTPS URL for the Issuing CA's Certificate Policies, Certification Practice Statement, Relying Party Agreement, or other pointer to online policy information provided by the Issuing CA. |
| Any other qualifier                  | MUST NOT     | -              | -             |


**Note**: See [Section 7.1.2.8.2](#71282-ocsp-responder-extensions) for applicable effective dates for when this extension may be included.

**Note**: Because the Certificate Policies extension may be used to restrict the applicable usages for a Certificate, incorrect policies may result in OCSP Responder Certificates that fail to successfully validate, resulting in invalid OCSP Responses. Including the `anyPolicy` policy can reduce this risk, but add to client processing complexity and interoperability issues.

