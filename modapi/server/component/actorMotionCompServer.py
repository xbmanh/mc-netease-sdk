# -*- coding: utf-8 -*-

from typing import Tuple
from mod.common.component.baseComponent import BaseComponent
from mod.common.minecraftEnum import TimeEaseType

class ActorMotionComponentServer(BaseComponent):
    def SetMotion(self, motion):
        # type: (Tuple[float,float,float]) -> 'bool'
        """
        设置生物（不含玩家）的瞬时移动方向向量
        """
        pass

    def SetPlayerMotion(self, motion):
        # type: (Tuple[float,float,float]) -> 'bool'
        """
        设置玩家的瞬时移动方向向量(可解决SetMotion闪现问题)
        """
        pass

    def GetMotion(self):
        # type: () -> 'Tuple[float,float,float]'
        """
        获取生物（含玩家）的瞬时移动方向向量
        """
        pass

    def ResetMotion(self):
        # type: () -> 'bool'
        """
        重置生物（不含玩家）的瞬时移动方向向量
        """
        pass

    def AddEntityTrackMotion(self, targetPos, duraTime, startPos=None, relativeCoord=False, isLoop=False, targetRot=None, startRot=None, useVelocityDir=False, ease='linear'):
        # type: (Tuple[float,float,float], float, Tuple[float,float,float], bool, bool, Tuple[float,float], Tuple[float,float], bool, TimeEaseType) -> 'int'
        """
        给实体（不含玩家）添加轨迹运动器
        """
        pass

    def AddEntityVelocityMotion(self, velocity, accelerate=None, useVelocityDir=True):
        # type: (Tuple[float,float,float], Tuple[float,float,float], bool) -> 'int'
        """
        给实体（不含玩家）添加速度运动器
        """
        pass

    def AddEntityAroundPointMotion(self, center, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0):
        # type: (Tuple[float,float,float], float, Tuple[float,float,float], bool, float) -> 'int'
        """
        给实体（不含玩家）添加对点环绕运动器
        """
        pass

    def AddEntityAroundEntityMotion(self, eID, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0, radius=-1):
        # type: (str, float, Tuple[float,float,float], bool, float, float) -> 'int'
        """
        给实体（不含玩家）添加对实体环绕运动器
        """
        pass

    def GetEntityMotions(self):
        # type: () -> 'dict'
        """
        获取实体（不含玩家）身上的所有运动器
        """
        pass

    def RemoveEntityMotion(self, motionId):
        # type: (int) -> 'bool'
        """
        移除实体（不含玩家）身上的运动器
        """
        pass

    def StartEntityMotion(self, motionId):
        # type: (int) -> 'bool'
        """
        启动实体（不含玩家）身上的某个运动器
        """
        pass

    def StopEntityMotion(self, motionId):
        # type: (int) -> 'bool'
        """
        停止实体（不含玩家）身上的某个运动器
        """
        pass

    def AddPlayerTrackMotion(self, targetPos, duraTime, startPos=None, relativeCoord=False, isLoop=False, targetRot=None, startRot=None, useVelocityDir=False, ease='linear'):
        # type: (Tuple[float,float,float], float, Tuple[float,float,float], bool, bool, Tuple[float,float], Tuple[float,float], bool, TimeEaseType) -> 'int'
        """
        给玩家添加轨迹运动器
        """
        pass

    def AddPlayerVelocityMotion(self, velocity, accelerate=None, useVelocityDir=True):
        # type: (Tuple[float,float,float], Tuple[float,float,float], bool) -> 'int'
        """
        给玩家添加速度运动器
        """
        pass

    def AddPlayerAroundPointMotion(self, center, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0):
        # type: (Tuple[float,float,float], float, Tuple[float,float,float], bool, float) -> 'int'
        """
        给玩家添加对点环绕运动器
        """
        pass

    def AddPlayerAroundEntityMotion(self, eID, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0, radius=-1):
        # type: (str, float, Tuple[float,float,float], bool, float, float) -> 'int'
        """
        给玩家添加对实体环绕运动器
        """
        pass

    def GetPlayerMotions(self):
        # type: () -> 'dict'
        """
        获取玩家身上的所有运动器
        """
        pass

    def RemovePlayerMotion(self, motionId):
        # type: (int) -> 'bool'
        """
        移除玩家身上的运动器
        """
        pass

    def StartPlayerMotion(self, motionId):
        # type: (int) -> 'bool'
        """
        启动玩家身上的某个运动器
        """
        pass

    def StopPlayerMotion(self, motionId):
        # type: (int) -> 'bool'
        """
        停止玩家身上的某个运动器
        """
        pass

