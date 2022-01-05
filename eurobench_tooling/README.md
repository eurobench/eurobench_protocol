# Eurobench tooling

2 tools are implemented.
Mainly for internal use

* `check_template`: sanity check on the information associated to a protocol.
  Verify the consistency of some elements set in the yaml file
* `check_synchro`: verify if dev and eurbench repo are synchro, and if the latest committed version has a tag

## Installation

To be launched from the upper directory

```term
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -e eurobench_tooling
```

## Usage

```term
# to launch check_template, the yaml file to check is to be provided as parameter
check_template data/pepato.yaml
# check_synchro uses default config of urls located in config file
# not that accessing some repos may require a ssh access configured on the machine
check_synchro
```