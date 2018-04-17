import os
import sys
from time import strftime

import yaml
from pkg_resources import resource_filename as rs_fn

if os.name == 'nt':
    _user_conf = os.path.join(os.environ['APPDATA'], 'acq')
    CONFIG_SEARCH_PATH = (_user_conf,)
else:
    _user_conf = os.path.join(os.path.expanduser('~'), '.config', 'acq')
    _local_etc = os.path.join(os.path.dirname(os.path.dirname(sys.executable)),
                              'etc', 'acq')
    _system_etc = os.path.join('/', 'etc', 'acq')
    CONFIG_SEARCH_PATH = (_user_conf, _local_etc, _system_etc)

sim_config_path = rs_fn('xpdconf', 'examples/sim.yaml')


def lookup_config():
    """Copyright (c) 2014-2017 Brookhaven Science Associates, Brookhaven
    National Laboratory"""
    tried = []
    for path in CONFIG_SEARCH_PATH:
        if os.path.exists(path):
            filenames = os.listdir(path)
        else:
            filenames = []
        filename = next(iter(filenames), None)
        tried.append(path)
        if filename and os.path.isfile(os.path.join(path, filename)):
            with open(os.path.join(path, filename)) as f:
                d = yaml.load(f)
    else:
        print("No config file could be found in "
              "the following locations:\n{}"
              "".format('\n'.join(tried)))
        print('Loading from packaged simulation configuration')
        with open(sim_config_path) as f:
            d = yaml.load(f)
    d = {k.lower(): v for k, v in d.items()}
    d.update()
    return d


glbl_dict = lookup_config()
glbl_dict.update(USER_BACKUP_DIR_NAME=strftime('%Y'))
XPD_SHUTTER_CONF = glbl_dict['SHUTTER_CONF']

""" Expect dir
config_base/
            yaml/
                bt_bt.yaml
                samples/
                scanplnas/
"""
base_dirs_list = ['ARCHIVE_ROOT_DIR', 'BASE_DIR']
for d in base_dirs_list:
    glbl_dict[d] = os.path.expanduser(glbl_dict[d])

ARCHIVE_BASE_DIR = os.path.join(glbl_dict['ARCHIVE_ROOT_DIR'],
                                glbl_dict['ARCHIVE_BASE_DIR_NAME'])
USER_BACKUP_DIR_NAME = strftime('%Y')
HOME_DIR = os.path.join(glbl_dict['BASE_DIR'], glbl_dict['HOME_DIR_NAME'])
BLCONFIG_DIR = os.path.join(glbl_dict['BASE_DIR'],
                            glbl_dict['BLCONFIG_DIR_NAME'])
CONFIG_BASE = os.path.join(HOME_DIR, 'config_base')
YAML_DIR = os.path.join(HOME_DIR, 'config_base', 'yml')
BT_DIR = YAML_DIR
SAMPLE_DIR = os.path.join(YAML_DIR, 'samples')
SCANPLAN_DIR = os.path.join(YAML_DIR, 'scanplans')
IMPORT_DIR = os.path.join(HOME_DIR, 'Import')
ANALYSIS_DIR = os.path.join(HOME_DIR, 'userAnalysis')
USERSCRIPT_DIR = os.path.join(HOME_DIR, 'userScripts')
TIFF_BASE = os.path.join(HOME_DIR, 'tiff_base')
USER_BACKUP_DIR = os.path.join(ARCHIVE_BASE_DIR, USER_BACKUP_DIR_NAME)
GLBL_YAML_PATH = os.path.join(YAML_DIR, glbl_dict['GLBL_YAML_NAME'])
BLCONFIG_PATH = os.path.join(BLCONFIG_DIR, glbl_dict['BLCONFIG_NAME'])
ALL_FOLDERS = [
    HOME_DIR,
    BLCONFIG_DIR,
    YAML_DIR,
    CONFIG_BASE,
    SAMPLE_DIR,
    SCANPLAN_DIR,
    TIFF_BASE,
    USERSCRIPT_DIR,
    IMPORT_DIR,
    ANALYSIS_DIR
]
_EXCLUDE_DIR = [HOME_DIR, BLCONFIG_DIR, YAML_DIR]
_EXPORT_TAR_DIR = [CONFIG_BASE, USERSCRIPT_DIR]

glbl_dict = dict(is_simulation=glbl_dict['SIMULATION'],
                 # beamline info
                 owner=glbl_dict['OWNER'],
                 beamline_id=glbl_dict['BEAMLINE_ID'],
                 group=glbl_dict['GROUP'],
                 facility=glbl_dict['FACILITY'],
                 beamline_host_name=glbl_dict['BEAMLINE_HOST_NAME'],
                 # directory names
                 base=glbl_dict['BASE_DIR'],
                 home=HOME_DIR,
                 _export_tar_dir=_EXPORT_TAR_DIR,
                 xpdconfig=BLCONFIG_DIR,
                 import_dir=IMPORT_DIR,
                 config_base=CONFIG_BASE,
                 tiff_base=TIFF_BASE,
                 usrScript_dir=USERSCRIPT_DIR,
                 usrAnalysis_dir=ANALYSIS_DIR,
                 yaml_dir=YAML_DIR,
                 bt_dir=BT_DIR,
                 sample_dir=SAMPLE_DIR,
                 scanplan_dir=SCANPLAN_DIR,
                 allfolders=ALL_FOLDERS,
                 archive_dir=USER_BACKUP_DIR,
                 glbl_yaml_path=GLBL_YAML_PATH,
                 blconfig_path=BLCONFIG_PATH,
                 # options for functionalities
                 frame_acq_time=glbl_dict['FRAME_ACQUIRE_TIME'],
                 auto_dark=True,
                 dk_window=glbl_dict['DARK_WINDOW'],
                 _dark_dict_list=[],
                 shutter_control=True,
                 auto_load_calib=True,
                 calib_config_name=glbl_dict['CALIB_CONFIG_NAME'],
                 # instrument config
                 det_image_field=glbl_dict['IMAGE_FIELD']
                 )