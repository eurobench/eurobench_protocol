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

    if self.name is None or self.dev_url is None or self.eurobench_url is None:
      logger.error('undefined entry: ')
      logger.error(self.__dict__)
      return False
    return True

  def check_synchro(self):
    if not self.is_configured:
      logger.error('item not configured')
      return False

    logger.debug(f'Acceding to the dev repository: {self.dev_url}')
    process = subprocess.Popen(["git", "ls-remote", self.dev_url],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
    stdout, stderr = process.communicate()
    # sha_dev = re.split(r'\t+', stdout.decode('ascii'))[0]
    sha_dev = re.split(r'\t+', stdout)[0]

    if process.returncode != 0:
      logger.error(f'Access to dev repository error({self.dev_url})')
      logger.error(f'{stderr}')
      return False
    # logger.error(f'return code: {process.returncode}')

    # logger.info(stdout)
    # logger.info(stderr)

    logger.debug(f'Acceding to the the Eurobench repo: {self.eurobench_url}')
    process = subprocess.Popen(["git", "ls-remote", self.eurobench_url],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
      logger.error(f'Access to dev repository error({self.eurobench_url})')
      logger.error(f'{stderr}')
      return False

    sha_eurob = re.split(r'\t+', stdout)[0]

    # logger.info(stdout)
    # logger.info(stderr)

    if sha_dev == sha_eurob:
      logger.info("Repo are synch")
    else:
      logger.info("Repo are not synch")
      return False

    logger.debug('Checking the latest tag hash')
    process = subprocess.Popen(["git", "ls-remote", "--tags",
                                self.eurobench_url], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
      logger.error(f'Access to dev repository error({self.eurobench_url})')
      logger.error(f'{stderr}')
      return False

    tags = stdout.splitlines()

    if not tags:
      logger.error('no Tags defined')
      return False
    last_tag_hash, last_tag = tags[-1].split('\t')
    logger.debug(f"result:{last_tag}: {last_tag_hash}")
    if last_tag_hash == sha_eurob:
      logger.info ("Last commit is tagged version")
    else:
      logger.info (f"Last commit {sha_eurob[0:7]} differs from tagged version {last_tag}: {last_tag_hash[0:7]}")
      return False
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

  l_revise = list()
  l_synch = list()
  for one_spec in spec['algorithms']:
    one_synch = SynchronizedRepository()
    if one_synch.init(one_spec):
      logger.debug(f'Adding synch {one_synch.name}')
      l_synch.append(one_synch)
    else:
      logger.warn(f'could not load {one_spec}')
      l_revise.append(one_spec)

  logger.debug(f'{len(l_synch)} items loaded')

  l_issue = list()
  for idx, item in enumerate(l_synch):
    logger.info(f'Processing item {idx}: {item.name}')
    if not item.check_synchro():
      l_issue.append(item.name)

  logger.error('item not loaded')
  logger.error(l_revise)

  logger.error('item to revise')
  logger.error(l_issue)

  logger.info('All done')
