# -*- coding: utf-8 -*-
"""
旋转组件客户端模块

本模块提供实体旋转角度的查询和控制功能。旋转组件用于管理实体的朝向和视角。

主要功能：
    - 获取和设置实体的头部旋转角度
    - 获取实体身体旋转角度
    - 锁定本地玩家的头部角度
    - 控制玩家视角看向指定位置

旋转角度说明：
    旋转角度由两个值组成 (pitch, yaw)：
    - pitch (俯仰角): 头部与水平方向的角度
      * -90度: 向上看（天空）
      * 0度: 水平看
      * 90度: 向下看（地面）
    - yaw (偏航角): 竖直方向的旋转角度
      * 0度: 正南方向
      * 90度: 正西方向
      * 180度: 正北方向
      * 270度: 正东方向

使用场景：
    - 控制实体朝向
    - 实现自动瞄准功能
    - 创建过场动画
    - 相机控制系统
    - NPC视线跟踪

注意事项：
    - 客户端只能修改本地玩家的旋转
    - 其他实体的旋转需要在服务端修改
    - 旋转角度使用度数制，不是弧度制

示例：
    >>> import mod.client.extraClientApi as clientApi
    >>> comp = clientApi.GetEngineCompFactory().CreateComponent(playerId, "Minecraft", "rot")
    >>> rot = comp.GetRot()
    >>> print(f"玩家视角: 俯仰={rot[0]}, 偏航={rot[1]}")
"""

from typing import Tuple

class RotComponentClient(object):
    """
    旋转组件客户端类
    
    提供实体旋转角度的查询和控制接口。可用于获取视角方向、控制玩家朝向等。
    """
    
    def GetRot(self):
        # type: () -> 'Tuple[float,float]'
        """
        获取实体头部的旋转角度
        
        返回实体头部与水平方向的俯仰角和竖直方向的旋转角。获得角度后可使用
        GetDirFromRot接口转换为朝向的单位向量。
        
        Returns:
            Tuple[float, float]: (pitch, yaw) 旋转角度，单位为度
                - pitch: 俯仰角，范围 -90° 到 90°
                - yaw: 偏航角，范围 0° 到 360°
                
        示例：
            >>> import mod.client.extraClientApi as clientApi
            >>> comp = clientApi.GetEngineCompFactory().CreateComponent(playerId, "Minecraft", "rot")
            >>> rot = comp.GetRot()
            >>> pitch, yaw = rot
            >>> print(f"俯仰角: {pitch}°, 偏航角: {yaw}°")
            >>> 
            >>> # 判断玩家是否在向上看
            >>> if pitch < -45:
            ...     print("玩家正在仰望天空")
            >>> elif pitch > 45:
            ...     print("玩家正在俯视地面")
            
        应用场景：
            >>> # 获取玩家视线方向
            >>> def GetPlayerLookDirection(player_id):
            ...     comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "rot"
            ...     )
            ...     rot = comp.GetRot()
            ...     
            ...     # 转换为方向向量
            ...     direction = clientApi.GetDirFromRot(rot)
            ...     return direction
            
            >>> # 检测玩家朝向
            >>> def GetPlayerFacing(player_id):
            ...     comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "rot"
            ...     )
            ...     rot = comp.GetRot()
            ...     yaw = rot[1]
            ...     
            ...     # 判断主要朝向
            ...     if 315 <= yaw or yaw < 45:
            ...         return "南"
            ...     elif 45 <= yaw < 135:
            ...         return "西"
            ...     elif 135 <= yaw < 225:
            ...         return "北"
            ...     else:
            ...         return "东"
            
            >>> # 实现射线检测起点和方向
            >>> def RaycastFromPlayer(player_id, distance):
            ...     pos_comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "pos"
            ...     )
            ...     rot_comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "rot"
            ...     )
            ...     
            ...     pos = pos_comp.GetPos()
            ...     rot = rot_comp.GetRot()
            ...     
            ...     # 从玩家位置和视角方向发射射线
            ...     results = clientApi.getEntitiesOrBlockFromRay(pos, rot, distance)
            ...     return results
            
        注意：
            - 返回值的单位是度（°），不是弧度
            - pitch范围是-90到90，超出此范围会被限制
            - yaw范围是0到360，循环使用
            - 可配合GetDirFromRot转换为方向向量
        
        相关方法：
            - SetRot: 设置旋转角度
            - GetBodyRot: 获取身体旋转角度
        
        相关API：
            - clientApi.GetDirFromRot: 将旋转角度转换为方向向量
            - clientApi.GetRotFromDir: 将方向向量转换为旋转角度
        """
        pass

    def SetRot(self, rot):
        # type: (Tuple[float,float]) -> 'bool'
        """
        设置实体头部的旋转角度
        
        设置实体头与水平方向的俯仰角度和竖直方向的旋转角度。
        注意：客户端只能设置本地玩家的旋转角度。
        
        Args:
            rot (Tuple[float, float]): (pitch, yaw) 旋转角度
                - pitch: 俯仰角，范围 -90° 到 90°
                - yaw: 偏航角，范围 0° 到 360°
                
        Returns:
            bool: 设置成功返回True，失败返回False
            
        示例：
            >>> import mod.client.extraClientApi as clientApi
            >>> player_id = clientApi.GetLocalPlayerId()
            >>> comp = clientApi.GetEngineCompFactory().CreateComponent(player_id, "Minecraft", "rot")
            >>> 
            >>> # 设置玩家向前平视
            >>> comp.SetRot((0.0, 0.0))  # 向南平视
            >>> 
            >>> # 设置玩家仰望天空
            >>> comp.SetRot((-90.0, 0.0))
            >>> 
            >>> # 设置玩家向东看
            >>> comp.SetRot((0.0, 270.0))
            
        应用场景：
            >>> # 强制玩家看向指定方向
            >>> def ForceLookDirection(pitch, yaw):
            ...     player_id = clientApi.GetLocalPlayerId()
            ...     comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "rot"
            ...     )
            ...     comp.SetRot((pitch, yaw))
            
            >>> # 实现过场动画中的视角控制
            >>> def CutsceneLookAt(target_pitch, target_yaw, duration_ticks):
            ...     player_id = clientApi.GetLocalPlayerId()
            ...     comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "rot"
            ...     )
            ...     
            ...     # 获取当前角度
            ...     current_rot = comp.GetRot()
            ...     start_pitch, start_yaw = current_rot
            ...     
            ...     # 逐帧插值旋转
            ...     for i in range(duration_ticks):
            ...         t = i / duration_ticks  # 0到1的插值参数
            ...         pitch = start_pitch + (target_pitch - start_pitch) * t
            ...         yaw = start_yaw + (target_yaw - start_yaw) * t
            ...         comp.SetRot((pitch, yaw))
            
        注意：
            - 客户端只能修改本地玩家的旋转
            - 其他实体需要在服务端使用对应组件修改
            - pitch会被限制在-90到90度范围内
            - 突然改变角度可能影响玩家体验，建议平滑过渡
        
        相关方法：
            - GetRot: 获取旋转角度
            - SetPlayerLookAtPos: 平滑看向指定位置
        """
        pass

    def GetBodyRot(self):
        # type: () -> 'float'
        """
        获取实体身体的旋转角度
        
        返回实体身体（而非头部）的旋转角度。身体角度可能与头部角度不同，
        特别是当实体头部转动但身体尚未跟随时。
        
        Returns:
            float: 身体旋转角度（yaw），范围 0° 到 360°
            
        示例：
            >>> import mod.client.extraClientApi as clientApi
            >>> comp = clientApi.GetEngineCompFactory().CreateComponent(entityId, "Minecraft", "rot")
            >>> body_yaw = comp.GetBodyRot()
            >>> print(f"身体朝向: {body_yaw}°")
            >>> 
            >>> # 比较头部和身体朝向差异
            >>> head_rot = comp.GetRot()
            >>> head_yaw = head_rot[1]
            >>> body_yaw = comp.GetBodyRot()
            >>> angle_diff = abs(head_yaw - body_yaw)
            >>> if angle_diff > 45:
            ...     print("头部和身体朝向差异较大")
            
        应用场景：
            >>> # 检测实体是否在回头看
            >>> def IsLookingBack(entity_id):
            ...     comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         entity_id, "Minecraft", "rot"
            ...     )
            ...     head_yaw = comp.GetRot()[1]
            ...     body_yaw = comp.GetBodyRot()
            ...     
            ...     angle_diff = abs(head_yaw - body_yaw)
            ...     # 如果头部和身体角度差超过90度，说明在回头看
            ...     return angle_diff > 90
            
        注意：
            - 身体旋转通常比头部旋转变化慢
            - 身体只有yaw角度，没有pitch
            - 身体会逐渐跟随头部旋转
        
        相关方法：
            - GetRot: 获取头部旋转（包含pitch和yaw）
        """
        pass

    def LockLocalPlayerRot(self, lock):
        # type: (bool) -> 'bool'
        """
        锁定或解锁本地玩家的头部角度
        
        在使用分离摄像机时，锁定本地玩家的头部角度，防止玩家移动鼠标改变视角。
        常用于过场动画或特殊游戏模式。
        
        Args:
            lock (bool): True为锁定，False为解锁
            
        Returns:
            bool: 设置成功返回True，失败返回False
            
        示例：
            >>> import mod.client.extraClientApi as clientApi
            >>> player_id = clientApi.GetLocalPlayerId()
            >>> comp = clientApi.GetEngineCompFactory().CreateComponent(player_id, "Minecraft", "rot")
            >>> 
            >>> # 锁定玩家视角
            >>> comp.LockLocalPlayerRot(True)
            >>> 
            >>> # 解锁玩家视角
            >>> comp.LockLocalPlayerRot(False)
            
        应用场景：
            >>> # 播放过场动画时锁定玩家视角
            >>> def PlayCutscene():
            ...     player_id = clientApi.GetLocalPlayerId()
            ...     rot_comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "rot"
            ...     )
            ...     
            ...     # 锁定视角
            ...     rot_comp.LockLocalPlayerRot(True)
            ...     
            ...     # 设置动画开始视角
            ...     rot_comp.SetRot((0.0, 180.0))
            ...     
            ...     # 播放动画...
            ...     # ...
            ...     
            ...     # 动画结束后解锁
            ...     rot_comp.LockLocalPlayerRot(False)
            
            >>> # 实现观察模式
            >>> def EnterSpectatorMode():
            ...     player_id = clientApi.GetLocalPlayerId()
            ...     comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "rot"
            ...     )
            ...     
            ...     # 分离摄像机并锁定玩家角度
            ...     camera_comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "camera"
            ...     )
            ...     camera_comp.SetFollowCamera(False)  # 分离摄像机
            ...     comp.LockLocalPlayerRot(True)  # 锁定玩家角度
            
        注意：
            - 只对本地玩家有效
            - 锁定后玩家无法通过鼠标改变视角
            - 但仍可以通过SetRot等API修改角度
            - 记得在适当时候解锁，避免影响正常游戏
            - 通常配合分离摄像机使用
        
        相关方法：
            - SetRot: 在锁定状态下仍可使用此方法修改角度
            - SetPlayerLookAtPos: 平滑看向目标位置
        """
        pass

    def SetPlayerLookAtPos(self, targetPos, pitchStep, yawStep, blockInput=True):
        # type: (Tuple[float,float,float], float, float, bool) -> 'bool'
        """
        设置本地玩家平滑地看向某个位置
        
        让玩家的视角平滑地转向目标位置，可以设置旋转速度。
        此方法会自动计算所需的pitch和yaw角度。
        
        Args:
            targetPos (Tuple[float,float,float]): 目标位置的世界坐标 (x, y, z)
            pitchStep (float): 每帧俯仰角变化速度（度/帧），建议范围1-10
            yawStep (float): 每帧偏航角变化速度（度/帧），建议范围1-10
            blockInput (bool, optional): 是否阻止玩家输入。默认为True
            
        Returns:
            bool: 设置成功返回True，失败返回False
            
        示例：
            >>> import mod.client.extraClientApi as clientApi
            >>> player_id = clientApi.GetLocalPlayerId()
            >>> comp = clientApi.GetEngineCompFactory().CreateComponent(player_id, "Minecraft", "rot")
            >>> 
            >>> # 让玩家看向坐标(100, 64, 100)
            >>> target_pos = (100.0, 64.0, 100.0)
            >>> comp.SetPlayerLookAtPos(target_pos, 5.0, 5.0, True)
            
        应用场景：
            >>> # 让玩家看向NPC
            >>> def LookAtNPC(npc_id):
            ...     player_id = clientApi.GetLocalPlayerId()
            ...     
            ...     # 获取NPC位置
            ...     npc_pos_comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         npc_id, "Minecraft", "pos"
            ...     )
            ...     npc_pos = npc_pos_comp.GetPos()
            ...     
            ...     # 让玩家看向NPC
            ...     rot_comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "rot"
            ...     )
            ...     rot_comp.SetPlayerLookAtPos(npc_pos, 3.0, 3.0, False)
            
            >>> # 引导玩家注意特定位置
            >>> def PointOutLocation(target_pos):
            ...     player_id = clientApi.GetLocalPlayerId()
            ...     comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "rot"
            ...     )
            ...     
            ...     # 快速转向目标
            ...     comp.SetPlayerLookAtPos(target_pos, 10.0, 10.0, True)
            ...     
            ...     # 3秒后解除输入阻止
            ...     # ... 使用定时器
            
            >>> # 实现自动瞄准功能
            >>> def AutoAim(target_entity_id):
            ...     player_id = clientApi.GetLocalPlayerId()
            ...     
            ...     # 获取目标位置
            ...     target_comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         target_entity_id, "Minecraft", "pos"
            ...     )
            ...     target_pos = target_comp.GetPos()
            ...     
            ...     # 瞄准目标
            ...     rot_comp = clientApi.GetEngineCompFactory().CreateComponent(
            ...         player_id, "Minecraft", "rot"
            ...     )
            ...     # 使用较高的速度实现快速瞄准
            ...     rot_comp.SetPlayerLookAtPos(target_pos, 15.0, 15.0, False)
            
        参数说明：
            - pitchStep和yawStep控制旋转速度
            - 值越大，旋转越快
            - 建议范围1-10，过大可能导致视角抖动
            - blockInput=True时玩家无法手动控制视角
            
        注意：
            - 只对本地玩家有效
            - 旋转是平滑的，不是瞬间完成
            - blockInput会阻止玩家的所有输入，使用时要谨慎
            - 如果目标位置在玩家背后，会选择较短的旋转路径
            - 旋转完成后不会自动解除blockInput，需要手动处理
        
        相关方法：
            - SetRot: 立即设置角度（无平滑过渡）
            - GetRot: 获取当前角度
            - LockLocalPlayerRot: 锁定玩家角度
        """
        pass

