from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import compas_rhino
import uuid

from compas_rv2.rhino import SettingsForm
from compas_rv2.rhino import MeshObject


__all__ = ['Scene']


class Scene(object):
    """"""

    def __init__(self, settings={}):
        self.nodes = {}
        self.settings = settings

    def add(self, item, **kwargs):
        node = MeshObject.build(item, **kwargs)
        guid = uuid.uuid4()
        node.id = guid
        self.nodes[guid] = node
        return node

    def get(self, name):
        selected = []
        for _id in self.nodes:
            if name == self.nodes[_id].name:
                selected.append(self.nodes[_id])
        if len(selected) == 0:
            return [None]
        else:
            return selected

    def update(self):
        compas_rhino.rs.EnableRedraw(False)
        for _id in self.nodes:
            node = self.nodes[_id]
            if node.visible:
                node.draw()
        compas_rhino.rs.EnableRedraw(True)
        compas_rhino.rs.Redraw()

    def clear(self):
        compas_rhino.rs.EnableRedraw(False)
        for _id in list(self.nodes.keys()):
            node = self.nodes[_id]
            node.clear()
            del self.nodes[_id]
        self.nodes = {}
        compas_rhino.rs.EnableRedraw(True)
        compas_rhino.rs.Redraw()

    def update_settings(self, settings=None):
        # should this not produce some kind of result we can react to?
        SettingsForm.from_settings(self.settings)

    def clear_selection(self):
        compas_rhino.rs.UnselectAllObjects()

    def update_selection(self, guids):
        compas_rhino.rs.SelectObjects(guids)

    @property
    def registered_object_types(self):
        return MeshObject.registered_object_types()


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    from compas.geometry import Point
    from compas.geometry import Line
    from compas.geometry import Frame

    from compas.datastructures import Mesh

    scene = Scene()

    a = Point(1.0, 1.0, 0.0)
    b = Point(5.0, 5.0, 0.0)
    ab = Line(a, b)
    world = Frame.worldXY()

    mesh = Mesh.from_polyhedron(6)

    scene.add(a, name="A", color=(0, 0, 0), layer="A")
    scene.add(b, name="B", color=(255, 255, 255), layer="B")
    scene.add(ab, name="AB", color=(128, 128, 128), layer="AB")
    scene.add(world, name="World", layer="World")
    scene.add(mesh, name="Cube", layer="Cube")

    scene.update()
