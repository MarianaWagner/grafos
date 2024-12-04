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

def main():
    network = SocialNetwork()
    print("Social Network Connection Management CLI")
    print("Available commands:")
    print("- add_connection <user1> <user2>")
    print("- remove_connection <user1> <user2>")
    print("- is_connected <user1> <user2>")
    print("- list_connections <user>")
    print("- mutual_connections <user1> <user2>")
    print("- connection_degree <user>")
    print("- exit")

    while True:
        try:
            command = input(">>> ").strip().split()

            if not command:
                continue

            if command[0] == 'exit':
                print("Exiting Social Network CLI...")
                break

            elif command[0] == 'add_connection':
                if len(command) == 3:
                    print(network.add_connection(command[1], command[2]))
                else:
                    print("Invalid command. Usage: add_connection <user1> <user2>")

            elif command[0] == 'remove_connection':
                if len(command) == 3:
                    print(network.remove_connection(command[1], command[2]))
                else:
                    print("Invalid command. Usage: remove_connection <user1> <user2>")

            elif command[0] == 'is_connected':
                if len(command) == 3:
                    result = network.is_connected(command[1], command[2])
                    print(f"Connection status: {result}")
                else:
                    print("Invalid command. Usage: is_connected <user1> <user2>")

            elif command[0] == 'list_connections':
                if len(command) == 2:
                    connections = network.list_connections(command[1])
                    print(f"Connections for {command[1]}: {connections}")
                else:
                    print("Invalid command. Usage: list_connections <user>")

            elif command[0] == 'mutual_connections':
                if len(command) == 3:
                    mutual = network.find_mutual_connections(command[1], command[2])
                    print(f"Mutual connections: {mutual}")
                else:
                    print("Invalid command. Usage: mutual_connections <user1> <user2>")

            elif command[0] == 'connection_degree':
                if len(command) == 2:
                    degree = network.get_connection_degree(command[1])
                    print(f"Connection degree for {command[1]}: {degree}")
                else:
                    print("Invalid command. Usage: connection_degree <user>")

            else:
                print("Unknown command. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
