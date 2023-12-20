##### 7.1.4.2.4 Subject Jurisdiction of Incorporation or Registration Field

__Certificate Fields__:

Locality (if required):  
  `subject:jurisdictionLocalityName` (OID: 1.3.6.1.4.1.311.60.2.1.1)

State or province (if required):  
  `subject:jurisdictionStateOrProvinceName` (OID: 1.3.6.1.4.1.311.60.2.1.2)

Country:  
  `subject:jurisdictionCountryName` (OID: 1.3.6.1.4.1.311.60.2.1.3)

__Required/Optional__: Required  
__Contents__: These fields MUST NOT contain information that is not relevant to the level of the Incorporating Agency or Registration Agency.  For example, the Jurisdiction of Incorporation for an Incorporating Agency or Jurisdiction of Registration for a Registration Agency that operates at the country level MUST include the country information but MUST NOT include the state or province or locality information.  Similarly, the jurisdiction for the applicable Incorporating Agency or Registration Agency at the state or province level MUST include both country and state or province information, but MUST NOT include locality information.  And, the jurisdiction for the applicable Incorporating Agency or Registration Agency at the locality level MUST include the country and state or province information, where the state or province regulates the registration of the entities at the locality level, as well as the locality information.  Country information MUST be specified using the applicable ISO country code.  State or province or locality information (where applicable) for the Subject's Jurisdiction of Incorporation or Registration MUST be specified using the full name of the applicable jurisdiction.

Effective as of 1 October 2020, the CA SHALL ensure that, at time of issuance, the values within these fields have been disclosed within the latest publicly-available disclosure, as described in [Section 3.2.2.1.3](#32213-disclosure-of-verification-sources), as acceptable values for the applicable Incorporating Agency or Registration Agency.

