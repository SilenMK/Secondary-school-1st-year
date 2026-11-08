computers = []

for i in range(1, 11):
    computer = {
        "name": f"PC{i}",
        "ip": f"192.168.1.{i}",
        "subnet": "255.255.255.0",
        "connected": True
    }

    computers.append(computer)

for computer in computers:
    print(computer["name"], computer["ip"], computer["connected"])

topology = "star"

connections = []

if topology == "star":
    for computer in computers:
        connections.append(
            ("Switch", computer["name"])
        )

for connection in connections:
    print(connection[0], "<---->", connection[1])

running = True

while running:
    print("\n===== NETWORK SIMULATOR =====")
    print("1. View computers")
    print("2. View connections")
    print("3. Choose computer")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        for computer in computers:
            print(computer["name"], computer["ip"])

    elif choice == "2":
        for connection in connections:
            print(connection[0], "<---->", connection[1])

    elif choice == "3":
        sender = input("Choose sender (PC1-PC10): ")

        sender_found = False

        for computer in computers:
            if computer["name"] == sender:
                sender_found = True

        if sender_found == False:
            print("Sender computer not found!")

        else:
            receiver = input("Choose receiver (PC1-PC10): ")
            
            receiver_found = False

            for computer in computers:
                if computer["name"] == receiver:
                    receiver_found = True

            if receiver_found == False:
                print("Receiver computer not found!")

            else:
                message = input("Enter your message: ")

                print("\n===== MESSAGE SENT =====")
                print(sender, "---->", receiver)
                print("Message:", message)

    elif choice == "4":
        running = False