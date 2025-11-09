# -*- coding: utf-8 -*-
"""
驯服组件服务端模块

本模块提供实体驯服功能的管理接口，允许开发者实现生物的驯服机制。
驯服后的生物会与玩家建立主从关系，但不包含骑乘功能。

主要功能：
    - 获取驯服生物的主人ID
    - 设置生物的驯服状态

使用场景：
    - 实现自定义宠物系统
    - 创建可驯服的生物
    - 管理生物与玩家的归属关系
    - 实现召唤兽或仆从系统

注意事项：
    - 此组件只处理驯服关系，不包含骑乘功能
    - 需要配合entityEvent组件使用以触发驯服事件
    - 建议结合AI组件实现驯服后的跟随行为

示例：
    >>> import mod.server.extraServerApi as serverApi
    >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "tame")
    >>> # 设置生物被玩家驯服
    >>> comp.SetEntityTamed(playerId, entityId)
    >>> # 获取驯服者ID
    >>> owner_id = comp.GetOwnerId()
"""

from mod.common.component.baseComponent import BaseComponent

class TameComponentServer(BaseComponent):
    """
    驯服组件服务端类
    
    用于管理生物的驯服状态和主人关系。驯服是指生物与玩家建立归属关系，
    成为玩家的宠物或随从。
    """
    
    def GetOwnerId(self):
        # type: () -> 'str'
        """
        获取驯服生物的主人ID
        
        返回当前驯服了该生物的玩家的实体ID。如果生物未被驯服，则返回空字符串。
        
        Returns:
            str: 主人的实体ID（玩家ID）。如果生物未被驯服，返回空字符串""
            
        示例：
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "tame")
            >>> owner_id = comp.GetOwnerId()
            >>> if owner_id:
            ...     print(f"这个生物的主人是: {owner_id}")
            ... else:
            ...     print("这个生物未被驯服")
            
        使用场景：
            >>> # 检查实体是否属于特定玩家
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(wolf_id, "Minecraft", "tame")
            >>> owner = comp.GetOwnerId()
            >>> if owner == current_player_id:
            ...     print("这是你的狼")
            ... else:
            ...     print("这不是你的狼")
            
        注意：
            - 只有被驯服的生物才会有主人ID
            - 主人离开游戏后，生物仍保持驯服状态
        
        相关方法：
            - SetEntityTamed: 设置生物的驯服状态
        """
        pass

    def SetEntityTamed(self, playerId, tamedId):
        # type: (str, str) -> 'bool'
        """
        设置生物被玩家驯服
        
        将指定的生物设置为被某个玩家驯服。此方法需要配合entityEvent组件使用，
        以触发相应的驯服事件。注意：此驯服功能不包含骑乘能力。
        
        Args:
            playerId (str): 主人的实体ID（玩家ID），不能为空
            tamedId (str): 被驯服生物的实体ID，不能为空
            
        Returns:
            bool: 设置成功返回True，失败返回False
            
        示例：
            >>> import mod.server.extraServerApi as serverApi
            >>> 
            >>> # 在玩家与生物交互时驯服生物
            >>> def OnPlayerInteract(args):
            ...     player_id = args['playerId']
            ...     entity_id = args['entityId']
            ...     
            ...     # 创建驯服组件
            ...     comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...         entity_id, "Minecraft", "tame"
            ...     )
            ...     
            ...     # 设置驯服
            ...     if comp.SetEntityTamed(player_id, entity_id):
            ...         print(f"生物 {entity_id} 已被玩家 {player_id} 驯服")
            ...         
            ...         # 可以配合entityEvent组件触发驯服效果
            ...         event_comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...             entity_id, "Minecraft", "entityEvent"
            ...         )
            ...         event_comp.TriggerEntityEvent("minecraft:on_tame")
            
        完整示例：
            >>> # 创建自定义宠物驯服系统
            >>> class PetSystem:
            ...     def TamePet(self, player_id, pet_id):
            ...         # 检查是否可以驯服
            ...         tame_comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...             pet_id, "Minecraft", "tame"
            ...         )
            ...         
            ...         if tame_comp.GetOwnerId():
            ...             return False  # 已被驯服
            ...         
            ...         # 执行驯服
            ...         if tame_comp.SetEntityTamed(player_id, pet_id):
            ...             # 触发驯服事件
            ...             event_comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...                 pet_id, "Minecraft", "entityEvent"
            ...             )
            ...             event_comp.TriggerEntityEvent("custom:tamed")
            ...             
            ...             # 添加驯服标签
            ...             tag_comp = serverApi.GetEngineCompFactory().CreateComponent(
            ...                 pet_id, "Minecraft", "tag"
            ...             )
            ...             tag_comp.AddEntityTag("tamed_pet")
            ...             
            ...             return True
            ...         return False
            
        注意事项：
            - 必须配合entityEvent组件使用，单独调用此方法不会触发驯服动画和音效
            - 此方法不包含骑乘功能，如需骑乘请使用其他相关组件
            - 驯服后建议配合AI组件实现跟随主人等行为
            - playerId和tamedId都必须是有效的实体ID
            - 驯服状态在生物被销毁前会一直保持
        
        相关组件：
            - entityEvent: 用于触发驯服事件和动画
            - ai: 用于实现驯服后的跟随等行为
            - tag: 可用于标记驯服状态
        
        相关方法：
            - GetOwnerId: 获取驯服者ID
        """
        pass

