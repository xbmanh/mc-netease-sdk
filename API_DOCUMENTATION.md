# Minecraft 网易 SDK API 文档

## 概述

Minecraft 网易 SDK 是用于开发 Minecraft 中国版 MOD 的 Python 开发工具包。本 SDK 提供了客户端、服务端和通用的 API 接口，使开发者能够创建自定义游戏内容和功能。

### SDK 版本

- **3.4 版本**：稳定版本
- **3.5 版本**：新版本，包含额外功能（如绘图组件）

## 目录

1. [快速开始](#快速开始)
2. [架构概览](#架构概览)
3. [服务端 API](#服务端-api)
4. [客户端 API](#客户端-api)
5. [通用 API](#通用-api)
6. [组件系统](#组件系统)
7. [事件系统](#事件系统)
8. [UI 系统](#ui-系统)
9. [常用枚举](#常用枚举)
10. [最佳实践](#最佳实践)

---

## 快速开始

### 基本结构

MOD 项目通常包含以下结构：

```
mod/
├── client/          # 客户端代码
│   ├── component/   # 客户端组件
│   ├── system/      # 客户端系统
│   └── ui/          # UI 界面
├── server/          # 服务端代码
│   ├── component/   # 服务端组件
│   └── system/      # 服务端系统
└── common/          # 通用代码
    ├── component/   # 通用组件
    └── utils/       # 工具类
```

### 注册系统

服务端系统注册示例：

```python
import mod.server.extraServerApi as serverApi

# 注册服务端系统
@serverApi.RegisterSystem("MyNamespace", "MySystem", "path.to.MyServerSystem")
class MyServerSystem(serverApi.ServerSystem):
    def __init__(self, namespace, systemName):
        super(MyServerSystem, self).__init__(namespace, systemName)
        
    def OnDestroy(self):
        pass
```

客户端系统注册示例：

```python
import mod.client.extraClientApi as clientApi

# 注册客户端系统
@clientApi.RegisterSystem("MyNamespace", "MySystem", "path.to.MyClientSystem")
class MyClientSystem(clientApi.ClientSystem):
    def __init__(self, namespace, systemName):
        super(MyClientSystem, self).__init__(namespace, systemName)
        
    def OnDestroy(self):
        pass
```

---

## 架构概览

### 系统（System）

系统是 MOD 的核心逻辑单元，分为：

- **ServerSystem**：服务端系统，处理游戏逻辑
- **ClientSystem**：客户端系统，处理客户端逻辑和 UI
- **MasterSystem**：大厅系统
- **ServiceSystem**：服务系统

### 组件（Component）

组件是附加到实体的功能模块，分为：

- **服务端组件**：在服务端运行，处理游戏逻辑
- **客户端组件**：在客户端运行，处理显示和交互
- **通用组件**：基础组件类

### 事件（Event）

系统通过事件进行通信和响应游戏状态变化。

---

## 服务端 API

### extraServerApi

服务端主 API 模块，提供系统和组件注册功能。

#### 核心函数

##### RegisterSystem

注册服务端系统到引擎。

```python
def RegisterSystem(nameSpace, systemName, clsPath):
    # type: (str, str, str) -> ServerSystem
    """
    用于将系统注册到引擎中，引擎会创建一个该系统的实例，并在退出游戏时回收。
    系统可以执行我们引擎赋予的基本逻辑，例如监听事件、执行Tick函数、与客户端进行通讯等。
    
    参数：
        nameSpace: 命名空间，通常是MOD的唯一标识
        systemName: 系统名称
        clsPath: 系统类的路径
        
    返回：
        ServerSystem 实例
    """
```

##### GetSystem

获取已注册的系统实例。

```python
def GetSystem(nameSpace, systemName):
    # type: (str, str) -> ServerSystem
    """
    获取已注册的系统
    
    参数：
        nameSpace: 命名空间
        systemName: 系统名称
        
    返回：
        ServerSystem 实例
    """
```

##### RegisterComponent

注册自定义组件。

```python
def RegisterComponent(nameSpace, name, clsPath):
    # type: (str, str, str) -> bool
    """
    用于将组件注册到引擎中
    
    参数：
        nameSpace: 命名空间
        name: 组件名称
        clsPath: 组件类路径
        
    返回：
        注册是否成功
    """
```

##### CreateComponent

为实体创建组件。

```python
def CreateComponent(entityId, nameSpace, name):
    # type: (Union[str,int], str, str) -> BaseComponent
    """
    给实体创建服务端组件
    
    参数：
        entityId: 实体ID
        nameSpace: 命名空间
        name: 组件名称
        
    返回：
        组件实例
    """
```

##### GetComponent

获取实体的组件。

```python
def GetComponent(entityId, nameSpace, name):
    # type: (str, str, str) -> BaseComponent
    """
    获取实体的服务端组件。一般用来判断某个组件是否创建过，其他情况请使用CreateComponent
    
    参数：
        entityId: 实体ID
        nameSpace: 命名空间
        name: 组件名称
        
    返回：
        组件实例或None
    """
```

### ServerSystem

服务端系统基类。

#### 基本方法

```python
class ServerSystem:
    def __init__(self, namespace, systemName):
        """初始化系统"""
        pass
        
    def OnDestroy(self):
        """系统销毁时调用"""
        pass
        
    def Update(self):
        """每个游戏刻（Tick）调用一次"""
        pass
        
    def ListenForEvent(self, namespace, systemName, eventName, instance, func, priority=0):
        """监听事件"""
        pass
        
    def UnListenForEvent(self, namespace, systemName, eventName, instance, func):
        """取消监听事件"""
        pass
        
    def NotifyToClient(self, playerId, eventName, eventData):
        """向客户端发送消息"""
        pass
        
    def BroadcastToAllClient(self, eventName, eventData):
        """向所有客户端广播消息"""
        pass
```

### 服务端组件

#### AttrCompServer

属性组件，用于管理实体的各种属性。

```python
class AttrCompServer(BaseComponent):
    def SetAttrValue(self, attrType, value, setDefault=1):
        # type: (int, float, int) -> bool
        """
        设置实体的引擎属性
        
        参数：
            attrType: 属性类型（参考 AttrType 枚举）
            value: 属性值
            setDefault: 是否设置默认值
            
        返回：
            是否设置成功
        """
        
    def GetAttrValue(self, attrType):
        # type: (int) -> float
        """
        获取实体的引擎属性
        
        参数：
            attrType: 属性类型
            
        返回：
            属性值
        """
        
    def SetAttrMaxValue(self, type, value):
        # type: (int, float) -> bool
        """设置实体的引擎属性的最大值"""
        
    def GetAttrMaxValue(self, type):
        # type: (int) -> float
        """获取实体的引擎属性的最大值"""
        
    def IsEntityOnFire(self):
        # type: () -> bool
        """获取实体是否着火"""
        
    def SetEntityOnFire(self, seconds, burn_damage=1):
        # type: (int, int) -> bool
        """设置实体着火"""
        
    def SetStepHeight(self, stepHeight):
        # type: (float) -> bool
        """
        设置玩家前进非跳跃状态下能上的最大台阶高度
        默认值为0.5625，1表示能上一个台阶
        """
        
    def GetTypeFamily(self):
        # type: () -> List[str]
        """获取生物行为包字段 type_family"""
```

#### ItemCompServer

物品组件，管理玩家物品栏。

```python
class ItemCompServer(BaseComponent):
    def GetPlayerItem(self, itemType, auxValue=0):
        """获取玩家物品"""
        
    def SetInvItemNum(self, slot, num):
        """设置物品栏指定槽位的物品数量"""
        
    def GetInvItem(self, slot):
        """获取物品栏指定槽位的物品信息"""
        
    def SpawnItemToPlayerInv(self, itemDict, playerId):
        """生成物品到玩家背包"""
        
    def GetPlayerAllItems(self, posType=-1):
        """获取玩家所有物品"""
```

#### PositionCompServer

位置组件。

```python
class PosCompServer(BaseComponent):
    def GetPos(self):
        # type: () -> Tuple[float, float, float]
        """获取实体位置坐标"""
        
    def SetPos(self, pos):
        # type: (Tuple[float, float, float]) -> bool
        """设置实体位置坐标"""
        
    def GetFootPos(self):
        """获取实体脚底位置"""
```

#### GameCompServer

游戏管理组件。

```python
class GameCompServer(BaseComponent):
    def SetCanRespawn(self, canRespawn):
        """设置玩家是否可以重生"""
        
    def ChangePlayerGameMode(self, gameMode):
        """改变玩家游戏模式"""
        
    def SetTime(self, time):
        """设置世界时间"""
        
    def GetTime(self):
        """获取世界时间"""
        
    def SetDefaultGameMode(self, gameMode):
        """设置默认游戏模式"""
```

#### BlockCompServer

方块组件。

```python
class BlockCompServer(BaseComponent):
    def GetBlockNew(self, pos):
        """获取指定位置的方块信息"""
        
    def SetBlockNew(self, pos, blockDict, oldBlockHandling=0):
        """设置指定位置的方块"""
        
    def GetBlockClicked(self):
        """获取被点击的方块位置"""
```

#### EffectCompServer

效果组件，管理状态效果（如中毒、速度提升等）。

```python
class EffectCompServer(BaseComponent):
    def AddEffectToEntity(self, effectId, duration, amplifier=0, showParticles=True):
        """给实体添加状态效果"""
        
    def RemoveEffectFromEntity(self, effectId):
        """移除实体的状态效果"""
        
    def GetAllEffects(self):
        """获取实体所有状态效果"""
```

---

## 客户端 API

### extraClientApi

客户端主 API 模块。

#### 核心函数

##### RegisterSystem

```python
def RegisterSystem(nameSpace, systemName, clsPath):
    # type: (str, str, str) -> ClientSystem
    """
    用于将系统注册到引擎中，引擎会创建一个该系统的实例，并在退出游戏时回收。
    系统可以执行我们引擎赋予的基本逻辑，例如监听事件、执行Tick函数、与服务端进行通讯等。
    """
```

##### GetSystem

```python
def GetSystem(nameSpace, systemName):
    # type: (str, str) -> ClientSystem
    """用于获取其他系统实例"""
```

##### CreateComponent

```python
def CreateComponent(entityId, nameSpace, name):
    # type: (Union[str,int], str, str) -> BaseComponent
    """给实体创建客户端组件"""
```

### ClientSystem

客户端系统基类。

```python
class ClientSystem:
    def __init__(self, namespace, systemName):
        """初始化系统"""
        
    def OnDestroy(self):
        """系统销毁时调用"""
        
    def Update(self):
        """每个游戏刻（Tick）调用一次"""
        
    def ListenForEvent(self, namespace, systemName, eventName, instance, func, priority=0):
        """监听事件"""
        
    def UnListenForEvent(self, namespace, systemName, eventName, instance, func):
        """取消监听事件"""
        
    def NotifyToServer(self, eventName, eventData):
        """向服务端发送消息"""
        
    def CreateUI(self, modName, clsPath, screenDef):
        """创建 UI 界面"""
```

### 客户端组件

#### AttrCompClient

客户端属性组件。

```python
class AttrCompClient(BaseComponent):
    def isEntityInLava(self):
        # type: () -> bool
        """实体是否在岩浆中"""
        
    def isEntityOnGround(self):
        # type: () -> bool
        """实体是否触地"""
        
    def GetAttrValue(self, attrType):
        # type: (int) -> float
        """获取属性值，包括生命值，饥饿度，移速"""
        
    def GetAttrMaxValue(self, type):
        # type: (int) -> float
        """获取属性最大值"""
```

#### CameraCompClient

相机组件。

```python
class CameraCompClient(BaseComponent):
    def SetCameraMode(self, mode):
        """设置相机模式（第一人称/第三人称）"""
        
    def LockCamera(self, rot):
        """锁定相机角度"""
        
    def UnlockCamera(self):
        """解锁相机"""
        
    def SetFov(self, fov):
        """设置视野角度"""
```

#### ModelCompClient

模型组件。

```python
class ModelCompClient(BaseComponent):
    def SetModel(self, model):
        """设置实体模型"""
        
    def ResetModel(self):
        """重置实体模型"""
        
    def GetModel(self):
        """获取实体模型标识符"""
```

#### DrawingCompClient（3.5 版本新增）

绘图组件，用于在游戏中绘制各种形状。

```python
class DrawingCompClient(BaseComponent):
    def AddBoxShape(self, pos, scale=(1, 1, 1), color=(1, 1, 1)):
        # type: (Tuple[float,float,float], Tuple[float,float,float], Tuple[float,float,float]) -> DrawingShape
        """新建盒子形状"""
        
    def AddLineShape(self, startPos, endPos, color=(1, 1, 1)):
        # type: (Tuple[float,float,float], Tuple[float,float,float], Tuple[float,float,float]) -> DrawingShape
        """新建线条形状"""
        
    def AddCircleShape(self, pos, radius, color=(1, 1, 1), plane=2, segmentsNum=20):
        # type: (Tuple[float,float,float], float, Tuple[float,float,float], int, int) -> DrawingShape
        """新建圆形状"""
        
    def AddArrowShape(self, startPos, endPos, color=(1, 1, 1), headSegmentsNum=20, arrowHeadLength=1, radius=0.5):
        # type: (Tuple[float,float,float], Tuple[float,float,float], Tuple[float,float,float], int, float, float) -> DrawingShape
        """新建箭头形状"""
        
    def AddTextShape(self, pos, text, color=(1, 1, 1)):
        # type: (Tuple[float,float,float], str, Tuple[float,float,float]) -> DrawingShape
        """新建文本形状"""
        
    def AddSphereShape(self, pos, radius, color=(1, 1, 1), segmentsNum=20):
        # type: (Tuple[float,float,float], float, Tuple[float,float,float], int) -> DrawingShape
        """新建球形状"""
        
    def RemoveAll(self):
        # type: () -> bool
        """移除所有形状"""
```

---

## 通用 API

### minecraftEnum

游戏常量和枚举定义。

#### ActorDamageCause

伤害类型枚举。

```python
class ActorDamageCause:
    NONE = "none"                          # 其他
    Override = "override"                  # 非正常方式
    Contact = "contact"                    # 接触伤害（如仙人掌）
    EntityAttack = "entity_attack"         # 生物攻击
    Projectile = "projectile"              # 抛射物攻击
    Suffocation = "suffocation"            # 窒息
    Fall = "fall"                          # 掉落
    Fire = "fire"                          # 着火
    FireTick = "fire_tick"                 # 连续着火
    Lava = "lava"                          # 熔岩
    Drowning = "drowning"                  # 溺水
    BlockExplosion = "block_explosion"     # 方块爆炸
    EntityExplosion = "entity_explosion"   # 生物爆炸
    Void = "void"                          # 虚空
    Magic = "magic"                        # 魔法伤害
    Wither = "wither"                      # 凋零效果
    Starve = "starve"                      # 饥饿
    Lightning = "lightning"                # 闪电
    Freezing = "freezing"                  # 冰冻
```

#### AttrType

属性类型枚举。

```python
class AttrType:
    HEALTH = 0              # 生命值，原版范围 [0,20]
    SPEED = 1               # 移速，原版范围 [0,+∞]
    DAMAGE = 2              # 攻击力，原版范围 [1,+∞]
    UNDERWATER_SPEED = 3    # 水里的移速
    HUNGER = 4              # 饥饿值，原版范围 [0,20]
    SATURATION = 5          # 饱和值，原版范围 [0,20]
    ABSORPTION = 6          # 伤害吸收生命值，原版范围 [0,16]
    LAVA_SPEED = 7          # 岩浆里的移速
    LUCK = 8                # 幸运值，原版范围 [-1024,1024]
    FOLLOW_RANGE = 9        # 跟随方块数（怪物仇恨范围）
    KNOCKBACK_RESISTANCE = 10  # 击退抵抗
    JUMP_STRENGTH = 11      # 跳跃力（骑乘后跳跃高度）
    ARMOR = 12              # 护甲值
```

#### GameType

游戏模式枚举。

```python
class GameType:
    Survival = 0      # 生存模式
    Creative = 1      # 创造模式
    Adventure = 2     # 冒险模式
    Spectator = 3     # 旁观者模式
```

#### ArmorSlotType

装备槽位枚举。

```python
class ArmorSlotType:
    DEFAULT = -1
    HEAD = 0    # 头盔
    BODY = 1    # 胸甲
    LEG = 2     # 护腿
    FOOT = 3    # 鞋子
```

---

## UI 系统

### 创建 UI

```python
# 在客户端系统中
class MyClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        super(MyClientSystem, self).__init__(namespace, systemName)
        
    def OpenMyUI(self):
        uiNode = self.CreateUI("MyMod", "MyUIPath", "MyUIScreen.main")
```

### ScreenNode

UI 界面节点基类。

```python
class ScreenNode:
    def __init__(self, namespace, name, path):
        """初始化 UI 节点"""
        
    def OnDestroy(self):
        """界面销毁时调用"""
        
    def GetBaseUIControl(self, path):
        """获取 UI 控件"""
        
    def SetVisible(self, path, visible):
        """设置 UI 控件可见性"""
```

### ViewBinder

UI 数据绑定类。

```python
class ViewBinder:
    def GetComponent(self, key):
        """获取组件"""
        
    def BindComponent(self, key, component):
        """绑定组件到视图"""
```

---

## 组件系统

### 创建自定义组件

服务端组件示例：

```python
from mod.common.component.baseComponent import BaseComponent

class MyCustomCompServer(BaseComponent):
    def __init__(self):
        super(MyCustomCompServer, self).__init__()
        
    def MyMethod(self):
        """自定义方法"""
        pass
```

### 注册和使用组件

```python
import mod.server.extraServerApi as serverApi

# 注册组件
serverApi.RegisterComponent("MyNamespace", "MyComp", "path.to.MyCustomCompServer")

# 创建组件
comp = serverApi.CreateComponent(entityId, "MyNamespace", "MyComp")

# 使用组件
comp.MyMethod()
```

---

## 事件系统

### 监听事件

```python
class MyServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        super(MyServerSystem, self).__init__(namespace, systemName)
        
        # 监听玩家加入事件
        self.ListenForEvent(
            "Minecraft",           # 命名空间
            "Minecraft",           # 系统名
            "PlayerJoinEvent",     # 事件名
            self,                  # 实例
            self.OnPlayerJoin      # 回调函数
        )
        
    def OnPlayerJoin(self, args):
        """玩家加入事件处理"""
        playerId = args["playerId"]
        print("Player joined:", playerId)
```

### 常用事件

#### 服务端事件

- `PlayerJoinEvent` - 玩家加入
- `PlayerDieEvent` - 玩家死亡
- `ServerPlayerGetExperienceOrbEvent` - 玩家获得经验球
- `PlayerAttackEvent` - 玩家攻击
- `DamageEvent` - 伤害事件
- `BlockNeighborChangedServerEvent` - 方块邻居改变

#### 客户端事件

- `OnLocalPlayerStopLoading` - 本地玩家加载完成
- `PlayerAttackEvent` - 玩家攻击
- `UiInitFinished` - UI 初始化完成
- `OnScriptTickClient` - 客户端Tick事件

### 自定义事件

```python
# 服务端创建自定义事件
def CreateCustomEvent():
    """创建并触发自定义事件"""
    import mod.server.extraServerApi as serverApi
    
    # 获取事件管理器
    eventSystem = serverApi.GetSystem("Minecraft", "Minecraft")
    
    # 创建事件数据
    eventData = {
        "playerId": "player_id_here",
        "data": "custom_data"
    }
    
    # 发送事件
    eventSystem.NotifyToClient(playerId, "MyCustomEvent", eventData)
```

---

## 最佳实践

### 1. 命名规范

- 使用有意义的命名空间，避免与其他 MOD 冲突
- 系统名称使用驼峰命名法
- 组件名称以 Comp 结尾

### 2. 内存管理

```python
class MyServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        super(MyServerSystem, self).__init__(namespace, systemName)
        self.timers = []
        
    def OnDestroy(self):
        """清理资源"""
        # 取消所有监听的事件
        self.UnListenForEvent(...)
        
        # 清理定时器
        for timer in self.timers:
            timer.Cancel()
        
        # 清空引用
        self.timers = []
```

### 3. 错误处理

```python
def SafeOperation(self, entityId):
    """安全操作示例"""
    try:
        comp = self.CreateComponent(entityId, "Minecraft", "pos")
        if comp:
            pos = comp.GetPos()
            return pos
        else:
            print("Failed to create component")
            return None
    except Exception as e:
        print("Error:", str(e))
        return None
```

### 4. 性能优化

- 避免在 Update/Tick 函数中执行大量操作
- 使用缓存减少重复计算
- 合理使用事件监听，避免不必要的事件处理

```python
class OptimizedSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        super(OptimizedSystem, self).__init__(namespace, systemName)
        self.cache = {}
        self.tickCount = 0
        
    def Update(self):
        """优化的更新函数"""
        self.tickCount += 1
        
        # 每10个tick执行一次，而不是每个tick都执行
        if self.tickCount % 10 == 0:
            self.DoExpensiveOperation()
```

### 5. 客户端-服务端通信

服务端向客户端发送消息：

```python
# 服务端
def NotifyClient(self, playerId, message):
    eventData = {"message": message}
    self.NotifyToClient(playerId, "ShowMessage", eventData)
```

客户端接收并处理消息：

```python
# 客户端
class MyClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        super(MyClientSystem, self).__init__(namespace, systemName)
        
        # 监听来自服务端的消息
        self.ListenForEvent("MyNamespace", "MySystem", "ShowMessage", self, self.OnShowMessage)
        
    def OnShowMessage(self, args):
        message = args["message"]
        print("Message from server:", message)
```

客户端向服务端发送消息：

```python
# 客户端
def SendToServer(self, data):
    eventData = {"data": data}
    self.NotifyToServer("ClientData", eventData)
```

### 6. 调试技巧

```python
# 启用调试日志
import logging

class MySystem(ServerSystem):
    def __init__(self, namespace, systemName):
        super(MySystem, self).__init__(namespace, systemName)
        self.debug = True
        
    def DebugLog(self, message):
        """调试日志"""
        if self.debug:
            print("[DEBUG]", message)
            
    def DoSomething(self):
        self.DebugLog("Executing DoSomething")
        # 实现逻辑...
```

---

## 常见问题

### Q: 如何获取玩家位置？

```python
# 服务端
comp = serverApi.CreateComponent(playerId, "Minecraft", "pos")
pos = comp.GetPos()  # 返回 (x, y, z) 元组
```

### Q: 如何给玩家添加物品？

```python
# 服务端
comp = serverApi.CreateComponent(playerId, "Minecraft", "item")
itemDict = {
    "itemName": "minecraft:diamond",
    "count": 1,
    "auxValue": 0
}
comp.SpawnItemToPlayerInv(itemDict, playerId)
```

### Q: 如何检测玩家点击方块？

```python
# 服务端系统
def __init__(self, namespace, systemName):
    super(MySystem, self).__init__(namespace, systemName)
    self.ListenForEvent("Minecraft", "Minecraft", "ServerPlayerTryTouchBlockEvent", self, self.OnBlockClick)
    
def OnBlockClick(self, args):
    playerId = args["playerId"]
    blockPos = args["blockPos"]  # (x, y, z)
    print(f"Player {playerId} clicked block at {blockPos}")
```

### Q: 如何修改玩家生命值？

```python
# 服务端
comp = serverApi.CreateComponent(playerId, "Minecraft", "attr")
comp.SetAttrValue(AttrType.HEALTH, 20.0)  # 设置生命值为20（满血）
```

### Q: 如何创建自定义 UI？

```python
# 客户端系统
def ShowCustomUI(self):
    # 创建 UI
    uiNode = self.CreateUI("MyMod", "path.to.MyUIScreen", "MyUI.main")
    
    # 获取 UI 控件
    button = uiNode.GetBaseUIControl("button_path")
    
    # 设置控件属性
    uiNode.SetVisible("button_path", True)
```

---

## 版本差异

### 3.4 vs 3.5

主要新增功能（3.5）：

1. **DrawingCompClient** - 新增绘图组件，支持在游戏中绘制各种形状
   - 盒子、线条、圆形、箭头、文本、球体等

2. **DrawingShapeCompClient** - 形状控制组件
   - 控制绘制形状的显示、隐藏、位置等

使用建议：

- 稳定项目推荐使用 3.4 版本
- 需要绘图功能的项目使用 3.5 版本
- 两个版本的核心 API 基本兼容

---

## 示例项目

### 简单的欢迎系统

```python
# server/welcomeSystem.py
import mod.server.extraServerApi as serverApi

class WelcomeSystem(serverApi.ServerSystem):
    def __init__(self, namespace, systemName):
        super(WelcomeSystem, self).__init__(namespace, systemName)
        
        # 监听玩家加入事件
        self.ListenForEvent(
            "Minecraft",
            "Minecraft", 
            "PlayerJoinEvent",
            self,
            self.OnPlayerJoin
        )
        
    def OnPlayerJoin(self, args):
        """玩家加入时发送欢迎消息"""
        playerId = args["playerId"]
        
        # 获取玩家名字组件
        nameComp = serverApi.CreateComponent(playerId, "Minecraft", "name")
        playerName = nameComp.GetName()
        
        # 向玩家发送欢迎消息
        self.NotifyToClient(playerId, "ShowWelcome", {
            "message": f"欢迎 {playerName} 加入游戏！"
        })
        
    def OnDestroy(self):
        """清理资源"""
        self.UnListenForEvent(
            "Minecraft",
            "Minecraft",
            "PlayerJoinEvent",
            self,
            self.OnPlayerJoin
        )
```

```python
# client/welcomeSystem.py
import mod.client.extraClientApi as clientApi

class WelcomeClientSystem(clientApi.ClientSystem):
    def __init__(self, namespace, systemName):
        super(WelcomeClientSystem, self).__init__(namespace, systemName)
        
        # 监听服务端发来的欢迎消息
        self.ListenForEvent(
            "WelcomeMod",
            "WelcomeSystem",
            "ShowWelcome",
            self,
            self.OnShowWelcome
        )
        
    def OnShowWelcome(self, args):
        """显示欢迎消息"""
        message = args["message"]
        
        # 在聊天栏显示消息
        comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "game")
        comp.AddChatTips(message)
        
    def OnDestroy(self):
        """清理资源"""
        self.UnListenForEvent(
            "WelcomeMod",
            "WelcomeSystem",
            "ShowWelcome",
            self,
            self.OnShowWelcome
        )
```

---

## 参考资源

### 官方资源

- 网易我的世界开发者平台
- Minecraft Bedrock Edition 文档

### 社区资源

- 相关开发者论坛
- GitHub 示例项目

---

## 更新日志

### 最新版本

- 添加了完整的 API 文档
- 包含 3.4 和 3.5 版本的 API 说明
- 添加了示例代码和最佳实践

---

## 贡献

欢迎提交问题和改进建议！

## 许可证

本文档基于 SDK 的使用说明编写，仅供学习和开发参考。
