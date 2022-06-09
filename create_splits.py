import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger
import shutil


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.
    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    # TODO: Implement function
    print(source)
    print(destination)
    files = [filename for filename in glob.glob(f'{source}/*.tfrecord')]
    # disturbed the order
    np.random.shuffle(files)
    train_files, val_files, test_files = np.split(files, [int(.80*len(files)), int(.95*len(files))])
    print("there are ", len(train_files), 'files for training')
    print("there are ", len(val_files), 'files for validation')
    print("there are ", len(test_files), 'files for testing')
    
    # create dirs and move target files into them
    # check if dirs exist and then move the data files in dirs
    # for train
    train = os.path.join(destination, 'train')

    if not os.path.exists(train):
        os.makedirs(train)
    #move
    for file in train_files:
        file = os.path.join(source, file)
        shutil.copy(file, train)
#         shutil.move(file, train)
        
    # for validation
    val = os.path.join(destination, 'val')

    if not os.path.exists(val):
        os.makedirs(val)
    #move
    for file in val_files:
        file = os.path.join(source, file)
        shutil.copy(file, val)
#         shutil.move(file, val)
        
    # for test
    test = os.path.join(destination, 'test')

    if not os.path.exists(test):
        os.makedirs(test)
    #move
    for file in test_files:
        file = os.path.join(source, file)
        shutil.copy(file, test)
        #         shutil.move(file, test)
        
#     # for validation
#     val = os.path.join(destination, 'val')
#     try:
#         if os.path.exists(val):
#             os.makedirs(val)
#     except:
#         os.makedirs(val,exist_ok=True)
#     # move
#     for file in val_files:
#         shutil.move(file, val)
    
#     # for test
#     test = os.path.join(destination, 'test')
#     os.makedirs(test, exist_ok=True)
#     for file in test_files:
#         shutil.move(file, test) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)