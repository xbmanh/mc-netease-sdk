# -*- coding: utf-8 -*-
"""
位置组件客户端模块

本模块提供实体位置信息的查询功能。位置组件用于获取实体在游戏世界中的坐标位置。

主要功能：
    - 获取实体的中心位置
    - 获取实体脚部位置

使用场景：
    - 计算实体间的距离
    - 实现自定义导航系统
    - 粒子效果定位
    - 碰撞检测
    - UI绑定到实体位置

坐标系统说明：
    Minecraft使用三维笛卡尔坐标系：
    - X轴：东西方向（正为东）
    - Y轴：垂直方向（正为上）
    - Z轴：南北方向（正为南）

注意事项：
    - 位置组件为只读组件，客户端无法修改实体位置
    - 如需修改位置，请在服务端使用actorMotionCompServer
    - 客户端获取的位置可能有网络延迟

示例：
    >>> import mod.client.extraClientApi as clientApi
    >>> comp = clientApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "pos")
    >>> pos = comp.GetPos()
    >>> print(f"实体位置: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")
"""

from typing import Tuple

class PosComponentClient(object):
    """
    位置组件客户端类
    
    提供实体位置信息的查询接口。客户端位置组件为只读，不能修改实体位置。
    """
    
    def GetPos(self):
        # type: () -> 'Tuple[float,float,float]'
        """
        获取实体的中心位置
        
        返回实体中心点在世界坐标系中的位置。对于大多数实体，这是实体模型的
        几何中心；对于玩家，这大约在眼睛位置。
        
        Returns:
            Tuple[float, float, float]: 实体位置坐标 (x, y, z)
            
        示例：
            >>> import mod.client.extraClientApi as clientApi
            >>> comp = clientApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "pos")
            >>> pos = comp.GetPos()
            >>> print(f"实体位置: X={pos[0]:.2f}, Y={pos[1]:.2f}, Z={pos[2]:.2f}")
            
        应用场景：
            >>> # 计算两个实体之间的距离
            >>> def GetDistance(entity1_id, entity2_id):
            ...     comp1 = clientApi.GetEngineCompFactory().CreateComponent(
            ...         entity1_id, "Minecraft", "pos"
            ...     )
            ...     comp2 = clientApi.GetEngineCompFactory().CreateComponent(
            ...         entity2_id, "Minecraft", "pos"
            ...     )
            ...     pos1 = comp1.GetPos()
            ...     pos2 = comp2.GetPos()
            ...     
            ...     import math
            ...     dx = pos2[0] - pos1[0]
            ...     dy = pos2[1] - pos1[1]
            ...     dz = pos2[2] - pos1[2]
            ...     distance = math.sqrt(dx*dx + dy*dy + dz*dz)
            ...     return distance
            
            >>> # 在实体位置生成粒子效果
            >>> def SpawnParticleAtEntity(entity_id):
            ...     comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         entity_id, "Minecraft", "pos"
            ...     )
            ...     pos = comp.GetPos()
            ...     
            ...     # 创建粒子组件
            ...     particle_comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         clientApi.GetLevelId(), "Minecraft", "particle"
            ...     )
            ...     particle_comp.CreateParticle("minecraft:flame_particle", pos)
            
            >>> # 将UI绑定到实体位置
            >>> def BindUIToEntity(ui, entity_id):
            ...     comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         entity_id, "Minecraft", "pos"
            ...     )
            ...     pos = comp.GetPos()
            ...     # 转换为屏幕坐标并设置UI位置
            ...     # ... 屏幕坐标转换逻辑
            
        注意：
            - 返回的是实体中心位置，不是脚部位置
            - 客户端获取的位置可能有轻微的网络延迟
            - 位置坐标为浮点数，精度足够高
            - 对于玩家，中心位置大约在眼睛高度
        
        相关方法：
            - GetFootPos: 获取脚部位置
        """
        pass

    def GetFootPos(self):
        # type: () -> 'Tuple[float,float,float]'
        """
        获取实体脚部所在的位置
        
        返回实体脚底在世界坐标系中的位置。脚部位置通常用于判断实体
        站在哪个方块上，或进行地面碰撞检测。
        
        Returns:
            Tuple[float, float, float]: 实体脚部位置坐标 (x, y, z)
            
        示例：
            >>> import mod.client.extraClientApi as clientApi
            >>> comp = clientApi.GetEngineCompFactory().CreateComponent(playerId, "Minecraft", "pos")
            >>> foot_pos = comp.GetFootPos()
            >>> print(f"玩家脚部位置: {foot_pos}")
            >>> 
            >>> # 获取玩家站立的方块坐标
            >>> block_pos = (int(foot_pos[0]), int(foot_pos[1]), int(foot_pos[2]))
            >>> print(f"站立方块: {block_pos}")
            
        应用场景：
            >>> # 检测实体站在什么方块上
            >>> def GetStandingBlock(entity_id):
            ...     comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         entity_id, "Minecraft", "pos"
            ...     )
            ...     foot_pos = comp.GetFootPos()
            ...     
            ...     # 获取方块坐标（向下取整）
            ...     block_x = int(foot_pos[0])
            ...     block_y = int(foot_pos[1]) - 1  # 脚下的方块
            ...     block_z = int(foot_pos[2])
            ...     
            ...     # 获取方块信息
            ...     block_comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         clientApi.GetLevelId(), "Minecraft", "blockInfo"
            ...     )
            ...     block_name = block_comp.GetBlockName((block_x, block_y, block_z))
            ...     return block_name
            
            >>> # 在脚部位置播放踩踏音效
            >>> def PlayFootstepSound(player_id):
            ...     comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "pos"
            ...     )
            ...     foot_pos = comp.GetFootPos()
            ...     
            ...     # 获取站立方块类型
            ...     block_type = GetStandingBlock(player_id)
            ...     
            ...     # 播放对应的音效
            ...     if "stone" in block_type:
            ...         sound_path = "sounds/footstep/stone.ogg"
            ...     elif "wood" in block_type:
            ...         sound_path = "sounds/footstep/wood.ogg"
            ...     # ... 播放音效
            
            >>> # 检测实体是否在水中
            >>> def IsInWater(entity_id):
            ...     comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         entity_id, "Minecraft", "pos"
            ...     )
            ...     foot_pos = comp.GetFootPos()
            ...     
            ...     # 检查脚部位置的方块
            ...     block_comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         clientApi.GetLevelId(), "Minecraft", "blockInfo"
            ...     )
            ...     block_pos = (int(foot_pos[0]), int(foot_pos[1]), int(foot_pos[2]))
            ...     block_name = block_comp.GetBlockName(block_pos)
            ...     
            ...     return "water" in block_name
            
        注意：
            - 脚部位置Y坐标通常比中心位置低1-2个单位
            - 用于判断站立方块时，通常需要Y-1获取脚下方块
            - 脚部位置对于碰撞检测和地形判断很重要
            - 坐标转换为方块坐标时使用int()向下取整
        
        相关方法：
            - GetPos: 获取中心位置
        
        相关组件：
            - blockInfo: 用于获取方块信息
            - block: 用于方块操作
        """
        pass

