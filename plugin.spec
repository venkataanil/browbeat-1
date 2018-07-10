config:
    plugin_type: test
subparsers:
    browbeat:
        description: The Browbeat performance test runner
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Browbeat
              options:
                  install:
                    type: Bool
                    help: |
                      Runs the browbeat installer
                    default: False
                  config-file:
                      type: FileValue
                      help: |
                        The browbeat configuration to execute
                  workloads:
                      type: Value
                      help: |
                        The workloads to run, comma separated (rally,shaker.perfkit)
                  ansible-vars:
                      type: FileValue
                      help: |
                        The ansbile vars file for installation
                  monitor:
                      type: Bool
                      help: |
                        Setup collectd to monitor cloud
                      default: False
                  visualize:
                      type: Bool
                      help:
                        Visualize system metrics through grafana dashboards
                      default: False      
