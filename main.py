import os
import os.path
import sys
import venv
  

'''
def create(self, env_dir):
    env_dir = os.path.abspath(env_dir)
    context = self.ensure_directories(env_dir)
    self.create_configuration(context)
    self.setup_python(context)
    self.setup_scripts(context)
    self.post_setup(context)
'''
test = venv.EnvBuilder(system_site_packages=True, clear=True, upgrade=True, with_pip= True,
                       upgrade_deps=True)

test = venv.create("/home/diaoko/venv/test")

