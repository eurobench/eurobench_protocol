# Eurobench protocols

Re-transcription of the Protocol template sheet into YAML structure.

Objective of such structure:

* Perform systematic checking of the information
* Enable more automatic protocol insertion in the database

* [eurobench documentation](https://github.com/aremazeilles/eurobench_documentation)
* [github eurobench](https://github.com/orgs/eurobench)

## Scripting functionality

Check [eurobench_tooling/README.md](eurobench_tooling/README.md).

## Advancement

[General template sheet](https://drive.google.com/drive/u/0/folders/186_p3bJVd_ugNNAe3cgfW72ZDYCC8oIy)

### Embedded in database

* **madrob**:
  * [code](https://github.com/madrob-beast/madrob_beast_pi),
    [yaml](data/madrob.yaml),
    [github repo](https://github.com/eurobench/pi_madrob_beast),
    [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_madrob_beast),
    [excel](https://docs.google.com/spreadsheets/d/1-PaNEjkP6uf4XaTbmNykUySV5ok0mSn_/edit#gid=439895919)

* **bestable**:
  * [code](https://gitlab.com/matjazzadravec/bestable-platform-codes),
    [excel](https://docs.google.com/spreadsheets/d/1s25AMTL7PYxhq8h4dv4UFB7Mkbr5oJsI/edit#gid=2118535745),
    [yaml](data/bestable.yaml),
    [github repo](https://github.com/eurobench/pi_bestable),
    [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_bestable),
    [data_set](https://gitlab.com/matjazzadravec/bestable-platform-manual/-/tree/master),
  * Missing:
    * official template file to be adjusted with the PI excel present in the code repo.
    * some words about the data collected file
    * double check docker entry in yaml
### Ready to be tested in database

* **beat**:
  * [code](https://github.com/aremazeilles/beat_routine),
    [github repo](https://github.com/eurobench/pi_beat),
    [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_beat),
    [yaml](data/beat.yaml),
    [excel](https://docs.google.com/spreadsheets/d/16fQ5ReesRFfUHpOVV2ekaKSuec2XO0-H/edit?rtpof=true)
  * current state: waiting for PI output adjustment in code.

* **bullet**:
  * [code](https://github.com/eurobench/pi_bullet),
    [yaml](data/bullet.yaml),
    [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_bullet)
  * excels:
    * [walking](https://docs.google.com/spreadsheets/d/1BPKyCwdTW-pmccuSc34m4ZglnibAZeu4/edit#gid=766575927)
    * [walking_complete](https://docs.google.com/spreadsheets/d/1rAJXqnzodYghTHCIcKvOM6r8MwtHygkn/edit#gid=716373661)
  * current state: ready for database trial
  * discussion opened on the inter-intra aggregation


### Under progress

* **beast**:
  * [code](https://docs.google.com/spreadsheets/d/1Wp9QYMm_V1tOCheF185pOYPcIm9yt6AU/edit?rtpof=true),
    [yaml](data/beast.yaml),
    [github repo](https://github.com/eurobench/pi_madrob_beast),
    [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_madrob_beast),
    [excel](https://docs.google.com/spreadsheets/d/16fQ5ReesRFfUHpOVV2ekaKSuec2XO0-H/edit?rtpof=true)
  * current state: waiting for reference data set

* **tested**:
  * [code](https://github.com/jamatics/pi_ctag),
    [yaml](data/tested.yaml),
    [excel](https://docs.google.com/spreadsheets/d/1N8o89BSfUftSgnNhfLfsSkG39G1vy0Ej/edit#gid=714596252),
    [fork](https://github.com/eurobench/pi_ctag),
    [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_ctag)
  * current state:
    * Maybe still discussion on data format?
    * Answer received the 20/11.
      Answered back the 23/11
    * PR on latest CI process
    * Open discussion on PI Algo structure.
    * Eurobench repo created, with access secret to docker hub.
      Waiting for CI process PR merging

* **pepato**:
  * [code](https://github.com/dzhvansky/pepato/tree/octave_version),
    [template](https://docs.google.com/spreadsheets/d/19HB6j2O9O_58Vs_J8xOiOlo_4o82bRgQ/edit?rtpof=true#gid=1199258036),
    [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_pepato),
    [github_repo](https://github.com/eurobench/pi_pepato),
  * pending on:
    * check the change of parameters, as mentioned in [this post](https://github.com/dzhvansky/pepato/issues/1#issuecomment-685111620)
    * asked to have an explicit naming of the input files.
  * all PI not described
  * check if input file should be `speed2kmh_emg`, or `emg_speed2kmh`.

* **bench**:
  * [code](https://bitbucket.org/sophiaanais/benchproject_code/src),
    [template](https://docs.google.com/spreadsheets/d/1aWFmSCAFN7uPAP6EE4EbTqAzXHEhEsBR/edit#gid=1429738760),
    [yaml](data/bench.yaml)
  * docker: **not yet**
  * pending on:
    * github repo creation
    * discussion on the input data (calib file per user, not in the current options)
    * Issues on output format consistency (excel vs test data)

* **udbenchmarking**:
  * [code](https://github.com/nickkluft/udbenchmark_PIs),
    [template](https://docs.google.com/spreadsheets/d/1-RljxtIx78AwL1OhIunS7IkDdmNun782/edit?rtpof=true),
    [yaml](data/udbenchmark.yaml),
    [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_udbenchmark),
    [github clone](https://github.com/eurobench/pi_udbenchmark)

  * current state:
    * PR on CI update (unclear issue with csvlint?)
    * Check template content (missing PI)
    * deploy release.

* **csic irregular terrain**:
  * [code](https://github.com/AdrianaTorres/Irregular_Terrains),
    [template](https://docs.google.com/spreadsheets/d/15D-Y3-Ww13DznaztmUy-Gm7DIwyBc2RrfWgHs92U84U/edit#gid=2119968338)
  * current state:
    * begining
    * 11/12: sent a set of issues (Nan results
### Not (really) started

* **dysturbance**
  * [code](https://github.com/CentroEPiaggio/dysturbance),
    [template](https://docs.google.com/spreadsheets/d/1KVN53LgOVEf6wXLv6P1bwBZ2TTyM6KCT/edit#gid=1128053105)
  * current state:
    * 01/12: PI code provided
    * 09/12: opened a set of question to start the work with them
    * matlab code, far from the requested format.
    * 17/12: ping

* **benchbalance**:
  * [code](https://github.com/FraCampus/PI_BenchBalance),
    [template](https://docs.google.com/spreadsheets/d/1zSQMW6GKx8NKQQa3OtJadAOLG2MImqWH/edit?rtpof=true#gid=205650062)
  * current state:
    * ping sent on the 02/11
    * new ping 17/11
    * Answered the 19/11.
      Should conduct experiment the we of the 23
    * Ping sent the 11/12/2020

* **forecast**:
  * [code](https://gitlab.com/altairLab/elasticteam/SESim)
    * other source: https://gitlab.com/altairLab/elasticteam/forecastnucleoframework
  * [template](https://docs.google.com/spreadsheets/d/1uUrcksjbLyCbvQSyDyrYa8tyZdJtafJD/edit?rtpof=true#gid=236233280)
  * current state:
    * ping the 02/11
    * ping the 17/11
    * Missing reference data that could be used for testing the code.
      Asked since 02/10
    * Answer received on the 21/11
    * Matlab code. Likely to require Matlab for computation.
    * Not following the global spirit for metric computation.

* **comtest**:
  * [code](https://github.com/VittorioFreiburg/COMTEST),
    [template](https://docs.google.com/spreadsheets/d/1pNnTnDbOIPU1YKuLAcdEWkCqQlhmGoV5/edit?rtpof=true)
  * octave code.
  * current state:
    * no started yet
    * 17/11: sent an email.
    * 18/11: received an answer.
      Info should come around the 28/11
    * Sent a ping the 11/12
    * 14/12: not yet ready

* **stepByStep**
  * [code](https://github.com/Nic31894/EUROBENCH_STEPbySTEP_repo),
    [template](https://docs.google.com/spreadsheets/d/1h962eXf1NHLEpMpGme9hqomxpiUZnLzS/edit?rtpof=true)
  * current state:
    * not started. Code to be separated from other documentation

* **experience**:
  * [code](https://github.com/FraCampus/EXPERIENCE),
    [template](https://docs.google.com/spreadsheets/d/14sFKjz1v2VXwnMLnJ3QaYyyK4dCqby7x/edit?rtpof=true#gid=1998009330)
  * current state:
    * require special licenses of Matlab
    * should resume the analysis, even if the code is not launched yet.

* **csic manipulation**:
  * [code](https://github.com/AdrianaTorres/Manipulation),
    [template](https://docs.google.com/spreadsheets/d/1yNLcaj91ECUWv9wxQz-sFBWKsg0A_OPaPxXvauqpyew/edit)
  * current state:
    * not started
