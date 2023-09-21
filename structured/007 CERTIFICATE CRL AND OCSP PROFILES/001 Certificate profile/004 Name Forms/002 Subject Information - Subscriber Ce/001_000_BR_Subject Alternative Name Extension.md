##### 7.1.4.2.1 Subject Alternative Name Extension

__Certificate Field:__ `extensions:subjectAltName`  
__Required/Optional:__ Required  
__Contents:__ This extension MUST contain at least one entry. Each entry MUST be one of the following types:

* `dNSName`: The entry MUST contain either a Fully-Qualified Domain Name or Wildcard Domain Name that the CA has validated in accordance with [Section 3.2.2.4](#3224-validation-of-domain-authorization-or-control). Wildcard Domain Names MUST be validated for consistency with [Section 3.2.2.6](#3226-wildcard-domain-validation). The entry MUST NOT contain an Internal Name.

   The Fully-Qualified Domain Name or the FQDN portion of the Wildcard Domain Name contained in the entry MUST be composed entirely of LDH Labels joined together by a U+002E FULL STOP (".") character. The zero-length Domain Label representing the root zone of the Internet Domain Name System MUST NOT be included (e.g. "example.com" MUST be encoded as "example.com" and MUST NOT be encoded as "example.com.").

   The Fully-Qualified Domain Name or the FQDN portion of the Wildcard Domain Name MUST consist solely of Domain Labels that are P-Labels or Non-Reserved LDH Labels.

* `iPAddress`: The entry MUST contain an IPv4 or IPv6 address that the CA has validated in accordance with [Section 3.2.2.5](#3225-authentication-for-an-ip-address). The entry MUST NOT contain a Reserved IP Address.

