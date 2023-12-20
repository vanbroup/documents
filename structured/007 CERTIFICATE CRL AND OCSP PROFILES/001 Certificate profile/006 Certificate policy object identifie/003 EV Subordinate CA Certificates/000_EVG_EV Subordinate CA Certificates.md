#### 7.1.6.3 EV Subordinate CA Certificates

1. Certificates issued to Subordinate CAs that are not controlled by the issuing CA MUST contain one or more policy identifiers defined by the issuing CA that explicitly identify the EV Policies that are implemented by the Subordinate CA.
2. Certificates issued to Subordinate CAs that are controlled by the Root CA MAY contain the special `anyPolicy` identifier (OID: 2.5.29.32.0).

