# CDUMM 汉化维护指南（快速复用版）

本文档用于后续 CDUMM 新版本发布后，快速重新套用中文汉化并完成验证与发布。

## 1. 当前汉化架构（这版做了什么）

当前汉化不是只改单个按钮，而是采用了“源码精翻 + 运行时翻译层”双轨方案：

1. 源码精翻（稳定、高质量）
- 直接改中文的页面：
  - `src/cdumm/gui/setup_dialog.py`
  - `src/cdumm/gui/import_widget.py`
  - `src/cdumm/gui/activity_panel.py`
  - `src/cdumm/gui/asi_panel.py`
  - `src/cdumm/gui/conflict_view.py`
  - `src/cdumm/gui/main_window.py`（工具页/关于页关键文案）
  - `src/cdumm/gui/mod_list_model.py`（表头与状态值）
  - `src/cdumm/engine/conflict_detector.py`（冲突解释文本）

2. 运行时翻译层（兜底、低维护）
- 核心文件：`src/cdumm/gui/i18n_zh.py`
- 在 `src/cdumm/main.py` 启动时调用 `install_chs_locale()`
- 用于兜底翻译：
  - 按钮/标签文本
  - 弹窗标题与正文
  - 表头文本
  - 下拉框条目
  - 菜单动作文本

3. 中文字体优化（解决锯齿和可读性）
- `main.py` 设置全局字体：
  - `Microsoft YaHei UI`
  - `PreferAntialias`
- `theme.py` 字体栈改为中文优先：
  - `"Microsoft YaHei UI", "PingFang SC", "Noto Sans CJK SC", "Segoe UI", sans-serif`

4. 本地测试脚本
- `run_cdumm_test.bat`：
  - 优先使用项目内 `.venv\Scripts\python.exe`
  - 否则再回退系统 Python
  - 自动安装依赖并启动


## 2. 新版本到来后的标准流程

假设你已经把上游新版本代码合并到本仓库（或直接在新版本分支工作）：

1. 拉取最新代码并检查差异
```powershell
git pull
git diff --name-only HEAD~1..HEAD
```

2. 优先检查这些高风险文件（最容易出现漏翻）
- `src/cdumm/gui/main_window.py`
- `src/cdumm/gui/mod_list_model.py`
- `src/cdumm/gui/binary_search_dialog.py`
- `src/cdumm/gui/bug_report.py`
- `src/cdumm/gui/verify_dialog.py`
- `src/cdumm/engine/conflict_detector.py`

3. 扩充 `i18n_zh.py` 词表
- 新增固定词条放 `EXACT_MAP`
- 动态拼接文本放 `SUBSTR_MAP`
- 原则：先保证功能可用，再精修语句

4. 对核心页面做源码精翻（优先用户高频界面）
- 表头、按钮、工具菜单、错误提示先改
- 复杂说明文案可后续精修

5. 运行本地测试
```powershell
.\run_cdumm_test.bat
```
- 至少手动走一遍：
  - PAZ 模组页
  - 工具页
  - 冲突面板
  - About 页
  - 至少触发 1 个 QMessageBox

6. 编译检查（防止语法回归）
```powershell
.venv\Scripts\python.exe -m compileall src/cdumm
```


## 3. 实战经验与常见坑

### 坑 1：翻译包装函数只支持字符串，导致启动崩溃
- 现象：`TypeError: unhashable type: 'list'`
- 原因：`setHorizontalHeaderLabels([...])` 传的是 `list`
- 结论：`tr()` 必须支持 `str/list/tuple`

### 坑 2：WindowsApps 假 Python 导致脚本闪退
- 现象：双击脚本后快速退出，或解释器启动失败
- 结论：优先用项目 `.venv`，不要依赖系统 `py` 自动选择

### 坑 3：中文字体发虚/锯齿
- 处理：全局字体改为 `Microsoft YaHei UI`，并启用抗锯齿策略

### 坑 4：只靠映射不够
- 某些文本是状态拼接或算法输出（如冲突解释），必须源码改中文


## 4. 推荐汉化优先级（时间紧时）

1. 一级（必须先做）
- `main_window.py` 工具页、导航页、弹窗标题
- `mod_list_model.py` 表头与状态
- `conflict_detector.py` 冲突解释

2. 二级（建议做）
- `binary_search_dialog.py`
- `bug_report.py`
- `profile_dialog.py`
- `verify_dialog.py`

3. 三级（可后续）
- 低频提示、开发日志、内部诊断文案


## 5. 提交前检查清单

- [ ] 双击 `run_cdumm_test.bat` 能正常启动
- [ ] PAZ 列表表头与状态全中文
- [ ] 工具页按钮全中文
- [ ] 冲突面板解释文本中文可读
- [ ] 弹窗标题/按钮无明显英文残留
- [ ] 没有把临时日志提交进仓库（`run_cdumm_test.log` 已在 `.gitignore`）


## 6. 建议的提交信息模板

```text
feat(i18n): update zh-CN localization for latest upstream UI changes
```

如果改了字体可附加：
```text
fix(ui): improve zh-CN font rendering with YaHei UI + antialias
```

