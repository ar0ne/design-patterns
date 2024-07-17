"""
Object pool uses a set of initialized objects kept ready to use – a "pool" – rather than allocating
and destroying them on demand. A client of the pool will request an object from the pool and perform
 operations on the returned object. When the client has finished, it returns the object to the pool
 rather than destroying it; this can be done manually or automatically.
"""


class Connection:
    pass


class ConnectionPool:

    def __init__(self, size: int = 10) -> None:
        self._available_connections = set(Connection() for _ in range(size))
        self._acquired_connections = set()

    def acquire(self) -> Connection:
        connection = self._available_connections.pop()
        self._acquired_connections.add(connection)
        return connection

    def release(self, connection: Connection) -> None:
        self._acquired_connections.remove(connection)
        self._available_connections.add(connection)

    def get_info(self) -> str:
        return f"{len(self._available_connections)}/{len(self._acquired_connections)}"


if __name__ == "__main__":
    pool = ConnectionPool(10)
    conn = pool.acquire()
    print(pool.get_info())
    pool.release(conn)
    print(pool.get_info())
