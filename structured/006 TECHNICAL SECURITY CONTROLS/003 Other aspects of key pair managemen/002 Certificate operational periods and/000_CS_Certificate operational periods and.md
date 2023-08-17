### 6.3.2 Certificate operational periods and key pair usage periods

Subscribers and Signing Services MAY sign Code at any point in the development or distribution process. Code Signatures may be verified at any time, including during download, unpacking, installation, reinstallation, or execution, or during a forensic investigation.

The validity period for a Code Signing Certificate issued to a Subscriber or Signing Service MUST NOT exceed 39 months.

The Timestamp Authority MUST use a new Timestamp Certificate with a new private key no later than every 15 months to minimize the impact to users in the event that a Timestamp Certificate\'s private key is compromised. The validity for a Timestamp Certificate must not exceed 135 months. The Timestamp Certificate MUST meet the requirements in [Section 6.1.5](#615-key-sizes) for the communicated time period.

Cryptographic algorithms, key sizes and certificate life-times for both authorities and Subscribers are governed by the NIST key management guidelines.

