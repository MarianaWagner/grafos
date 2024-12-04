from social_network import SocialNetwork

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
