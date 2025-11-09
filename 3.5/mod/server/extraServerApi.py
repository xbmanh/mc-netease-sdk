# -*- coding: utf-8 -*-
"""
服务端API模块 (Server API Module)

本模块是Minecraft网易版MOD开发的核心服务端API，提供了服务端系统和组件的注册、
创建、管理功能，以及各种游戏逻辑相关的工具函数。

=================================================================================================
主要功能分类
=================================================================================================

1. 系统管理 (System Management)
   - RegisterSystem: 注册服务端系统
   - GetSystem: 获取已注册的系统实例
   - GetServerSystemCls: 获取ServerSystem基类

2. 组件管理 (Component Management)
   - RegisterComponent: 注册自定义组件
   - CreateComponent: 创建实体组件
   - GetComponent: 获取实体组件
   - DestroyComponent: 销毁实体组件
   - GetComponentCls: 获取组件基类
   - GetEngineCompFactory: 获取引擎组件工厂

3. 实体管理 (Entity Management)
   - GetPlayerList: 获取所有玩家列表
   - GetEngineActor: 获取所有实体
   - GetHostPlayerId: 获取房主ID
   - SetEntityLimit/GetEntityLimit: 管理实体数量上限

4. 坐标与方向 (Coordinates & Directions)
   - GetLocalPosFromWorld: 世界坐标转局部坐标
   - GetWorldPosFromLocal: 局部坐标转世界坐标
   - GetDirFromRot: 旋转角度转朝向
   - GetRotFromDir: 朝向转旋转角度
   - GetIntPos: 获取方块坐标

5. 射线检测 (Raycasting)
   - getEntitiesOrBlockFromRay: 射线检测实体和方块

6. 性能分析 (Profiling)
   - StartProfile/StopProfile: 性能分析
   - StartMemProfile/StopMemProfile: 内存分析
   - StartMultiProfile/StopMultiProfile: 双端分析

7. 网络与事件监控 (Network & Event Monitoring)
   - StartRecordPacket/StopRecordPacket: 网络包统计
   - StartRecordEvent/StopRecordEvent: 事件统计

8. 协程支持 (Coroutine Support)
   - StartCoroutine: 开启协程
   - StopCoroutine: 停止协程

9. 环境信息 (Environment Info)
   - IsInServer: 是否在服务器环境
   - IsInApollo: 是否在Apollo网络服环境
   - GetPlatform: 获取运行平台
   - GetMinecraftVersion: 获取Minecraft版本

10. 工具函数 (Utilities)
    - GetMinecraftEnum: 获取枚举值
    - GetLevelId: 获取关卡ID
    - ImportModule: 导入模块
    - GetServerTickTime: 获取服务端帧时间

=================================================================================================
快速开始示例
=================================================================================================

>>> # 1. 注册服务端系统
>>> import mod.server.extraServerApi as serverApi
>>> 
>>> @serverApi.RegisterSystem("MyMod", "MyServerSystem", "path.to.MyServerSystem")
>>> class MyServerSystem(serverApi.ServerSystem):
...     def __init__(self, namespace, systemName):
...         super(MyServerSystem, self).__init__(namespace, systemName)
...         # 监听玩家加入事件
...         self.ListenForEvent("Minecraft", "Minecraft", "PlayerJoinEvent", 
...                           self, self.OnPlayerJoin)
...     
...     def OnPlayerJoin(self, args):
...         playerId = args["playerId"]
...         print(f"玩家 {playerId} 加入游戏")
...         
...         # 获取玩家生命值
...         comp = serverApi.GetEngineCompFactory().CreateComponent(
...             playerId, "Minecraft", "attr"
...         )
...         health = comp.GetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH)
...         print(f"玩家生命值: {health}")
...     
...     def OnDestroy(self):
...         pass

>>> # 2. 创建和使用组件
>>> comp_factory = serverApi.GetEngineCompFactory()
>>> 
>>> # 创建属性组件
>>> attr_comp = comp_factory.CreateComponent(entityId, "Minecraft", "attr")
>>> attr_comp.SetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH, 20.0)
>>> 
>>> # 创建标签组件
>>> tag_comp = comp_factory.CreateComponent(entityId, "Minecraft", "tag")
>>> tag_comp.AddEntityTag("custom_mob")

>>> # 3. 使用工具函数
>>> # 获取所有玩家
>>> player_list = serverApi.GetPlayerList()
>>> for player_id in player_list:
...     print(f"玩家ID: {player_id}")
>>> 
>>> # 射线检测
>>> results = serverApi.getEntitiesOrBlockFromRay(
...     dimensionId=0,
...     pos=(0, 64, 0),
...     rot=(0, 0, 0),
...     distance=100
... )

=================================================================================================
注意事项
=================================================================================================

1. 系统注册
   - 必须在MOD加载时注册系统
   - 系统名称在命名空间内必须唯一
   - 继承ServerSystem基类实现自定义系统

2. 组件使用
   - 优先使用CreateComponent而非GetComponent
   - 组件创建后会自动缓存，重复创建返回同一实例
   - 使用DestroyComponent清理不需要的组件

3. 性能优化
   - 使用协程处理复杂计算，避免卡顿
   - 合理使用性能分析工具定位瓶颈
   - 注意实体数量限制，避免过多实体

4. 调试技巧
   - 使用StartProfile进行性能分析
   - 使用StartRecordPacket监控网络通信
   - 检查GetServerTickTime监控帧时间

=================================================================================================
相关文档
=================================================================================================

- API文档: API_DOCUMENTATION.md
- 组件参考: COMPONENT_REFERENCE.md
- 快速参考: QUICK_REFERENCE.md
- 客户端API: mod.client.extraClientApi

=================================================================================================
"""

from typing import Generator
from typing import Tuple
from typing import Union
from typing import List
from mod.server.component.engineCompFactoryServer import EngineCompFactoryServer
from typing import Any
from typing import Callable
from mod.server.gamePlay.AI.customGoal import CustomGoal
from mod.server.system.serverSystem import ServerSystem
from typing import Type
from mod.common.component.baseComponent import BaseComponent
import mod.common.minecraftEnum as minecraftEnum

def RegisterComponent(nameSpace, name, clsPath):
    # type: (str, str, str) -> 'bool'
    """
    注册自定义组件到引擎
    
    将自定义组件类注册到MOD引擎中，注册后可以通过CreateComponent创建该组件的实例。
    注册通常在MOD初始化阶段完成。
    
    Args:
        nameSpace (str): 命名空间，通常使用MOD的名称，如"MyMod"
        name (str): 组件名称，在命名空间内必须唯一
        clsPath (str): 组件类的完整路径，如"mymod.components.MyComponent"
        
    Returns:
        bool: 注册成功返回True，失败返回False
        
    示例:
        >>> import mod.server.extraServerApi as serverApi
        >>> 
        >>> # 注册自定义组件
        >>> serverApi.RegisterComponent("MyMod", "customComp", "mymod.components.CustomComponent")
        >>> 
        >>> # 之后可以创建该组件
        >>> comp = serverApi.CreateComponent(entityId, "MyMod", "customComp")
        
    注意:
        - 组件类必须继承自BaseComponent
        - 命名空间和名称组合必须唯一
        - 建议在系统初始化时注册所有组件
        - clsPath必须是可导入的有效Python路径
    
    相关方法:
        - CreateComponent: 创建已注册的组件实例
        - GetComponentCls: 获取组件基类
    """
    pass

def RegisterSystem(nameSpace, systemName, clsPath):
    # type: (str, str, str) -> 'ServerSystem'
    """
    注册服务端系统到引擎
    
    将系统注册到MOD引擎中，引擎会创建该系统的实例并管理其生命周期。
    系统是MOD的核心逻辑单元，可以监听事件、执行Tick函数、与客户端通讯等。
    
    Args:
        nameSpace (str): 命名空间，建议使用MOD名称
        systemName (str): 系统名称，在命名空间内必须唯一
        clsPath (str): 系统类的完整路径
        
    Returns:
        ServerSystem: 返回创建的系统实例
        
    示例:
        >>> import mod.server.extraServerApi as serverApi
        >>> 
        >>> @serverApi.RegisterSystem("MyMod", "MySystem", "mymod.systems.MyServerSystem")
        >>> class MyServerSystem(serverApi.ServerSystem):
        ...     def __init__(self, namespace, systemName):
        ...         super(MyServerSystem, self).__init__(namespace, systemName)
        ...         # 监听事件
        ...         self.ListenForEvent("Minecraft", "Minecraft", "PlayerJoinEvent",
        ...                           self, self.OnPlayerJoin)
        ...     
        ...     def OnPlayerJoin(self, args):
        ...         playerId = args["playerId"]
        ...         print(f"玩家 {playerId} 加入游戏")
        ...     
        ...     def Update(self):
        ...         # 每tick执行一次
        ...         pass
        ...     
        ...     def OnDestroy(self):
        ...         # 清理资源
        ...         pass
        
    注意:
        - 系统类必须继承自ServerSystem
        - 使用装饰器语法@RegisterSystem最为方便
        - 系统在游戏退出时会自动调用OnDestroy
        - 一个命名空间可以有多个系统
    
    相关方法:
        - GetSystem: 获取已注册的系统实例
        - GetServerSystemCls: 获取ServerSystem基类
    """
    pass

def GetSystem(nameSpace, systemName):
    # type: (str, str) -> 'ServerSystem'
    """
    获取已注册的系统实例
    
    通过命名空间和系统名称获取已注册的系统实例，用于系统间通讯。
    
    Args:
        nameSpace (str): 系统的命名空间
        systemName (str): 系统名称
        
    Returns:
        ServerSystem: 系统实例，如果系统不存在返回None
        
    示例:
        >>> import mod.server.extraServerApi as serverApi
        >>> 
        >>> # 获取其他系统实例
        >>> other_system = serverApi.GetSystem("MyMod", "OtherSystem")
        >>> if other_system:
        ...     # 调用其他系统的方法
        ...     other_system.DoSomething()
        
    应用场景:
        >>> # 系统间协作
        >>> class MainSystem(serverApi.ServerSystem):
        ...     def CallOtherSystem(self):
        ...         other = serverApi.GetSystem("MyMod", "HelperSystem")
        ...         if other:
        ...             result = other.CalculateSomething()
        ...             return result
        
    注意:
        - 系统必须已经注册才能获取
        - 建议在使用前检查返回值是否为None
        - 避免循环依赖导致的问题
    
    相关方法:
        - RegisterSystem: 注册系统
    """
    pass

def CreateComponent(entityId, nameSpace, name):
    # type: (Union[str,int], str, str) -> 'BaseComponent'
    """
    为实体创建或获取服务端组件
    
    为指定实体创建组件实例。如果组件已存在，则返回现有实例（单例模式）。
    这是使用组件的主要方法。
    
    Args:
        entityId (Union[str, int]): 实体ID，可以是字符串或整数
        nameSpace (str): 组件的命名空间，如"Minecraft"表示引擎组件
        name (str): 组件名称
        
    Returns:
        BaseComponent: 组件实例，如果创建失败返回None
        
    示例:
        >>> import mod.server.extraServerApi as serverApi
        >>> 
        >>> # 创建引擎组件
        >>> comp_factory = serverApi.GetEngineCompFactory()
        >>> attr_comp = comp_factory.CreateComponent(playerId, "Minecraft", "attr")
        >>> 
        >>> # 或直接使用CreateComponent
        >>> tag_comp = serverApi.CreateComponent(entityId, "Minecraft", "tag")
        >>> tag_comp.AddEntityTag("custom")
        
    常用引擎组件:
        >>> # 属性组件
        >>> attr_comp = serverApi.CreateComponent(entityId, "Minecraft", "attr")
        >>> attr_comp.SetAttrValue(AttrType.HEALTH, 20.0)
        >>> 
        >>> # 位置组件
        >>> pos_comp = serverApi.CreateComponent(entityId, "Minecraft", "pos")
        >>> pos = pos_comp.GetPos()
        >>> 
        >>> # 物品组件
        >>> item_comp = serverApi.CreateComponent(playerId, "Minecraft", "item")
        >>> item_comp.SpawnItemToPlayerInv(itemDict, playerId)
        
    注意:
        - 组件遵循单例模式，多次创建返回同一实例
        - 优先使用CreateComponent而非GetComponent
        - entityId必须是有效的实体ID
        - 组件在实体销毁时自动清理
    
    相关方法:
        - GetComponent: 检查组件是否存在
        - DestroyComponent: 销毁组件
        - GetEngineCompFactory: 获取引擎组件工厂
    """
    pass

def GetComponent(entityId, nameSpace, name):
    # type: (str, str, str) -> 'BaseComponent'
    """
    获取实体的服务端组件（仅用于检查）
    
    检查实体是否已创建指定组件。一般仅用于判断组件是否存在，
    其他情况请使用CreateComponent。
    
    Args:
        entityId (str): 实体ID
        nameSpace (str): 组件命名空间
        name (str): 组件名称
        
    Returns:
        BaseComponent: 如果组件存在返回组件实例，否则返回None
        
    示例:
        >>> import mod.server.extraServerApi as serverApi
        >>> 
        >>> # 检查组件是否已创建
        >>> comp = serverApi.GetComponent(entityId, "Minecraft", "tag")
        >>> if comp:
        ...     print("标签组件已存在")
        ...     tags = comp.GetEntityTags()
        ... else:
        ...     print("标签组件不存在")
        
    应用场景:
        >>> # 条件性创建组件
        >>> if not serverApi.GetComponent(entityId, "MyMod", "customComp"):
        ...     # 首次创建
        ...     comp = serverApi.CreateComponent(entityId, "MyMod", "customComp")
        ...     comp.Initialize()
        
    注意:
        - 主要用于检查组件是否存在
        - 大多数情况应使用CreateComponent
        - 返回None不表示错误，只是组件未创建
    
    相关方法:
        - CreateComponent: 创建或获取组件（推荐）
    """
    pass

def DestroyComponent(entityId, nameSpace, name):
    # type: (str, str, str) -> 'None'
    """
    删除实体的服务端组件
    """
    pass

def GetEngineCompFactory():
    # type: () -> 'EngineCompFactoryServer'
    """
    获取引擎组件的工厂，通过工厂可以创建服务端的引擎组件
    """
    pass

def GetMinecraftEnum():
    # type: () -> 'minecraftEnum'
    """
    用于获取枚举值文档中的枚举值
    """
    pass

def GetServerSystemCls():
    # type: () -> 'Type[ServerSystem]'
    """
    用于获取服务器system基类。实现新的system时，需要继承该接口返回的类
    """
    pass

def GetComponentCls():
    # type: () -> 'Type[BaseComponent]'
    """
    用于获取服务器component基类。实现新的component时，需要继承该接口返回的类
    """
    pass

def GetEngineNamespace():
    # type: () -> 'str'
    """
    获取引擎事件的命名空间。监听引擎事件时，namespace传该接口返回的namespace
    """
    pass

def GetEngineSystemName():
    # type: () -> 'str'
    """
    获取引擎系统名。监听引擎事件时，systemName传该接口返回的systemName
    """
    pass

def GetLevelId():
    # type: () -> 'str'
    """
    获取levelId。某些组件需要levelId创建，可以用此接口获取levelId。其中level即为当前地图的游戏。
    """
    pass

def GetEngineActor():
    # type: () -> 'dict'
    """
    获取所有维度中已加载的所有实体（不包含玩家）。
    """
    pass

def getEntitiesOrBlockFromRay(dimensionId, pos, rot, distance=16, isThrough=False, filterType=1):
    # type: (int, Tuple[float,float,float], Tuple[float,float,float], int, bool, minecraftEnum) -> 'List[dict]'
    """
    从指定位置发射一条射线，获取与射线相交的实体和方块
    """
    pass

def GetPlayerList():
    # type: () -> 'List[str]'
    """
    获取所有维度中的全部玩家的id列表
    """
    pass

def SetEntityLimit(num):
    # type: (int) -> 'bool'
    """
    设置世界最大可生成实体数量上限。可生成实体指具有spawnrule的实体。当前世界上被加载的可生成实体数量超过这个上限时，生物就不会再通过spawnrule刷出。
    """
    pass

def GetEntityLimit():
    # type: () -> 'int'
    """
    获取世界最大可生成实体数量上限。可生成实体的含义见SetEntityLimit
    """
    pass

def GetLocalPosFromWorld(pos, entityId):
    # type: (Tuple[float,float,float], str) -> 'Tuple[float,float,float]'
    """
    获取基于实体的世界坐标对应的局部坐标
    """
    pass

def GetWorldPosFromLocal(pos, entityId):
    # type: (Tuple[float,float,float], str) -> 'Tuple[float,float,float]'
    """
    获取基于实体的局部坐标对应的世界坐标
    """
    pass

def GetDirFromRot(rot):
    # type: (Tuple[float,float]) -> 'Tuple[float,float,float]'
    """
    通过旋转角度获取朝向
    """
    pass

def GetRotFromDir(dir):
    # type: (Tuple[float,float,float]) -> 'Tuple[float,float]'
    """
    通过朝向获取旋转角度
    """
    pass

def StartProfile():
    # type: () -> 'bool'
    """
    开始启动服务端脚本性能分析，启动后调用StopProfile即可在路径fileName生成函数性能火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。
    """
    pass

def StopProfile(fileName=None):
    # type: (str) -> 'bool'
    """
    停止服务端脚本性能分析并生成火焰图，与StartProfile配合使用，此接口只支持PC端
    """
    pass

def StartMemProfile():
    # type: () -> 'bool'
    """
    开始启动服务端脚本内存分析，启动后调用StopMemProfile即可在路径fileName生成函数内存火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。
    """
    pass

def StopMemProfile(fileName=None):
    # type: (str) -> 'bool'
    """
    停止服务端脚本内存分析并生成火焰图，与StartMemProfile配合使用，此接口只支持PC端
    """
    pass

def StartMultiProfile():
    # type: () -> 'bool'
    """
    开始启动服务端与客户端双端脚本性能分析，启动后调用StopMultiProfile即可在路径fileName生成函数性能火焰图。双端采集时数据误差较大，建议优先使用StartProfile单端版本，此接口只支持PC端
    """
    pass

def StopMultiProfile(fileName=None):
    # type: (str) -> 'bool'
    """
    停止双端脚本性能分析并生成火焰图，与StartMultiProfile配合使用，此接口只支持PC端
    """
    pass

def StartRecordPacket():
    # type: () -> 'bool'
    """
    开始启动服务端与客户端之间的引擎收发包统计，启动后调用StopRecordPacket即可获取两个函数调用之间引擎收发包的统计信息，仅支持租赁服与Apollo网络服环境（不支持单机环境）
    """
    pass

def StopRecordPacket():
    # type: () -> 'dict'
    """
    停止服务端与客户端之间的引擎收发包统计并输出结果，与StartRecordPacket配合使用，输出结果为字典，key为网络包名，value字典中记录收发信息，具体见示例，仅支持租赁服与Apollo网络服环境（不支持单机环境）
    """
    pass

def StartRecordEvent():
    # type: () -> 'bool'
    """
    开始启动服务端与客户端之间的脚本事件收发统计，启动后调用StopRecordEvent即可获取两个函数调用之间脚本事件收发的统计信息，仅支持租赁服与Apollo网络服环境（不支持单机环境）
    """
    pass

def StopRecordEvent():
    # type: () -> 'dict'
    """
    停止服务端与客户端之间的脚本事件收发统计并输出结果，与StartRecordEvent配合使用，输出结果为字典，key为网络包名，value字典中记录收发信息，具体见示例，仅支持租赁服与Apollo网络服环境（不支持单机环境）
    """
    pass

def IsInServer():
    # type: () -> 'bool'
    """
    获取当前游戏是否跑在服务器环境下
    """
    pass

def IsInApollo():
    # type: () -> 'bool'
    """
    返回当前游戏Mod是否运行在Apollo网络服
    """
    pass

def AddEntityTickEventWhiteList(identifier):
    # type: (str) -> 'bool'
    """
    添加实体类型到EntityTickServerEvent事件的触发白名单。
    """
    pass

def GetPlatform():
    # type: () -> 'int'
    """
    获取脚本运行的平台
    """
    pass

def GetCustomGoalCls():
    # type: () -> 'Type[CustomGoal]'
    """
    用于获取服务器自定义行为节点的基类。实现新的行为节点时，需要继承该接口返回的类
    """
    pass

def StartCoroutine(iterOrFunc, callback=None):
    # type: (Union[Generator,Callable[[], Generator]], function) -> 'Generator'
    """
    开启服务端协程，实现函数分段式执行，可用于缓解复杂逻辑计算导致游戏卡顿问题
    """
    pass

def StopCoroutine(iter):
    # type: (Generator) -> 'bool'
    """
    停止协程
    """
    pass

def GetServerTickTime():
    # type: () -> 'float'
    """
    获取服务端引擎上一帧的帧消耗时间
    """
    pass

def SetMcpModLogCanPostDump(canPost):
    # type: (bool) -> 'None'
    """
    设置是否可以打印错误信息到McpModLog日志。
    """
    pass

def GetMcpModLogCanPostDump():
    # type: () -> 'bool'
    """
    获取是否可以打印错误信息到McpModLog日志。
    """
    pass

def PostMcpModDump(msg, *args, **kwargs):
    # type: (str, Any, dict) -> 'None'
    """
    主动打印信息到McpModLog日志，需要先调用 SetMcpModLogCanPostDump 接口进行设置，才能生效。
    """
    pass

def ImportModule(path):
    # type: (str) -> 'Any'
    """
    使用字符串路径导入模块，作用与importlib.import_module类似，但只能导入当前加载的mod中的模块
    """
    pass

def GetMinecraftVersion():
    # type: () -> 'str'
    """
    获取Minecraft版本-服务端。
    """
    pass

def GetIntPos(pos):
    # type: (Tuple[float,float,float]) -> 'Tuple[int,int,int]'
    """
    获取坐标所在方块的位置，即浮点数坐标向下取整后的整数坐标。
    """
    pass

def GetHostPlayerId():
    # type: () -> 'str'
    """
    获取房主的entityId
    """
    pass

