# Make demo closer to production

- [ ] [Add PMA to mariadb](https://mariadb.com/docs/server/clients-and-utilities/graphical-and-enhanced-clients/phpmyadmin)
- [ ] Generate random password for database

# demo using PQC certificate

- [x] [PQC nginx](https://hub.docker.com/r/openquantumsafe/nginx)
- [x] [PQC curl](https://hub.docker.com/r/openquantumsafe/curl)
- [ ] [PQC OpenSSL](https://github.com/open-quantum-safe/oqs-provider/)
  - to read certificate and keys manually

# EJBCA scripting

- [ ] Automate with [EJBCA REST API](https://www.ejbca.org/case/automated-certificate-issuing-via-ejbca-rest/)
  - Makes demo more easily reproducible

# Hybrid Certificates

- [ ] Create a demo of hybrid certificate between PQC and non-PQC
- [ ] Follow [EJBCA hybrid CA guide](https://docs.keyfactor.com/ejbca/latest/hybrid-ca)

NOTE: The proposal for [Multiple Public-Key Algorithm X.509 Certificates](https://datatracker.ietf.org/doc/draft-truskovsky-lamps-pq-hybrid-x509/)
is not being pursued because the same functionality is already covered by [ITU-T X509 (10/2019)](https://www.itu.int/ITU-T/recommendations/rec.aspx?rec=X.509).

# What are big players doing?

- https://cloud.google.com/security/resources/post-quantum-cryptography?hl=en
- https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html

# Hybrid

- https://qcve.org/blog/what-is-hybrid-post-quantum-encryption
  - [ ] **Layered** --- double encryption.
    Encrypt with PQC first, then do normal encryption on top. Everything looks
    the same to most program. But now we have quantum safe guarantee.
  - [ ] **Composite** --- key parts are negotiated using different algorithms.
    Meaning server and client has to successfully use all algorithms.
  - [ ] **Interoperable** --- choose one of possible algorithms to use.
    - Seems like chrome did. but then it changed.

# Is X25519MLKEM768 already supported?

- https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-support/

