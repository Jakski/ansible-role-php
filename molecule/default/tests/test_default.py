import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pool_files(host):
    assert not host.file('/etc/php/7.0/fpm/pool.d/www.conf').exists
    example1 = host.file('/etc/php/7.0/fpm/pool.d/example1.conf')
    example2 = host.file('/etc/php/7.0/fpm/pool.d/example2.conf')
    assert example1.exists
    assert example2.exists
    assert example1.contains(r'^\[example1\]$')
    assert example2.contains(r'^\[example2\]$')
    assert example1.contains(r'^pm\.max_children = 10$')
    assert example2.contains(r'^pm\.max_children = 5$')


def test_ini_files(host):
    fpm_ini = host.file('/etc/php/7.0/fpm/php.ini')
    cli_ini = host.file('/etc/php/7.0/cli/php.ini')
    assert cli_ini.contains('^display_errors = 1$')
    assert fpm_ini.contains('^expose_php = Off$')


def test_packages(host):
    assert host.package('php7.0-fpm').is_installed
    assert host.package('php7.0-cli').is_installed


def test_fpm(host):
    fpm = host.service('php7.0-fpm')
    assert fpm.is_running
    assert fpm.is_enabled
