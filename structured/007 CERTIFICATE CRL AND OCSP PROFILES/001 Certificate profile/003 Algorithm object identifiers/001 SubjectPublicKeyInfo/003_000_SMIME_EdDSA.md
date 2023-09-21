##### 7.1.3.1.3 EdDSA

The CA SHALL indicate an EdDSA key using one of the following algorithm identifiers below:

* For curve25519 keys, the `algorithm` SHALL be id-Ed25519 (OID: 1.3.101.112).
* For curve448 keys, the `algorithm` SHALL be id-Ed448 (OID: 1.3.101.113).

The parameters for EdDSA keys SHALL be absent.

When encoded, the `AlgorithmIdentifier` for EdDSA keys SHALL be byte-for-byte identical with the following hex-encoded bytes:

* For Curve25519 keys, `300506032b6570`.
* For Curve448 keys, `300506032b6571`.

