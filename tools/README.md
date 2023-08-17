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

## Usage

Transform documents:

```sh
py transform.py ../docs/BR.md
py transform.py ../docs/CS.md
py transform.py ../docs/SMIME.md
```

Remove duplicates:

```sh
py duplicates.py
```

Build documents and requirement sheets:

```sh
py build.py BR
py build.py CS
py build.py SMIME
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

## Duplicate sections

The tool duplicates.py compares sections from different documents and automatically deletes duplicates to ensure that modifications in the baseline requirements wil automatically be adopted in the relying document.

The following sections have been identified as equal, the corresponding CS and SMIME files have been deleted.

```
1.3.3 equal to SMIME
1.5.4 equal to CS
1.5.4 equal to SMIME
2.3 equal to CS
2.4 equal to CS
3 equal to CS
3 equal to SMIME
3.1 equal to CS
3.1 equal to SMIME
3.1.1 equal to CS
3.1.2 equal to CS
3.1.3 equal to CS
3.1.4 equal to CS
3.1.4 equal to SMIME
3.1.5 equal to CS
3.1.5 equal to SMIME
3.1.6 equal to CS
3.1.6 equal to SMIME
3.2 equal to CS
3.2.1 equal to CS
3.2.1 equal to SMIME
3.2.4 equal to CS
3.3 equal to CS
3.3 equal to SMIME
3.3.1 equal to CS
3.3.1 equal to SMIME
3.3.2 equal to CS
3.3.2 equal to SMIME
3.4 equal to CS
3.4 equal to SMIME
4 equal to CS
4 equal to SMIME
4.1 equal to CS
4.1.1 equal to SMIME
4.2 equal to CS
4.2 equal to SMIME
4.2.3 equal to CS
4.2.3 equal to SMIME
4.3 equal to CS
4.3 equal to SMIME
4.3.2 equal to CS
4.3.2 equal to SMIME
4.4 equal to CS
4.4 equal to SMIME
4.4.1 equal to CS
4.4.1 equal to SMIME
4.4.2 equal to CS
4.4.2 equal to SMIME
4.4.3 equal to CS
4.4.3 equal to SMIME
4.5 equal to CS
4.5 equal to SMIME
4.5.1 equal to CS
4.5.1 equal to SMIME
4.5.2 equal to CS
4.5.2 equal to SMIME
4.6 equal to CS
4.6 equal to SMIME
4.6.1 equal to CS
4.6.1 equal to SMIME
4.6.2 equal to CS
4.6.2 equal to SMIME
4.6.3 equal to CS
4.6.3 equal to SMIME
4.6.4 equal to CS
4.6.4 equal to SMIME
4.6.5 equal to CS
4.6.5 equal to SMIME
4.6.6 equal to CS
4.6.6 equal to SMIME
4.6.7 equal to CS
4.6.7 equal to SMIME
4.7 equal to CS
4.7 equal to SMIME
4.7.1 equal to CS
4.7.1 equal to SMIME
4.7.2 equal to CS
4.7.2 equal to SMIME
4.7.3 equal to CS
4.7.3 equal to SMIME
4.7.4 equal to CS
4.7.4 equal to SMIME
4.7.5 equal to CS
4.7.5 equal to SMIME
4.7.6 equal to CS
4.7.6 equal to SMIME
4.7.7 equal to CS
4.7.7 equal to SMIME
4.8 equal to CS
4.8 equal to SMIME
4.8.1 equal to CS
4.8.1 equal to SMIME
4.8.2 equal to CS
4.8.2 equal to SMIME
4.8.3 equal to CS
4.8.3 equal to SMIME
4.8.4 equal to CS
4.8.4 equal to SMIME
4.8.5 equal to CS
4.8.5 equal to SMIME
4.8.6 equal to CS
4.8.6 equal to SMIME
4.8.7 equal to CS
4.8.7 equal to SMIME
4.9 equal to SMIME
4.9.1 equal to SMIME
4.9.1.2 equal to CS
4.9.3 equal to CS
4.9.4 equal to CS
4.9.4 equal to SMIME
4.9.9 equal to CS
4.9.12 equal to CS
4.9.12 equal to SMIME
4.9.14 equal to CS
4.9.15 equal to CS
4.9.16 equal to CS
4.10 equal to CS
4.10 equal to SMIME
4.10.2 equal to SMIME
4.10.3 equal to CS
4.10.3 equal to SMIME
4.11 equal to CS
4.11 equal to SMIME
4.12 equal to CS
4.12 equal to SMIME
4.12.1 equal to CS
4.12.2 equal to CS
5.1.1 equal to CS
5.1.1 equal to SMIME
5.1.2 equal to CS
5.1.2 equal to SMIME
5.1.3 equal to CS
5.1.3 equal to SMIME
5.1.4 equal to CS
5.1.4 equal to SMIME
5.1.5 equal to CS
5.1.5 equal to SMIME
5.1.6 equal to CS
5.1.6 equal to SMIME
5.1.7 equal to CS
5.1.7 equal to SMIME
5.1.8 equal to CS
5.1.8 equal to SMIME
5.2 equal to CS
5.2 equal to SMIME
5.2.1 equal to CS
5.2.1 equal to SMIME
5.2.3 equal to CS
5.2.3 equal to SMIME
5.2.4 equal to SMIME
5.3 equal to CS
5.3 equal to SMIME
5.3.1 equal to CS
5.3.1 equal to SMIME
5.3.2 equal to SMIME
5.3.4 equal to CS
5.3.4 equal to SMIME
5.3.5 equal to CS
5.3.5 equal to SMIME
5.3.6 equal to CS
5.3.6 equal to SMIME
5.3.8 equal to CS
5.3.8 equal to SMIME
5.4 equal to CS
5.4 equal to SMIME
5.4.2 equal to SMIME
5.4.4 equal to CS
5.4.4 equal to SMIME
5.4.5 equal to CS
5.4.5 equal to SMIME
5.4.6 equal to SMIME
5.4.7 equal to CS
5.4.7 equal to SMIME
5.5 equal to CS
5.5 equal to SMIME
5.5.1 equal to CS
5.5.2 equal to CS
5.5.3 equal to CS
5.5.3 equal to SMIME
5.5.4 equal to CS
5.5.4 equal to SMIME
5.5.5 equal to CS
5.5.5 equal to SMIME
5.5.6 equal to CS
5.5.6 equal to SMIME
5.5.7 equal to CS
5.5.7 equal to SMIME
5.6 equal to CS
5.6 equal to SMIME
5.7 equal to CS
5.7 equal to SMIME
5.7.4 equal to CS
5.7.4 equal to SMIME
5.8 equal to SMIME
6 equal to CS
6 equal to SMIME
6.1 equal to CS
6.1 equal to SMIME
6.1.1 equal to CS
6.1.1 equal to SMIME
6.1.1.1 equal to CS
6.1.1.2 equal to CS
6.1.3 equal to CS
6.1.3 equal to SMIME
6.1.4 equal to CS
6.1.4 equal to SMIME
6.1.6 equal to CS
6.2 equal to CS
6.2.1 equal to CS
6.2.1 equal to SMIME
6.2.2 equal to CS
6.2.2 equal to SMIME
6.2.3 equal to CS
6.2.3 equal to SMIME
6.2.5 equal to CS
6.2.5 equal to SMIME
6.2.7 equal to SMIME
6.2.11 equal to CS
6.3 equal to CS
6.3 equal to SMIME
6.3.1 equal to CS
6.3.1 equal to SMIME
6.4 equal to CS
6.4 equal to SMIME
6.4.1 equal to CS
6.4.1 equal to SMIME
6.4.2 equal to CS
6.4.2 equal to SMIME
6.4.3 equal to CS
6.4.3 equal to SMIME
6.5 equal to CS
6.5 equal to SMIME
6.5.1 equal to CS
6.5.1 equal to SMIME
6.5.2 equal to CS
6.5.2 equal to SMIME
6.6 equal to CS
6.6 equal to SMIME
6.6.1 equal to CS
6.6.1 equal to SMIME
6.6.2 equal to CS
6.6.2 equal to SMIME
6.6.3 equal to CS
6.6.3 equal to SMIME
6.7 equal to CS
6.8 equal to SMIME
7 equal to CS
7 equal to SMIME
7.1.1 equal to CS
7.1.2.1 equal to CS
7.1.7 equal to CS
7.1.8 equal to CS
7.1.8 equal to SMIME
7.1.9 equal to CS
7.2 equal to SMIME
7.2.1 equal to CS
7.2.1 equal to SMIME
7.3.1 equal to CS
7.3.1 equal to SMIME
8.3 equal to CS
8.3 equal to SMIME
8.5 equal to CS
8.5 equal to SMIME
8.6 equal to CS
9 equal to CS
9 equal to SMIME
9.1 equal to CS
9.1 equal to SMIME
9.1.1 equal to CS
9.1.1 equal to SMIME
9.1.2 equal to CS
9.1.2 equal to SMIME
9.1.3 equal to CS
9.1.3 equal to SMIME
9.1.4 equal to CS
9.1.4 equal to SMIME
9.1.5 equal to CS
9.1.5 equal to SMIME
9.2 equal to CS
9.2 equal to SMIME
9.2.1 equal to SMIME
9.2.2 equal to CS
9.2.2 equal to SMIME
9.2.3 equal to CS
9.2.3 equal to SMIME
9.3 equal to CS
9.3 equal to SMIME
9.3.1 equal to CS
9.3.1 equal to SMIME
9.3.2 equal to CS
9.3.2 equal to SMIME
9.3.3 equal to CS
9.3.3 equal to SMIME
9.4 equal to CS
9.4 equal to SMIME
9.4.1 equal to CS
9.4.2 equal to CS
9.4.3 equal to CS
9.4.3 equal to SMIME
9.4.4 equal to CS
9.4.5 equal to CS
9.4.6 equal to CS
9.4.6 equal to SMIME
9.4.7 equal to CS
9.4.7 equal to SMIME
9.5 equal to CS
9.5 equal to SMIME
9.6 equal to CS
9.6 equal to SMIME
9.6.2 equal to CS
9.6.2 equal to SMIME
9.6.4 equal to CS
9.6.4 equal to SMIME
9.6.5 equal to SMIME
9.7 equal to CS
9.7 equal to SMIME
9.9 equal to CS
9.10 equal to CS
9.10 equal to SMIME
9.10.1 equal to CS
9.10.1 equal to SMIME
9.10.2 equal to CS
9.10.2 equal to SMIME
9.10.3 equal to CS
9.10.3 equal to SMIME
9.11 equal to CS
9.11 equal to SMIME
9.12 equal to CS
9.12 equal to SMIME
9.12.1 equal to CS
9.12.1 equal to SMIME
9.12.2 equal to CS
9.12.2 equal to SMIME
9.12.3 equal to CS
9.12.3 equal to SMIME
9.13 equal to CS
9.13 equal to SMIME
9.14 equal to CS
9.14 equal to SMIME
9.16 equal to CS
9.16 equal to SMIME
9.16.1 equal to CS
9.16.1 equal to SMIME
9.16.2 equal to CS
9.16.2 equal to SMIME
9.16.4 equal to CS
9.16.4 equal to SMIME
9.16.5 equal to CS
9.17 equal to CS
9.17 equal to SMIME
```

## TODO
- Handle "No stipulation", this is now less predictable, when do we want this?
- Review the requirement matrix, do we need to add more information.
- Move TLS requirements from BR to TLS to ensure that they are not included in CS or SMIME requirements.
- Define a LoA (OV/EV or something new) for in addition to the document type.
- Ensure that files are processed before subdirectories (e.g., a file starting with 001, before a subdirectory with 001).
- Create an option to create a CSV file with all requirements for all document types.
