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
