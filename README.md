# GitHubActions-Test

> 一个用 GitHub Actions 把 Python 小工具自动打包 的试验仓库。
> 下载即用，不用本地装 Python。

---

## 📦 工具清单

| 工具 | 文件 | 产物 | 说明 |
|------|------|------|------|
| 📝 小本 | `notebook.py` | `notebook.exe` | 极简记事本，tkinter 实现，无第三方依赖 |
| ⏱️ 计时器 | `pyside_timer/timer.py` | `pyside_timer`（平台相关，可为 exe/app） | 使用 PySide6 实现的桌面计时器（开始/暂停/重置/倒计时提醒） |

---

## 🚀 下载 exe / 可执行程序

1. 打开 Actions 页面
2. 点击 Run workflow（或等 push 触发）
3. 等运行变绿
4. 在运行页面底部 Artifacts 下载对应平台的压缩包（例如 `pyside_timer-windows-latest.zip`）
5. 解压得到可执行文件，双击运行

---

## 📁 使用步骤

见 [steps](./steps) 目录:

- `steps/notebook.md`（记事本使用说明）
- `steps/timer.md`（计时器使用与打包说明）


## 📄 License

MIT
