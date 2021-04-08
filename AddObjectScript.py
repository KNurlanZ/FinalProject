bl_info = {
    "name" : "Object Adder",
    "author" : "danissa_s",
    "version" : (1, 0),
    "blender" : (2, 92, 0),
    "location" : "View3d > Tool",
    "warnings" : "This is just a demo",
    "wiki_url" : "",
    "category" : "Add Mesh Add-on",
}

import bpy


class TestPanel(bpy.types.Panel):
    bl_label = "Custom Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My custom tab'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Create a new regular object", icon = 'PLUS')
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon = 'MATCUBE')
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon = 'MESH_UVSPHERE')


class Panel1(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "PT_PanelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My custom tab'
    bl_parent_id = "PT_TestPanel"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text = "This is a panel for scaling", icon = 'OBJECT_HIDDEN')
        row = layout.row()
        row.operator("transform.resize")
        row = layout.row()
        
        col = layout.column()
        col.prop(obj, "scale")


class Panel2(bpy.types.Panel):
    bl_label = "Rotation"
    bl_idname = "PT_PanelB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My custom tab'
    bl_parent_id = "PT_TestPanel"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text = "This is a panel for rotation", icon = 'CON_ROTLIKE')
        col = layout.column()
        col.prop(obj, "rotation_euler")

class Panel3(bpy.types.Panel):
    bl_label = "Bounds"
    bl_idname = "PT_PanelC"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My custom tab'
    bl_parent_id = "PT_TestPanel"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        col = layout.column()
        col.prop(obj, "show_bounds", icon = 'UGLYPACKAGE')

def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(Panel1)
    bpy.utils.register_class(Panel2)
    bpy.utils.register_class(Panel3)
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(Panel1)
    bpy.utils.unregister_class(Panel2)
    bpy.utils.unregister_class(Panel3)
    
if __name__ == "__main__":
    register()
    