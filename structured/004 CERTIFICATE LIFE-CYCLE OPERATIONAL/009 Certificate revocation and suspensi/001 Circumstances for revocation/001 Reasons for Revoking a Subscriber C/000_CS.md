#### 4.9.1.1 Reasons for Revoking a Subscriber Certificate
 
The CA SHALL revoke a Certificate within 24 hours if one or more of the following occurs:
 
1. The Subscriber requests in writing that the CA revoke the Certificate;
2. The Subscriber notifies the CA that the original certificate request was not authorized and does not retroactively grant authorization;
3. The CA obtains evidence that the Subscriber's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise;
4. The CA is made aware of a demonstrated or proven method that can easily compute the Subscriber's Private Key based on the Public Key in the Certificate;
5. The CA is made aware of a demonstrated or proven method that exposes the Subscriber’s Private Key to compromise or if there is clear evidence that the specific method used to generate the Private Key was flawed; or
6. The CA has reasonable assurance that a Certificate was used to sign Suspect Code.
 
The CA SHOULD revoke a certificate within 24 hours and SHALL revoke a Certificate within 5 days if one or more of the following occurs:

7. The Certificate no longer complies with the requirements of Section 6.1.5 and Section 6.1.6; 
8. The CA obtains evidence that the Certificate was misused. 
9. The CA is made aware that a Subscriber has violated one or more of its material obligations under the Subscriber Agreement or Terms of Use. 
10. The CA is made aware of a material change in the information contained in the Certificate. 
11. The CA is made aware that the Certificate was not issued in accordance with these Requirements or the CA's Certificate Policy or Certification Practice Statement. 
12. The CA determines or is made aware that any of the information appearing in the Certificate is inaccurate. 
13. The CA's right to issue Certificates under these Requirements expires or is revoked or terminated, unless the CA has made arrangements to continue maintaining the CRL/OCSP Repository. 
14. Revocation is required by the CA's Certificate Policy and/or Certification Practice Statement. 
 
The CA MAY delay revocation based on a request from Application Software Suppliers where immediate revocation has a potentially large negative impact to the ecosystem.

 
**Note:** Nothing herein prohibits a CA from revoking a Code Signing Certificate prior to these time frames.
 
