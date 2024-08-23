import open3d as o3d

import numpy as np
import sys

import argparse
import datetime


def save_lidar_data_to_pcd(lidar_data, filename):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(lidar_data[:, :3])
    
    # 添加强度信息
    intensities = lidar_data[:, 3]
    pcd.colors = o3d.utility.Vector3dVector(np.tile(intensities[:, None], (1, 3)))

    o3d.io.write_point_cloud(filename, pcd)


def arg_parser():
    parser = argparse.ArgumentParser(description="Options for define input and output params")
    datetime_ = str(datetime.date.today())

    parser.add_argument("--input_bin", type=str)
    parser.add_argument("--output_pcd", type=str, default='./output_{}.pcd'.format(datetime_))

    args = parser.parse_args()

    return args



if __name__ == "__main__":
    args = arg_parser()
    input_bin = args.input_bin
    output_pcd = args.output_pcd

    bin_array = np.fromfile(input_bin, dtype=np.float32).reshape(-1, 4)

    save_lidar_data_to_pcd(bin_array, output_pcd)
    
