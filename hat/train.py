# flake8: noqa
import os.path as osp

import hat.archs
import hat.data
import hat.models
from basicsr.train import train_pipeline
# import ssl

# ssl._create_default_https_context = ssl._create_stdlib_context

if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    train_pipeline(root_path)
