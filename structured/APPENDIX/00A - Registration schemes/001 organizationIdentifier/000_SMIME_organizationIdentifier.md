## A.1 organizationIdentifier

The following Registration Schemes are recognized as valid under these Requirements for use in the `subject:organizationIdentifier` attribute described in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields).

The country code used in the Registration Scheme identifier SHALL match that of the `subject:countryName` in the Certificate as specified in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields).

* **NTR**: For an identifier allocated by a national or state trade register to the Legal Entity named in the `subject:organizationName`. 

* **VAT**: For an identifier allocated by the national tax authorities to the Legal Entity named in the `subject:organizationName`. 

* **PSD**: For a national authorization number allocated to the payment service provider named in the `subject:organizationName` under Payments Services Directive (EU) 2015/2366. This shall use the extended structure as defined in ETSI TS 119 495, clause 5.2.1. 

* **LEI**: For a Legal Entity Identifier as specified in ISO 17442 for the entity named in the `subject:organizationName`. The 2 character ISO 3166 country code SHALL be set to 'XG'. 

