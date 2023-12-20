#### 7.1.2.1 Subject Alternative Name Extension

__Certificate Field__: `subjectAltName:dNSName`  
__Required/Optional__: __Required__  
__Contents__: This extension MUST contain one or more host Domain Name(s) owned or controlled by the Subject and to be associated with the Subject's server.  Such server MAY be owned and operated by the Subject or another entity (e.g., a hosting service). This extension MUST NOT contain a Wildcard Domain Name unless the FQDN portion of the Wildcard Domain Name is an Onion Domain Name verified in accordance with Appendix B of the Baseline Requirements.

