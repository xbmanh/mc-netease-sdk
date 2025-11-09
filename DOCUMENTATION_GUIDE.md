# Python库文件文档编写指南

## 概述

本指南说明如何为Minecraft网易版MOD Python库文件编写开发文档。遵循此指南可以确保文档的一致性和质量。

## 文档标准

每个Python库文件应包含三个层次的文档：

### 1. 模块级文档（文件顶部）

在文件开头的模块docstring中包含：

```python
# -*- coding: utf-8 -*-
"""
模块名称

模块功能的简要描述（1-2句话）。

主要功能：
    - 功能1的说明
    - 功能2的说明
    - 功能3的说明

使用场景：
    - 场景1
    - 场景2
    - 场景3

重要概念说明：
    如有必要，解释相关的技术概念、系统机制等

注意事项：
    - 重要的注意事项
    - 限制条件
    - 最佳实践

示例：
    >>> import mod.server.extraServerApi as serverApi
    >>> # 简单的使用示例
    >>> comp = serverApi.CreateComponent(entityId, "Minecraft", "componentName")
    >>> result = comp.SomeMethod()
"""
```

### 2. 类级文档

为每个类添加docstring：

```python
class ComponentName(BaseClass):
    """
    类的简要描述
    
    类的详细说明，包括用途、职责、使用方式等。
    """
```

### 3. 方法级文档

为每个方法添加详细的docstring：

```python
def MethodName(self, param1, param2=default):
    # type: (Type1, Type2) -> 'ReturnType'
    """
    方法的简要描述（一句话）
    
    方法的详细描述，说明功能、行为、特性等（2-3句话）。
    
    Args:
        param1 (Type1): 参数1的详细说明，包括含义、有效范围等
        param2 (Type2, optional): 参数2的详细说明。默认为default
        
    Returns:
        ReturnType: 返回值的详细说明，包括含义、可能的值等
        
    示例：
        >>> # 基础使用示例
        >>> comp = serverApi.CreateComponent(entityId, "Minecraft", "component")
        >>> result = comp.MethodName(value1, value2)
        >>> print(result)
        
    应用场景：
        >>> # 实际应用场景示例
        >>> def ComplexUseCase():
        ...     comp = serverApi.CreateComponent(entityId, "Minecraft", "component")
        ...     result = comp.MethodName(value1)
        ...     if result:
        ...         # 处理结果
        ...         pass
        
    参数说明：（如有复杂参数需要详细解释）
        - param1的详细说明
        - param2的详细说明
        
    注意：
        - 重要的注意事项
        - 使用限制
        - 性能考虑
        - 边界情况
    
    相关方法：
        - RelatedMethod1: 相关方法的说明
        - RelatedMethod2: 相关方法的说明
    
    相关组件：（如适用）
        - ComponentName: 组件说明
    """
    pass
```

## 文档编写要点

### 1. 使用清晰的中文

- 使用准确、专业的术语
- 避免歧义和模糊表述
- 保持语言简洁明了

### 2. 提供充分的示例

每个方法至少包含：
- 1个基础使用示例
- 1-2个实际应用场景示例
- 示例代码应该是可运行的（或接近可运行）

### 3. 详细说明参数

对于每个参数：
- 说明参数的含义和用途
- 标注参数类型
- 说明默认值（如有）
- 说明有效范围或约束
- 提供示例值

### 4. 说明返回值

对于返回值：
- 说明返回值的含义
- 说明可能的返回值
- 说明特殊情况的返回值（如失败、未找到等）

### 5. 注意事项

列出：
- 使用限制
- 性能注意事项
- 常见错误
- 最佳实践
- 版本相关信息

### 6. 交叉引用

- 引用相关的方法
- 引用相关的组件
- 引用相关的API
- 提供文档链接

## 示例：完整文档

参考以下已完成文档的文件作为示例：

### 服务端组件示例

- `3.4/mod/server/component/tagCompServer.py` - 简单组件的文档示例
- `3.4/mod/server/component/attrCompServer.py` - 复杂组件的文档示例

### 客户端组件示例

- `3.4/mod/client/component/posCompClient.py` - 位置组件文档示例
- `3.4/mod/client/component/rotCompClient.py` - 旋转组件文档示例

### API文件示例

- `3.4/mod/server/extraServerApi.py` - 服务端API完整文档
- `3.4/mod/client/extraClientApi.py` - 客户端API完整文档

## 文档审查清单

在提交文档前，检查：

- [ ] 模块级文档是否完整
- [ ] 每个公开类都有文档
- [ ] 每个公开方法都有详细文档
- [ ] 每个方法至少有1个示例
- [ ] 参数说明完整且准确
- [ ] 返回值说明清晰
- [ ] 注意事项列举充分
- [ ] 相关方法引用正确
- [ ] 中文表述准确无歧义
- [ ] 代码示例可以运行
- [ ] 格式符合Python docstring标准

## 特殊情况处理

### 复杂方法

对于参数多、逻辑复杂的方法：
1. 增加"参数说明"部分详细解释每个参数
2. 提供多个示例覆盖不同使用场景
3. 在注意事项中说明参数之间的关系

### 废弃的方法

对于已废弃但仍保留的方法：
```python
def OldMethod(self):
    """
    旧方法说明
    
    .. deprecated:: 版本号
        此方法已废弃，请使用 NewMethod 代替。
        
    相关方法：
        - NewMethod: 新方法的说明
    """
    pass
```

### 实验性功能

对于实验性功能：
```python
def ExperimentalMethod(self):
    """
    实验性方法说明
    
    .. warning::
        这是实验性功能，API可能在未来版本中改变。
        
    注意：
        - 不建议在生产环境使用
        - API可能会发生变化
    """
    pass
```

## 工具和辅助

### VS Code 扩展

推荐使用以下VS Code扩展辅助文档编写：
- Python Docstring Generator
- autoDocstring

### 文档生成

未来可以使用以下工具生成HTML文档：
- Sphinx
- pdoc

## 贡献指南

1. 选择需要文档化的文件
2. 按照本指南编写文档
3. 参考已完成的示例文件
4. 提交前使用审查清单检查
5. 创建Pull Request

## 联系和反馈

如有文档编写相关问题：
- 查看已完成的示例文件
- 参考本指南
- 在GitHub Issue中提问

---

遵循此指南可以确保MOD开发文档的高质量和一致性，帮助开发者更好地理解和使用API。
