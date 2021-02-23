
from platform import system
from platformio.managers.platform import PlatformBase

class P67Platform(PlatformBase):
    def configure_default_packages(self, variables, targets):
        framework = variables.get("pioframework", [])
        if variables["board"].startswith('ec2'):
            del self.packages["toolchain-gccarmnoneeabi"]
        return PlatformBase.configure_default_packages(self, variables, targets)
