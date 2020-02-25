from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_rv2.rhino import get_scene


__commandname__ = "RV2force_update_faces"


HERE = compas_rhino.get_document_dirname()


def RunCommand(is_interactive):
    scene = get_scene()
    if not scene:
        return

    rhinoforce = scene.get("force")

    if not rhinoforce:
        return

    if rhinoforce.update_faces_attributes():
        scene.update()


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":

    RunCommand(True)
