from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, user1, user2):
        """Add a bidirectional edge between two users."""
        self.adj_list.setdefault(user1, []).append(user2)
        self.adj_list.setdefault(user2, []).append(user1)

    def bfs(self, start):
        """Perform BFS to find all friends of a user."""
        visited = set()
        queue = deque([start])
        friends = set()

        while queue:
            user = queue.popleft()
            if user not in visited:
                visited.add(user)
                friends.update(self.adj_list.get(user, []))
        return friends

    def find_mutual_friends(self, user1, user2):
        """Find mutual friends between two users."""
        friends1 = self.bfs(user1)
        friends2 = self.bfs(user2)
        return friends1 & friends2

# Create a graph representing the social network
network = Graph()
network.add_edge("Alice", "Bob")
network.add_edge("Alice", "Charlie")
network.add_edge("Bob", "Charlie")
network.add_edge("Charlie", "David")
network.add_edge("David", "Eve")

# Find mutual friends between Alice and Bob
mutual_friends = network.find_mutual_friends("Alice", "Bob")
print("Mutual Friends:", mutual_friends)
