# Make demo closer to production

- [ ] [Add PMA to mariadb](https://mariadb.com/docs/server/clients-and-utilities/graphical-and-enhanced-clients/phpmyadmin)
- [ ] Generate random password for database

# demo using PQC certificate

- [PQC nginx](https://hub.docker.com/r/openquantumsafe/nginx)
- [PQC curl](https://hub.docker.com/r/openquantumsafe/curl)
- [PQC OpenSSL](https://github.com/open-quantum-safe/oqs-provider/)
  - to read certificate and keys manually

# EJBCA scripting

- [ ] Automate with [EJBCA REST API](https://www.ejbca.org/case/automated-certificate-issuing-via-ejbca-rest/)
  - Makes demo more easily reproducible

# Hybrid Certificates

- [ ] Create a demo of hybrid certificate between PQC and non-PQC
- [ ] Follow [EJBCA hybrid CA guide](https://docs.keyfactor.com/ejbca/latest/hybrid-ca)

NOTE: The proposal for [Multiple Public-Key Algorithm X.509 Certificates](https://datatracker.ietf.org/doc/draft-truskovsky-lamps-pq-hybrid-x509/)
is not being pursued because the same functionality is already covered by [ITU-T X509 (10/2019)](https://www.itu.int/ITU-T/recommendations/rec.aspx?rec=X.509).

