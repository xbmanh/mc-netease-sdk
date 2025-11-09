# Minecraft Netease SDK API Documentation

## Overview

The Minecraft Netease SDK is a Python development toolkit for creating mods for Minecraft China Edition. This SDK provides client-side, server-side, and common API interfaces, enabling developers to create custom game content and functionality.

### SDK Versions

- **Version 3.4**: Stable version
- **Version 3.5**: New version with additional features (such as drawing components)

## Table of Contents

1. [Quick Start](#quick-start)
2. [Architecture Overview](#architecture-overview)
3. [Server API](#server-api)
4. [Client API](#client-api)
5. [Common API](#common-api)
6. [Component System](#component-system)
7. [Event System](#event-system)
8. [UI System](#ui-system)
9. [Common Enumerations](#common-enumerations)
10. [Best Practices](#best-practices)

---

## Quick Start

### Basic Structure

A typical MOD project structure:

```
mod/
├── client/          # Client-side code
│   ├── component/   # Client components
│   ├── system/      # Client systems
│   └── ui/          # UI interfaces
├── server/          # Server-side code
│   ├── component/   # Server components
│   └── system/      # Server systems
└── common/          # Common code
    ├── component/   # Common components
    └── utils/       # Utility classes
```

### System Registration

Server system registration example:

```python
import mod.server.extraServerApi as serverApi

# Register server system
@serverApi.RegisterSystem("MyNamespace", "MySystem", "path.to.MyServerSystem")
class MyServerSystem(serverApi.ServerSystem):
    def __init__(self, namespace, systemName):
        super(MyServerSystem, self).__init__(namespace, systemName)
        
    def OnDestroy(self):
        pass
```

Client system registration example:

```python
import mod.client.extraClientApi as clientApi

# Register client system
@clientApi.RegisterSystem("MyNamespace", "MySystem", "path.to.MyClientSystem")
class MyClientSystem(clientApi.ClientSystem):
    def __init__(self, namespace, systemName):
        super(MyClientSystem, self).__init__(namespace, systemName)
        
    def OnDestroy(self):
        pass
```

---

## Architecture Overview

### Systems

Systems are the core logic units of MODs, divided into:

- **ServerSystem**: Server-side system, handles game logic
- **ClientSystem**: Client-side system, handles client logic and UI
- **MasterSystem**: Lobby system
- **ServiceSystem**: Service system

### Components

Components are functional modules attached to entities, divided into:

- **Server Components**: Run on the server, handle game logic
- **Client Components**: Run on the client, handle display and interaction
- **Common Components**: Base component classes

### Events

Systems communicate and respond to game state changes through events.

---

## Server API

### extraServerApi

Main server API module providing system and component registration.

#### Core Functions

##### RegisterSystem

Registers a server system to the engine.

```python
def RegisterSystem(nameSpace, systemName, clsPath):
    # type: (str, str, str) -> ServerSystem
    """
    Registers a system to the engine. The engine creates an instance of this system
    and recycles it when exiting the game. Systems can perform basic logic provided
    by the engine, such as listening to events, executing Tick functions, and
    communicating with clients.
    
    Args:
        nameSpace: Namespace, usually the unique identifier of the MOD
        systemName: System name
        clsPath: Path to the system class
        
    Returns:
        ServerSystem instance
    """
```

##### GetSystem

Gets a registered system instance.

```python
def GetSystem(nameSpace, systemName):
    # type: (str, str) -> ServerSystem
    """
    Gets a registered system
    
    Args:
        nameSpace: Namespace
        systemName: System name
        
    Returns:
        ServerSystem instance
    """
```

##### RegisterComponent

Registers a custom component.

```python
def RegisterComponent(nameSpace, name, clsPath):
    # type: (str, str, str) -> bool
    """
    Registers a component to the engine
    
    Args:
        nameSpace: Namespace
        name: Component name
        clsPath: Component class path
        
    Returns:
        Whether registration was successful
    """
```

##### CreateComponent

Creates a component for an entity.

```python
def CreateComponent(entityId, nameSpace, name):
    # type: (Union[str,int], str, str) -> BaseComponent
    """
    Creates a server component for an entity
    
    Args:
        entityId: Entity ID
        nameSpace: Namespace
        name: Component name
        
    Returns:
        Component instance
    """
```

##### GetComponent

Gets a component of an entity.

```python
def GetComponent(entityId, nameSpace, name):
    # type: (str, str, str) -> BaseComponent
    """
    Gets a server component of an entity. Usually used to check if a component
    has been created; use CreateComponent in other situations
    
    Args:
        entityId: Entity ID
        nameSpace: Namespace
        name: Component name
        
    Returns:
        Component instance or None
    """
```

### ServerSystem

Server system base class.

#### Basic Methods

```python
class ServerSystem:
    def __init__(self, namespace, systemName):
        """Initialize system"""
        pass
        
    def OnDestroy(self):
        """Called when system is destroyed"""
        pass
        
    def Update(self):
        """Called once per game tick"""
        pass
        
    def ListenForEvent(self, namespace, systemName, eventName, instance, func, priority=0):
        """Listen for event"""
        pass
        
    def UnListenForEvent(self, namespace, systemName, eventName, instance, func):
        """Stop listening for event"""
        pass
        
    def NotifyToClient(self, playerId, eventName, eventData):
        """Send message to client"""
        pass
        
    def BroadcastToAllClient(self, eventName, eventData):
        """Broadcast message to all clients"""
        pass
```

### Server Components

#### AttrCompServer

Attribute component for managing entity attributes.

```python
class AttrCompServer(BaseComponent):
    def SetAttrValue(self, attrType, value, setDefault=1):
        # type: (int, float, int) -> bool
        """
        Sets an entity's engine attribute
        
        Args:
            attrType: Attribute type (refer to AttrType enum)
            value: Attribute value
            setDefault: Whether to set default value
            
        Returns:
            Whether setting was successful
        """
        
    def GetAttrValue(self, attrType):
        # type: (int) -> float
        """
        Gets an entity's engine attribute
        
        Args:
            attrType: Attribute type
            
        Returns:
            Attribute value
        """
        
    def SetAttrMaxValue(self, type, value):
        # type: (int, float) -> bool
        """Sets the maximum value of an entity's engine attribute"""
        
    def GetAttrMaxValue(self, type):
        # type: (int) -> float
        """Gets the maximum value of an entity's engine attribute"""
        
    def IsEntityOnFire(self):
        # type: () -> bool
        """Gets whether the entity is on fire"""
        
    def SetEntityOnFire(self, seconds, burn_damage=1):
        # type: (int, int) -> bool
        """Sets the entity on fire"""
        
    def SetStepHeight(self, stepHeight):
        # type: (float) -> bool
        """
        Sets the maximum step height a player can walk up without jumping
        Default is 0.5625; 1 means can walk up one block
        """
        
    def GetTypeFamily(self):
        # type: () -> List[str]
        """Gets the entity's behavior pack type_family field"""
```

#### ItemCompServer

Item component for managing player inventory.

```python
class ItemCompServer(BaseComponent):
    def GetPlayerItem(self, itemType, auxValue=0):
        """Gets player item"""
        
    def SetInvItemNum(self, slot, num):
        """Sets the number of items in a specific inventory slot"""
        
    def GetInvItem(self, slot):
        """Gets item information from a specific inventory slot"""
        
    def SpawnItemToPlayerInv(self, itemDict, playerId):
        """Spawns an item into the player's inventory"""
        
    def GetPlayerAllItems(self, posType=-1):
        """Gets all player items"""
```

#### PosCompServer

Position component.

```python
class PosCompServer(BaseComponent):
    def GetPos(self):
        # type: () -> Tuple[float, float, float]
        """Gets entity position coordinates"""
        
    def SetPos(self, pos):
        # type: (Tuple[float, float, float]) -> bool
        """Sets entity position coordinates"""
        
    def GetFootPos(self):
        """Gets entity foot position"""
```

#### GameCompServer

Game management component.

```python
class GameCompServer(BaseComponent):
    def SetCanRespawn(self, canRespawn):
        """Sets whether the player can respawn"""
        
    def ChangePlayerGameMode(self, gameMode):
        """Changes player game mode"""
        
    def SetTime(self, time):
        """Sets world time"""
        
    def GetTime(self):
        """Gets world time"""
        
    def SetDefaultGameMode(self, gameMode):
        """Sets default game mode"""
```

#### BlockCompServer

Block component.

```python
class BlockCompServer(BaseComponent):
    def GetBlockNew(self, pos):
        """Gets block information at specified position"""
        
    def SetBlockNew(self, pos, blockDict, oldBlockHandling=0):
        """Sets block at specified position"""
        
    def GetBlockClicked(self):
        """Gets the position of the clicked block"""
```

#### EffectCompServer

Effect component for managing status effects (such as poison, speed boost, etc.).

```python
class EffectCompServer(BaseComponent):
    def AddEffectToEntity(self, effectId, duration, amplifier=0, showParticles=True):
        """Adds a status effect to an entity"""
        
    def RemoveEffectFromEntity(self, effectId):
        """Removes a status effect from an entity"""
        
    def GetAllEffects(self):
        """Gets all status effects on an entity"""
```

---

## Client API

### extraClientApi

Main client API module.

#### Core Functions

##### RegisterSystem

```python
def RegisterSystem(nameSpace, systemName, clsPath):
    # type: (str, str, str) -> ClientSystem
    """
    Registers a system to the engine. The engine creates an instance of this system
    and recycles it when exiting the game. Systems can perform basic logic provided
    by the engine, such as listening to events, executing Tick functions, and
    communicating with the server.
    """
```

##### GetSystem

```python
def GetSystem(nameSpace, systemName):
    # type: (str, str) -> ClientSystem
    """Gets another system instance"""
```

##### CreateComponent

```python
def CreateComponent(entityId, nameSpace, name):
    # type: (Union[str,int], str, str) -> BaseComponent
    """Creates a client component for an entity"""
```

### ClientSystem

Client system base class.

```python
class ClientSystem:
    def __init__(self, namespace, systemName):
        """Initialize system"""
        
    def OnDestroy(self):
        """Called when system is destroyed"""
        
    def Update(self):
        """Called once per game tick"""
        
    def ListenForEvent(self, namespace, systemName, eventName, instance, func, priority=0):
        """Listen for event"""
        
    def UnListenForEvent(self, namespace, systemName, eventName, instance, func):
        """Stop listening for event"""
        
    def NotifyToServer(self, eventName, eventData):
        """Send message to server"""
        
    def CreateUI(self, modName, clsPath, screenDef):
        """Create UI interface"""
```

### Client Components

#### AttrCompClient

Client attribute component.

```python
class AttrCompClient(BaseComponent):
    def isEntityInLava(self):
        # type: () -> bool
        """Whether the entity is in lava"""
        
    def isEntityOnGround(self):
        # type: () -> bool
        """Whether the entity is on the ground"""
        
    def GetAttrValue(self, attrType):
        # type: (int) -> float
        """Gets attribute value including health, hunger, speed"""
        
    def GetAttrMaxValue(self, type):
        # type: (int) -> float
        """Gets maximum attribute value"""
```

#### CameraCompClient

Camera component.

```python
class CameraCompClient(BaseComponent):
    def SetCameraMode(self, mode):
        """Sets camera mode (first-person/third-person)"""
        
    def LockCamera(self, rot):
        """Locks camera angle"""
        
    def UnlockCamera(self):
        """Unlocks camera"""
        
    def SetFov(self, fov):
        """Sets field of view angle"""
```

#### ModelCompClient

Model component.

```python
class ModelCompClient(BaseComponent):
    def SetModel(self, model):
        """Sets entity model"""
        
    def ResetModel(self):
        """Resets entity model"""
        
    def GetModel(self):
        """Gets entity model identifier"""
```

#### DrawingCompClient (New in Version 3.5)

Drawing component for rendering various shapes in the game.

```python
class DrawingCompClient(BaseComponent):
    def AddBoxShape(self, pos, scale=(1, 1, 1), color=(1, 1, 1)):
        # type: (Tuple[float,float,float], Tuple[float,float,float], Tuple[float,float,float]) -> DrawingShape
        """Creates a box shape"""
        
    def AddLineShape(self, startPos, endPos, color=(1, 1, 1)):
        # type: (Tuple[float,float,float], Tuple[float,float,float], Tuple[float,float,float]) -> DrawingShape
        """Creates a line shape"""
        
    def AddCircleShape(self, pos, radius, color=(1, 1, 1), plane=2, segmentsNum=20):
        # type: (Tuple[float,float,float], float, Tuple[float,float,float], int, int) -> DrawingShape
        """Creates a circle shape"""
        
    def AddArrowShape(self, startPos, endPos, color=(1, 1, 1), headSegmentsNum=20, arrowHeadLength=1, radius=0.5):
        # type: (Tuple[float,float,float], Tuple[float,float,float], Tuple[float,float,float], int, float, float) -> DrawingShape
        """Creates an arrow shape"""
        
    def AddTextShape(self, pos, text, color=(1, 1, 1)):
        # type: (Tuple[float,float,float], str, Tuple[float,float,float]) -> DrawingShape
        """Creates a text shape"""
        
    def AddSphereShape(self, pos, radius, color=(1, 1, 1), segmentsNum=20):
        # type: (Tuple[float,float,float], float, Tuple[float,float,float], int) -> DrawingShape
        """Creates a sphere shape"""
        
    def RemoveAll(self):
        # type: () -> bool
        """Removes all shapes"""
```

---

## Common API

### minecraftEnum

Game constants and enumeration definitions.

#### ActorDamageCause

Damage type enumeration.

```python
class ActorDamageCause:
    NONE = "none"                          # Other
    Override = "override"                  # Abnormal method
    Contact = "contact"                    # Contact damage (e.g., cactus)
    EntityAttack = "entity_attack"         # Entity attack
    Projectile = "projectile"              # Projectile attack
    Suffocation = "suffocation"            # Suffocation
    Fall = "fall"                          # Fall damage
    Fire = "fire"                          # Fire
    FireTick = "fire_tick"                 # Continuous fire
    Lava = "lava"                          # Lava
    Drowning = "drowning"                  # Drowning
    BlockExplosion = "block_explosion"     # Block explosion
    EntityExplosion = "entity_explosion"   # Entity explosion
    Void = "void"                          # Void
    Magic = "magic"                        # Magic damage
    Wither = "wither"                      # Wither effect
    Starve = "starve"                      # Starvation
    Lightning = "lightning"                # Lightning
    Freezing = "freezing"                  # Freezing
```

#### AttrType

Attribute type enumeration.

```python
class AttrType:
    HEALTH = 0              # Health, vanilla range [0,20]
    SPEED = 1               # Speed, vanilla range [0,+∞]
    DAMAGE = 2              # Attack damage, vanilla range [1,+∞]
    UNDERWATER_SPEED = 3    # Underwater speed
    HUNGER = 4              # Hunger, vanilla range [0,20]
    SATURATION = 5          # Saturation, vanilla range [0,20]
    ABSORPTION = 6          # Absorption health, vanilla range [0,16]
    LAVA_SPEED = 7          # Speed in lava
    LUCK = 8                # Luck, vanilla range [-1024,1024]
    FOLLOW_RANGE = 9        # Follow range (mob aggro range)
    KNOCKBACK_RESISTANCE = 10  # Knockback resistance
    JUMP_STRENGTH = 11      # Jump strength (mount jump height)
    ARMOR = 12              # Armor value
```

#### GameType

Game mode enumeration.

```python
class GameType:
    Survival = 0      # Survival mode
    Creative = 1      # Creative mode
    Adventure = 2     # Adventure mode
    Spectator = 3     # Spectator mode
```

#### ArmorSlotType

Equipment slot enumeration.

```python
class ArmorSlotType:
    DEFAULT = -1
    HEAD = 0    # Helmet
    BODY = 1    # Chestplate
    LEG = 2     # Leggings
    FOOT = 3    # Boots
```

---

## Component System

### Creating Custom Components

Server component example:

```python
from mod.common.component.baseComponent import BaseComponent

class MyCustomCompServer(BaseComponent):
    def __init__(self):
        super(MyCustomCompServer, self).__init__()
        
    def MyMethod(self):
        """Custom method"""
        pass
```

### Registering and Using Components

```python
import mod.server.extraServerApi as serverApi

# Register component
serverApi.RegisterComponent("MyNamespace", "MyComp", "path.to.MyCustomCompServer")

# Create component
comp = serverApi.CreateComponent(entityId, "MyNamespace", "MyComp")

# Use component
comp.MyMethod()
```

---

## Event System

### Listening for Events

```python
class MyServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        super(MyServerSystem, self).__init__(namespace, systemName)
        
        # Listen for player join event
        self.ListenForEvent(
            "Minecraft",           # Namespace
            "Minecraft",           # System name
            "PlayerJoinEvent",     # Event name
            self,                  # Instance
            self.OnPlayerJoin      # Callback function
        )
        
    def OnPlayerJoin(self, args):
        """Player join event handler"""
        playerId = args["playerId"]
        print("Player joined:", playerId)
```

### Common Events

#### Server Events

- `PlayerJoinEvent` - Player join
- `PlayerDieEvent` - Player death
- `ServerPlayerGetExperienceOrbEvent` - Player gains experience orb
- `PlayerAttackEvent` - Player attack
- `DamageEvent` - Damage event
- `BlockNeighborChangedServerEvent` - Block neighbor changed

#### Client Events

- `OnLocalPlayerStopLoading` - Local player finished loading
- `PlayerAttackEvent` - Player attack
- `UiInitFinished` - UI initialization finished
- `OnScriptTickClient` - Client tick event

---

## Best Practices

### 1. Naming Conventions

- Use meaningful namespaces to avoid conflicts with other MODs
- Use CamelCase for system names
- End component names with Comp

### 2. Memory Management

```python
class MyServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        super(MyServerSystem, self).__init__(namespace, systemName)
        self.timers = []
        
    def OnDestroy(self):
        """Clean up resources"""
        # Unlisten all events
        self.UnListenForEvent(...)
        
        # Clean up timers
        for timer in self.timers:
            timer.Cancel()
        
        # Clear references
        self.timers = []
```

### 3. Error Handling

```python
def SafeOperation(self, entityId):
    """Safe operation example"""
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

### 4. Performance Optimization

- Avoid heavy operations in Update/Tick functions
- Use caching to reduce redundant calculations
- Use event listeners wisely, avoid unnecessary event handling

```python
class OptimizedSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        super(OptimizedSystem, self).__init__(namespace, systemName)
        self.cache = {}
        self.tickCount = 0
        
    def Update(self):
        """Optimized update function"""
        self.tickCount += 1
        
        # Execute every 10 ticks instead of every tick
        if self.tickCount % 10 == 0:
            self.DoExpensiveOperation()
```

### 5. Client-Server Communication

Server sends message to client:

```python
# Server side
def NotifyClient(self, playerId, message):
    eventData = {"message": message}
    self.NotifyToClient(playerId, "ShowMessage", eventData)
```

Client receives and handles message:

```python
# Client side
class MyClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        super(MyClientSystem, self).__init__(namespace, systemName)
        
        # Listen for message from server
        self.ListenForEvent("MyNamespace", "MySystem", "ShowMessage", self, self.OnShowMessage)
        
    def OnShowMessage(self, args):
        message = args["message"]
        print("Message from server:", message)
```

---

## Version Differences

### 3.4 vs 3.5

Main new features (3.5):

1. **DrawingCompClient** - New drawing component supporting various shapes in game
   - Box, line, circle, arrow, text, sphere, etc.

2. **DrawingShapeCompClient** - Shape control component
   - Control display, hide, position of drawn shapes

Recommendations:

- Use version 3.4 for stable projects
- Use version 3.5 for projects requiring drawing features
- Core APIs are mostly compatible between versions

---

## Contributing

Welcome to submit issues and improvement suggestions!

## License

This documentation is written based on SDK usage instructions, for learning and development reference only.
