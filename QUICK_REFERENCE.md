# Minecraft 网易 SDK 快速参考

## 常用代码片段

### 服务端

#### 获取玩家位置
```python
comp = serverApi.CreateComponent(playerId, "Minecraft", "pos")
pos = comp.GetPos()  # 返回 (x, y, z)
```

#### 设置玩家位置
```python
comp = serverApi.CreateComponent(playerId, "Minecraft", "pos")
comp.SetPos((100, 64, 100))
```

#### 获取/设置生命值
```python
comp = serverApi.CreateComponent(playerId, "Minecraft", "attr")
health = comp.GetAttrValue(AttrType.HEALTH)  # 获取
comp.SetAttrValue(AttrType.HEALTH, 20.0)     # 设置
```

#### 给玩家添加物品
```python
comp = serverApi.CreateComponent(playerId, "Minecraft", "item")
itemDict = {
    "itemName": "minecraft:diamond",
    "count": 64,
    "auxValue": 0
}
comp.SpawnItemToPlayerInv(itemDict, playerId)
```

#### 获取/设置方块
```python
comp = serverApi.CreateComponent(levelId, "Minecraft", "block")
# 获取方块
blockDict = comp.GetBlockNew((x, y, z))
# 设置方块
comp.SetBlockNew((x, y, z), {"name": "minecraft:stone"})
```

#### 传送玩家
```python
comp = serverApi.CreateComponent(playerId, "Minecraft", "pos")
comp.SetPos((x, y, z))
```

#### 改变游戏模式
```python
comp = serverApi.CreateComponent(playerId, "Minecraft", "game")
comp.ChangePlayerGameMode(GameType.Creative)  # 创造模式
```

#### 添加状态效果
```python
comp = serverApi.CreateComponent(playerId, "Minecraft", "effect")
# 添加速度效果，持续60秒，等级2
comp.AddEffectToEntity(1, 60, 2)
```

#### 生成实体
```python
comp = serverApi.CreateComponent(levelId, "Minecraft", "entity")
entityId = comp.CreateEntity("minecraft:zombie", (x, y, z))
```

#### 设置世界时间
```python
comp = serverApi.CreateComponent(levelId, "Minecraft", "time")
comp.SetTime(6000)  # 设置为中午
```

### 客户端

#### 显示聊天消息
```python
comp = clientApi.CreateComponent(localPlayerId, "Minecraft", "game")
comp.AddChatTips("你的消息")
```

#### 播放音效
```python
comp = clientApi.CreateComponent(entityId, "Minecraft", "audioCustom")
comp.PlayCustomMusic("music_name", 1.0, 1.0, False)
```

#### 设置相机模式
```python
comp = clientApi.CreateComponent(localPlayerId, "Minecraft", "camera")
comp.SetCameraMode(0)  # 第一人称
comp.SetCameraMode(1)  # 第三人称
```

#### 获取玩家输入
```python
comp = clientApi.CreateComponent(localPlayerId, "Minecraft", "operation")
isJumping = comp.IsPlayerJumping()
```

#### 绘制形状（3.5 版本）
```python
comp = clientApi.CreateComponent(localPlayerId, "Minecraft", "drawing")
# 绘制盒子
shape = comp.AddBoxShape((x, y, z), scale=(1, 1, 1), color=(1, 0, 0))
# 绘制线条
shape = comp.AddLineShape((x1, y1, z1), (x2, y2, z2), color=(0, 1, 0))
```

### 事件监听

#### 监听玩家加入
```python
self.ListenForEvent("Minecraft", "Minecraft", "PlayerJoinEvent", self, self.OnPlayerJoin)

def OnPlayerJoin(self, args):
    playerId = args["playerId"]
    # 处理逻辑
```

#### 监听玩家死亡
```python
self.ListenForEvent("Minecraft", "Minecraft", "PlayerDieEvent", self, self.OnPlayerDie)

def OnPlayerDie(self, args):
    playerId = args["playerId"]
    # 处理逻辑
```

#### 监听方块破坏
```python
self.ListenForEvent("Minecraft", "Minecraft", "PlayerTryDestroyBlockServerEvent", self, self.OnBlockDestroy)

def OnBlockDestroy(self, args):
    playerId = args["playerId"]
    blockPos = args["blockPos"]
    # 处理逻辑
```

#### 监听玩家攻击
```python
self.ListenForEvent("Minecraft", "Minecraft", "PlayerAttackEntityServerEvent", self, self.OnPlayerAttack)

def OnPlayerAttack(self, args):
    playerId = args["playerId"]
    victimId = args["victimId"]
    # 处理逻辑
```

### 客户端-服务端通信

#### 服务端 -> 客户端
```python
# 服务端发送
self.NotifyToClient(playerId, "MyEvent", {"data": "value"})

# 客户端接收
self.ListenForEvent("MyNamespace", "MySystem", "MyEvent", self, self.OnMyEvent)
def OnMyEvent(self, args):
    data = args["data"]
```

#### 客户端 -> 服务端
```python
# 客户端发送
self.NotifyToServer("MyEvent", {"data": "value"})

# 服务端接收
self.ListenForEvent("MyNamespace", "MySystem", "MyEvent", self, self.OnMyEvent)
def OnMyEvent(self, args):
    data = args["data"]
```

## 常用枚举值

### 游戏模式 (GameType)
- `0` - 生存模式 (Survival)
- `1` - 创造模式 (Creative)
- `2` - 冒险模式 (Adventure)
- `3` - 旁观者模式 (Spectator)

### 属性类型 (AttrType)
- `0` - 生命值 (HEALTH)
- `1` - 移速 (SPEED)
- `2` - 攻击力 (DAMAGE)
- `4` - 饥饿值 (HUNGER)
- `5` - 饱和值 (SATURATION)

### 装备槽位 (ArmorSlotType)
- `0` - 头盔 (HEAD)
- `1` - 胸甲 (BODY)
- `2` - 护腿 (LEG)
- `3` - 鞋子 (FOOT)

### 伤害类型 (ActorDamageCause)
- `"contact"` - 接触伤害
- `"entity_attack"` - 生物攻击
- `"fall"` - 掉落伤害
- `"fire"` - 火焰伤害
- `"lava"` - 熔岩伤害
- `"drowning"` - 溺水伤害

## 常用维度 ID
- `0` - 主世界 (Overworld)
- `1` - 下界 (Nether)
- `2` - 末地 (The End)

## 调试技巧

### 打印调试信息
```python
print("[DEBUG] 玩家位置:", pos)
```

### 检查组件是否创建
```python
comp = serverApi.GetComponent(entityId, "Minecraft", "pos")
if comp:
    print("组件已创建")
else:
    print("组件未创建")
```

### 异常处理
```python
try:
    comp = serverApi.CreateComponent(entityId, "Minecraft", "pos")
    pos = comp.GetPos()
except Exception as e:
    print("错误:", str(e))
```

## 性能优化

### 使用缓存
```python
class MySystem(ServerSystem):
    def __init__(self, namespace, systemName):
        super(MySystem, self).__init__(namespace, systemName)
        self.posCache = {}
    
    def GetPlayerPosWithCache(self, playerId):
        if playerId not in self.posCache:
            comp = serverApi.CreateComponent(playerId, "Minecraft", "pos")
            self.posCache[playerId] = comp.GetPos()
        return self.posCache[playerId]
```

### 限制执行频率
```python
class MySystem(ServerSystem):
    def __init__(self, namespace, systemName):
        super(MySystem, self).__init__(namespace, systemName)
        self.tickCount = 0
    
    def Update(self):
        self.tickCount += 1
        if self.tickCount % 20 == 0:  # 每秒执行一次
            self.DoExpensiveOperation()
```

## 完整示例

### 传送门系统
```python
import mod.server.extraServerApi as serverApi

class PortalSystem(serverApi.ServerSystem):
    def __init__(self, namespace, systemName):
        super(PortalSystem, self).__init__(namespace, systemName)
        self.portals = {
            (100, 64, 100): (200, 64, 200),  # 入口 -> 出口
        }
        self.ListenForEvent("Minecraft", "Minecraft", "OnPlayerMoveServerEvent", 
                          self, self.OnPlayerMove)
    
    def OnPlayerMove(self, args):
        playerId = args["playerId"]
        posComp = serverApi.CreateComponent(playerId, "Minecraft", "pos")
        pos = posComp.GetFootPos()
        blockPos = (int(pos[0]), int(pos[1]), int(pos[2]))
        
        if blockPos in self.portals:
            targetPos = self.portals[blockPos]
            posComp.SetPos(targetPos)
            # 向客户端发送传送特效
            self.NotifyToClient(playerId, "ShowTeleportEffect", {})
```

---

更多详细信息请参考 [完整 API 文档](API_DOCUMENTATION.md)
