# 计时器（pyside_timer）使用与打包说明

路径：`pyside_timer/timer.py`

## 概要

这是一个用 PySide6（Qt for Python）实现的桌面计时器，支持：

- 设置分钟与秒进行倒计时
- 开始 / 暂停 / 重置
- 倒计时结束弹出提示窗口

## 本地运行（开发）

1. 建议使用虚拟环境：
   - python -m venv .venv
   - source .venv/bin/activate（Windows: .venv\Scripts\activate）
2. 安装依赖：
   - pip install -r requirements.txt
3. 运行：
   - python pyside_timer/timer.py

## 功能说明

- 时间显示：HH:MM:SS
- 设置：左侧为分钟（0-999），右侧为秒（0-59）
- 按钮：
  - 开始：从输入时间开始倒计时（如果当前为 0，会弹警告）
  - 暂停：暂停倒计时，可再次开始继续剩余时间
  - 重置：停止并清零显示
- 结束提示：倒计时结束会弹出信息框“时间到！”

## 打包说明（GitHub Actions / 本地）

推荐使用 PyInstaller 生成单文件可执行（跨平台需在对应平台打包）：

基本命令（本地或 CI）：

```bash
pyinstaller --noconfirm --onefile --name pyside_timer pyside_timer/timer.py
```

注意事项与常见问题：

- Qt 资源与插件：
  - PyInstaller 有时不能自动包含 Qt 平台插件、图标或其他动态库，打包后如果程序启动报错，需为 PyInstaller 增加 --add-data / --add-binary 参数或使用 .spec 文件显式包含。
- Linux：
  - 运行时常见缺少库：libGL、libxcb、libglib 等。CI 中可在打包前安装对应系统包（例如 apt-get install libgl1 libxcb1 libglib2.0-0 ...）。
- macOS：
  - 若需要生成 `.app`，可用 PyInstaller 的 --windowed 并后续生成 dmg；发布到真实用户机器时通常需要签名与公证。
- Windows：
  - 可使用 --onefile 生成单个 exe，若要隐藏控制台使用 --windowed。
- 依赖版本：
  - 推荐在 requirements.txt 固定 PySide6 版本（例如 PySide6==6.5.*）以保证构建可复现。

## CI（仓库自带工作流）

- 仓库中提供名为 `build-timer` 的 GitHub Actions 工作流（位于 `.github/workflows/build-timer.yml`），会在 push 指向 `pyside_timer/**` 或 `requirements.txt` 时触发，或可手动运行（workflow_dispatch）。
- 工作流会在 ubuntu/windows/macos 三平台分别：
  - 安装依赖（pip、pyinstaller、build）
  - 生成 wheel 与 sdist
  - 使用 PyInstaller 打包单文件可执行
  - 上传构建产物为 Action artifacts，供下载

## 下载 Actions 产物

1. 打开仓库的 Actions -> 选择对应运行 -> 在页面底部找到 Artifacts
2. 下载平台对应压缩包并解压，运行其中的可执行文件

