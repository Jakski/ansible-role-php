ansible-role-php
================================================================================

Role to setup PHP and PHP-FPM

Variables
--------------------------------------------------------------------------------

php_package_release

   Package default release

.. autoyaml:: defaults/main.yml

Examples
--------------------------------------------------------------------------------

.. literalinclude:: molecule/default/playbook.yml
   :language: yaml

Documentation
--------------------------------------------------------------------------------

Compile::

   $ pip3 install -r requirements.txt
   $ make text

View::

   $ less ./docs/text/ansible-role-php.txt
