##### 7.1.2.7.1 Subscriber Certificate Types

There are four types of Subscriber Certificates that may be issued, which vary based on the amount of Subject Information that is included.  Each of these certificate types shares a common profile, with three exceptions: the `subject` name fields that may occur, how those fields are validated, and the contents of the `certificatePolicies` extension. 

| __Type__                    | __Description__                                       |
| ---                         | -------                                                |
| Domain Validated (DV)       | See [Section 7.1.2.7.2](#71272-domain-validated)       |
| Individual Validated (IV)   | See [Section 7.1.2.7.3](#71273-individual-validated)   |
| Organization Validated (OV) | See [Section 7.1.2.7.4](#71274-organization-validated) |
| Extended Validation (EV)    | See [Section 7.1.2.7.5](#71275-extended-validation)    |

**Note**: Although each Subscriber Certificate type varies in Subject Information, all Certificates provide the same level of assurance of the device identity (domain name and/or IP address).

