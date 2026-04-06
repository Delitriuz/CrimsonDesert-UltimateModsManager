"""Runtime Simplified Chinese localization helpers for CDUMM."""

from __future__ import annotations

from typing import Callable

from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QGroupBox,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStatusBar,
    QTableWidget,
    QTabWidget,
    QWidget,
)
from PySide6.QtGui import QAction, QStandardItem, QStandardItemModel

# Exact replacements are applied first. Substring replacements are applied
# afterward so dynamic messages with variables can still be translated.
EXACT_MAP: dict[str, str] = {
    "Crimson Desert Ultimate Mods Manager": "红色沙漠终极 Mod 管理器",
    "Game Directory Setup": "游戏目录设置",
    "Select your Crimson Desert installation folder:": "请选择《Crimson Desert》安装目录：",
    "Steam or Xbox Game Pass install folder": "Steam 或 Xbox Game Pass 安装目录",
    "Browse...": "浏览...",
    "OK": "确定",
    "Cancel": "取消",
    "Select Crimson Desert Folder": "选择 Crimson Desert 文件夹",
    "Valid Crimson Desert installation found.": "已找到有效的 Crimson Desert 安装目录。",
    "bin64/CrimsonDesert.exe not found at this path.": "此路径下未找到 bin64/CrimsonDesert.exe。",
    "PAZ Mods": "PAZ 模组",
    "ASI Mods": "ASI 模组",
    "Log": "日志",
    "Tools": "工具",
    "About": "关于",
    "Verify Game State": "验证游戏状态",
    "Check Mods For Issues": "检查模组问题",
    "Find Problem Mod": "定位问题模组",
    "Profiles": "配置档",
    "Export Mod List": "导出模组列表",
    "Import Mod List": "导入模组列表",
    "No Snapshot": "无快照",
    "No game directory selected, exiting": "未选择游戏目录，程序将退出",
    "Drop files to import": "拖放文件以导入",
    "Activity Log": "活动日志",
    "Session:": "会话：",
    "Search": "搜索",
    "Clear": "清除",
    "Export Log": "导出日志",
    "All Sessions": "全部会话",
    "No log entries": "暂无日志记录",
    "ASI Plugins": "ASI 插件",
    "Refresh": "刷新",
    "Plugin": "插件",
    "Status": "状态",
    "Conflicts": "冲突",
    "Enabled": "已启用",
    "Disabled": "已禁用",
    "Enable": "启用",
    "Disable": "禁用",
    "Edit Config": "编辑配置",
    "Update": "更新",
    "Uninstall": "卸载",
    "Close": "关闭",
    "No ASI Found": "未找到 ASI",
    "Updated": "已更新",
    "Uninstall ASI Plugin": "卸载 ASI 插件",
    "Conflict": "冲突项",
    "Level": "级别",
    "Resolution": "解决方式",
    "No conflicts detected": "未检测到冲突",
    "Choose Mod Preset": "选择模组预设",
    "Choose What to Apply": "选择要应用的内容",
    "Install": "安装",
    "Apply Selected": "应用所选",
    "Select All": "全选",
    "Deselect All": "取消全选",
    "Mod Profiles": "模组配置档",
    "Saved Profiles:": "已保存配置档：",
    "Save Current": "保存当前配置",
    "Delete": "删除",
    "Rename": "重命名",
    "Load Selected Profile": "加载选中配置档",
    "Mods in profile:": "配置档中的模组：",
    "Bug Report": "问题报告",
    "Severity:": "严重级别：",
    "Report preview:": "报告预览：",
    "Copy to Clipboard": "复制到剪贴板",
    "Save as File": "保存为文件",
    "Copied": "已复制",
    "Saved": "已保存",
    "CDUMM Patch Notes": "CDUMM 更新说明",
    "Game State Verification": "游戏状态验证",
    "I'll Verify Through Steam": "我会通过 Steam 验证",
    "Starting...": "正在开始...",
    "Ready": "就绪",
    "Import Date": "导入时间",
    "Name": "名称",
    "Type": "类型",
    "Author": "作者",
    "Import": "导入",
    "Complete!": "完成！",
    "Operation failed": "操作失败",
    "Snapshot: No database": "快照：无数据库",
    "Snapshot: Not scanned yet": "快照：尚未扫描",
    "Find Problem Mod": "定位问题模组",
    "No Problems Found": "未发现问题",
    "All enabled mods appear to work together.": "所有已启用模组看起来可以同时工作。",
    "These mods are enabled for this test:": "本轮测试启用的模组如下：",
    "Bug (wrong behavior)": "Bug（行为异常）",
    "Crash (app closed/froze)": "崩溃（程序关闭/卡死）",
    "Performance (lag/stutter)": "性能问题（卡顿/掉帧）",
    "UI issue": "界面问题",
    "Exported": "已导出",
}

SUBSTR_MAP: dict[str, str] = {
    "Crimson Desert Ultimate Mods Manager v": "红色沙漠终极 Mod 管理器 v",
    "Crimson Desert Ultimate Mods Manager": "红色沙漠终极 Mod 管理器",
    "Drop a mod to install or update": "拖放模组进行安装或更新",
    "Drop an update to replace existing": "拖放更新包以替换现有版本",
    "Right-click mods for more options": "右键模组查看更多选项",
    "zip, folder, .json, .bat, .py": "zip、文件夹、.json、.bat、.py",
    "Apply": "应用",
    "Revert to Vanilla": "还原原版",
    "Refresh Snapshot": "刷新快照",
    "Import": "导入",
    "Update available": "发现新版本",
    "Critical Update Required": "必须更新",
    "Update Available": "有可用更新",
    "Download and install now?": "是否现在下载并安装？",
    "Downloading Update": "正在下载更新",
    "Download Failed": "下载失败",
    "Game Files Scan Needed": "需要扫描游戏文件",
    "Game Files Changed": "游戏文件已变更",
    "Fix Game State": "修复游戏状态",
    "Fix Everything": "一键修复",
    "Invalid Directory": "无效目录",
    "Game Directory Changed": "游戏目录已更改",
    "Find Problem Mod": "定位问题模组",
    "Mod Check": "模组检查",
    "Verifying Game State": "正在验证游戏状态",
    "Patch Notes": "更新说明",
    "Report Bug": "提交问题报告",
    "Previous Session Crashed": "上次会话异常退出",
    "Warning": "警告",
    "Error": "错误",
    "Success": "成功",
    "Auto-detected": "自动检测到",
    "Loading database...": "正在加载数据库...",
    "Checking game state...": "正在检查游戏状态...",
    "Verifying game files...": "正在验证游戏文件...",
    "Building UI...": "正在构建界面...",
    "Right-click a plugin for actions": "右键插件可执行更多操作",
    "Search logs...": "搜索日志...",
    "Export Activity Log": "导出活动日志",
    "Text Files (*.txt);;All Files (*)": "文本文件 (*.txt);;所有文件 (*)",
    "ASI Loader: Installed": "ASI Loader：已安装",
    "ASI Loader: Installed (auto)": "ASI Loader：已安装（自动）",
    "ASI Loader: Missing": "ASI Loader：缺失",
    "No .asi files found in that folder.": "该文件夹中未找到 .asi 文件。",
    "Delete ": "删除 ",
    " from bin64?": "（位于 bin64）？",
    "Files: ": "文件：",
    "Set \"": "设为优先生效：",
    "\" as winner": "",
    "Winner: ": "优先生效：",
    "issue(s)": "个问题",
    "Tools & Settings": "工具与设置",
    "Checking for updates...": "正在检查更新...",
    "Links": "相关链接",
    "No game directory": "无游戏目录",
    "No database": "无数据库",
    "No database connected": "未连接数据库",
    "Launch Game": "启动游戏",
    "Right-click a mod for more options": "右键模组查看更多选项",
    "Drag rows to reorder": "拖拽行可调整顺序",
    "Ctrl+click to multi-select": "Ctrl+单击可多选",
    "This mod has multiple presets.\nChoose which one to install:": "该模组包含多个预设。\n请选择要安装的版本：",
    "Choose a preset:": "选择预设：",
    "Check the items you want to apply:": "勾选要应用的项目：",
    "What happened? (steps to reproduce):": "发生了什么？（复现步骤）",
    "What's New in v": "v",
    "Mod Health Check: ": "模组健康检查：",
    "Copy Bug Report": "复制问题报告",
    "Apply Anyway (risky)": "仍要应用（有风险）",
    "Mod Contents: ": "模组内容：",
    "No mods found in the file.": "文件中未找到模组。",
    "CDUMM is up to date": "CDUMM 已是最新版本",
    "Update available: ": "发现新版本：",
    "click here to update now": "点击此处立即更新",
    "Database or game directory not configured.": "数据库或游戏目录尚未配置。",
    "Cannot Configure": "无法配置",
    "Configure...": "配置...",
    "Update (replace with new version)": "更新（替换为新版本）",
    "Revert Incomplete": "还原未完成",
    "Script Mod": "脚本模组",
    "I/O error while writing to game files:": "写入游戏文件时发生 I/O 错误：",
    "What happened?": "发生了什么？",
    "Please close the game and any mod tools, then retry.": "请关闭游戏和其他模组工具后重试。",
    "Import List": "导入列表",
    "Mod List": "模组列表",
    "Session ": "会话 ",
    " entries)": " 条记录)",
}

_INSTALLED = False


def tr(text):
    """Translate UI text to Simplified Chinese.

    Supports str/list/tuple so APIs like setHorizontalHeaderLabels(list[str])
    can be wrapped safely.
    """
    if text is None:
        return text

    if isinstance(text, list):
        return [tr(x) for x in text]
    if isinstance(text, tuple):
        return tuple(tr(x) for x in text)
    if not isinstance(text, str):
        return text
    if not text:
        return text
    if text in EXACT_MAP:
        return EXACT_MAP[text]

    translated = text
    for src, dst in sorted(SUBSTR_MAP.items(), key=lambda item: len(item[0]), reverse=True):
        if src in translated:
            translated = translated.replace(src, dst)
    return translated


def _wrap_text_method(cls: type, method_name: str) -> None:
    original = getattr(cls, method_name, None)
    if original is None:
        return
    if getattr(original, "_cdumm_i18n_wrapped", False):
        return

    def wrapped(self, text: str, *args, **kwargs):
        return original(self, tr(text), *args, **kwargs)

    wrapped._cdumm_i18n_wrapped = True
    setattr(cls, method_name, wrapped)


def _wrap_qmessagebox_static(name: str) -> None:
    original: Callable | None = getattr(QMessageBox, name, None)
    if original is None:
        return
    if getattr(original, "_cdumm_i18n_wrapped", False):
        return

    def wrapped(parent, title, text, *args, **kwargs):
        return original(parent, tr(title), tr(text), *args, **kwargs)

    wrapped._cdumm_i18n_wrapped = True
    setattr(QMessageBox, name, staticmethod(wrapped))


def translate_widget_tree(root: QWidget) -> None:
    """Best-effort recursive translation of visible widget text."""
    if root is None:
        return

    if isinstance(root, (QMainWindow, QDialog)):
        title = root.windowTitle()
        if title:
            root.setWindowTitle(tr(title))

    if isinstance(root, QGroupBox):
        title = root.title()
        if title:
            root.setTitle(tr(title))

    if isinstance(root, QTabWidget):
        for i in range(root.count()):
            root.setTabText(i, tr(root.tabText(i)))

    # Generic text-bearing widgets
    if hasattr(root, "text") and hasattr(root, "setText"):
        try:
            current = root.text()
            if isinstance(current, str) and current:
                root.setText(tr(current))
        except Exception:
            pass

    if hasattr(root, "placeholderText") and hasattr(root, "setPlaceholderText"):
        try:
            placeholder = root.placeholderText()
            if isinstance(placeholder, str) and placeholder:
                root.setPlaceholderText(tr(placeholder))
        except Exception:
            pass

    for child in root.findChildren(QWidget):
        if child is root:
            continue
        if getattr(child, "_cdumm_i18n_done", False):
            continue
        translate_widget_tree(child)
        setattr(child, "_cdumm_i18n_done", True)


def install_chs_locale() -> None:
    """Install runtime CHS localization hooks."""
    global _INSTALLED
    if _INSTALLED:
        return

    _wrap_text_method(QStatusBar, "showMessage")
    _wrap_text_method(QMainWindow, "setWindowTitle")
    _wrap_text_method(QLabel, "setText")
    _wrap_text_method(QPushButton, "setText")
    _wrap_text_method(QAction, "setText")
    _wrap_text_method(QStandardItem, "setText")
    _wrap_text_method(QComboBox, "addItem")
    _wrap_text_method(QComboBox, "addItems")
    _wrap_text_method(QComboBox, "setItemText")
    _wrap_text_method(QTableWidget, "setHorizontalHeaderLabels")
    _wrap_text_method(QStandardItemModel, "setHorizontalHeaderLabels")
    _wrap_text_method(QWidget, "setWindowTitle")
    _wrap_qmessagebox_static("information")
    _wrap_qmessagebox_static("warning")
    _wrap_qmessagebox_static("critical")
    _wrap_qmessagebox_static("question")

    original_show = QWidget.show
    if not getattr(original_show, "_cdumm_i18n_wrapped", False):
        def wrapped_show(self, *args, **kwargs):
            translate_widget_tree(self)
            return original_show(self, *args, **kwargs)

        wrapped_show._cdumm_i18n_wrapped = True
        QWidget.show = wrapped_show

    _INSTALLED = True
