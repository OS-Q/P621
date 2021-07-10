from platform import system
from platformio.managers.platform import PlatformBase

class P621Platform(PlatformBase):
    def configure_default_packages(self, variables, targets):
        return PlatformBase.configure_default_packages(self, variables, targets)
