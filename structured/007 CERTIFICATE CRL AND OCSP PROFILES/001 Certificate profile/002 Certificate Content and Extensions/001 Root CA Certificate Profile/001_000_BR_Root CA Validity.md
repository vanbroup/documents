##### 7.1.2.1.1 Root CA Validity

| __Field__   | __Minimum__ | __Maximum__ |
| -           | ----        | ----        |
| `notBefore` | One day prior to the time of signing | The time of signing |
| `notAfter`  | 2922 days (approx. 8 years)  | 9132 days (approx. 25 years) |

**Note**: This restriction applies even in the event of generating a new Root CA Certificate for an existing `subject` and `subjectPublicKeyInfo` (e.g. reissuance). The new CA Certificate MUST conform to these rules.

