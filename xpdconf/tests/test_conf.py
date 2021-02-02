from databroker.v2 import Broker


def test_glbl_dict():
    from xpdconf.conf import glbl_dict
    print(list(glbl_dict.keys()))
    for k in [
        "home_dir",
        "blconfig_dir",
        "yaml_dir",
        "config_base",
        "sample_dir",
        "scanplan_dir",
        "tiff_base",
        "import_dir",
        "all_folders",
        "_exclude_dir",
        "_export_tar_dir",
        "archive_base_dir",
        "base_dir",
        "home_dir",
        "blconfig_dir",
    ]:
        assert glbl_dict.get(k)
    assert isinstance(glbl_dict.get("exp_db"), Broker)
