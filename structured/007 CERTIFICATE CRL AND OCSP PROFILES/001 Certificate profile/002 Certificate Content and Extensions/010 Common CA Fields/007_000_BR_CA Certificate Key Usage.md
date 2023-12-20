##### 7.1.2.10.7 CA Certificate Key Usage

| __Key Usage__      | __Permitted__ | __Required__     |
| ----               | -             | -                |
| `digitalSignature` | Y             | N[^ocsp_signing] |
| `nonRepudiation`   | N             | --               |
| `keyEncipherment`  | N             | --               |
| `dataEncipherment` | N             | --               |
| `keyAgreement`     | N             | --               |
| `keyCertSign`      | Y             | Y                |
| `cRLSign`          | Y             | Y                |
| `encipherOnly`     | N             | --               |
| `decipherOnly`     | N             | --               |

[^ocsp_signing]: If a CA Certificate does not assert the `digitalSignature` bit, the CA Private Key MUST NOT be used to sign an OCSP Response. See [Section 7.3](#73-ocsp-profile) for more information.

