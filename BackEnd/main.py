import server as s
import client
import game as g
from collections import deque


def main():
    
    client_queue: deque[tuple[str, client.Client]] = deque([])
    server = s.Server(client_queue)
    game = g.Game(client_queue)
    
    try:
        while True:
            server.update()

    except KeyboardInterrupt:
        server.close()

if __name__ == "__main__":
    main()