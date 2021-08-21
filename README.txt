ansible-role-php
****************

Role to setup PHP and PHP-FPM


Variables
=========

php_package_release

   Package default release

php_manage_fpm

   Manage FPM

php_fpm_service

   PHP-FPM service name

php_fpm_enable

   Enable PHP-FPM service

php_package

   Package with PHP

   Use only PHP CLI package here, if you don't want FPM.

php_config_dir

php_fpm_config

   Sections/variables dictionary with overrides for FPM configuration

php_fpm_pools

   Pool/sections/variables nested dictionary with FPM pools
   configurations

php_cli_ini

   Sections/variables dictionary with INI configuration overrides for
   CLI

php_fpm_ini

   Sections/variables dictionary with INI configuration overrides for
   FPM

php_fpm_reload

   Reload FPM when necessary

php_fpm_restart

   Restart FPM when necessary

php_fpm_manage_pools

   Remove unmanaged FPM pool definitions

php_fpm_pools_dir

   Path to directory with FPM pools definitions

   This should be changed together with *include* directive in FPM
   configuration. If you change this, then you need to ensure that
   this directory exists.


Examples
========

   ---
   - hosts: instance
     tasks:
       - import_role:
           name: php
         vars:
           php_cli_ini:
             PHP:
               display_errors: 1
             bcmath:
               bcmath.scale: 20
           php_fpm_pools:
             example1:
               user: www-data
               group: www-data
               listen: /run/php/php7.0-fpm-example1.sock
               listen.owner: www-data
               listen.group: www-data
               pm: dynamic
               pm.max_children: 10
               pm.start_servers: 2
               pm.min_spare_servers: 1
               pm.max_spare_servers: 3
             example2:
               user: www-data
               group: www-data
               listen: /run/php/php7.0-fpm-example2.sock
               listen.owner: www-data
               listen.group: www-data
               pm: dynamic
               pm.max_children: 5
               pm.start_servers: 2
               pm.min_spare_servers: 1
               pm.max_spare_servers: 3


Documentation
=============

Compile:

   $ pip3 install -r requirements.txt
   $ make text

View:

   $ less ./docs/text/ansible-role-php.txt
