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

* **beast**:
  * [code](https://docs.google.com/spreadsheets/d/1Wp9QYMm_V1tOCheF185pOYPcIm9yt6AU/edit?rtpof=true)
  * docker:
  * yaml:
  * excel:
  * current state: ready for database trial
* **beat**:
  * [code](https://docs.google.com/spreadsheets/d/16fQ5ReesRFfUHpOVV2ekaKSuec2XO0-H/edit?rtpof=true)
  * docker:
  * [yaml](data/beat.yaml):
  * excel:
  * current state: waiting for PI output adjustment in code.
* **bullet**:
  * [code](https://github.com/eurobench/pi_bullet)
  * [yaml](data/bullet.yaml)
  * excels:
    * [walking](https://docs.google.com/spreadsheets/d/1BPKyCwdTW-pmccuSc34m4ZglnibAZeu4/edit#gid=766575927)
    * [walking_complete](https://docs.google.com/spreadsheets/d/1rAJXqnzodYghTHCIcKvOM6r8MwtHygkn/edit#gid=716373661)
  * current state: ready for database trial

### Under progress

* **bestable**:
  * [code](https://gitlab.com/matjazzadravec/bestable-platform-codes)
  * [excel](https://docs.google.com/spreadsheets/d/1s25AMTL7PYxhq8h4dv4UFB7Mkbr5oJsI/edit#gid=2118535745)
  * [yaml](bestable.yaml)
  * current state: missing
    * create github repo
    * insert github process
    * all PIs not described in excel sheet

* **tested**
  * [code](https://github.com/jamatics/pi_ctag)
  * docker
  * [yaml](data/tested.yaml)
  * [excel](https://docs.google.com/spreadsheets/d/1N8o89BSfUftSgnNhfLfsSkG39G1vy0Ej/edit#gid=714596252)
  * current state: PR on updated CI process.
    Open discussion on PI Algo structure.

### Not (really) started
