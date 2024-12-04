class SocialNetwork:
    def __init__(self):
        # Using an adjacency list representation for the graph
        self.connections = {}

    def add_user(self, user):
        """Add a new user to the network if they don't already exist."""
        if user not in self.connections:
            self.connections[user] = set()
        return f"User {user} added to the network."

    def add_connection(self, user1, user2):
        """Create a bidirectional connection between two users."""
        # Ensure both users exist in the network
        self.add_user(user1)
        self.add_user(user2)

        # Add connections in both directions
        self.connections[user1].add(user2)
        self.connections[user2].add(user1)
        return f"Connection created between {user1} and {user2}."

    def remove_connection(self, user1, user2):
        """Remove the connection between two users."""
        if user1 in self.connections and user2 in self.connections:
            self.connections[user1].discard(user2)
            self.connections[user2].discard(user1)
            return f"Connection removed between {user1} and {user2}."
        return "Users not found in the network."

    def is_connected(self, user1, user2):
        """Check if two users are directly connected."""
        return (user1 in self.connections and
                user2 in self.connections[user1])

    def list_connections(self, user):
        """List all connections for a specific user."""
        if user in self.connections:
            return list(self.connections[user])
        return "User not found in the network."

    def find_mutual_connections(self, user1, user2):
        """Find mutual connections between two users."""
        if user1 in self.connections and user2 in self.connections:
            return list(self.connections[user1].intersection(self.connections[user2]))
        return "One or both users not found in the network."

    def get_connection_degree(self, user):
        """Get the number of direct connections for a user."""
        if user in self.connections:
            return len(self.connections[user])
        return "User not found in the network."
