## 7.2 CRL profile

The serial number of a revoked Certificate MUST remain on the CRL for at least 10 years after the expiration of the Certificate. Application Software Suppliers MAY require the CA to support a longer life-time in its contract with the CA. If a Code Signing Certificate contains the Lifetime Signing OID, the Code Signature becomes invalid when the Code Signing Certificate expires, even if the Code Signature is timestamped. Because the Lifetime Signing OID is intended to be used with test purposes only, a CA MAY cease maintaining revocation information for a Code Signing Certificate with the Lifetime Signing OID after the Code Signing Certificate expires.

If a Code Signing Certificate previously has been revoked, and the CA later becomes aware of a more appropriate revocation date, then the CA MAY use that revocation date in subsequent CRL entries for that Code Signing Certificate.

