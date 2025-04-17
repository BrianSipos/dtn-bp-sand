# BPv7 Secure Advertisement and Neighborhood Discovery (SAND)

The internet-draft is tracked as [draft-ietf-dtn-bp-sand](https://datatracker.ietf.org/doc/draft-ietf-dtn-bp-sand/).

A local build of the current main branch is available [draft-ietf-dtn-bp-sand.html](https://briansipos.github.io/dtn-bp-sand/draft-ietf-dtn-bp-sand.html).
A difference from the datatracker draft and this local version can be [viewed side-by-side](https://author-tools.ietf.org/diff?doc_1=draft-ietf-dtn-bp-sand&url_2=https://briansipos.github.io/dtn-bp-sand/draft-ietf-dtn-bp-sand.txt&raw=1).

Prerequisites to building can be installed on Ubuntu with:
```
sudo apt-get install -y cmake python3 python3-pip python3-setuptools python3-wheel ruby xmlstarlet aspell cargo
pip3 install xml2rfc abnf
sudo gem install cbor-diag
sudo cargo install --root /usr/local cddl
```

Then the document can be built with
```
cmake -S . -B build/default
cmake --build build/default
```

# Demo Implementation

The demo agent is in a separate project [dtn-demo-agent](https://github.com/BSipos-RKF/dtn-demo-agent).

# Wireshark Protocols and Dissectors

The wireshark modules are in a separate project [dtn-wireshark](https://github.com/BSipos-RKF/dtn-wireshark).
