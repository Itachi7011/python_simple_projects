# Security Policy

## Scope

This repository contains local, offline Python CLI scripts with no network calls, no external API keys, and no backend. `Password_Generator.py` generates passwords locally and does not transmit or store them anywhere. The realistic attack surface is limited to issues within an individual script's logic (e.g. a genuinely weak randomness source, if ever changed).

## Reporting a Vulnerability

If you discover a security issue (for example, a weakness in `Password_Generator.py`'s randomness), please report it privately rather than opening a public issue:

- Open a [GitHub Security Advisory](../../security/advisories/new) for this repository, **or**
- Contact the maintainer directly via the contact information on the maintainer's GitHub profile.

Please include a description of the issue, the affected script, and steps to reproduce.

## Response

This is a small, actively-maintained personal/open-source project. Reports will be acknowledged on a best-effort basis; there is no formal SLA.

## Supported Versions

There are no versioned releases; the `main` branch is always the supported version.
