from xpdconf.conf import glbl_dict


def test_glbl_dict():
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
        "exp_db",
        "home_dir",
        "blconfig_dir",
    ]:
        assert glbl_dict.get(k)
