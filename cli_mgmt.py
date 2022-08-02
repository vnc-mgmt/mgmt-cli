import vnc_cmd as cmd

class VNCCLI(cmd.Cmd):
    prompt = 'VNC Manager: '
    def __init__(self, socket):
        cmd.Cmd.__init__(self, completekey='tab', stdin=None, stdout=None)
        self.socket = socket
    def default(self, line):
        pass
    def precmd(self, cmd):
        if not cmd == '':
            self.socket.send(cmd.encode())
            print(self.socket.recv(2048).decode('utf-8'))
        if cmd == 'exit':
            self.stop = True
