# browbeat
Browbeat InfraRed Plugin

*WORK IN PROGRESS*
*This plugin is not ready for use*

## Installation

1. Install infrared (https://github.com/redhat-openstack/infrared)
2. Install browbeat infrared plugin::

    infrared plugin add <ir_brownbeat_plugin_path>

3. Run the plugin::

    infrared browbeat -h

## Usage

To run stress tests::

    infrared browbeat --stress yes

To run YODA::

    infrared --yoda yes

To run multiple types of tests::

    infrared --yoda yes --stress yes

## Contributions

Contributions are done with pull requests :)
