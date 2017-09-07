plugin_type: test
description: Browbeat runner
subparsers:
    browbeat:
        help: Browbeat tests runner
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: BrowBeat
              options:
                  stress:
                      type: Bool
                      help: Run stress tests
                      default: False
                  yoda:
                      type: Bool
                      help: Run YODA
                      default: False
                  git-repo:
                      type: Value
                      help: URL of browbeat git repository to clone
                      default: https://git.openstack.org/openstack/browbeat
                  git-revision:
                      type: Value
                      help: Revision of browbeat repository
                      default: HEAD
