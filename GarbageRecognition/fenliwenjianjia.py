import os

# 获取a文件夹中的所有文件名（不含后缀名）
a_files = set([os.path.splitext(name)[0] for name in os.listdir(r'D:\bishe\rubbishdata\VOCdevkit_YoloFormat\VOCdevkit\images\rubbish_data\test\image')])

# 获取b文件夹中的所有文件名（不含后缀名）
b_folder = r'D:\bishe\rubbishdata\VOCdevkit_YoloFormat\VOCdevkit\images\rubbish_data\test\txt'
b_files = [os.path.splitext(name)[0] for name in os.listdir(b_folder)]

# 计数器
count = 0

# 遍历b文件夹中的所有文件名，如果该文件名不在a文件夹中，则删除该文件。
for file_name in b_files:
    if file_name not in a_files:
        file_path = os.path.join(b_folder, file_name + '.txt')
        os.remove(file_path)
        count += 1

# 输出删除成功的文件数
print('b文件夹中有%d个文件与a文件夹命名不一样，已经被删除。' % count)
