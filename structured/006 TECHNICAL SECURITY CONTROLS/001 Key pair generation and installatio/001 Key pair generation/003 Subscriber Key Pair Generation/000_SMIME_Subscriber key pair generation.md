#### 6.1.1.3 Subscriber key pair generation

The CA SHALL reject a Certificate Request if one or more of the following conditions are met:

1. The Key Pair does not meet the requirements set forth in [Section 6.1.5](#615-key-sizes) and/or [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
2. There is clear evidence that the specific method used to generate the Private Key was flawed;
3. The CA is aware of a demonstrated or proven method that exposes the Applicant's Private Key to compromise;
4. The CA has previously been made aware that the Applicant's Private Key has suffered a Key Compromise, such as through the provisions of [Section 4.9.1.1](#4911-reasons-for-revoking-a-subscriber-certificate);
5. The CA is aware of a demonstrated or proven method to easily compute the Applicant's Private Key based on the Public Key (such as a Debian weak key, see <https://wiki.debian.org/SSLkeys>).

The CA or a Delegated Third Party MAY generate the Private Key on behalf of the Subscriber.

