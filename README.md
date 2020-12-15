# Eurobench protocols

Re-transcription of the Protocol template sheet into YAML structure.

Objective of such structure:

* Perform systematic checking of the information
* Enable more automatic protocol insertion in the database

## Scripting functionality

Check [eurobench_tooling/README.md](eurobench_tooling/README.md).

## Advancement

[General template sheet](https://drive.google.com/drive/u/0/folders/186_p3bJVd_ugNNAe3cgfW72ZDYCC8oIy)

### Embedded in database

### Ready to be tested in database

* **madrob**:
  * [code](https://github.com/madrob-beast/madrob_beast_pi)
  * docker:
  * [yaml](data/madrob.yaml)
  * [github repo](https://github.com/eurobench/pi_madrob_beast)
  * [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_madrob_beast)
  * [excel](https://docs.google.com/spreadsheets/d/1-PaNEjkP6uf4XaTbmNykUySV5ok0mSn_/edit#gid=439895919)
  * current state: ready for database trial

* **beat**:
  * [code](https://github.com/aremazeilles/beat_routine)
  * [github repo](https://github.com/eurobench/pi_beat)
  * [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_beat)
  * [yaml](data/beat.yaml):
  * [excel](https://docs.google.com/spreadsheets/d/16fQ5ReesRFfUHpOVV2ekaKSuec2XO0-H/edit?rtpof=true)
  * current state: waiting for PI output adjustment in code.

* **bullet**:
  * [code](https://github.com/eurobench/pi_bullet)
  * [yaml](data/bullet.yaml)
  * excels:
    * [walking](https://docs.google.com/spreadsheets/d/1BPKyCwdTW-pmccuSc34m4ZglnibAZeu4/edit#gid=766575927)
    * [walking_complete](https://docs.google.com/spreadsheets/d/1rAJXqnzodYghTHCIcKvOM6r8MwtHygkn/edit#gid=716373661)
  * current state: ready for database trial

* **bestable**:
  * [code](https://gitlab.com/matjazzadravec/bestable-platform-codes)
  * [excel](https://docs.google.com/spreadsheets/d/1s25AMTL7PYxhq8h4dv4UFB7Mkbr5oJsI/edit#gid=2118535745)
  * [yaml](data/bestable.yaml)
  * [github repo](https://github.com/eurobench/pi_bestable)
  * [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_bestable)
  * Mising:
    * official template file to be adjusted with the PI excel present in the code repo.
    * some words about the data collected file
    * double check docker entry in yaml

### Under progress

* **beast**:
  * [code](https://docs.google.com/spreadsheets/d/1Wp9QYMm_V1tOCheF185pOYPcIm9yt6AU/edit?rtpof=true)
  * docker:
  * yaml:
  * excel:
  * current state: waiting for reference data set

* **tested**
  * [code](https://github.com/jamatics/pi_ctag)
  * docker
  * [yaml](data/tested.yaml)
  * [excel](https://docs.google.com/spreadsheets/d/1N8o89BSfUftSgnNhfLfsSkG39G1vy0Ej/edit#gid=714596252)
  * current state: PR on updated CI process.
    Open discussion on PI Algo structure.

* **pepato**:
  * [code](https://github.com/dzhvansky/pepato/tree/octave_version)
  * [template](https://docs.google.com/spreadsheets/d/19HB6j2O9O_58Vs_J8xOiOlo_4o82bRgQ/edit?rtpof=true#gid=1199258036)
  * private repo
  * pending on:
    * check the change of parameters, as mentioned in [this post](https://github.com/dzhvansky/pepato/issues/1#issuecomment-685111620)
    * asked to have an explicit naming of the input files.
  * Request to create public repo as well (or maintain it private?)
  * yaml file to be finished.

### Not (really) started
