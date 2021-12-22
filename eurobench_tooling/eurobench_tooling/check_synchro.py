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

def main():

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