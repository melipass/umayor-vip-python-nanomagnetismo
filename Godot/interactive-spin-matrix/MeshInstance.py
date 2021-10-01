from godot import exposed, export
from godot import *


@exposed
class MeshInstance(MeshInstance):

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		self.translation = Vector3(1, 1, 1)
	
	def _process(self, delta):
		self.translation.x = self.translation.x + 5 * delta
		#if self.translation.x > 500:
			#self.translation.x = 0
