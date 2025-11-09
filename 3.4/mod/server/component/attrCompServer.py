# -*- coding: utf-8 -*-
"""
属性组件服务端模块

本模块提供实体属性管理功能，用于获取和修改实体的各种引擎属性。
引擎属性包括生命值、移动速度、攻击力、防御力等核心游戏属性。

主要功能：
    - 获取和设置实体的各类属性值
    - 管理属性的最大值
    - 控制实体的着火状态
    - 设置玩家的台阶高度
    - 管理实体持久化状态

使用场景：
    - 修改生物的生命值和移动速度
    - 创建自定义属性系统
    - 实现BUFF和DEBUFF效果
    - 控制实体的特殊状态（如着火、无敌等）

属性类型常用枚举：
    - AttrType.HEALTH: 生命值
    - AttrType.MAX_HEALTH: 最大生命值  
    - AttrType.MOVEMENT: 移动速度
    - AttrType.ATTACK: 攻击力
    - AttrType.DEFENSE: 防御力
    
示例：
    >>> import mod.server.extraServerApi as serverApi
    >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "attr")
    >>> # 设置生命值为20（10颗心）
    >>> comp.SetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH, 20.0)
    >>> # 获取当前生命值
    >>> health = comp.GetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH)
"""

from typing import List
from mod.common.component.baseComponent import BaseComponent

class AttrCompServer(BaseComponent):
    """
    属性组件服务端类
    
    用于管理实体的各种引擎属性，包括生命值、速度、攻击力等。
    """
    
    def SetAttrValue(self, attrType, value, setDefault=1):
        # type: (int, float, int) -> 'bool'
        """
        设置实体的引擎属性值
        
        修改实体的指定属性为新值。可以设置各种引擎属性，如生命值、移动速度等。
        
        Args:
            attrType (int): 属性类型，使用AttrType枚举值，如AttrType.HEALTH
            value (float): 要设置的属性值，具体范围取决于属性类型
            setDefault (int, optional): 是否同时设置默认值。1表示设置，0表示不设置。默认为1
            
        Returns:
            bool: 设置成功返回True，失败返回False
            
        示例：
            >>> import mod.server.extraServerApi as serverApi
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "attr")
            >>> 
            >>> # 设置生命值为20（10颗心）
            >>> attrType = serverApi.GetMinecraftEnum().AttrType.HEALTH
            >>> comp.SetAttrValue(attrType, 20.0)
            >>> 
            >>> # 设置移动速度为原来的1.5倍
            >>> speedType = serverApi.GetMinecraftEnum().AttrType.MOVEMENT
            >>> comp.SetAttrValue(speedType, 0.15)  # 默认速度约0.1
            
        常用属性类型：
            >>> # 设置不同类型的属性
            >>> enum = serverApi.GetMinecraftEnum()
            >>> comp.SetAttrValue(enum.AttrType.HEALTH, 40.0)  # 生命值
            >>> comp.SetAttrValue(enum.AttrType.ATTACK, 10.0)  # 攻击力
            >>> comp.SetAttrValue(enum.AttrType.MOVEMENT, 0.2) # 移动速度
            
        注意事项：
            - 属性值受最大值限制，超过最大值会被限制为最大值
            - 某些属性修改后需要重新加载才能生效
            - setDefault参数影响实体重生后的属性值
            - 建议先用GetAttrMaxValue检查最大值，避免设置无效值
        
        相关方法：
            - GetAttrValue: 获取属性值
            - SetAttrMaxValue: 设置属性最大值
        """
        pass

    def GetAttrValue(self, attrType):
        # type: (int) -> 'float'
        """
        获取实体的引擎属性当前值
        
        返回实体指定属性的当前值。
        
        Args:
            attrType (int): 属性类型，使用AttrType枚举值
            
        Returns:
            float: 属性的当前值
            
        示例：
            >>> import mod.server.extraServerApi as serverApi
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "attr")
            >>> 
            >>> # 获取当前生命值
            >>> enum = serverApi.GetMinecraftEnum()
            >>> health = comp.GetAttrValue(enum.AttrType.HEALTH)
            >>> print(f"当前生命值: {health}")
            >>> 
            >>> # 检查生命值百分比
            >>> max_health = comp.GetAttrMaxValue(enum.AttrType.HEALTH)
            >>> health_percent = (health / max_health) * 100
            >>> print(f"生命值百分比: {health_percent}%")
            
        使用场景：
            >>> # 根据生命值执行不同逻辑
            >>> health = comp.GetAttrValue(enum.AttrType.HEALTH)
            >>> if health < 10:
            ...     print("生命值过低，触发警告")
            ... elif health < 5:
            ...     # 触发濒死状态
            ...     pass
            
        注意：
            - 返回的是实时值，会随游戏进行而变化
            - 建议配合GetAttrMaxValue使用以计算百分比
        
        相关方法：
            - SetAttrValue: 设置属性值
            - GetAttrMaxValue: 获取属性最大值
        """
        pass

    def SetAttrMaxValue(self, type, value):
        # type: (int, float) -> 'bool'
        """
        设置实体引擎属性的最大值
        
        修改指定属性的最大值上限。当前值如果超过新的最大值会被调整。
        
        Args:
            type (int): 属性类型，使用AttrType枚举值
            value (float): 新的最大值
            
        Returns:
            bool: 设置成功返回True，失败返回False
            
        示例：
            >>> import mod.server.extraServerApi as serverApi
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "attr")
            >>> enum = serverApi.GetMinecraftEnum()
            >>> 
            >>> # 设置最大生命值为100（50颗心）
            >>> comp.SetAttrMaxValue(enum.AttrType.HEALTH, 100.0)
            >>> # 设置当前生命值也为100
            >>> comp.SetAttrValue(enum.AttrType.HEALTH, 100.0)
            
        应用场景：
            >>> # 实现等级系统，提升最大生命值
            >>> def LevelUp(entity_id, level):
            ...     comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...         entity_id, "Minecraft", "attr"
            ...     )
            ...     enum = serverApi.GetMinecraftEnum()
            ...     
            ...     # 每级增加10点最大生命值
            ...     max_health = 20 + (level * 10)
            ...     comp.SetAttrMaxValue(enum.AttrType.HEALTH, max_health)
            ...     comp.SetAttrValue(enum.AttrType.HEALTH, max_health)  # 恢复满血
            
        注意：
            - 降低最大值会自动调整当前值，不会超过新的最大值
            - 最大值设置会影响属性恢复的上限
        
        相关方法：
            - GetAttrMaxValue: 获取最大值
            - SetAttrValue: 设置当前值
        """
        pass

    def GetAttrMaxValue(self, type):
        # type: (int) -> 'float'
        """
        获取实体引擎属性的最大值
        
        返回指定属性的最大值上限。
        
        Args:
            type (int): 属性类型，使用AttrType枚举值
            
        Returns:
            float: 属性的最大值
            
        示例：
            >>> import mod.server.extraServerApi as serverApi
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "attr")
            >>> enum = serverApi.GetMinecraftEnum()
            >>> 
            >>> # 获取最大生命值
            >>> max_health = comp.GetAttrMaxValue(enum.AttrType.HEALTH)
            >>> print(f"最大生命值: {max_health}")
            >>> 
            >>> # 计算生命值百分比
            >>> current_health = comp.GetAttrValue(enum.AttrType.HEALTH)
            >>> percent = (current_health / max_health) * 100
            
        相关方法：
            - SetAttrMaxValue: 设置最大值
            - GetAttrValue: 获取当前值
        """
        pass

    def IsEntityOnFire(self):
        # type: () -> 'bool'
        """
        检查实体是否处于着火状态
        
        判断实体当前是否在燃烧。
        
        Returns:
            bool: 实体着火返回True，否则返回False
            
        示例：
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "attr")
            >>> if comp.IsEntityOnFire():
            ...     print("实体正在燃烧！")
            ...     # 可以执行灭火逻辑
            
        相关方法：
            - SetEntityOnFire: 设置实体着火
        """
        pass

    def SetEntityOnFire(self, seconds, burn_damage=1):
        # type: (int, int) -> 'bool'
        """
        设置实体进入着火状态
        
        使实体燃烧指定时间，并造成火焰伤害。
        
        Args:
            seconds (int): 燃烧持续时间（秒），必须大于0
            burn_damage (int, optional): 每秒造成的火焰伤害。默认为1
            
        Returns:
            bool: 设置成功返回True，失败返回False
            
        示例：
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "attr")
            >>> 
            >>> # 让实体燃烧5秒，每秒1点伤害
            >>> comp.SetEntityOnFire(5, 1)
            >>> 
            >>> # 让实体燃烧10秒，每秒2点伤害
            >>> comp.SetEntityOnFire(10, 2)
            
        应用场景：
            >>> # 实现火焰陷阱
            >>> def OnPlayerEnterFireTrap(player_id):
            ...     comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "attr"
            ...     )
            ...     comp.SetEntityOnFire(8, 1)  # 燃烧8秒
            
        注意：
            - 火焰会随时间自然熄灭
            - 在水中会加速熄灭
            - burn_damage为0时只有视觉效果，不造成伤害
        
        相关方法：
            - IsEntityOnFire: 检查是否着火
        """
        pass

    def SetStepHeight(self, stepHeight):
        # type: (float) -> 'bool'
        """
        设置玩家能上的最大台阶高度
        
        修改玩家在非跳跃状态下前进时能够自动上的台阶高度。
        默认值为0.5625，设置为1.0表示能上一格方块高度。
        
        Args:
            stepHeight (float): 台阶高度，单位为方块。范围建议0.0-2.0
            
        Returns:
            bool: 设置成功返回True，失败返回False
            
        示例：
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(playerId, "Minecraft", "attr")
            >>> 
            >>> # 允许玩家直接走上一格方块
            >>> comp.SetStepHeight(1.0)
            >>> 
            >>> # 设置为默认值
            >>> comp.SetStepHeight(0.5625)
            >>> 
            >>> # 降低台阶高度，只能上半格
            >>> comp.SetStepHeight(0.5)
            
        应用场景：
            >>> # 给予玩家特殊能力
            >>> def GiveClimbAbility(player_id):
            ...     comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "attr"
            ...     )
            ...     comp.SetStepHeight(1.5)  # 可以直接走上1.5格高度
            
        注意：
            - 只对玩家有效
            - 设置过高可能影响游戏体验
            - 建议配合ResetStepHeight在效果结束后恢复默认值
        
        相关方法：
            - GetStepHeight: 获取当前台阶高度
            - ResetStepHeight: 恢复默认台阶高度
        """
        pass

    def GetStepHeight(self):
        # type: () -> 'float'
        """
        获取玩家当前能上的最大台阶高度
        
        返回玩家在非跳跃状态下能够自动上的台阶高度。
        
        Returns:
            float: 当前台阶高度值（方块单位）
            
        示例：
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(playerId, "Minecraft", "attr")
            >>> height = comp.GetStepHeight()
            >>> print(f"当前台阶高度: {height}")
            
        相关方法：
            - SetStepHeight: 设置台阶高度
        """
        pass

    def ResetStepHeight(self):
        # type: () -> 'bool'
        """
        恢复玩家台阶高度为引擎默认值
        
        将玩家的台阶高度重置为默认值0.5625。
        
        Returns:
            bool: 重置成功返回True，失败返回False
            
        示例：
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(playerId, "Minecraft", "attr")
            >>> comp.ResetStepHeight()
            
        应用场景：
            >>> # BUFF效果结束后恢复默认值
            >>> def RemoveClimbBuff(player_id):
            ...     comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "attr"
            ...     )
            ...     comp.ResetStepHeight()
            
        相关方法：
            - SetStepHeight: 设置台阶高度
            - GetStepHeight: 获取台阶高度
        """
        pass

    def GetTypeFamily(self):
        # type: () -> 'List[str]'
        """
        获取生物的类型家族（type_family）
        
        返回生物行为包中定义的type_family字段，用于分类和识别生物类型。
        
        Returns:
            List[str]: 类型家族列表，如['mob', 'zombie', 'undead']
            
        示例：
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "attr")
            >>> families = comp.GetTypeFamily()
            >>> print(f"生物类型: {families}")
            >>> 
            >>> # 检查是否为亡灵生物
            >>> if 'undead' in families:
            ...     print("这是亡灵生物")
            
        应用场景：
            >>> # 根据生物类型执行不同逻辑
            >>> families = comp.GetTypeFamily()
            >>> if 'boss' in families:
            ...     # 特殊Boss逻辑
            ...     pass
            >>> elif 'passive' in families:
            ...     # 被动生物逻辑
            ...     pass
            
        注意：
            - 此字段由行为包定义，不同生物返回不同
            - 可用于实现基于类型的特殊效果
        """
        pass

    def SetPersistent(self, persistent):
        # type: (bool) -> 'bool'
        """
        设置实体是否持久化（不会因距离而被清除）
        
        控制实体是否会因为离玩家太远而被游戏自动清除。
        设置为True可以使实体永久保留。
        
        Args:
            persistent (bool): True表示持久化，False表示可被清除
            
        Returns:
            bool: 设置成功返回True，失败返回False
            
        示例：
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "attr")
            >>> 
            >>> # 设置为持久化，不会被清除
            >>> comp.SetPersistent(True)
            >>> 
            >>> # 允许被清除
            >>> comp.SetPersistent(False)
            
        应用场景：
            >>> # 创建重要NPC，确保不被清除
            >>> def CreateImportantNPC(entity_id):
            ...     comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...         entity_id, "Minecraft", "attr"
            ...     )
            ...     comp.SetPersistent(True)
            ...     
            ...     # 添加标签标记为重要NPC
            ...     tag_comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...         entity_id, "Minecraft", "tag"
            ...     )
            ...     tag_comp.AddEntityTag("important_npc")
            
        注意：
            - 过多持久化实体可能影响性能
            - 建议只对重要实体使用
            - 持久化实体仍会在世界卸载时被移除
        """
        pass

    def ResetToDefaultValue(self, type):
        # type: (int) -> 'bool'
        """
        重置实体引擎属性到默认值
        
        将指定属性恢复为实体定义时的默认值。
        
        Args:
            type (int): 属性类型，使用AttrType枚举值
            
        Returns:
            bool: 重置成功返回True，失败返回False
            
        示例：
            >>> import mod.server.extraServerApi as serverApi
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "attr")
            >>> enum = serverApi.GetMinecraftEnum()
            >>> 
            >>> # 重置生命值到默认值
            >>> comp.ResetToDefaultValue(enum.AttrType.HEALTH)
            >>> 
            >>> # 重置移动速度到默认值
            >>> comp.ResetToDefaultValue(enum.AttrType.MOVEMENT)
            
        应用场景：
            >>> # BUFF效果结束后恢复默认属性
            >>> def RemoveSpeedBuff(entity_id):
            ...     comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...         entity_id, "Minecraft", "attr"
            ...     )
            ...     enum = serverApi.GetMinecraftEnum()
            ...     comp.ResetToDefaultValue(enum.AttrType.MOVEMENT)
            
        相关方法：
            - ResetToMaxValue: 重置到最大值
        """
        pass

    def ResetToMaxValue(self, type):
        # type: (int) -> 'bool'
        """
        重置实体引擎属性到最大值
        
        将指定属性设置为其当前的最大值。常用于恢复满血等操作。
        
        Args:
            type (int): 属性类型，使用AttrType枚举值
            
        Returns:
            bool: 重置成功返回True，失败返回False
            
        示例：
            >>> import mod.server.extraServerApi as serverApi
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "attr")
            >>> enum = serverApi.GetMinecraftEnum()
            >>> 
            >>> # 恢复满血
            >>> comp.ResetToMaxValue(enum.AttrType.HEALTH)
            
        应用场景：
            >>> # 玩家使用治疗技能
            >>> def HealPlayer(player_id):
            ...     comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "attr"
            ...     )
            ...     enum = serverApi.GetMinecraftEnum()
            ...     comp.ResetToMaxValue(enum.AttrType.HEALTH)
            ...     print("玩家已恢复满血")
            
        注意：
            - 重置到最大值，而非默认值
            - 最大值可能已被SetAttrMaxValue修改过
        
        相关方法：
            - ResetToDefaultValue: 重置到默认值
            - GetAttrMaxValue: 获取最大值
        """
        pass

