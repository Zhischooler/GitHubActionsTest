
# GitHubActionsTest

> 一个用 GitHub Actions 把 Python 小工具自动打包成 Windows `.exe` 的试验仓库。
> 下载即用，不用本地装 Python。

---

## 📦 工具清单

| 工具 | 文件 | 产物 | 说明 |
|------|------|------|------|
| 📝 小本 | `notebook.py` | `notebook.exe` | 极简记事本，tkinter 实现，无第三方依赖 |

---

## 🚀 下载 exe

1. 打开 Actions 页面
2. 点击 Run workflow
3. 等运行变绿
4. 在运行页面底部 Artifacts 下载 `notebook-exe.zip`
5. 解压得到 `notebook.exe`，双击运行

---

## 📝 小本使用说明

功能：

- 新建、打开、保存、另存为
- UTF-8 文本读写
- 菜单栏操作，界面简洁

本地运行：

    python notebook.py

本地打包：

    pip install pyinstaller
    pyinstaller --onefile --noconsole --name notebook notebook.py

产物在 `dist/notebook.exe`。

---

## 📁 仓库结构

    .
    ├─ .github/
    │  └─ workflows/
    │     └─ build-exe.yml
    ├─ notebook.py
    ├─ README.md
    └─ LICENSE



---


## 📄 License

见 LICENSE 文件。