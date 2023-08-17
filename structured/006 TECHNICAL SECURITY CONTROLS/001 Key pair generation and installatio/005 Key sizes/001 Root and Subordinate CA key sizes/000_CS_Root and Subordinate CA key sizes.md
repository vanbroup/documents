#### 6.1.5.1 Root and Subordinate CA key sizes

For Keys corresponding to Root and Subordinate CAs:

* If the Key is RSA, then the modulus MUST be at least 4096 bits in length. [^legacy_key_length]
* If the Key is ECDSA, then the curve MUST be one of NIST P-256, P-384, or P-521.
* If the Key is DSA, then one of the following key parameter options MUST be used:
  * Key length (`L`) of 2048 bits and modulus length (`N`) of 224 bits
  * Key length (`L`) of 2048 bits and modulus length (`N`) of 256 bits

[^legacy_key_length]: CAs MAY sign Cross-Certificates with Root CA RSA Private Keys whose modulus length is less than 4096 bits, provided that the Cross-Certificate is issued to a Root CA whose Public Key adheres to the key size requirements of this section. 

