#### 6.1.5.2 Code signing Certificate and Timestamp Authority key sizes

For Keys corresponding to Subscriber code signing and Timestamp Authority Certificates:

* If the Key is RSA, then the modulus MUST be at least 3072 bits in length.
* If the Key is ECDSA, then the curve MUST be one of NIST P-256, P-384, or P-521.
* If the Key is DSA, then one of the following key parameter options MUST be used:
  * Key length (`L`) of 2048 bits and modulus length (`N`) of 224 bits
  * Key length (`L`) of 2048 bits and modulus length (`N`) of 256 bits

