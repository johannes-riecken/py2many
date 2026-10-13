import ast


class _Num(ast.Constant):
    @property
    def n(self):
        return self.value

    @n.setter
    def n(self, val):
        self.value = val


class _Str(ast.Constant):
    @property
    def s(self):
        return self.value

    @s.setter
    def s(self, val):
        self.value = val


class _Bytes(ast.Constant):
    @property
    def s(self):
        return self.value

    @s.setter
    def s(self, val):
        self.value = val


class _Ellipsis(ast.Constant):
    pass


class _NameConstant(ast.Constant):
    pass


_Num.__name__ = "Num"
_Str.__name__ = "Str"
_Bytes.__name__ = "Bytes"
_Ellipsis.__name__ = "Ellipsis"
_NameConstant.__name__ = "NameConstant"

_Num.__qualname__ = "Num"
_Str.__qualname__ = "Str"
_Bytes.__qualname__ = "Bytes"
_Ellipsis.__qualname__ = "Ellipsis"
_NameConstant.__qualname__ = "NameConstant"

ast.Num = _Num
ast.Str = _Str
ast.Bytes = _Bytes
ast.Ellipsis = _Ellipsis
ast.NameConstant = _NameConstant


class AstCompatRewriter(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, bool):
            new_node = _NameConstant(node.value)
        elif node.value is None:
            new_node = _NameConstant(node.value)
        elif node.value is ...:
            new_node = _Ellipsis()
        elif isinstance(node.value, (int, float, complex)):
            new_node = _Num(node.value, node.kind if hasattr(node, 'kind') else None)
        elif isinstance(node.value, str):
            new_node = _Str(node.value, node.kind if hasattr(node, 'kind') else None)
        elif isinstance(node.value, bytes):
            new_node = _Bytes(node.value, node.kind if hasattr(node, 'kind') else None)
        else:
            return node
        new_node.lineno = node.lineno
        new_node.col_offset = node.col_offset
        new_node.end_lineno = node.end_lineno
        new_node.end_col_offset = node.end_col_offset
        ast.fix_missing_locations(new_node)
        return new_node