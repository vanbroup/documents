### 6.1.5 Key sizes

For RSA key pairs the CA SHALL:

* Ensure that the modulus size, when encoded, is at least 2048 bits, and;
* Ensure that the modulus size, in bits, is evenly divisible by 8.

For ECDSA key pairs, the CA SHALL:

* Ensure that the key represents a valid point on the NIST P-256, NIST P-384 or NIST P-521 elliptic curve.

No other algorithms or key sizes are permitted.

