### 6.3.2 Certificate operational periods and key pair usage periods

| Generation | Maximum Validity Period      | 
|------|-----------------------|
| Strict and Multipurpose | 825 days |
| Legacy | 1185 days |

For the purpose of calculations, a day is measured as 86,400 seconds. Any amount of time greater than this, including fractional seconds and/or leap seconds, SHALL represent an additional day. For this reason, Subscriber Certificates SHOULD NOT be issued for the maximum permissible time by default, in order to account for such adjustments.

