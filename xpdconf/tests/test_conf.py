import os
import tempfile


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
        "exp_db",
        "home_dir",
        "blconfig_dir",
    ]:
        assert glbl_dict.get(k)


def test_base_dir_from_env():
    """Test if the base directory can be loaded using the environment variable."""
    with tempfile.TemporaryDirectory() as d:
        os.environ["TEST_XPDACQ_BASE_DIR"] = str(d)
        from xpdconf.conf import glbl_dict
        assert glbl_dict.get("base_dir") == str(d)
        os.environ.pop("TEST_XPDACQ_BASE_DIR")
