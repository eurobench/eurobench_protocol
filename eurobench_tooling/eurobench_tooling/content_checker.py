#!/usr/bin/env python3
"""
@package eurobench_tooling
@file content_checker.py
@author Anthony Remazeilles
@brief Tool parsing the yaml descrption of a protocol content, and make some sanity check on it

Copyright (C) 2020 Tecnalia Research and Innovation
Distributed under the Apache 2.0 license.
"""

import sys
from termcolor import colored
import os
import yaml

# spec (todo: move elswehere)
FILES_INPUT = ['event.yaml', 'wrench.csv', 'jointState.csv', 'condition.csv']


def get_algo_input(spec, verbose=True):
  if 'pi_algo' not in spec:
    return
  linput = list()
  for item in spec['pi_algo']:
    if verbose:
      print("Algo: {}".format(item['name']))
      print("  input: {}".format(item['input_files']))
    linput = linput + item['input_files']
  # remove duplicates
    linput = set(linput)
  if verbose:
    print ("All together: {}".format(linput))
  return linput

def check_input(spec):
  linput = get_algo_input(spec)

  all_ok = True
  for item in linput:
    if item not in FILES_INPUT:
      print(colored('Unknown input file: {}'.format(item), 'red'))
      all_ok = False

  return all_ok

USAGE = """usage: check_template yaml_file
yaml_file: YAML file containing the protocol description
return 0 if all good, 1 elsewise
"""

def main():
  if len(sys.argv) != 2:
      print(colored("Wrong input parameters !", "red"))
      print(colored(USAGE, "yellow"))
      return -1
  yaml_file = sys.argv[1]

  try:
    with open(yaml_file, 'r') as open_file:
      spec = yaml.load(open_file, Loader=yaml.FullLoader)
  except IOError as err:
    print(colored("IO Error: {}".format(err), 'red'))
    return 1
  except yaml.parser.ParserError as err:
    print(colored("Parsing Error detected: {}".format(err), 'red'))
    return 1

  all_ok = True

  print("check input files")
  if not check_input(spec):
    all_ok = False

  return all_ok