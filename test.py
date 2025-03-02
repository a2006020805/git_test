import numpy as np



if __name__ == "__main__":
    if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Demo Script to turn GT into json submission.')
    parser.add_argument('--dataroot', type=str, default='dataset/nuScenes/')
    parser.add_argument('--version', type=str, default='v1.0-mini', choices=['v1.0-trainval', 'v1.0-mini'])
    parser.add_argument('--eval_set', type=str, default='mini_val', choices=['train', 'val', 'test', 'mini_train', 'mini_val'])
    parser.add_argument('--output', type=str, default='submission.json')
    parser.add_argument('--thickness', type=int, default=100)
    parser.add_argument('--max_channel', type=int, default=300)
    parser.add_argument("--xbound", nargs=3, type=float, default=[-3000.0, 3000.0, 0.15])
    parser.add_argument("--ybound", nargs=3, type=float, default=[-1500.0, 1500.0, 0.15])
    parser.add_argument('--raster', action='store_true', default=False)
    args = parser.parse_args()

    main(args)
    arr = np.zeros([3,3,3])
    print(arr)