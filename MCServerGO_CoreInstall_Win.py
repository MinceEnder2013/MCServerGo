import os
import requests

def main():
    print("欢迎使用MCServerGO|此处为核心下载部分")
    print()
    print("[1]我要开插件服(使用Purpur端)")
    print("[2]我要开MOD端(使用Fabric端)")
    print("本程序仅面向新手，如果你是大神，没必要用这个")
    print("输入序号和版本开始下载核心")
    
    choice = input("你要开什么服？(填序号): ")
    
    if choice == "1":
        download_url = "https://download.fastmirror.net/download/Purpur/1.20.4/build2176"
        target_dir = os.path.join(os.path.dirname(__file__), "Core")
        os.makedirs(target_dir, exist_ok=True)
        
        # 添加下载逻辑
        response = requests.get(download_url, stream=True)
        if response.status_code == 200:
            file_path = os.path.join(target_dir, "purpur_server.jar")
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print(f"成功从 {download_url} 下载文件到 {file_path}")
        else:
            print(f"下载失败，状态码: {response.status_code}")

if __name__ == "__main__":
    main()