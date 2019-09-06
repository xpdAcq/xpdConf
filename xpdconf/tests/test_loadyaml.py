import os
import yaml
import pytest
from pkg_resources import resource_filename as rs_fn
from pkg_resources import parse_version

EXP_DIR = rs_fn("xpdconf", "examples/")


def test_yaml_load():
    # test version
    assert parse_version(yaml.__version__) > parse_version('3.13')
    # assert no warning
    with pytest.warns(None) as record:
        fn = os.path.join(EXP_DIR, 'sim.yaml')
        with open(fn) as f:
            yaml.full_load(f)
    assert not record
