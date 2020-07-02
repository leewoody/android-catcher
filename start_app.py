# -*- coding: UTF-8 -*-

import _main_
from task import Task


class StartAppTask(Task): 
	def init(self,name): 
		super().init(name) 
	def execute(self): 
		self.d.app_start("com.mitac.sirius_ap.debug")
	
_main_.main(StartAppTask("StartApp"))

