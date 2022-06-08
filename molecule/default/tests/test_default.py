import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = '/usr/local/bin/infracost'


def test_infracost_binary_exists(host):
    """
    Tests if infracost binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_infracost_binary_file(host):
    """
    Tests if infracost binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_infracost_binary_which(host):
    """
    Tests the output to confirm infracost's binary location.
    """
    assert host.check_output('which infracost') == PACKAGE_BINARY
