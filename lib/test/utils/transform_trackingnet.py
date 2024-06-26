import argparse
import os
import shutil

import _init_paths
import numpy as np

from lib.test.evaluation.environment import env_settings


def transform_trackingnet(tracker_name, cfg_name):
    env = env_settings(env_num=0)
    result_dir = env.results_path
    src_dir = os.path.join(result_dir, "%s/%s/trackingnet/" % (tracker_name, cfg_name))
    dest_dir = os.path.join(
        result_dir, "%s/%s/trackingnet_submit/" % (tracker_name, cfg_name)
    )
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    items = os.listdir(src_dir)
    for item in items:
        if "all" in item:
            continue
        if "time" not in item:
            src_path = os.path.join(src_dir, item)
            dest_path = os.path.join(dest_dir, item)
            try:
                bbox_arr = np.loadtxt(src_path, dtype=np.int64, delimiter="\t")
            except:
                print(src_path)
            np.savetxt(dest_path, bbox_arr, fmt="%d", delimiter=",")
    # make zip archive
    shutil.make_archive(src_dir, "zip", src_dir)
    shutil.make_archive(dest_dir, "zip", dest_dir)
    # Remove the original files
    shutil.rmtree(src_dir)
    shutil.rmtree(dest_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="transform trackingnet results.")
    parser.add_argument("--tracker_name", type=str, help="Name of tracking method.")
    parser.add_argument("--cfg_name", type=str, help="Name of config file.")

    args = parser.parse_args()
    transform_trackingnet(
        "lightfc",
        "mobilenetv2_p_pwcorr_se_ffn_next_concat_repn_33_se_center_concat_adamw_wiou",
    )
