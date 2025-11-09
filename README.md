# Minecraft 网易 SDK

[![Version](https://img.shields.io/badge/version-3.4%20|%203.5-blue.svg)](https://github.com/xbmanh/mc-netease-sdk)
[![Python](https://img.shields.io/badge/python-2.7-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)

Minecraft 中国版 MOD 开发 SDK - 提供完整的 Python API，用于开发 Minecraft 网易版的客户端和服务端模组。

## 📖 文档

### 主要文档
- **[完整 API 文档（中文）](API_DOCUMENTATION.md)** - 详细的中文 API 文档，包含所有 API、示例和最佳实践
- **[Full API Documentation (English)](API_DOCUMENTATION_EN.md)** - Complete English API documentation with examples

### 快速参考
- **[快速参考手册](QUICK_REFERENCE.md)** - 常用代码片段和快速查询
- **[组件参考手册](COMPONENT_REFERENCE.md)** - 所有组件的完整列表和说明

## ✨ 特性

- 🎮 **客户端 API** - 完整的客户端功能，包括 UI、渲染、输入处理等
- 🖥️ **服务端 API** - 强大的服务端逻辑，包括实体管理、世界操作、游戏规则等
- 🔧 **组件系统** - 灵活的组件架构，易于扩展和维护
- 📡 **事件系统** - 完善的事件监听和处理机制
- 🎨 **UI 系统** - 自定义界面开发支持
- 📊 **版本支持** - 同时支持 3.4 和 3.5 版本

## 📂 项目结构

```
mc-netease-sdk/
├── 3.4/                    # SDK 3.4 版本
│   └── mod/
│       ├── client/         # 客户端模块
│       │   ├── component/  # 客户端组件
│       │   ├── system/     # 客户端系统
│       │   └── ui/         # UI 界面
│       ├── server/         # 服务端模块
│       │   ├── component/  # 服务端组件
│       │   └── system/     # 服务端系统
│       └── common/         # 通用模块
│           ├── component/  # 通用组件
│           └── utils/      # 工具类
├── 3.5/                    # SDK 3.5 版本（包含新功能）
│   └── mod/
│       └── ...             # 结构与 3.4 相同
├── API_DOCUMENTATION.md    # 中文 API 文档
└── API_DOCUMENTATION_EN.md # 英文 API 文档
```

## 🚀 快速开始

### 创建服务端系统

```python
import mod.server.extraServerApi as serverApi

@serverApi.RegisterSystem("MyMod", "MyServerSystem", "path.to.MyServerSystem")
class MyServerSystem(serverApi.ServerSystem):
    def __init__(self, namespace, systemName):
        super(MyServerSystem, self).__init__(namespace, systemName)
        # 监听玩家加入事件
        self.ListenForEvent("Minecraft", "Minecraft", "PlayerJoinEvent", self, self.OnPlayerJoin)
        
    def OnPlayerJoin(self, args):
        playerId = args["playerId"]
        print(f"玩家 {playerId} 加入了游戏")
        
    def OnDestroy(self):
        pass
```

### 创建客户端系统

```python
import mod.client.extraClientApi as clientApi

@clientApi.RegisterSystem("MyMod", "MyClientSystem", "path.to.MyClientSystem")
class MyClientSystem(clientApi.ClientSystem):
    def __init__(self, namespace, systemName):
        super(MyClientSystem, self).__init__(namespace, systemName)
        
    def Update(self):
        # 每个游戏刻执行
        pass
        
    def OnDestroy(self):
        pass
```

## 📚 主要功能

### 服务端功能

- ✅ 实体管理（生成、销毁、属性修改）
- ✅ 方块操作（获取、设置、事件监听）
- ✅ 物品管理（背包操作、物品生成）
- ✅ 玩家管理（属性、位置、游戏模式）
- ✅ 世界操作（时间、天气、维度）
- ✅ 事件系统（丰富的游戏事件）
- ✅ AI 系统（自定义生物行为）

### 客户端功能

- ✅ UI 系统（自定义界面、控件）
- ✅ 渲染控制（模型、粒子、特效）
- ✅ 相机控制（视角、FOV）
- ✅ 输入处理（键盘、鼠标）
- ✅ 音效系统
- ✅ 绘图功能（3.5 版本新增）

## 🆕 版本 3.5 新功能

- 🎨 **DrawingCompClient** - 绘图组件，支持绘制盒子、线条、圆形、箭头、文本、球体等形状
- 📐 **DrawingShapeCompClient** - 形状控制组件，管理绘制的形状

## 📖 详细文档

请查看以下文档了解更多信息：

- [完整 API 文档（中文）](API_DOCUMENTATION.md) - 包含所有 API 的详细说明、参数、返回值和示例
- [Full API Documentation (English)](API_DOCUMENTATION_EN.md) - Complete API reference with examples

文档包含：
- 📘 **API 参考** - 所有类和方法的详细说明
- 💡 **示例代码** - 实用的代码示例和完整项目示例
- 🎯 **最佳实践** - 开发建议、性能优化和调试技巧
- ❓ **常见问题** - 常见问题解答和解决方案
- 🔄 **版本对比** - 3.4 和 3.5 版本的差异说明
- ⚡ **快速参考** - 常用代码片段和速查表
- 🧩 **组件参考** - 所有组件的完整列表

## 🤝 贡献

欢迎提交问题报告和改进建议！

## 📄 许可证

本项目基于开源协议发布，详见 [LICENSE](LICENSE) 文件。

## 🔗 相关链接

- [网易我的世界官网](https://mc.163.com/)
- [Minecraft Bedrock Edition 文档](https://docs.microsoft.com/minecraft/creator/)

---

Made with ❤️ for Minecraft China Edition developers
