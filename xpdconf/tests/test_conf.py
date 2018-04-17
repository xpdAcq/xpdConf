from xpdconf.conf import glbl_dict


def test_glbl_dict():
    assert glbl_dict.get('frame_acq_time')
