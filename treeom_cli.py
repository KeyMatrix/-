import json

# TreeOM structure
treeom = {
    "nodes": [
        {"id": "OM", "type": "core", "color": "#00FFFF"},
        {"id": "StreamPanel", "type": "module", "color": "#FF00FF"},
        {"id": "GitHubEvents", "type": "feed", "color": "#FFFF00"},
        {"id": "MetaBridge", "type": "bridge", "color": "#FFA500"}
    ],
    "links": [
        {"source": "OM", "target": "StreamPanel", "type": "flow", "channel": "aura-visual", "description": "Передача импульсов визуализации в режиме реального времени."},
        {"source": "OM", "target": "GitHubEvents", "type": "signal", "channel": "dev-events", "description": "Поток сигналов активности репозиториев."},
        {"source": "GitHubEvents", "target": "StreamPanel", "type": "data", "channel": "event-feed", "description": "Передача событий для визуализации."},
        {"source": "OM", "target": "MetaBridge", "type": "link", "channel": "meta-sync", "description": "Связь ядра с мостом MetaBridge."},
        {"source": "MetaBridge", "target": "StreamPanel", "type": "aura-flow", "channel": "dash-ready-pack", "description": "Экспорт визуализации в готовые пакеты."}
    ]
}

# CLI Initialization
def cli_interface():
    print("🌐 TreeOM CLI Interface 🌐")
    print("1. View TreeOM Structure")
    print("2. Add Node")
    print("3. Add Link")
    print("4. Exit")
    
    while True:
        choice = input("Select an option: ")
        if choice == "1":
            print(json.dumps(treeom, indent=4, ensure_ascii=False))
        elif choice == "2":
            node_id = input("Enter node ID: ")
            node_type = input("Enter node type (core/module/feed/bridge): ")
            node_color = input("Enter node color (hex format): ")
            treeom["nodes"].append({"id": node_id, "type": node_type, "color": node_color})
            print(f"Node {node_id} added successfully!")
        elif choice == "3":
            source = input("Enter source node ID: ")
            target = input("Enter target node ID: ")
            link_type = input("Enter link type (flow/signal/data/link): ")
            channel = input("Enter channel name: ")
            description = input("Enter description: ")
            treeom["links"].append({"source": source, "target": target, "type": link_type, "channel": channel, "description": description})
            print(f"Link from {source} to {target} added successfully!")
        elif choice == "4":
            print("Exiting TreeOM CLI. Resonance maintained.")
            break
        else:
            print("Invalid option. Please try again.")

# Start CLI
if __name__ == "__main__":
    cli_interface()