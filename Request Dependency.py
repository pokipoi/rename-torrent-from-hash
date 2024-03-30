import subprocess

def install_requirements():
    subprocess.run(["pip", "install", "--upgrade", "-r", "requirements.txt"])

if __name__ == "__main__":
    # 安装 requirements.txt 中的依赖
    install_requirements()

    # 在这里添加您的 Request Dependency.py 的代码
    # ...