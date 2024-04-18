import server as s
import client


def main():
    
    clients = []
    server = s.Server(clients)
    
    try:
        while True:
            server.update()
            # TODO: process client messages
    except KeyboardInterrupt:
        server.close()

if __name__ == "__main__":
    main()