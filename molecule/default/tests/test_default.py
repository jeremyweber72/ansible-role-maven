import os

import testinfra.utils.ansible_runner

import logging

LOG = logging.getLogger("toto")


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    host.package("unzip").is_installed


def test_symlink(host):
    host.file("/usr/local/bin/mvn").is_symlink
