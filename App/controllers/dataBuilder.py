"""
Builder Pattern simplificat, sense clase pare director.
"""
class DataBuilder():
    def __init__(self) -> None:
        self.data = {}

    def set_ip_address(self, ip_address):
        self.data["ip_address"] = ip_address

    def set_user_agent(self, user_agent):
        self.data["user_agent"] = user_agent
    
    def set_accept_languages(self, accept_languages):
        self.data["accept_languages"] = accept_languages

    def set_resolution(self, resolution):
        self.data["resolution"] = resolution

    def set_ppi(self, ppi):
        self.data["ppi"] = ppi
    
    def set_server_time(self, server_time):
        self.data["server_time"] = server_time

    def set_cookie(self, cookie):
        self.data["cookie"] = cookie

    def set_local_time(self, local_time):
        self.data["local_time"] = local_time
    
    def build(self):
        return self.data