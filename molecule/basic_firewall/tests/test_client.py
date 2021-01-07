import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('client')


def test_server_open(host):

    ssh = host.run('nc -zvw10 ufw-server-open 22')
    http = host.run('nc -zvw10 ufw-server-open 80')
    assert ssh.rc == 0
    assert http.rc == 0


def test_server_closed(host):
    ssh = host.run('nc -zvw10 ufw-server-closed 22')
    http = host.run('nc -zvw10 ufw-server-closed 80')
    assert ssh.rc == 0
    assert http.rc == 1
