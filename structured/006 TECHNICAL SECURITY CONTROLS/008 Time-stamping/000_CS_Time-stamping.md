## 6.8 Time-stamping

If the CA issues Code Signing Certificates, then the CA MUST operate a Timestamp Authority that complies with RFC 3161. CAs MUST recommend to Subscribers that they use the CA's Timestamp Authority to timestamp signed code.

The Timestamp Authority MUST ensure that clock synchronization is maintained when a leap second occurs. A Timestamp Authority MUST synchronize its timestamp server at least every 24 hours with a UTC(k) time source. The timestamp server MUST automatically detect and report on clock drifts or jumps out of synchronization with UTC. Clock adjustments of one second or greater MUST be auditable events. Any changes to its signing process MUST be an auditable event.

The digest algorithm used to sign Timestamp tokens must match the digest algorithm used to sign the Timestamp Certificate.

