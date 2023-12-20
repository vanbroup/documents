##### 7.1.4.2.2 Subject Common Name Field

__Certificate Field__: `subject:commonName` (OID: 2.5.4.3)  
__Required/Optional__: Deprecated (Discouraged, but not prohibited)  
__Contents__: If present, this field MUST contain a single Domain Name(s) owned or controlled by the Subject and to be associated with the Subject's server.  Such server MAY be owned and operated by the Subject or another entity (e.g., a hosting service). This field MUST NOT contain a Wildcard Domain Name unless the FQDN portion of the Wildcard Domain Name is an Onion Domain Name verified in accordance with Appendix B of the Baseline Requirements.

