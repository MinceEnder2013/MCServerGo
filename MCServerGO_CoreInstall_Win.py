import os
import requests
from tqdm import tqdm

def download_file(url, target_path):
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

    with open(target_path, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()

    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")

def main():
    print("欢迎使用MCServerGO|此处为核心下载部分")
    print()
    print("[1]我要开插件服(使用Purpur端)")
    print("[2]我要开MOD端(使用Fabric端)")
    print("本程序仅面向新手，如果你是大神，没必要用这个")
    print("输入序号开始下载核心(插件默认1.20.4，MOD端默认1.20.1)不仅因为我懒，还因为mod端我是真没找到1.20.4的jar客户端，等有时间了我再写2")
    
    choice = input("你要开什么服？(填序号): ")
    
    if choice == "1":
        download_url = "https://download.fastmirror.net/download/Purpur/1.20.4/build2176"
        target_dir = os.path.join(os.path.dirname(__file__), "Core")
        os.makedirs(target_dir, exist_ok=True)
        filename = "purpur_server.jar"
    elif choice == '2':
        download_url = "https://repo.res.nullatom.com/Minecraft/Server/Fabric/fabric-server-mc.1.20.1-loader.0.14.21-launcher.0.11.2.jar"
        target_dir = os.path.join(os.path.dirname(__file__), "Core")
        os.makedirs(target_dir, exist_ok=True)
        filename = "fabric-server-mc.1.20.1-loader.0.14.21-launcher.0.11.2.jar"
    else:
        print("选择了其他选项。")
        return
    
    file_path = os.path.join(target_dir, filename)

    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"开始下载 {download_url} 到 {target_dir}...")
        
        # 下载文件并显示进度条
        download_file(download_url, file_path)
        
        if os.path.exists(file_path):
            print(f"成功从 {download_url} 下载文件到 {file_path}")
        else:
            print(f"下载失败，文件未保存到 {file_path}")
    else:
        print("文件已存在，无需重新下载。")

if __name__ == "__main__":
    main()