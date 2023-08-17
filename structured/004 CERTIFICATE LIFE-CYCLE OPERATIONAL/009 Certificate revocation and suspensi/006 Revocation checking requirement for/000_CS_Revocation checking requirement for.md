### 4.9.6 Revocation checking requirement for relying parties

 A Certificate MAY have a one-to-one relationship or one-to-many relationship with the signed Code. Regardless, revocation of a Certificate may invalidate the Code Signatures on all signed Code, some of which could be perfectly sound. Because of this, the CA MAY specify the time at which the Certificate is first considered to be invalid in the `revocationDate` field of a CRL entry or the `revocationTime` field of an OCSP response to time-bind the set of software affected by the revocation[^*], and software should continue to treat objects containing a timestamp dated before the revocation date as valid.

[^*]: Backdating the `revocationDate` field is an exception to best practice described in RFC 5280 (section 5.3.2); however, these Requirements specify the use of the `revocationDate` field to convey the “invalidity date” to support Application Software Supplier software implementations that process the `revocationDate` field as the date when the Certificate is first considered to be invalid.

