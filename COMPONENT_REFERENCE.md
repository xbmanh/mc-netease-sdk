# Minecraft 网易 SDK 组件参考

本文档列出了所有可用的服务端和客户端组件及其主要功能。

## 服务端组件

### 实体相关

#### `AttrCompServer` - 属性组件
- 管理实体属性（生命值、速度、攻击力等）
- 设置/获取属性值和最大值
- 控制实体着火状态
- 设置台阶高度

#### `PosCompServer` - 位置组件
- 获取/设置实体位置
- 获取脚底位置
- 位置相关操作

#### `RotCompServer` - 旋转组件
- 获取/设置实体旋转角度
- 头部旋转控制

#### `NameCompServer` - 名称组件
- 获取/设置实体名称
- 显示名称管理

#### `RideCompServer` - 骑乘组件
- 实体骑乘控制
- 获取骑乘者和被骑乘者

#### `ModelCompServer` - 模型组件
- 设置实体模型
- 模型缩放控制

#### `ScaleCompServer` - 缩放组件
- 设置实体大小比例

#### `HealthCompServer` - 生命值组件（已废弃）
- ⚠️ **已废弃**：请使用 `AttrCompServer` 代替
- 获取/设置生命值
- 迁移方法：使用 `AttrCompServer.GetAttrValue(AttrType.HEALTH)` 替代

### 玩家相关

#### `PlayerCompServer` - 玩家组件
- 玩家特有功能
- 踢出玩家
- 转换实体类型

#### `ItemCompServer` - 物品组件
- 物品栏管理
- 添加/删除物品
- 获取玩家所有物品

#### `ExpCompServer` - 经验组件
- 经验值管理
- 等级控制

#### `GameCompServer` - 游戏组件
- 游戏模式切换
- 重生控制
- 时间管理
- 天气控制

#### `AchievementCompServer` - 成就组件
- 成就管理
- 触发成就

### 世界相关

#### `BlockCompServer` - 方块组件
- 获取/设置方块
- 方块状态管理
- 方块实体数据

#### `BlockInfoCompServer` - 方块信息组件
- 获取方块详细信息
- 方块属性查询

#### `BlockStateCompServer` - 方块状态组件
- 方块状态管理
- 自定义方块状态

#### `ChunkSourceComp` - 区块源组件
- 区块加载管理
- 区块数据访问

#### `DimensionCompServer` - 维度组件
- 维度管理
- 维度切换

#### `TimeCompServer` - 时间组件
- 世界时间控制
- 昼夜循环管理

#### `WeatherCompServer` - 天气组件
- 天气控制
- 雨雪雷电

#### `BiomeCompServer` - 生物群系组件
- 获取生物群系信息
- 生物群系相关操作

### 战斗相关

#### `HurtCompServer` - 伤害组件
- 造成伤害
- 伤害类型控制

#### `EffectCompServer` - 效果组件
- 添加/移除状态效果
- 获取所有效果

#### `ExplosionCompServer` - 爆炸组件
- 创建爆炸效果
- 爆炸参数控制

#### `ProjectileCompServer` - 抛射物组件
- 抛射物管理
- 弹道控制

#### `BulletAttributesCompServer` - 子弹属性组件
- 子弹属性设置
- 伤害控制

### AI 相关

#### `AiCommandCompServer` - AI 命令组件
- AI 行为控制
- 命令执行

#### `ControlAiCompServer` - 控制 AI 组件
- AI 开关控制
- 行为模式切换

#### `MoveToCompServer` - 移动到组件
- 实体移动控制
- 路径规划

#### `TameCompServer` - 驯服组件
- 实体驯服
- 主人管理

#### `PetCompServer` - 宠物组件
- 宠物相关功能
- 跟随行为

### 容器相关

#### `ChestContainerCompServer` - 箱子容器组件
- 箱子物品管理
- 容器操作

#### `BlockEntityCompServer` - 方块实体组件
- 方块实体数据
- 特殊方块管理

#### `BlockEntityExDataCompServer` - 方块实体扩展数据组件
- 扩展数据存储
- 自定义数据

### 其他服务端组件

#### `ActionCompServer` - 动作组件
- 实体动作控制
- 动画触发

#### `ActorMotionCompServer` - 实体运动组件
- 运动控制
- 速度设置

#### `ActorOwnerCompServer` - 实体所有者组件
- 所有权管理
- 归属控制

#### `ActorCollidableCompServer` - 实体碰撞组件
- 碰撞检测
- 碰撞箱管理

#### `ActorLootCompServer` - 实体战利品组件
- 战利品表管理
- 掉落物控制

#### `ActorPushableCompServer` - 实体可推动组件
- 推动控制
- 物理交互

#### `AuxValueCompServer` - 附加值组件
- 物品附加值
- 数据存储

#### `BreathCompServer` - 呼吸组件
- 氧气值管理
- 溺水控制

#### `CollisionBoxCompServer` - 碰撞箱组件
- 碰撞箱大小设置
- 碰撞检测范围

#### `CommandCompServer` - 命令组件
- 执行命令
- 命令反馈

#### `EntityEventCompServer` - 实体事件组件
- 触发实体事件
- 事件管理

#### `ExDataCompServer` - 扩展数据组件
- 存储自定义数据
- 数据持久化

#### `FlyCompServer` - 飞行组件
- 飞行能力控制
- 飞行模式

#### `GravityCompServer` - 重力组件
- 重力控制
- 物理效果

#### `InteractCompServer` - 交互组件
- 实体交互
- 交互事件

#### `LootCompServer` - 战利品组件
- 战利品生成
- 掉落控制

#### `MobSpawnCompServer` - 生物生成组件
- 生物生成控制
- 刷怪管理

#### `PersistenceCompServer` - 持久化组件
- 实体持久化
- 数据保存

#### `PortalCompServer` - 传送门组件
- 传送门管理
- 维度传送

#### `RecipeCompServer` - 配方组件
- 合成配方管理
- 配方解锁

#### `RedStoneCompServer` - 红石组件
- 红石信号
- 电路控制

#### `ShareableCompServer` - 可分享组件
- 物品分享
- 交易控制

#### `TagCompServer` - 标签组件
- 标签管理
- 标签检测

#### `BlockUseEventWhiteListCompServer` - 方块使用事件白名单组件
- 事件白名单管理
- 权限控制

#### `ChatExtensionCompServer` - 聊天扩展组件
- 聊天功能扩展
- 自定义聊天

#### `EntityDefinitionsCompServer` - 实体定义组件
- 实体定义管理
- 动态实体

#### `FeatureCompServer` - 特性组件
- 世界特性
- 结构生成

#### `HttpToWebServerCompServer` - HTTP 到 Web 服务器组件
- HTTP 请求
- 网络通信

#### `ItemBannedCompServer` - 物品封禁组件
- 物品封禁管理
- 权限控制

#### `LevelCompServer` - 等级组件
- 世界级别管理
- 难度控制

#### `ModAttrCompServer` - MOD 属性组件
- MOD 自定义属性
- 扩展属性系统

#### `MsgCompServer` - 消息组件
- 消息发送
- 聊天管理

#### `QueryVariableCompServer` - 查询变量组件
- 变量查询
- Molang 表达式

---

## 客户端组件

### 实体相关

#### `AttrCompClient` - 属性组件
- 获取实体属性
- 状态查询（触地、在岩浆中等）

#### `PosCompClient` - 位置组件
- 获取实体位置
- 位置相关查询

#### `RotCompClient` - 旋转组件
- 获取实体旋转角度

#### `NameCompClient` - 名称组件
- 获取实体名称

#### `RideCompClient` - 骑乘组件
- 骑乘状态查询

#### `ModelCompClient` - 模型组件
- 模型显示控制
- 模型替换

#### `TameCompClient` - 驯服组件
- 驯服状态查询

#### `HealthCompClient` - 生命值组件
- 获取生命值

### 玩家相关

#### `PlayerCompClient` - 玩家组件
- 玩家状态查询
- 本地玩家信息

#### `ItemCompClient` - 物品组件
- 物品信息查询
- 手持物品获取

#### `PlayerViewCompClient` - 玩家视角组件
- 视角方向
- 目标检测

#### `PlayerAnimCompClient` - 玩家动画组件
- 播放动画
- 动画控制

#### `OperationCompClient` - 操作组件
- 输入检测
- 操作状态

### 渲染相关

#### `ActorRenderCompClient` - 实体渲染组件
- 渲染控制
- 可见性设置

#### `CameraCompClient` - 相机组件
- 相机模式切换
- 视角控制
- FOV 设置

#### `FogCompClient` - 迷雾组件
- 迷雾效果
- 可见距离

#### `SkyRenderCompClient` - 天空渲染组件
- 天空渲染控制
- 天空颜色

#### `ParticleSystemCompClient` - 粒子系统组件
- 粒子效果
- 特效播放

#### `ParticleControlComp` - 粒子控制组件
- 粒子控制
- 播放暂停

#### `ParticleEntityBindComp` - 粒子实体绑定组件
- 绑定粒子到实体

#### `ParticleSkeletonBindComp` - 粒子骨骼绑定组件
- 绑定粒子到骨骼

#### `ParticleTransComp` - 粒子变换组件
- 粒子位置旋转

#### `FrameAniControlComp` - 帧动画控制组件
- 帧动画播放

#### `FrameAniEntityBindComp` - 帧动画实体绑定组件
- 绑定帧动画到实体

#### `FrameAniSkeletonBindComp` - 帧动画骨骼绑定组件
- 绑定帧动画到骨骼

#### `FrameAniTransComp` - 帧动画变换组件
- 帧动画位置旋转

#### `EngineEffectBindControlComp` - 引擎特效绑定控制组件
- 引擎特效控制

#### `PostProcessControlComp` - 后处理控制组件
- 后处理效果

#### `DrawingCompClient` - 绘图组件（3.5 新增）
- 绘制几何形状
- 调试可视化

#### `DrawingShapeCompClient` - 绘图形状组件（3.5 新增）
- 形状控制
- 显示隐藏

### UI 相关

#### `TextNotifyCompClient` - 文本通知组件
- 屏幕提示
- 通知显示

#### `TextBoardCompClient` - 文本板组件
- 文本显示板

### 世界相关

#### `BlockCompClient` - 方块组件
- 获取方块信息

#### `BlockInfoCompClient` - 方块信息组件
- 方块详细信息

#### `BlockGeometryCompClient` - 方块几何组件
- 方块几何信息

#### `BiomeCompClient` - 生物群系组件
- 获取生物群系

#### `ChunkSourceCompClient` - 区块源组件
- 区块信息查询

#### `CollisionBoxCompClient` - 碰撞箱组件
- 碰撞箱信息

#### `DimensionCompClient` - 维度组件
- 维度信息

#### `TimeCompClient` - 时间组件
- 获取世界时间

#### `BrightnessCompClient` - 亮度组件
- 光照强度
- 亮度查询

### 游戏相关

#### `GameCompClient` - 游戏组件
- 游戏设置
- 聊天消息

#### `EffectCompClient` - 效果组件
- 获取状态效果

#### `RecipeCompClient` - 配方组件
- 配方信息查询

#### `AuxValueCompClient` - 附加值组件
- 获取附加值

### 系统相关

#### `ConfigCompClient` - 配置组件
- 游戏配置
- 设置获取

#### `DeviceCompClient` - 设备组件
- 设备信息
- 平台检测

#### `AudioCustomCompClient` - 自定义音频组件
- 播放音效
- 音频控制

#### `NeteaseShopCompClient` - 网易商城组件
- 商城接口
- 购买功能

#### `NeteaseWindowCompClient` - 网易窗口组件
- 窗口管理
- 特殊界面

#### `VirtualWorldCompClient` - 虚拟世界组件
- 虚拟世界功能

### 其他客户端组件

#### `AchievementCompClient` - 成就组件
- 成就查询

#### `ActionCompClient` - 动作组件
- 动作状态查询

#### `ActorMotionCompClient` - 实体运动组件
- 运动信息获取

#### `BlockUseEventWhiteListCompClient` - 方块使用事件白名单组件
- 白名单查询

#### `EngineTypeCompClient` - 引擎类型组件
- 引擎信息

#### `ModAttrCompClient` - MOD 属性组件
- MOD 属性查询

#### `QueryVariableCompClient` - 查询变量组件
- 变量查询

---

## 组件使用示例

### 服务端组件使用
```python
import mod.server.extraServerApi as serverApi

# 创建属性组件
attrComp = serverApi.CreateComponent(playerId, "Minecraft", "attr")
health = attrComp.GetAttrValue(0)  # 获取生命值

# 创建位置组件
posComp = serverApi.CreateComponent(playerId, "Minecraft", "pos")
pos = posComp.GetPos()  # 获取位置

# 创建物品组件
itemComp = serverApi.CreateComponent(playerId, "Minecraft", "item")
itemComp.SpawnItemToPlayerInv(itemDict, playerId)  # 给玩家添加物品
```

### 客户端组件使用
```python
import mod.client.extraClientApi as clientApi

# 创建相机组件
cameraComp = clientApi.CreateComponent(playerId, "Minecraft", "camera")
cameraComp.SetCameraMode(0)  # 设置第一人称

# 创建音频组件
audioComp = clientApi.CreateComponent(playerId, "Minecraft", "audioCustom")
audioComp.PlayCustomMusic("music_name", 1.0, 1.0, False)  # 播放音乐
```

---

更多详细信息请参考 [完整 API 文档](API_DOCUMENTATION.md)
