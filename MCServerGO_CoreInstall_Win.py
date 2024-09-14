import os

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
        # 这里可以添加下载逻辑，例如使用 `requests` 库下载文件
        print(f"正在从 {download_url} 下载文件到 {target_dir}")

if __name__ == "__main__":
    main()