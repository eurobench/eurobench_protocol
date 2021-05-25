# Eurobench protocols

Re-transcription of the Protocol template sheet into YAML structure, for easing the insertion into the Eurobench Database

Objective of such structure:

* Perform systematic checking of the information collected
* Enable more automatic protocol insertion in the database

Relevant links:

* [eurobench documentation](https://github.com/aremazeilles/eurobench_documentation)
* [github eurobench](https://github.com/orgs/eurobench)
* [Generic template sheet](https://eurobench.github.io/sofware_documentation/latest/_attachments/protocol_template.xlsx)
## Scripting functionality

Check [eurobench_tooling/README.md](eurobench_tooling/README.md).

## Code integration status

The hyperlinks refer to:

* `code`: the code repository owned by the test-bed developers
* `Eurobench repo`: fork of the code repository, managed by Eurobench (for deployment purposes)
* `docker`: link to the docker image of the code, to be used by the Eurobench server
* `excel`: protocol description, following the Eurobench template
* `yaml`: re-transcription of the excel sheet in computed-friendly format to ease insertion in database.

### Embedded in database

* **madrob**:
  * [code](https://github.com/madrob-beast/madrob_beast_pi),
    [Eurobench repo](https://github.com/eurobench/pi_madrob_beast),
    [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_madrob_beast),
    [excel](data/madrob/madrob-v4.0.xlsx),
    [yaml](data/madrob/madrob.yaml)
  * Missing: indication on data collected files.
  * A protocol: [Madrob: using a door](http://15.237.22.1/protocols/info/52)
  * documentation: NO pdf available. Available from the github repo. Image available 

* **bestable**:
  * [code](https://gitlab.com/matjazzadravec/bestable-platform-codes),
    [Eurobench repo](https://github.com/eurobench/pi_bestable),
    [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_bestable),
    [excel](data/bestable/bestable.xlsx),
    [yaml](data/bestable/bestable.yaml),
    [data_set](https://gitlab.com/matjazzadravec/bestable-platform-manual/-/tree/master)
  * integrated: 1 protocol: [Bestable: Visually-cued stepping perturbations on a treadmill](http://15.237.22.1/protocols/info/53). Manual uploaded.


* **udbenchmarking**:
  * [code](https://github.com/nickkluft/udbenchmark_PIs),
    [Eurobench repo](https://github.com/eurobench/pi_udbenchmark),
    [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_udbenchmark),
    [template](data/udbenchmarking/udbenchmarking.xlsx),
    [yaml](data/udbenchmark.yaml)
  * integrated: 2 protocols
    * [UDBenchmarking - "Walking on Slopes"](http://15.237.22.1/protocols/info/50)
    * [Walking on an inclined treadmill](http://15.237.22.1/protocols/info/54)
    * No manual uploaded. **File received, pending on insertion**.

* **bullet**:
  * [Eurobench repo](https://github.com/eurobench/pi_bullet),
    [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_bullet)
  * excels:
    * [walking](data/bullet/bullet_walking.xlsx)
    * [walking_complete](data/bullet/bullet_walkingComplete.xlsx)
  * [yaml](data/bullet.yaml),
  * discussion opened on the inter-intra aggregation
  * documentation: 

* **bench**:
  * [code](https://bitbucket.org/sophiaanais/benchproject_code/src),
    [Eurobench_repo](https://github.com/eurobench/pi_bench),
    [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_bench),
    [template](data/bench/bench.xlsx),
    [yaml](data/bench.yaml)
  * Discussion on the input data (calib file per user, not in the current options)
  * documentation: 

* **pepato**:
  * [code](https://github.com/dzhvansky/pepato/tree/octave_version),
    [Eurobench_repo](https://github.com/eurobench/pi_pepato),
    [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_pepato),
    [template](data/pepato/pepato.xlsx),
    [yaml](data/pepato.yaml),
    [dataset](https://yadi.sk/d/QMXiTgsKDC8-Zw)
  * documentation: to be asked.

* **experience**:
  * [code](https://github.com/FraCampus/EXPERIENCE),
    [template](data/experience/experience.xlsx),
    [yaml](data/experience.yaml)
  * current state:
    * **Matlab**, with specific licences. Not likely to be Octave compatible
    * Information about the protocols can be consulted but the algorithms are not callable at this moment.
  * documentation: provided by emails. To be uploaded.
  * implemented field set to False

### Ready to be tested for insertion in database

* **beat**:
  * [code](https://github.com/aremazeilles/beat_routine),
    [Eurobench repo](https://github.com/eurobench/pi_beat),
    [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_beat),
    [excel](data/beat/beat-v4.3.xlsx)
    [yaml](data/beat.yaml),
  * current state: waiting for PI output adjustment in code.
    * CI process failing due to csv linting issue

* **tested**:
  * [code](https://github.com/jamatics/pi_ctag),
    [Eurobench code](https://github.com/eurobench/pi_ctag),
    [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_ctag),
    [excel](data/tested/tested.xlsx),
    [yaml](data/tested.yaml)
  * current state:
    * ready to be tested?

* **benchbalance**:
  * [code](https://github.com/FraCampus/PI_BenchBalance),
    [template](data/benchbalance/benchbalance.xlsx)
    [yaml](data/benchbalance.yaml)
  * current state:
    * **Matlab** code, not likely to be Octave-compatible
    * would be in good shape

### Under progress

* **beast**:
  * [code](https://github.com/madrob-beast/madrob_beast_pi),
    [github repo](https://github.com/eurobench/pi_madrob_beast),
    [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_madrob_beast),
    [excel](data/beast/beast-v3.xlsx),
    [yaml](data/beast.yaml)
  * current state: waiting for reference data set

* **csic irregular terrain**:
  * [code](https://github.com/AdrianaTorres/Irregular_Terrains),
    [Eurobench fork](https://github.com/eurobench/pi_csic_irregular),
    [docker](https://hub.docker.com/r/eurobenchtest/pi_csic_irregular),
    [template](data/csic-irregular/csic-irregular-terrain.xlsx),
    [yaml](data/csic_irregular.yaml)
  * current state (26/01):
    * verify input data file
    * data collection check
    * excel sheet check

### Very early stage

* **dysturbance**
  * [code](https://github.com/CentroEPiaggio/dysturbance),
    [template](data/dysturbance/dysturbance.xlsx)
  * current state:
    * 01/12: PI code provided
    * 09/12: opened a set of question to start the integration process
    * matlab code, far from the requested format.
    * 22/12: working on a code revision.

* **forecast**:
  * [code](https://gitlab.com/altairLab/elasticteam/SESim)
    * other source: https://gitlab.com/altairLab/elasticteam/forecastnucleoframework
  * [template](data/forecast/forecast.xlsx)
  * current state:
    * Matlab code. Not likely to be Octave-compatible.
    * Not following the global spirit for metric computation.

* **comtest**:
  * [code](https://github.com/VittorioFreiburg/COMTEST),
    [template](data/comtest/comtest_v5.xlsx)
  * octave code. Still requires significant afjustment.
  * current state:
    * ping 19/02

* **stepByStep**
  * [old code](https://github.com/Nic31894/EUROBENCH_STEPbySTEP_repo),
    [code](https://github.com/STEPbySTEPproj/Protocol_biomechanics),
    [second repo](https://github.com/STEPbySTEPproj/HF_metrics)
    [template](data/stepByStep/stepByStep.xlsx),
    [yaml](data/stepByStep.yaml)
  * current state:
    * code only covering the biomechanics protocol.
    * first version of HF metrics.
    * Other are still missing

* **csic manipulation**:
  * [code](https://github.com/AdrianaTorres/Manipulation),
    [template](data/csic-manipulation/csic-manipulation.xlsx)
  * current state:
    * 22/12: very early stage.

* **uhei**:
  * [old code](https://gitlab.com/orb-benchmarking/eb_walkingpi)
  * [new code](https://gitlab.com/orb-benchmarking/eb_hum_bench)
  * no Excel sheet available
  * 25/03: repo changed, waiting for call example and input files.

* **rrd**:
  * [code](https://github.com/eurobench/rrd_pi_slope)
