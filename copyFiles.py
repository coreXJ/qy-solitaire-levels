import os
import shutil

def copy_json_files(src_dir, dest_dir):
    # 确保目标目录存在，如果不存在则创建
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 遍历源目录中的所有文件
    for filename in os.listdir(src_dir):
        if filename.endswith('.json'):
            src_file = os.path.join(src_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            
            # 复制文件并覆盖已存在的文件
            shutil.copy2(src_file, dest_file)
            print(f"Copied {src_file} to {dest_file}")

# 当前目录
current_dir = os.getcwd()

# 源目录和目标目录
src_dir = current_dir
dest_dir = os.path.join(current_dir, '../assets/config/level')

# 调用函数
copy_json_files(src_dir, dest_dir)