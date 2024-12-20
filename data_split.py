import os
import random
import shutil
from shutil import copy2

randnum = 2022


def data_set_split(src_folder, target_folder, train_scale=0.8, val_scale=0.1, test_scale=0.1):
    print("start dataset splitting")
    class_names = os.listdir(src_folder)
    print(class_names)
    split_names = ['train', 'val', 'test']
    for split_name in split_names:
        split_path = os.path.join(target_folder, split_name)
        if os.path.isdir(split_path):
            pass
        else:
            os.mkdir(split_path)
        for class_name in class_names:
            class_split_path = os.path.join(split_path, class_name)
            if os.path.isdir(class_split_path):
                pass
            else:
                os.mkdir(class_split_path)

    for class_name in class_names:
        if(class_name == ".DS_Store"):
            continue
        current_class_path = os.path.join(src_folder, class_name)
        print("current_class_path:", current_class_path)
        current_data = os.listdir(current_class_path)
        print("current_data:", current_class_path)
        current_data_length = len(current_data)
        print("current_data_length:",current_data_length)
        current_data_index_list = list(range(current_data_length))
        # shuffling the folders ?
        random.seed(randnum)
        random.shuffle(current_data_index_list)

        train_folder = os.path.join(os.path.join(target_folder, 'train'), class_name)
        print("train_folder:", train_folder)
        val_folder = os.path.join(os.path.join(target_folder, 'val'), class_name)
        test_folder = os.path.join(os.path.join(target_folder, 'test'), class_name)
        train_stop_flag = current_data_length * train_scale
        print("train_stop_flag:",train_stop_flag)
        val_stop_flag = current_data_length * (train_scale + val_scale)
        current_idx = 0
        train_num, val_num, test_num = 0, 0, 0
        print("current_data_index_list:",current_data_index_list )
        for i in current_data_index_list:
            print("for i in current_data_index_list:", current_data[i])
            if(current_data[i]== ".DS_Store"):
                continue
            src_img_path = os.path.join(current_class_path, current_data[i])
            print("src_img_path:",src_img_path)
            if current_idx <= train_stop_flag:
                print("src_img_path",src_img_path, "train_folder",train_folder)
                copy2(src_img_path, train_folder)
                print("copied")
                train_num = train_num + 1
            elif (current_idx > train_stop_flag) and (current_idx <= val_stop_flag):
                copy2(src_img_path, val_folder)
                val_num = val_num + 1
            else:
                copy2(src_img_path, test_folder)
                test_num = test_num + 1
            current_idx = current_idx + 1

        print("********************************")
        print("train set{}: {}".format(train_folder, train_num))
        print("val set{}: {}".format(val_folder, val_num))
        print("test set{}: {}".format(test_folder, test_num))


src_folder = "./data/benchmark"
target_folder = "./data/benchmark"
data_set_split(src_folder, target_folder)
