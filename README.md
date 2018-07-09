# browbeat
Browbeat InfraRed Plugin


## Installation

1. Install [infrared](https://github.com/redhat-openstack/infrared)
2. Install browbeat infrared plugin

```
infrared plugin add <ir_brownbeat_plugin_path>
```
3. Run the plugin

```
infrared browbeat -h
```

## Usage

To install and run browbeat on your TripleO cloud
 
```
infrared browbeat --ansoble-vars <filename> --config-file <filename> --workloads <rally/shaker/perfkit>
```

If you want to run workloads along with monitoring and visuzalization

```
infrared browbeat --ansoble-vars <filename> --config-file <filename> --workloads <rally/shaker/perfkit> --monitor yes --visualize yes
```
    
## Tests

To run Ansible linting tests, run the following command

```
tox -e ansible-lint

```
## Contributions

Contributions are made with pull requests :)
