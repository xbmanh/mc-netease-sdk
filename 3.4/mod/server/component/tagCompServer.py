# -*- coding: utf-8 -*-
"""
标签组件服务端模块

本模块提供实体标签管理功能，允许开发者为实体添加、删除和查询标签。
标签是附加到实体的字符串标识符，可用于分组、筛选和识别实体。

主要功能：
    - 获取实体的所有标签
    - 为实体添加新标签
    - 移除实体的指定标签
    - 检查实体是否拥有特定标签

使用场景：
    - 为特定类型的实体添加分类标签
    - 通过标签识别玩家创建的实体
    - 实现基于标签的实体筛选和查询
    - 标记特殊状态的实体（如"无敌"、"友好"等）

示例：
    >>> import mod.server.extraServerApi as serverApi
    >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "tag")
    >>> comp.AddEntityTag("custom_mob")
    >>> if comp.EntityHasTag("custom_mob"):
    ...     print("这是自定义生物")
"""

from typing import List
from mod.common.component.baseComponent import BaseComponent

class TagComponentServer(BaseComponent):
    """
    标签组件服务端类
    
    用于管理实体的标签系统。标签是附加到实体的字符串标识，可用于分类和识别。
    """
    
    def GetEntityTags(self):
        # type: () -> 'List[str]'
        """
        获取实体的所有标签列表
        
        返回实体当前拥有的所有标签。标签以字符串列表形式返回，如果实体没有任何标签，
        则返回空列表。
        
        Returns:
            List[str]: 实体的标签列表，每个元素为一个标签字符串
            
        示例：
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "tag")
            >>> tags = comp.GetEntityTags()
            >>> print(tags)  # 输出: ['monster', 'aggressive', 'fire_resistant']
            
        注意：
            - 标签区分大小写
            - 标签列表的顺序不保证固定
        """
        pass

    def AddEntityTag(self, tag):
        # type: (str) -> 'bool'
        """
        为实体添加一个新标签
        
        向实体添加指定的标签。如果实体已经拥有该标签，则不会重复添加。
        标签可以是任意字符串，建议使用有意义的命名。
        
        Args:
            tag (str): 要添加的标签名称，字符串类型，不能为空
            
        Returns:
            bool: 添加成功返回True，失败返回False
            
        示例：
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "tag")
            >>> comp.AddEntityTag("friendly")
            True
            >>> comp.AddEntityTag("friendly")  # 重复添加同一标签
            True  # 仍然返回True，但不会重复添加
            
        注意：
            - 标签名称区分大小写
            - 建议使用小写字母和下划线的命名规范
            - 标签不能包含空格，建议使用下划线分隔单词
        
        相关方法：
            - RemoveEntityTag: 移除标签
            - EntityHasTag: 检查标签是否存在
        """
        pass

    def RemoveEntityTag(self, tag):
        # type: (str) -> 'bool'
        """
        移除实体的指定标签
        
        从实体中移除指定的标签。如果实体没有该标签，操作仍然返回True。
        
        Args:
            tag (str): 要移除的标签名称
            
        Returns:
            bool: 移除成功返回True，失败返回False
            
        示例：
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "tag")
            >>> comp.AddEntityTag("temporary")
            >>> comp.RemoveEntityTag("temporary")
            True
            >>> comp.EntityHasTag("temporary")
            False
            
        注意：
            - 标签名称必须完全匹配（区分大小写）
            - 移除不存在的标签不会产生错误
        
        相关方法：
            - AddEntityTag: 添加标签
            - GetEntityTags: 获取所有标签
        """
        pass

    def EntityHasTag(self, tag):
        # type: (str) -> 'bool'
        """
        检查实体是否拥有指定的标签
        
        判断实体是否具有给定的标签，常用于条件判断和实体筛选。
        
        Args:
            tag (str): 要检查的标签名称
            
        Returns:
            bool: 如果实体拥有该标签返回True，否则返回False
            
        示例：
            >>> comp = serverApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "tag")
            >>> comp.AddEntityTag("boss")
            >>> if comp.EntityHasTag("boss"):
            ...     print("这是Boss实体")
            ...     # 对Boss实体执行特殊逻辑
            这是Boss实体
            
        使用场景：
            >>> # 筛选特定标签的实体
            >>> for entity_id in entity_list:
            ...     comp = serverApi.GetEngineCompFactory().CreateComponent(entity_id, "Minecraft", "tag")
            ...     if comp.EntityHasTag("quest_target"):
            ...         # 处理任务目标实体
            ...         pass
            
        注意：
            - 标签匹配区分大小写
            - 建议使用常量定义常用标签名，避免拼写错误
        
        相关方法：
            - GetEntityTags: 获取所有标签以进行批量检查
        """
        pass

