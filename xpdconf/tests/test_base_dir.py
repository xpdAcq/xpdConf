import os
import tempfile


def test_base_dir_from_env():
    """Test if the base directory can be loaded using the environment variable.

    This test sets environment variable TEST_XPDACQ_BASE_DIR and sets it back after use.
    """
    with tempfile.TemporaryDirectory() as d:
        env_var = os.getenv("TEST_XPDACQ_BASE_DIR")
        os.environ["TEST_XPDACQ_BASE_DIR"] = str(d)
        from xpdconf.conf import glbl_dict
        assert glbl_dict.get("base_dir") == str(d)
        if env_var:
            os.environ["TEST_XPDACQ_BASE_DIR"] = env_var
        else:
            os.environ.pop("TEST_XPDACQ_BASE_DIR")
