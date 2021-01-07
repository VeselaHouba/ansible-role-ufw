import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config_exists(host):
    f = host.file('/etc/ufw/user.rules')
    assert f.exists


def test_iptables_installed(host):
    c = host.run('iptables-save')
    assert c.rc == 0
    assert '22' in c.stdout
