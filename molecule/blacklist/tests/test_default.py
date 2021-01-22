import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config_exists(host):
    f = host.file('/etc/cron.d/blacklist')
    assert f.exists
    assert f.contains('Ansible')
    assert f.contains('0 3 1 * *')
    assert f.contains('root /opt/pull_blacklist.sh URL')
