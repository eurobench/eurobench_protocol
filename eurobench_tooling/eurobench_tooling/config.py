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
    'condition.yaml',
    'emg.csv',
    'event.yaml',
    'gaitEvents.yaml',
    'wrench.csv',
    'jointAngles.csv',
    'jointState.csv',
    'platformData.csv',
    'info.yaml'
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
