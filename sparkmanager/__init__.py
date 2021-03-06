def _jupyter_nbextension_paths():
    """Used by 'jupyter nbextension' command to install frontend extension"""
    return [
		dict(
        	section="notebook",
        	# the path is relative to the `my_fancy_module` directory
        	src="nbextension",
        	# directory in the `nbextension/` namespace
        	dest="sparkmanager",
        	# _also_ in the `nbextension/` namespace
        	require="sparkmanager/main"
		)
	]


def _jupyter_server_extension_paths():
    """Used by "jupyter serverextension" command to install web server extension'"""
    return [{
        "module": "sparkmanager.serverextension"
    }]

