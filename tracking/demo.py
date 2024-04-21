import argparse
import os
import sys
import time
import vot

prj_path = os.path.join(os.path.dirname(__file__), "..")
if prj_path not in sys.path:
    sys.path.append(prj_path)

from lib.test.evaluation.tracker import Tracker


if __name__ == "__main__":
    tracker = Tracker(
        "lightfc",
        "mobilnetv2_p_pwcorr_se_scf_sc_iab_sc_adj_concat_repn33_se_conv33_center_wiou",
        None,
        None,
        None,
        deploy=False,
    )

    tracker.run_video(
        videofilepath="data/sample.MP4"
    )