import argparse
from typing import Any

global conf


def init(defaultProfile: Any = ...):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--profile', default=defaultProfile,
                        help='an integer for the accumulator')

    args = parser.parse_args()

    global conf

    conf = {}

    conf['timeout'] = 300

    conf['clear-previous'] = False

    conf['url_grafana'] = 'https://api.carscanner.dev/grafana/input'
    # conf['x-auth-token'] = 'yknspyfCvSnHkpPMXw8Eahx'

    conf['system'] = 'CS_Robot'

    conf['category'] = 'InMotionTestLab'
    conf['sub-category'] = 'C2-13-50-22-FD-2E'

    conf['group_head'] = 'Head'
    conf['group_MainBoard'] = 'MainBoard'
    conf['group_Application'] = 'Application'

    conf['sub-group_Application'] = 'C2-13-50-22-FD-2E'
    conf['sub-group_head'] = '9E-80-1A-BC-36-A8'
    conf['sub-group_MainBoard'] = '36-55-20-D3-F4-4C'

    # conf['logs'] = 'monitor.log'
    conf['logs'] = None
