# BPv7 Secure Advertisement and Neighborhood Discovery

The internet-draft is tracked as [draft-sipos-dtn-bp-sand](https://datatracker.ietf.org/doc/draft-sipos-dtn-bp-sand/).

A local build of the current main branch is available [draft-sipos-dtn-bp-sand.html](https://briansipos.github.io/dtn-neighbor-msg/draft-sipos-dtn-bp-sand.html).
A difference from the datatracker draft and this local version can be [viewed side-by-side](https://author-tools.ietf.org/diff?doc_1=draft-sipos-dtn-bp-sand&url_2=https://briansipos.github.io/dtn-neighbor-msg/draft-sipos-dtn-bp-sand.txt&raw=1).

Prerequisites to building can be installed on Ubuntu with:
```
sudo apt-get install -y install aspell cmake python3 python3-pip python3-setuptools python3-wheel cargo xmlstarlet
sudo pip3 install xml2rfc
cargo install cddl
export PATH=$PATH:~/.cargo/bin
```
and then the document can be built with
```
cmake -S . -B build
cmake --build build
```

# Demo Convergence Layer Agent

The demo agent is in a separate project [dtn-demo-agent](https://github.com/BSipos-RKF/dtn-demo-agent).

# Wireshark Protocols and Dissectors

The wireshark modules are in a separate project [dtn-wireshark](https://github.com/BSipos-RKF/dtn-wireshark).
