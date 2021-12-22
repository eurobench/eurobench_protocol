#!/usr/bin/env python3
"""
@package eurobench_tooling
@file check_synchro.py
@author Anthony Remazeilles
@brief check synchro in between repos and official Eurobench ones.

Copyright (C) 2021 Tecnalia Research and Innovation
Distributed under the Apache 2.0 license.
"""


import subprocess
import re
import argparse
import sys
# from setuptools.dist import DistDeprecationWarning
import yaml
import logging

from pkg_resources import Requirement, resource_filename
DEFAULT_CONFIG = resource_filename(Requirement.parse('eurobench_tooling'),'eurobench_tooling/config_repo.yaml')


# TODO check https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
# package mentioned for color use 
class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
format = "%(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

ch.setFormatter(CustomFormatter(format))

logger.addHandler(ch)
class SynchronizedRepository(object):
  def __init__(self):
    self.is_configured = False
    self.name = None
    self.repo_dev = None
    self.repo_eurobench = None

  def reset(self):
    self.is_configured = False
    self.name = None
    self.dev_url = None
    self.eurobench_url = None

  def init(self, dictionary):
    # checking required entry
    msg_err = ''
    require = ['name', 'dev_url', 'eurobench_url']

    for item in require:
      if item not in dictionary:
        msg_err = f'Missing entry {item} in config: {dictionary}'
        logger.error(msg_err)
        break

    if msg_err:
      return False

    self.name = dictionary['name']
    self.dev_url = dictionary['dev_url']
    self.eurobench_url = dictionary['eurobench_url']
    self.is_configured = True
    return True

def main():

  parser = argparse.ArgumentParser(description='Process a YAML Use case')
  parser.add_argument('-c', '--config',
                       help='file with all repo spec')
  parser.add_argument('-f', '--focus', help='only process indicated repo')

  args = parser.parse_args()

  if args.config is None:
    logger.info('No config file defined, using default one')
    args.config = DEFAULT_CONFIG

  logger.info(f'Loading config at {args.config}')

  try:
      with open(args.config, 'r') as open_file:
          spec = yaml.load(open_file, Loader=yaml.FullLoader)
  except IOError as err:
      logger.critical("IO Error: {}".format(err))
      return
  except yaml.parser.ParserError as err:
      logger.critical("Parsing Error detected: {}".format(err))
      return

  if 'algorithms' not in spec:
    logger.fatal('Missing algorithms key in spec file')
    return

  nb_algo = len(spec['algorithms'])
  logger.info(f'Loading {nb_algo} items')

  l_synch = list()
  for one_spec in spec['algorithms']:
    one_synch = SynchronizedRepository()
    if one_synch.init(one_spec):
      logger.info(f'Adding synch {one_synch.name}')
      l_synch.append(one_synch)
    else:
      logger.warn(f'could not load {one_spec}')

  logger.debug(f'{len(l_synch)} items loaded')


  sys.exit()
  repo_dev_url = 'git@github.com:madrob-beast/madrob_beast_pi.git'
  repo_eurob_url = 'git@github.com:eurobench/pi_madrob_beast.git'
  print('Acceding to the the dev repository')
  process = subprocess.Popen(["git", "ls-remote", repo_dev_url], stdout=subprocess.PIPE)
  stdout, stderr = process.communicate()
  sha_dev = re.split(r'\t+', stdout.decode('ascii'))[0]

  print('Acceding to the the Eurobench repo')
  process = subprocess.Popen(["git", "ls-remote", repo_eurob_url], stdout=subprocess.PIPE)
  stdout, stderr = process.communicate()
  sha_eurob = re.split(r'\t+', stdout.decode('ascii'))[0]

  if sha_dev == sha_eurob:
    print("Repo are synch")
  else:
    print("Repo are not synch")

  print('Checking the latest tag hash')
  process = subprocess.Popen(["git", "ls-remote", "--tags", repo_eurob_url], stdout=subprocess.PIPE)
  stdout, stderr = process.communicate()

  stdout = stdout.decode('ascii')
  tags = stdout.splitlines()

  last_tag_hash, last_tag = tags[-1].split('\t')
  print(f"result:{last_tag}: {last_tag_hash}")
  if last_tag_hash == sha_eurob:
    print ("Last commit is tagged version")
  else:
    print (f"Last commit {sha_eurob[0:7]} differs from tagged version {last_tag}: {last_tag_hash[0:7]}")