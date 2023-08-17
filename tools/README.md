# Layered CA/Browser Forum requirements

## Introduction

The tools in this directory help to convert the existing documents in to a structured repository, it's the intention that we start working on the structured repository and only build the final documents.

The advantage of this setup is that you will no longer have to work with extremely large files and that it could help us to move to a BR of BR's section by section with minimal bootstrapping work.

The baseline requirements (BR) are incorporated unless the target document type includes a file for the same section with a weight of 000.

In following example each target document BR, CS, SMIME defines it's own introduction, when building the target document only one of these documents will be included:

```sh
000_BR_INTRODUCTION.md
000_CS_INTRODUCTION.md
000_SMIME_INTRODUCTION.md
```

If the weight of the CS and/or SMIME was different, like 001 in the example below, both the BR and the CS or SMIME introduction would be included if the target was CS or SMIME:

```sh
000_BR_INTRODUCTION.md
001_CS_INTRODUCTION.md
001_SMIME_INTRODUCTION.md
```

## Requirements

In each document you can specify a requirement, this would work following:

```md
    [001] This is an example requirement
```

This requirement will be extracted an included in the matrix as:

```csv
"ID","Section","LoA","Type","Requirement"
BR-1.3.1-001, 1.3.1, EV, BR, This is an example requirement
```

## TODO
- Handle "No stipulation", this is now less predictable, when do we want this?
- Review the requirement matrix, do we need to add more information
- Move TLS requirements from BR to TLS
- Define a LoA (OV/EV or something new) for in addition to the document type.
