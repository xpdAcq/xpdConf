import itertools
import os
import sys
from functools import partial
from pathlib import Path
from time import strftime

import databroker.v2
import yaml
from databroker import catalog
from pkg_resources import parse_version
from pkg_resources import resource_filename as rs_fn

if parse_version(yaml.__version__) > parse_version("3.13"):
    yaml_loader = partial(yaml.full_load)
else:
    yaml_loader = partial(yaml.load)

if os.name == "nt":
    _user_conf = os.path.join(os.environ["APPDATA"], "acq")
    CONFIG_SEARCH_PATH = (_user_conf,)
else:
    _user_conf = os.path.join(os.path.expanduser("~"), ".config", "acq")
    _local_etc = os.path.join(
        os.path.dirname(os.path.dirname(sys.executable)), "etc", "acq"
    )
    _system_etc = os.path.join("/", "etc", "acq")
    CONFIG_SEARCH_PATH = (_user_conf, _local_etc, _system_etc)

sim_config_path = rs_fn("xpdconf", "examples/sim.yaml")
sim_db_config_path = rs_fn("xpdconf", "examples/sim_db.yaml")


def lookup_config():
    """Copyright (c) 2014-2017 Brookhaven Science Associates, Brookhaven
    National Laboratory"""
    tried = []
    d = None
    for path in CONFIG_SEARCH_PATH:
        tried.append(path)
        config_path = Path(path)
        for filename in sorted(
                itertools.chain(config_path.glob("*.yaml"), config_path.glob("*.yml"))
        ):
            if (
                    filename
                    and os.path.isfile(os.path.join(path, filename))
                    and os.path.splitext(filename)[-1] in [".yaml", ".yml"]
            ):
                with open(os.path.join(path, filename)) as f:
                    d = yaml_loader(f)
    if d is None:
        print(
            "No config file could be found in "
            "the following locations:\n{}"
            "".format("\n".join(tried))
        )
        print("Loading from packaged simulation configuration")
        with open(sim_config_path) as f:
            d = yaml_loader(f)
    d = {k.lower(): v for k, v in d.items()}
    return d


glbl_dict = lookup_config()
glbl_dict.update(user_backup_dir_name=strftime("%Y"))
# if the env var exists, use that as the base directory
glbl_dict["base_dir"] = os.getenv("TEST_XPDACQ_BASE_DIR", glbl_dict["base_dir"])
XPD_SHUTTER_CONF = glbl_dict["shutter_conf"]

""" Expect dir
config_base/
            yaml/
                bt_bt.yaml
                samples/
                scanplnas/
"""
base_dirs_list = ["archive_root_dir", "base_dir"]
for d in base_dirs_list:
    glbl_dict[d] = os.path.expanduser(glbl_dict[d])

ARCHIVE_BASE_DIR = os.path.join(
    glbl_dict["archive_root_dir"], glbl_dict["archive_base_dir_name"]
)
USER_BACKUP_DIR_NAME = strftime("%Y")
HOME_DIR = os.path.join(glbl_dict["base_dir"], glbl_dict["home_dir_name"])
BLCONFIG_DIR = os.path.join(glbl_dict["base_dir"], glbl_dict["blconfig_dir_name"])
CONFIG_BASE = os.path.join(HOME_DIR, "config_base")
YAML_DIR = os.path.join(HOME_DIR, "config_base", "yml")
BT_DIR = YAML_DIR
SAMPLE_DIR = os.path.join(YAML_DIR, "samples")
SCANPLAN_DIR = os.path.join(YAML_DIR, "scanplans")
IMPORT_DIR = os.path.join(HOME_DIR, "Import")
ANALYSIS_DIR = os.path.join(HOME_DIR, "userAnalysis")
USERSCRIPT_DIR = os.path.join(HOME_DIR, "userScripts")
TIFF_BASE = os.path.join(HOME_DIR, "tiff_base")
USER_BACKUP_DIR = os.path.join(ARCHIVE_BASE_DIR, USER_BACKUP_DIR_NAME)
GLBL_YAML_PATH = os.path.join(YAML_DIR, glbl_dict["glbl_yaml_name"])
BLCONFIG_PATH = os.path.join(BLCONFIG_DIR, glbl_dict["blconfig_name"])
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
    ANALYSIS_DIR,
]
_EXCLUDE_DIR = [HOME_DIR, BLCONFIG_DIR, YAML_DIR]
_EXPORT_TAR_DIR = [CONFIG_BASE, USERSCRIPT_DIR]

glbl_dict.update(
    dict(
        is_simulation=glbl_dict["simulation"],
        # beamline info
        owner=glbl_dict["owner"],
        beamline_id=glbl_dict["beamline_id"],
        group=glbl_dict["group"],
        facility=glbl_dict["facility"],
        beamline_host_name=glbl_dict["beamline_host_name"],
        # directory names
        base=glbl_dict["base_dir"],
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
        frame_acq_time=glbl_dict["frame_acquire_time"],
        auto_dark=True,
        dk_window=glbl_dict["dark_window"],
        _dark_dict_list=[],
        shutter_control=True,
        auto_load_calib=True,
        calib_config_name=glbl_dict["calib_config_name"],
        # instrument config
        det_image_field=glbl_dict["image_fields"],
        all_folders=ALL_FOLDERS,
        userscript_dir=USERSCRIPT_DIR,
        _exclude_dir=[HOME_DIR, BLCONFIG_DIR, YAML_DIR],
        archive_base_dir=ARCHIVE_BASE_DIR,
    )
)
if glbl_dict["exp_broker_name"] == "xpd_sim_databroker":
    glbl_dict["exp_db"] = databroker.v2.temp()
else:
    glbl_dict["exp_db"] = catalog[glbl_dict["exp_broker_name"]]
glbl_dict.update(
    {
        k: os.path.join(glbl_dict["base_dir"], glbl_dict[z])
        for k, z in zip(
            ["home_dir", "blconfig_dir"],
            ["home_dir_name", "blconfig_dir_name"],
        )
    }
)
