#!/usr/bin/env python3

from dataclasses import dataclass
from dacite import from_dict

# see https://github.com/konradhalas/dacite

@dataclass
class EurobenchSetting:
  input_type: list
  output_type: list

config_set= {
  'input_type': [
    'angularMomentum.csv',
    'com.csv',
    'condition.yaml',
    'emg.csv',
    'event.yaml',
    'gaitEvents.yaml',
    'inertiaTensor.csv',
    'info.yaml',
    'jointAngles.csv',
    'jointState.csv',
    'jointTrajectories.csv',
    'platformData.csv',
    'wrench.csv'
  ],
  'output_type': [
    'scalar',
    'vector',
    'matrix',
    'vector_of_vector',
    'vector_of_matrix'
  ]
}

EurobenchConfig = from_dict(data_class=EurobenchSetting, data=config_set)
