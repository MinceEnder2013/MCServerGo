import os
import requests
from tqdm import tqdm

# 在程序开头添加星号画出的标题
# 打印50个星号
print("*" * 50)
# 打印中间的欢迎信息
print(" * 欢迎使用 MCServerGO | 此处为核心下载部分 * ")
# 再打印50个星号
print("*" * 50)

def validate_path(path):
    """
    验证给定的路径是否为当前文件所在目录的子目录。

    参数:
    path (str): 需要验证的路径。

    返回:
    bool: 如果路径有效，则返回True；否则，返回False。
    """
    # 获取当前脚本所在目录的绝对路径
    base_dir = os.path.dirname(__file__)
    # 检查给定路径是否以当前脚本所在目录的绝对路径开头
    return os.path.abspath(path).startswith(base_dir)

def download_file(url, path):
    """
    下载指定URL的文件，并将其保存到指定路径。

    参数:
    url (str): 文件的下载链接。
    path (str): 保存文件的目标路径。
    """
    try:
        # 发起GET请求获取文件
        response = requests.get(url, stream=True)
        # 检查响应状态码是否为200（成功）
        response.raise_for_status()
        
        # 获取文件大小
        total_size = int(response.headers.get('content-length', 0))
        # 设置块大小
        block_size = 1024
        
        # 打开文件进行写入，并显示下载进度条
        with open(path, 'wb') as f, tqdm(
            desc=path,  # 进度条描述
            total=total_size,  # 总大小
            unit='iB',  # 单位为字节
            unit_scale=True,  # 自动缩放单位
            unit_divisor=1024,  # 单位除数
        ) as bar:
            # 分块读取文件数据
            for data in response.iter_content(block_size):
                # 计算当前块的大小
                size = len(data)
                # 写入数据到文件
                f.write(data)
                # 更新进度条
                bar.update(size)
    except Exception as e:
        # 捕获异常并打印错误信息
        print(f"下载失败：{e}")

def main():
    """
    主函数，用于选择下载 Minecraft 服务器核心文件。
    """
    # 打印欢迎信息
    print("欢迎使用MCServerGO|此处为核心下载部分")
    print()
    # 打印选项
    print("[1]我要开插件服(使用Purpur端)")
    print("[2]我要开MOD端(使用Fabric端)")
    # 打印说明
    print("本程序仅面向新手，如果你是大神，没必要用这个")
    print("输入序号开始下载核心(插件默认1.20.4，MOD端默认1.20.1)不仅因为我懒，还因为mod端我是真没找到1.20.4的jar客户端，等有时间了我再写")
    
    # 循环处理用户输入
    while True:
        # 获取用户输入
        choice = input("你要开什么服？(填序号): ")
        
        # 根据用户选择设置下载链接和文件名
        if choice == "1":
            download_url = "https://download.fastmirror.net/download/Purpur/1.20.4/build2176"
            target_dir = os.path.join(os.path.dirname(__file__), "Core")
            filename = "purpur_server.jar"
        elif choice == '2':
            download_url = "https://repo.res.nullatom.com/Minecraft/Server/Fabric/fabric-server-mc.1.20.1-loader.0.14.21-launcher.0.11.2.jar"
            target_dir = os.path.join(os.path.dirname(__file__), "Core")
            filename = "fabric-server-mc.1.20.1-loader.0.14.21-launcher.0.11.2.jar"
        else:
            # 处理无效输入
            print("选择了其他选项。")
            continue
        
        # 验证目标路径是否安全
        if validate_path(target_dir):
            # 创建目标目录（如果不存在）
            os.makedirs(target_dir, exist_ok=True)
        else:
            # 抛出异常，路径不安全
            raise ValueError("目标路径不安全")

        # 构造文件完整路径
        file_path = os.path.join(target_dir, filename)

        # 检查文件是否存在
        if not os.path.exists(file_path):
            # 打印下载信息
            print(f"开始下载 {download_url} 到 {target_dir}...")
            
            # 下载文件并显示进度条
            download_file(download_url, file_path)
            
            # 检查文件是否成功下载
            if os.path.exists(file_path):
                print(f"成功从 {download_url} 下载文件到 {file_path}")
            else:
                print(f"下载失败，文件未保存到 {file_path}")
        else:
            # 文件已存在，无需重新下载
            print("文件已存在，无需重新下载。")
        
        # 提供继续或退出的选项
        continue_choice = input("输入y以退出此程序:")
        if continue_choice.lower() == 'y':
            # 用户选择退出，则结束循环
            break

# 程序入口
if __name__ == "__main__":
    main()