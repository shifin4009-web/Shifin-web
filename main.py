class PLC:
    def __init__(self,name):
        self.name = name
        self.is_running = False
    def start(self):
        self.is_running = True
        print(
            self.name, "is running"
        )
    def stop(self):
        self.is_running = False
        print(self.name, "is stopped")


plc1 = PLC("main plc")
plc1.start()
plc1.stop()
