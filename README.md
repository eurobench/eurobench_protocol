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
2 scripts are implemented.
`check_template` makes a sanity check on the yaml information.
`check_synchro` compares commits in the dev and eurobench fork of all PI repositories.

## General view on embedded protocols

### Wearable

| Name | Who | protocol uploaded  | PI uploaded |
| ---- | --- | ------------------ | ----------- |
| Walking/Standing on a moving surface | [beat](#beat) | 7 | yes |
| Walking on treadmill | [Bestable](#bestable) and treadmill | 1 | yes |
| Walking with crutches | [Bullet](#bullet) | 2 (missing pdf) | yes |
| Ascending/Descending slopes | Eurobench [UDBenchmark](#udbenchmarking) | 2 | yes |
| Kinematics of inclined walking of non-impared individuals | [RRD](#rrd) | 1 | yes |
| Characterization of the effects of the exoskeleton over muscle coordination | [Pepato](#pepato) | 1 | yes |
| Moving in narrow spaces | [tested](#tested) | 3 (no pdf) | yes |
| Opening closing doors | Eurobench-CSIC | 0
| Overcoming obstacles | Eurobench-CSIC | 0
| Straight walking | Eurobench-CSIC | 0
| Ascending/Descending stairs | [stepByStep](#stepByStep) |  6 of 7 | yes |
| Kinematics of stair walking of non-impared individuals | [RRD](#rrd) | 1 | yes |
| Sit-to-Stand, Stand-to-Sit | [Bench](#bench) | 2 | yes |
| Walking/Standing during pushes | [benchbalance](#benchbalance) | 1 | yes |
| Standing during manipulation | [Eurobench-CSIC](#csic_manipulation) | 2 | under dev |
| Walking over irregular terrains | [Eurobench-CSIC](#csic_irregular_terrain) | 1 | yes
| Characterization of user experience during exoskeleton-assisted walking | [Experience](#experience) | 2 | yes
| Robot Actuation characterization system | Forecast | under progress | **no**

### Humanoid

| Name | Who | protocol uploaded  | PI uploaded |
| ---- | --- | ------------------ | ----------- |
| Pushing a shopping trolley or walker	| [BEAST](#beast) | 1 | yes |
| Opening/Closing doors	Madrob | [madrob](#madrob) | 1 | yes |
| Walking on flat ground |[Eurobench-UHEI](#uhei) | 1 | yes |
| Sit-to-Stand, Stand-to-Sit| [Eurobench-UHEI](#uhei) | 2 | yes |
| Ascending/Descending slopes | [Eurobench-UHEI](#uhei) | 3 | yes |
| Ascending/Descending stairs | [Eurobench-Waterloo](#waterloo) | 5 | yes |
| Walking over irregular terrains | [Eurobench-PAL](#pal) | 3 |  **no** |
| Walking over soft terrains | *discarded* |||
| Overcoming obstacles | [Eurobench-PAL](#pal) | 3 | **no** |
| Standing during manipulation | [Eurobench-Waterloo](#waterloo) | 3 |  **no** |
| Picking and carrying objects | [Eurobench-Waterloo](#waterloo) | 4 | yes |
| Walking on a treadmill | [Eurobench-IIT and Treadmill](#iit) | 3 | yes  |
| Walking on laterally inclined surfaces | [Eurobench-IIT](#iit) | 1 | yes |
| Moving in narrow spaces	| discarded
| Standing on a moving surface | [COMTEST](#comtest) | 3 | yes |
| Walking/Standing during pushes | [Dysturbance](#dysturbance) | 4 | yes |

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
  [yaml](data/bench.yaml),
  [manual](data/bench/manual)
* Discussion on the input data (calib file per user, not in the current options)
* Integrated 2 protocols:
  * [5 sit to stand](https://platform.eurobench2020.eu/protocols/info/57)
  * [30 seconds sit to stand](https://platform.eurobench2020.eu/protocols/info/58)
  * manual uploaded

#### bestable

* [code](https://gitlab.com/matjazzadravec/bestable-platform-codes),
  [Eurobench repo](https://github.com/eurobench/pi_bestable),
  [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_bestable),
  [excel](data/bestable/bestable.xlsx),
  [yaml](data/bestable/bestable.yaml),
  [data_set](https://gitlab.com/matjazzadravec/bestable-platform-manual/-/tree/master)
  [manual](data/bestable/doc/BeStable_Manual_V5.pdf)
* integrated:
  * 1 protocol: [Bestable: Visually-cued stepping perturbations on a treadmill](https://platform.eurobench2020.eu/protocols/info/53).
  * Manual uploaded.

#### bullet

* [Eurobench repo](https://github.com/eurobench/pi_bullet),
  [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_bullet),
  [yaml](data/bullet.yaml),
* excels:
  * [walking](data/bullet/bullet_walking.xlsx)
  * [walking_complete](data/bullet/bullet_walkingComplete.xlsx)
* discussion opened on the inter-intra aggregation
* Integrated:
  * 2 protocols, **no pdf available**
    * [Walking on straight lines with instrumented crutches](https://platform.eurobench2020.eu/protocols/info/55)
    * [Walking on straight lines with instrumented crutches, mocap and force platforms](https://platform.eurobench2020.eu/protocols/info/56)

#### csic_irregular_terrain

* [code](https://github.com/AdrianaTorres/Irregular_Terrains),
  [Eurobench fork](https://github.com/eurobench/pi_csic_irregular),
  [docker](https://hub.docker.com/r/eurobenchtest/pi_csic_irregular),
  [template](data/csic-irregular/csic-irregular-terrains.xlsx),
  [yaml](data/csic_irregular.yaml),
  [manual](data/csic-irregular/manual)
* current state (26/01):
  * various issue opened, but the docker image is uploaded
* integrated: 1 protocol.
  * [Walking over irregular terrains](https://15.237.22.1/protocols/info/51)
  * manual uploaded.

#### madrob

* [code](https://github.com/madrob-beast/madrob_beast_pi),
  [Eurobench repo](https://github.com/eurobench/pi_madrob_beast),
  [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_madrob_beast),
  [excel](data/madrob/madrob-v4.0.xlsx),
  [yaml](data/madrob/madrob.yaml),
  [manual](data/madrob/manual/Detailed_Description_of_MADROB_Protocol_and_Performance_Indicators.pdf)
* Missing: indication on data collected files.
* A protocol: [Madrob: using a door](https://platform.eurobench2020.eu/protocols/info/52)
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
  * [Walking on a treadmill at 3 speeds](https://platform.eurobench2020.eu/protocols/info/59)

#### rrd

* [code](https://github.com/eurobench/rrd_pi_slope),
* current state: pending on validating the Docker images
* integrated protocol:
  * [Kinematics of stair walking of non-impared individuals](https://15.237.22.1/protocols/info/71)
  * [Kinematics of inclined walking of non-impared individuals](https://15.237.22.1/protocols/info/70)
  * PDF uploaded.

#### udbenchmarking

* [code](https://github.com/nickkluft/udbenchmark_PIs),
  [Eurobench repo](https://github.com/eurobench/pi_udbenchmark),
  [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_udbenchmark),
  [template](data/udbenchmarking/udbenchmarking.xlsx),
  [yaml](data/udbenchmark.yaml),
  [manual](data/udbenchmarking/doc/1.Protocol.pdf)
* integrated: 2 protocols
  * [UDBenchmarking - "Walking on Slopes"](https://platform.eurobench2020.eu/protocols/info/50)
  * [Walking on an inclined treadmill](https://platform.eurobench2020.eu/protocols/info/54)
  * Manual uploaded.

#### experience

* [code](https://github.com/FraCampus/EXPERIENCE),
  [active fork](https://github.com/aremazeilles/EXPERIENCE),
  [template](data/experience/experience.xlsx),
  [yaml](data/experience.yaml),
  [manual](data/experience/doc/EXPERIENCE_documentation_v2_0.pdf)
* current state:
  * **Matlab**, with specific licences. Not likely to be Octave compatible
  * Information about the protocols can be consulted but the algorithms are not callable at this moment.
* implemented field set to False
* integrated: 2 protocols, documentation uploaded
  * [User-centered assessment of exoskeleton-assisted treadmill-based walking](https://platform.eurobench2020.eu/protocols/info/44)
  * [User-centered assessment of exoskeleton-assisted overground walking](https://platform.eurobench2020.eu/protocols/info/43)

#### beat

* [code](https://github.com/aremazeilles/beat_routine),
  [Eurobench repo](https://github.com/eurobench/pi_beat),
  [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_beat),
  [excel](data/beat/beat-v4.3.xlsx)
  [yaml](data/beat.yaml),
* current state: waiting for PI output adjustment in code. Pending Merge Request.
* integrated: 7 protocols, **NO PDF**
  * [Static Balance - uneven surface](https://platform.eurobench2020.eu/protocols/info/23)
  * [Step perturbation - uneven surface](https://platform.eurobench2020.eu/protocols/info/25)
  * [Static Balance - even surface](https://platform.eurobench2020.eu/protocols/info/22)
  * [Stepping on platform - uneven surface](https://platform.eurobench2020.eu/protocols/info/20)
  * [Step perturbation - even surface](https://platform.eurobench2020.eu/protocols/info/24)
  * [Stepping on place - even surface](https://platform.eurobench2020.eu/protocols/info/18)
  * [Sinusoidal perturbation - even surface](https://platform.eurobench2020.eu/protocols/info/29)

#### beast

* [code](https://github.com/madrob-beast/madrob_beast_pi),
  [github repo](https://github.com/eurobench/pi_madrob_beast),
  [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_madrob_beast),
  [excel](data/beast/beast-v3.xlsx),
  [yaml](data/beast.yaml)
* integrated: 1 protocol. No pdf, but reference to repository
  * [BEAST: operating wheeled devices. This protocol has two variants, employing two different active devices (trolley and walker)](https://platform.eurobench2020.eu/protocols/info/21)

#### benchbalance

* [code](https://github.com/FraCampus/PI_BenchBalance),
  [active fork](https://github.com/aremazeilles/PI_BenchBalance)
  [template](data/benchbalance/benchbalance.xlsx)
  [yaml](data/benchbalance.yaml)
  [manual](data/benchbalance/doc/BenchBalance_Protocol_PIs.pdf)
* current state:
  * **Matlab** code
  * uploaded as a docker image
* integrated : 1 protocol, PDF inserted
  * [BenchBalance -Perturbated balance assessment](https://platform.eurobench2020.eu/protocols/info/33)

#### tested

* [code](https://github.com/jamatics/pi_ctag),
  [Eurobench code](https://github.com/eurobench/pi_ctag),
  [docker](https://hub.docker.com/repository/docker/eurobenchtest/pi_ctag),
  [excel](data/tested/tested.xlsx),
  [yaml](data/tested.yaml)
* current state:
  * ready to be tested?
* integrated: 1 protocol, **NO PDF**
  * [TestEd - Industrial Use-Cases in Narrow Spaces](https://platform.eurobench2020.eu/protocols/info/49)

##### comtest

* [code](https://github.com/VittorioFreiburg/COMTEST),
  [eurobench repo](https://github.com/eurobench/pi_comtest),
  [template](data/comtest/comtest.xlsx),
  [yaml](data/comtest.yaml),
  [docker](https://hub.docker.com/r/eurobenchtest/pi_comtest),
  [documentation](data/comtest/comtest-manual.pdf)
* current state:
  * docker mechanism ready, image available.
* integrated: 2 protocols (to be strongly revised),
  * [COMTEST - Step 1: Transient Test](https://platform.eurobench2020.eu/protocols/info/37)
  * [COMTEST - Step 2: Response characterization on the basis of frequency response functions (FRFs) using the Pseudorandom Ternary Sequence Stimulus, PRTS.](https://platform.eurobench2020.eu/protocols/info/38)
  * TODO: 3 protocols are now defined:
    * Transient Test of Standing Balance with Moving Support Surface
    * Body Sway Response characterization with frequency response functions (FRFs) to Support Surface moving with Pseudorandom (PRTS) profile
    * Test of Standing Balance with Moving Support Surface with Sinusoidal profile

#### stepByStep

* [old code](https://github.com/Nic31894/EUROBENCH_STEPbySTEP_repo),
  [biomechanics PI](https://github.com/STEPbySTEPproj/Protocol_biomechanics),
  [HF PI](https://github.com/STEPbySTEPproj/HF_metrics),
  [emg protocol](https://github.com/STEPbySTEPproj/protocol_emg),
  [second emg protocol](https://github.com/marcokai/Protocol_EMG),
  [template](data/stepByStep/stepByStep.xlsx),
  [yaml](data/stepByStep.yaml)
  [manuals](data/stepByStep/doc/)
* current state:
  * code only covering the biomechanics protocol.
  * HF metrics implemented (dual task, lpp, uei).
* Integrated: 7 protocols:
  * [Walking on stair: biomechanical analysis](https://15.237.22.1/protocols/info/60)
  * [Walking on stairs: dual task protocol](https://15.237.22.1/protocols/info/61)
  * [Walking on stair: User Exoskeleton Interaction Observation](https://15.237.22.1/protocols/info/62)
  * [Walking on stairs: Local Perceived Pressure Questionnaire](https://15.237.22.1/protocols/info/63)

  * [Combined protocol](https://15.237.22.1/protocols/info/64)
    * **This one may not be yet functional**
  * [Walking on stairs: emg analysis](https://15.237.22.1/protocols/info/65)
  * [Walking on stairs: ground and handrail reaction forces](https://15.237.22.1/protocols/info/66)
    * **No information on this one**
  * Biomechanical protocol (60) has manual and code implemented.
  * Human factors protocols (61, 62, 63) have manual

* integrated: **NO PROTOCOL**

#### dysturbance

* [code](https://github.com/CentroEPiaggio/dysturbance),
  [template](data/dysturbance/dysturbance.xlsx),
  [yaml_file](data/dysturbance.yaml),
  [original_repo](https://github.com/CentroEPiaggio/dysturbance),
  [eurobench repo](https://github.com/eurobench/dysturbance),
  [docker image](https://hub.docker.com/repository/docker/eurobenchtest/pi_dysturbance),
* Integrated: **4 protocols for now, a 5th to be added**, **NO PDF**
  * [Dysturbance -Reaction to Impulsive Disturbance](https://platform.eurobench2020.eu/protocols/info/39)
  * [Dysturbance - Reaction to Sinusoidal Force Disturbance](https://platform.eurobench2020.eu/protocols/info/40)
  * [Dysturbance - Reaction to Sinusoidal displacement Disturbance](https://platform.eurobench2020.eu/protocols/info/41)
  * [Dysturbance - Reaction to external Quasistatic Disturbance](https://platform.eurobench2020.eu/protocols/info/40)
  * 

#### waterloo

Related to humanoid

* Protocols uploaded based on [Eurobench data](https://eurobench2020.eu/wp-content/uploads/2020/09/EUROBENCH-benchmarking-scenarios-description_v2.pdf)
* Using code provided by [uhei](#uhei) for the stair and picking scenarios
* **No code for the manipulation scenario**

* [Ascending // Descending stairs with Humanoids](data/waterloo_stairs.yaml)
  * [Ascending / Descending stairs: standardized steps](https://platform.eurobench2020.eu/protocols/info/81)
  * [Ascending / Descending stairs: endurance steps](https://platform.eurobench2020.eu/protocols/info/82)
  * [Ascending / Descending stairs: maximum step](https://platform.eurobench2020.eu/protocols/info/83)
  * [Ascending / Descending stairs: fast steps](https://platform.eurobench2020.eu/protocols/info/84)
  * [Ascending / Descending stairs: varying steps up](https://platform.eurobench2020.eu/protocols/info/85)

* [standing during manipulation](data/waterloo_manipulation.yaml)
  * [Standing during manipulation: PLace in box](https://platform.eurobench2020.eu/protocols/info/74)
  * [Standing during manipulation: Place on shelf](https://platform.eurobench2020.eu/protocols/info/75)
  * [Standing during manipulation: Max weight and height](https://platform.eurobench2020.eu/protocols/info/76)
  * **NO CODE**

* [Picking and carrying objects](data/waterloo_pick.yaml)
  * [Picking and Carrying objects: basic carrying](https://platform.eurobench2020.eu/protocols/info/77)
  * [icking and Carrying objects: increasing weight carrying](https://platform.eurobench2020.eu/protocols/info/78)
  * [Picking and Carrying objects: increasing weight at given velocity](https://platform.eurobench2020.eu/protocols/info/79)
  * [Picking and Carrying objects: endurance carrying](https://platform.eurobench2020.eu/protocols/info/80)

#### uhei

* [old code](https://gitlab.com/orb-benchmarking/eb_walkingpi),
  [new code](https://gitlab.com/orb-benchmarking/eb_hum_bench),
  [github version](https://github.com/eurobench/eb_hum_bench)
* no Excel sheet available
* 20.12.2021:
  * issue for optional parameters.
* integrated: **NO PROTOCOL details**.
  Protocols uploaded based on [Eurobench data](https://eurobench2020.eu/wp-content/uploads/2020/09/EUROBENCH-benchmarking-scenarios-description_v2.pdf)

Several yaml files handled

* [Walking on slope](data/uhei_slope.yaml)
  * [Ascending / descending slope: basic slope walking](https://platform.eurobench2020.eu/protocols/info/92)
  * [Ascending / descending slope: maximum angle](https://platform.eurobench2020.eu/protocols/info/93)
  * [Ascending / descending slope: maximum velocity](https://platform.eurobench2020.eu/protocols/info/94)
* [Flat Ground Walking](data/uhei_flat.yaml)
  * [Flat Ground walking: I3SA - Increased Step Size Stability Assessment](https://platform.eurobench2020.eu/protocols/info/67)
* [Sit to stand (Humanoid)](data/uhei_sts.yaml)
  * [Sit to stand: Decreasing chair height assessment](https://platform.eurobench2020.eu/protocols/info/68)
  * [Sit to stand: Foot Placement Handicap](https://platform.eurobench2020.eu/protocols/info/69)

#### iit

Related to humanoid

* Protocols uploaded based on [Eurobench data](https://eurobench2020.eu/wp-content/uploads/2020/09/EUROBENCH-benchmarking-scenarios-description_v2.pdf)
* Using code provided by [uhei](#uhei)
* [Walking on a treadmill](data/iit_treadmill.yaml)
  * [Long time walking on level ground](https://platform.eurobench2020.eu/protocols/info/98)
  * [Long time walking on a slope with pitch angle](https://platform.eurobench2020.eu/protocols/info/99)
  * [Long time walking on a slope with roll angle](https://platform.eurobench2020.eu/protocols/info/100)
* [Walking on laterally inclined surface](data/iit_inclined.yaml)
  * [Walking on inclined terrain](https://platform.eurobench2020.eu/protocols/info/97)


### Ready to be tested for insertion in database
### Very early stage

#### csic_manipulation

* [code](https://github.com/AdrianaTorres/Manipulation),
  [template](data/csic-manipulation/csic-manipulation.xlsx)
  [yaml](data/csic_manipulation.yaml)
* current state:
  * 22/12: very early stage.
  * 25/06: update to revise
* Contains 2 protocol
* Status:
  * under revision.


##### forecast

* [code](https://gitlab.com/altairLab/elasticteam/SESim)
  * other source: https://gitlab.com/altairLab/elasticteam/forecastnucleoframework
* [template](data/forecast/forecast.xlsx)
* current state:
  * Matlab code. Not likely to be Octave-compatible.
  * Not following the global spirit for metric computation.
* integrated: **NO PROTOCOL**

#### pal

Related to humanoid

* Irregular scenario
  * [yaml file](data/pal_irregular.yaml)
  * Contains 3 protocols
  * Status: protocols uploaded based on [Eurobench data](https://eurobench2020.eu/wp-content/uploads/2020/09/EUROBENCH-benchmarking-scenarios-description_v2.pdf)
  * **NO PROTOCOL, NO CODE**
* Overcoming obstacle
  * [yaml file](data/pal_obstacles.yaml)
  * Contains 3 protocols
  * Status: protocols uploaded based on [Eurobench data](https://eurobench2020.eu/wp-content/uploads/2020/09/EUROBENCH-benchmarking-scenarios-description_v2.pdf)
  * **NO PROTOCOL, NO CODE**


## Acknowledgements

<a href="http://eurobench2020.eu">
  <img src="http://eurobench2020.eu/wp-content/uploads/2018/06/cropped-logoweb.png"
       alt="rosin_logo" height="60" >
</a>

Supported by Eurobench - the European robotic platform for bipedal locomotion benchmarking.
More information: [Eurobench website][eurobench_website]

<img src="http://eurobench2020.eu/wp-content/uploads/2018/02/euflag.png"
     alt="eu_flag" width="100" align="left" >

This project has received funding from the European Union’s Horizon 2020
research and innovation programme under grant agreement no. 779963.

The opinions and arguments expressed reflect only the author‘s view and
reflect in no way the European Commission‘s opinions.
The European Commission is not responsible for any use that may be made
of the information it contains.

[eurobench_logo]: http://eurobench2020.eu/wp-content/uploads/2018/06/cropped-logoweb.png
[eurobench_website]: http://eurobench2020.eu "Go to website"
