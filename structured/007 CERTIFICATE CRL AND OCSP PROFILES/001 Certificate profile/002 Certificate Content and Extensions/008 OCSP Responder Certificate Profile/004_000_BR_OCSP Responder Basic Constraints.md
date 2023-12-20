##### 7.1.2.8.4 OCSP Responder Basic Constraints

OCSP Responder certificates MUST NOT be CA certificates. The issuing CA may indicate this one of two ways: by omission of the `basicConstraints` extension, or through the inclusion of a `basicConstraints` extension that sets the `cA` boolean to FALSE.

| __Field__           | __Description__ |
| ---                 | ------- |
| `cA`                | MUST be FALSE |
| `pathLenConstraint` | MUST NOT be present |

**Note**: Due to DER encoding rules regarding the encoding of DEFAULT values within OPTIONAL fields, a `basicConstraints` extension that sets the `cA` boolean to FALSE MUST have an `extnValue` `OCTET STRING` which is exactly the hex-encoded bytes `3000`, the encoded representation of an empty ASN.1 `SEQUENCE` value.

