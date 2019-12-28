import bpy

from bpy.props import FloatProperty
from bpy.types import Node
from .._base.node_base import ScNode
from .._base.node_operator import ScObjectOperatorNode

class ScDisplaceUp(Node, ScObjectOperatorNode):
    bl_idname = "ScDisplaceUp"
    bl_label = "Displace Upwards (10 units)"

    in_factor: FloatProperty(default=2.0, min=0.0, update=ScNode.update_value)

    def init(self, context):
        super().init(context)
        self.inputs.new("ScNodeSocketBool", "Multiplier")
        self.inputs.new("ScNodeSocketNumber", "Factor").init("in_factor", True)
        self.outputs.new("ScNodeSocketNumber", "Factor")
    
    def error_condition(self):
        return (
            super().error_condition()
            or (self.inputs["Factor"].default_value < 0.0)
        )
    
    def functionality(self):
        if (self.inputs["Multiplier"].default_value):
            self.inputs["Object"].default_value.location[2] += 10 * self.inputs["Factor"].default_value
        else:
            self.inputs["Object"].default_value.location[2] += 10
    
    def post_execute(self):
        out = super().post_execute()
        if (self.inputs["Multiplier"].default_value):
            out["Factor"] = 10 * self.inputs["Factor"].default_value
        else:
            out["Factor"] = 10
        return out