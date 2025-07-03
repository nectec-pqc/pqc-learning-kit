# Post-Quantum Cryptography (PQC) demo

There are two main demos:

- Creating PKI and issuing PQC certificate with EJBCA.
- Using PQC certificate.

## Creating PQC PKI

This demo is in `pki` subdirectory.

- Quantum-safe PKI is setup with [EJBCA](https://www.ejbca.org/)
- First, setup [EJBCA with docker](https://docs.keyfactor.com/ejbca/latest/tutorial-start-out-with-ejbca-docker-container)
- Next, follow guide to [create a post-quantum PKI](https://docs.keyfactor.com/ejbca/latest/tutorial-create-a-post-quantum-pki)

### Corrections

- The guide refer to "Dilithium" algorithm, but the UI uses the NIST-renamed term "ML-DSA".
  - ML-DSA-44 = Dilithium 2
  - ML-DSA-65 = Dilithium 3
  - ML-DSA-87 = Dilithium 5

## Using PQC certificates

This demo is in `usage` subdirectory.

