==================
xpdConf Change Log
==================

.. current developments

v0.4.3
====================

**Added:**

* Add MANIFEST.in to include yaml files in distribution



v0.4.2
====================

**Added:**

* Users can use the environment variable "TEST_XPDACQ_BASE_DIR" to set the base directory

**Changed:**

* Shutter configure for PDF beamline changes to "Close" and "Open"

* Experiment changes to version 2 databroker



v0.4.1
====================

**Fixed:**

* fix syntax of loading yaml for pyyaml > 3.13



v0.4.0
====================

**Added:**

* Add the simulated detectors to yaml so we can run simulations

**Changed:**

* Databroker used for simulations is now stable under acqsim so acq and an
  touch the same databases

**Fixed:**

* load only files with extensions of ``yml`` or ``yaml``



v0.3.0
====================

**Added:**

* ``radiograph_names, radiogram_dets, diffraction_dets`` keys



v0.2.1
====================

**Fixed:**

* ``outbout`` to ``outbound``



v0.2.0
====================

**Added:**

* ``shutter_sleep`` key to examples


**Removed:**

* ``det_image_field`` key in preference for ``image_field``




v0.1.0
====================



v0.0.1
====================



