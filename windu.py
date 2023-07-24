#!/usr/bin/env python3
import os

def get_size_in_bytes(path):
    total_size = 0
    if os.path.isfile(path):
        total_size = os.path.getsize(path)
    elif os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if os.path.exists(filepath):
                    total_size += os.path.getsize(filepath)
    return total_size

def convert_size_to_human_readable(size_in_bytes):
    # 定义文件大小单位
    units = ['B', 'KB', 'MB', 'GB']
    size = float(size_in_bytes)
    for unit in units:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024

def sort_by_file_size(directory):
    items = os.listdir(directory)  # 列出指定目录下的文件及目录
    sorted_items = sorted(items, key=lambda item: get_size_in_bytes(os.path.join(directory, item)))  # 对文件列表按大小排序
    return sorted_items

def main():
    current_directory = os.getcwd()  # 获取指定目录名称
    sorted_items = sort_by_file_size(current_directory)
    for item in sorted_items:
        item_path = os.path.join(current_directory, item)  # 将指定目录和os.listdir()获取到的文件及目录名拼接成绝对路径
        item_size = get_size_in_bytes(item_path)  # 获取文件的大小
        size_human_readable = convert_size_to_human_readable(item_size)
        print(f"{size_human_readable}\t{item}")

if __name__ == "__main__":
    input("按任意键开始...")
    main()
    input("按任意键退出...")
