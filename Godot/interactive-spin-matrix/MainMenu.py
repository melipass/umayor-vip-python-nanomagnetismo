from godot import exposed, export, get_tree
from godot import *


@exposed
class MainMenu(Panel):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		get_tree().change_scene("res://spins.tscn")
