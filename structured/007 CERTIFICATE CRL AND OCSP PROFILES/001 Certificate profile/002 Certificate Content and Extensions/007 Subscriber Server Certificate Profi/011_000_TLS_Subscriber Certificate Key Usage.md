##### 7.1.2.7.11 Subscriber Certificate Key Usage

The acceptable Key Usage values vary based on whether the Certificate's `subjectPublicKeyInfo` identifies an RSA public key or an ECC public key. CAs MUST ensure the Key Usage is appropriate for the Certificate Public Key.

Table: Key Usage for RSA Public Keys

| __Key Usage__      | __Permitted__ | __Required__     |
| ----               | -             | -                |
| `digitalSignature` | Y             | SHOULD           |
| `nonRepudiation`   | N             | --               |
| `keyEncipherment`  | Y             | MAY              |
| `dataEncipherment` | Y             | NOT RECOMMENDED  |
| `keyAgreement`     | N             | --               |
| `keyCertSign`      | N             | --               |
| `cRLSign`          | N             | --               |
| `encipherOnly`     | N             | --               |
| `decipherOnly`     | N             | --               |

**Note**: At least one Key Usage MUST be set for RSA Public Keys. The `digitalSignature` bit is REQUIRED for use with modern protocols, such as TLS 1.3, and secure ciphersuites, while the `keyEncipherment` bit MAY be asserted to support older protocols, such as TLS 1.2, when using insecure ciphersuites. Subscribers MAY wish to ensure key separation to limit the risk from such legacy protocols, and thus a CA MAY issue a Subscriber certificate that only asserts the `keyEncipherment` bit. For most Subscribers, the `digitalSignature` bit is sufficient, while Subscribers that want to mix insecure and secure ciphersuites with the same algorithm may choose to assert both `digitalSignature` and `keyEncipherment` within the same certificate, although this is NOT RECOMMENDED. The `dataEncipherment` bit is currently permitted, although setting it is NOT RECOMMENDED, as it is a Pending Prohibition (https://github.com/cabforum/servercert/issues/384).

Table: Key Usage for ECC Public Keys

| __Key Usage__      | __Permitted__ | __Required__     |
| ----               | -             | -                |
| `digitalSignature` | Y             | MUST             |
| `nonRepudiation`   | N             | --               |
| `keyEncipherment`  | N             | --               |
| `dataEncipherment` | N             | --               |
| `keyAgreement`     | Y             | NOT RECOMMENDED  |
| `keyCertSign`      | N             | --               |
| `cRLSign`          | N             | --               |
| `encipherOnly`     | N             | --               |
| `decipherOnly`     | N             | --               |

**Note**: The `keyAgreement` bit is currently permitted, although setting it is NOT RECOMMENDED, as it is a Pending Prohibition (https://github.com/cabforum/servercert/issues/384).

