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


## General view on embedded protocols

### Wearable

| Name | Who | protocol uploaded  | PI uploaded |
| ---- | --- | ------------------ | ----------- |
| Walking/Standing on a moving surface | [beat](#beat) | 7 | no |
| Walking on treadmill	| [Bestable](#bestable) and treadmill | 1 | yes |
| Walking with crutches	 | [Bullet](#bullet) | 2 (missing pdf) | yes |
| Ascending/Descending slopes	| Eurobench [UDBenchmark](#udbenchmarking) | 2 | yes |
| Kinematics of inclined walking of non-impared individuals | [RRD](#rrd) | 1 | yes |
| Characterization of the effects of the exoskeleton over muscle coordination	| [Pepato](#pepato) | 1 | yes |
| Moving in narrow spaces	| [tested](#tested) | 1 (no pdf) | no |
| Opening closing doors	| Eurobench-CSIC | 0
| Overcoming obstacles | Eurobench-CSIC | 0
| Straight walking | Eurobench-CSIC | 0
| Ascending/Descending stairs	| [stepByStep](#stepByStep) | 5 (under integration) | no |
| Kinematics of stair walking of non-impared individuals | [RRD](#rrd) | 1 | no |
| Sit-to-Stand, Stand-to-Sit | [Bench](#bench) | 2 (no pdf) | yes |
| Walking/Standing during pushes | [benchbalance](#benchbalance) | 1 | no |
| Standing during manipulation | Eurobench-CSIC | 0 | no
| Walking over irregular terrains | [Eurobench-CSIC](#csic_irregular_terrain) | 1 (under progress) | no
| Characterization of user experience during exoskeleton-assisted walking |	[Experience](#experience) | 2 | no
| Robot Actuation characterization system	| Forecast | under progress | no

### Humanoid

| Name | Who | protocol uploaded  | PI uploaded |
| ---- | --- | ------------------ | ----------- |
| Pushing a shopping trolley or walker	| [BEAST](#beast) | 1 | under progress |
| Opening/Closing doors	Madrob | [madrob](#madrob) | 1 | yes |
| Walking on flat ground	|Eurobench-UHEI | 1 | no |
| Sit-to-Stand, Stand-to-Sit| Eurobench-UHEI | 2 | no |
| Ascending/Descending slopes	| Eurobench-UHEI | under dev
| Ascending/Descending stairs	| Eurobench-Waterloo | under dev
| Walking over irregular terrains	| Eurobench-PAL | under dev
| Walking over soft terrains | discarded | under dev
| Overcoming obstacles | Eurobench-PAL | under dev
| Standing during manipulation | Eurobench-Waterloo | under dev
| Picking and carrying objects | Eurobench-Waterloo | under dev
| Walking on a treadmill | Eurobench-IIT and Treadmill | under dev
| Walking on laterally inclined surfaces | Eurobench-IIT | under dev
| Moving in narrow spaces	| discarded | under dev
| Standing on a moving surface | [COMTEST](#comtest) | 0 | no |
| Walking/Standing during pushes | [Dysturbance](#disturbance) | 4 | no |


## Code integration status

The hyperlinks refer to:

* `code`: the code repository owned by the test-bed developers
* `Eurobench repo`: fork of the code repository, managed by Eurobench (for deployment purposes)
* `docker`: link to the docker image of the code, to be used by the Eurobench server
* `excel`: protocol description, following the Eurobench template
* `yaml`: re-transcription of the excel sheet in computed-friendly format to ease insertion in database.

### Embedded in database

#### bench

* [code](https://bitbucket.org/sophiaanais/benchproject_code/src),
  [Eurobench_repo](https://github.com/eurobench/pi_bench),
  [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_bench),
  [template](data/bench/bench.xlsx),
  [yaml](data/bench.yaml)
* Discussion on the input data (calib file per user, not in the current options)
* Integrated 2 protocols, **NO pdf**:
  * [5 sit to stand](http://15.237.22.1/protocols/info/57)
  * [30 seconds sit to stand](http://15.237.22.1/protocols/info/58)

#### bestable

* [code](https://gitlab.com/matjazzadravec/bestable-platform-codes),
  [Eurobench repo](https://github.com/eurobench/pi_bestable),
  [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_bestable),
  [excel](data/bestable/bestable.xlsx),
  [yaml](data/bestable/bestable.yaml),
  [data_set](https://gitlab.com/matjazzadravec/bestable-platform-manual/-/tree/master)
  [manual](data/bestable/doc/BeStable_Manual_V5.pdf)
* integrated:
  * 1 protocol: [Bestable: Visually-cued stepping perturbations on a treadmill](http://15.237.22.1/protocols/info/53).
  * Manual uploaded.

#### bullet

* [Eurobench repo](https://github.com/eurobench/pi_bullet),
  [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_bullet)
* excels:
  * [walking](data/bullet/bullet_walking.xlsx)
  * [walking_complete](data/bullet/bullet_walkingComplete.xlsx)
* [yaml](data/bullet.yaml),
* discussion opened on the inter-intra aggregation
* Integrated:
  * 2 protocols, **no pdf available**
    * [Walking on straight lines with instrumented crutches](http://15.237.22.1/protocols/info/55)
    * [Walking on straight lines with instrumented crutches, mocap and force platforms](http://15.237.22.1/protocols/info/56)

#### madrob

* [code](https://github.com/madrob-beast/madrob_beast_pi),
  [Eurobench repo](https://github.com/eurobench/pi_madrob_beast),
  [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_madrob_beast),
  [excel](data/madrob/madrob-v4.0.xlsx),
  [yaml](data/madrob/madrob.yaml),
  [manual](data/madrob/manual/Detailed_Description_of_MADROB_Protocol_and_Performance_Indicators.pdf)
* Missing: indication on data collected files.
* A protocol: [Madrob: using a door](http://15.237.22.1/protocols/info/52)
* documentation: PDF available. Available from the github repo. Image available


#### pepato

* [code](https://github.com/dzhvansky/pepato/tree/octave_version),
  [Eurobench_repo](https://github.com/eurobench/pi_pepato),
  [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_pepato),
  [template](data/pepato/pepato.xlsx),
  [yaml](data/pepato.yaml),
  [dataset](https://yadi.sk/d/QMXiTgsKDC8-Zw),
  [manual](data/pepato/manual/description_PEPATO.pdf)
* integrated: 1 protocol
  * [Walking on a treadmill at 3 speeds](http://15.237.22.1/protocols/info/59)  

#### udbenchmarking

* [code](https://github.com/nickkluft/udbenchmark_PIs),
  [Eurobench repo](https://github.com/eurobench/pi_udbenchmark),
  [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_udbenchmark),
  [template](data/udbenchmarking/udbenchmarking.xlsx),
  [yaml](data/udbenchmark.yaml),
  [manual](data/udbenchmarking/doc/1.Protocol.pdf)
* integrated: 2 protocols
  * [UDBenchmarking - "Walking on Slopes"](http://15.237.22.1/protocols/info/50)
  * [Walking on an inclined treadmill](http://15.237.22.1/protocols/info/54)
  * Manual uploaded.

#### experience

* [code](https://github.com/FraCampus/EXPERIENCE),
  [template](data/experience/experience.xlsx),
  [yaml](data/experience.yaml),
  [manual](data/experience/doc/EXPERIENCE_documentation_v2_0.pdf)
* current state:
  * **Matlab**, with specific licences. Not likely to be Octave compatible
  * Information about the protocols can be consulted but the algorithms are not callable at this moment.
* implemented field set to False
* integrated: 2 protocols, documentation uploaded
  * [User-centered assessment of exoskeleton-assisted treadmill-based walking](http://15.237.22.1/protocols/info/44)
  * [User-centered assessment of exoskeleton-assisted overground walking](http://15.237.22.1/protocols/info/43)

### Ready to be tested for insertion in database

#### beat

* [code](https://github.com/aremazeilles/beat_routine),
  [Eurobench repo](https://github.com/eurobench/pi_beat),
  [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_beat),
  [excel](data/beat/beat-v4.3.xlsx)
  [yaml](data/beat.yaml),
* current state: waiting for PI output adjustment in code.
* integrated: 7 protocols, **NO PDF**
  * [Static Balance - uneven surface](http://15.237.22.1/protocols/info/23)
  * [Step perturbation - uneven surface](http://15.237.22.1/protocols/info/25)
  * [Static Balance - even surface](http://15.237.22.1/protocols/info/22)
  * [Stepping on platform - uneven surface](http://15.237.22.1/protocols/info/20)
  * [Step perturbation - even surface](http://15.237.22.1/protocols/info/24)
  * [Stepping on place - even surface](http://15.237.22.1/protocols/info/18)
  * [Sinusoidal perturbation - even surface](http://15.237.22.1/protocols/info/29)

#### tested

* [code](https://github.com/jamatics/pi_ctag),
  [Eurobench code](https://github.com/eurobench/pi_ctag),
  [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_ctag),
  [excel](data/tested/tested.xlsx),
  [yaml](data/tested.yaml)
* current state:
  * ready to be tested?
* integrated: 1 protocol, **NO PDF**
  * [TestEd - Industrial Use-Cases in Narrow Spaces](http://15.237.22.1/protocols/info/49)

#### benchbalance

* [code](https://github.com/FraCampus/PI_BenchBalance),
  [template](data/benchbalance/benchbalance.xlsx)
  [yaml](data/benchbalance.yaml)
  [manual](data/benchbalance/doc/BenchBalance_Protocol_PIs.pdf)
* current state:
  * **Matlab** code, not likely to be Octave-compatible
  * would be in good shape
* integrated : 1 protocol, PDF inserted
  * [BenchBalance -Perturbated balance assessment](http://15.237.22.1/protocols/info/33)

#### rrd

* [code](https://github.com/eurobench/rrd_pi_slope), 
* current state: pending on validating the Docker images 
* integrated protocol:
  * [Kinematics of stair walking of non-impared individuals](https://15.237.22.1/protocols/info/71)
  * [Kinematics of inclined walking of non-impared individuals](https://15.237.22.1/protocols/info/70)
  * **NO PDF**

### Under progress

#### beast

* [code](https://github.com/madrob-beast/madrob_beast_pi),
  [github repo](https://github.com/eurobench/pi_madrob_beast),
  [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_madrob_beast),
  [excel](data/beast/beast-v3.xlsx),
  [yaml](data/beast.yaml),
  [manual](data/beast/manual//Detailed_Description_of_BEAST_Protocol_and_Performance_Indicators.pdf)
* current state: waiting for reference data set
* integrated: 1 protocol, pdf uploaded
  * [BEAST: operating wheeled devices. This protocol has two variants, employing two different active devices (trolley and walker)](http://15.237.22.1/protocols/info/21)

#### csic_irregular_terrain

* [code](https://github.com/AdrianaTorres/Irregular_Terrains),
  [Eurobench fork](https://github.com/eurobench/pi_csic_irregular),
  [docker](https://hub.docker.com/r/eurobenchtest/pi_csic_irregular),
  [template](data/csic-irregular/csic-irregular-terrain.xlsx),
  [yaml](data/csic_irregular.yaml)
* current state (26/01):
  * verify input data file
  * data collection check
  * excel sheet check
* integrated: **NO PROTOCOL**

### Very early stage

#### dysturbance

* [code](https://github.com/CentroEPiaggio/dysturbance),
  [template](data/dysturbance/dysturbance.xlsx)
* current state:
  * 01/12: PI code provided
  * 09/12: opened a set of question to start the integration process
  * matlab code, far from the requested format.
  * 22/12: working on a code revision.
* Integrated: 4 protocols, **NO PDF**
  * [Dysturbance -Reaction to Impulsive Disturbance](http://15.237.22.1/protocols/info/39)
  * [Dysturbance - Reaction to Sinusoidal Force Disturbance](http://15.237.22.1/protocols/info/40)
  * [Dysturbance - Reaction to Sinusoidal displacement Disturbance](http://15.237.22.1/protocols/info/41)
  * [Dysturbance - Reaction to external Quasistatic Disturbance](http://15.237.22.1/protocols/info/40)

##### forecast

* [code](https://gitlab.com/altairLab/elasticteam/SESim)
  * other source: https://gitlab.com/altairLab/elasticteam/forecastnucleoframework
* [template](data/forecast/forecast.xlsx)
* current state:
  * Matlab code. Not likely to be Octave-compatible.
  * Not following the global spirit for metric computation.
* integrated: **NO PROTOCOL**

##### comtest

* [code](https://github.com/VittorioFreiburg/COMTEST),
  [template](data/comtest/comtest_v5.xlsx)
* octave code. Still requires significant afjustment.
* current state:
  * ping 19/02
* integrated: 2 protocols (to be strongly revised), **NO PDF**
  * [COMTEST - Step 1: Transient Test](http://15.237.22.1/protocols/info/37)
  * [COMTEST - Step 2: Response characterization on the basis of frequency response functions (FRFs) using the Pseudorandom Ternary Sequence Stimulus, PRTS.](http://15.237.22.1/protocols/info/38)

#### stepByStep

* [old code](https://github.com/Nic31894/EUROBENCH_STEPbySTEP_repo),
  [code](https://github.com/STEPbySTEPproj/Protocol_biomechanics),
  [second repo](https://github.com/STEPbySTEPproj/HF_metrics)
  [template](data/stepByStep/stepByStep.xlsx),
  [yaml](data/stepByStep.yaml)
* current state:
  * code only covering the biomechanics protocol.
  * first version of HF metrics.
  * Other are still missing
* integrated: **NO PROTOCOL**

#### csic manipulation

* [code](https://github.com/AdrianaTorres/Manipulation),
  [template](data/csic-manipulation/csic-manipulation.xlsx)
* current state:
  * 22/12: very early stage.
* integrated: **NO PROTOCOL**

#### uhei

* [old code](https://gitlab.com/orb-benchmarking/eb_walkingpi)
* [new code](https://gitlab.com/orb-benchmarking/eb_hum_bench)
* no Excel sheet available
* 25/03: repo changed, waiting for call example and input files.
* integrated: **NO PROTOCOL**
 
