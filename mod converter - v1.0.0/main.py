import os
import re
import json

# Version mappings for each Minecraft version, including API changes
version_mappings = {
    "1.21": {
        "minecraft_version": "1.21",
        "yarn_mappings": "1.21+build.9",
        "loader_version": "0.16.5",
        "fabric_version": "0.102.0+1.21",
        "api_changes": ["entity_api", "rendering_api", "item_group_registration"]
    },
    "1.20.6": {
        "minecraft_version": "1.20.6",
        "yarn_mappings": "1.20.6+build.3",
        "loader_version": "0.16.5",
        "fabric_version": "0.100.8+1.20.6",
        "api_changes": []
    },
    "1.20.5": {
        "minecraft_version": "1.20.5",
        "yarn_mappings": "1.20.5+build.1",
        "loader_version": "0.16.5",
        "fabric_version": "0.97.8+1.20.5",
        "api_changes": []
    },
    "1.20.4": {
        "minecraft_version": "1.20.4",
        "yarn_mappings": "1.20.4+build.3",
        "loader_version": "0.16.5",
        "fabric_version": "0.97.2+1.20.4",
        "api_changes": ["loot_api", "gradle_tooling"]
    },
    "1.20.3": {
        "minecraft_version": "1.20.3",
        "yarn_mappings": "1.20.3+build.1",
        "loader_version": "0.16.5",
        "fabric_version": "0.91.1+1.20.3",
        "api_changes": ["transfer_api", "block_codecs"]
    },
    "1.20.2": {
        "minecraft_version": "1.20.2",
        "yarn_mappings": "1.20.2+build.4",
        "loader_version": "0.16.5",
        "fabric_version": "0.91.6+1.20.2",
        "api_changes": ["networking_overhaul", "block_wood_registry"]
    },
    "1.20.1": {
        "minecraft_version": "1.20.1",
        "yarn_mappings": "1.20.1+build.10",
        "loader_version": "0.16.5",
        "fabric_version": "0.92.2+1.20.1",
        "api_changes": []
    }
}

def get_version_choice():
    print("Available versions:")
    for version in version_mappings:
        print(f"- {version}")
    
    version = input("What version do you want to update this mod to? ")
    while version not in version_mappings:
        print("Invalid version. Please choose a valid version.")
        version = input("What version do you want to update this mod to? ")
    
    return version_mappings[version]

def update_gradle_properties(file_path, version_info):
    with open(file_path, 'r') as file:
        content = file.read()

    # Update the necessary lines in gradle.properties
    content = re.sub(r"minecraft_version=.*", f"minecraft_version={version_info['minecraft_version']}", content)
    content = re.sub(r"yarn_mappings=.*", f"yarn_mappings={version_info['yarn_mappings']}", content)
    content = re.sub(r"loader_version=.*", f"loader_version={version_info['loader_version']}", content)
    content = re.sub(r"fabric_version=.*", f"fabric_version={version_info['fabric_version']}", content)
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Updated {file_path}")

def update_fabric_mod_json(file_path, version_info):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Modify the "depends" section to use "*" for the versions
    depends = data.get("depends", {})
    if "fabricloader" in depends:
        depends["fabricloader"] = "*"
    if "fabric" in depends:
        depends["fabric"] = "*"
    if "minecraft" in depends:
        depends["minecraft"] = "*"

    # Write the modified data back to fabric.mod.json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Updated {file_path}")

def find_files(root_dir):
    gradle_properties_path = None
    fabric_mod_json_path = None

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'gradle.properties':
                gradle_properties_path = os.path.join(dirpath, filename)
            elif filename == 'fabric.mod.json':
                fabric_mod_json_path = os.path.join(dirpath, filename)
    
    return gradle_properties_path, fabric_mod_json_path

# Conditional API changes based on the selected version
def apply_api_changes(version_info, mod_folder):
    if "networking_overhaul" in version_info['api_changes']:
        # Networking API change from ServerLoginNetworking to ServerConfigurationNetworking
        for dirpath, _, filenames in os.walk(mod_folder):
            for filename in filenames:
                if filename.endswith(".java"):
                    filepath = os.path.join(dirpath, filename)
                    with open(filepath, 'r') as file:
                        content = file.read()
                    
                    content = content.replace('ServerLoginNetworking.registerGlobalReceiver', 'ServerConfigurationNetworking.register')
                    
                    with open(filepath, 'w') as file:
                        file.write(content)
        print("Applied Networking API changes for version 1.20.2+")

    if "block_wood_registry" in version_info['api_changes']:
        # Block/Wood Type Registry changes
        for dirpath, _, filenames in os.walk(mod_folder):
            for filename in filenames:
                if filename.endswith(".java"):
                    filepath = os.path.join(dirpath, filename)
                    with open(filepath, 'r') as file:
                        content = file.read()
                    
                    content = content.replace('BlockSetTypeRegistry.register', 'BlockSetTypeBuilder.create')
                    content = content.replace('WoodTypeRegistry.register', 'WoodTypeBuilder.create')
                    
                    with open(filepath, 'w') as file:
                        file.write(content)
        print("Applied Block and Wood Registry changes for version 1.20.2+")

    if "transfer_api" in version_info['api_changes']:
        # Transfer API changes
        for dirpath, _, filenames in os.walk(mod_folder):
            for filename in filenames:
                if filename.endswith(".java"):
                    filepath = os.path.join(dirpath, filename)
                    with open(filepath, 'r') as file:
                        content = file.read()
                    
                    content = content.replace('.simulateInsert', '')
                    content = content.replace('.simulateExtract', '')
                    content = content.replace('.exactView', '')
                    
                    with open(filepath, 'w') as file:
                        file.write(content)
        print("Applied Transfer API changes for version 1.20.3+")

    if "entity_api" in version_info['api_changes']:
        # Entity API changes
        for dirpath, _, filenames in os.walk(mod_folder):
            for filename in filenames:
                if filename.endswith(".java"):
                    filepath = os.path.join(dirpath, filename)
                    with open(filepath, 'r') as file:
                        content = file.read()
                    
                    content = content.replace('.world', '.getWorld()')
                    
                    with open(filepath, 'w') as file:
                        file.write(content)
        print("Applied Entity API changes for version 1.21+")

    if "rendering_api" in version_info['api_changes']:
        # Rendering API changes
        for dirpath, _, filenames in os.walk(mod_folder):
            for filename in filenames:
                if filename.endswith(".java"):
                    filepath = os.path.join(dirpath, filename)
                    with open(filepath, 'r') as file:
                        content = file.read()
                    
                    content = content.replace('MatrixStack', 'DrawContext')
                    
                    with open(filepath, 'w') as file:
                        file.write(content)
        print("Applied Rendering API changes for version 1.21+")

    if "item_group_registration" in version_info['api_changes']:
        # Item group registration changes
        for dirpath, _, filenames in os.walk(mod_folder):
            for filename in filenames:
                if filename.endswith(".java"):
                    filepath = os.path.join(dirpath, filename)
                    with open(filepath, 'r') as file:
                        content = file.read()
                    
                    content = content.replace('ItemGroup.Builder.create', 'RegistryKey.of')
                    
                    with open(filepath, 'w') as file:
                        file.write(content)
        print("Applied Item Group Registration changes for version 1.21+")

def main():
    # Get the folder path where the mod's source is located
    mod_folder = input("Please drop the folder containing the mod source: ").strip()

    # Remove leading and trailing quotes if present
    mod_folder = mod_folder.strip('"').strip("'")
    
    # Get the desired version mappings
    version_info = get_version_choice()

    # Find and update gradle.properties and fabric.mod.json files
    gradle_properties_path, fabric_mod_json_path = find_files(mod_folder)

    if gradle_properties_path:
        update_gradle_properties(gradle_properties_path, version_info)
    else:
        print("gradle.properties not found.")

    if fabric_mod_json_path:
        update_fabric_mod_json(fabric_mod_json_path, version_info)
    else:
        print("fabric.mod.json not found.")

    # Apply API changes if required for the selected version
    apply_api_changes(version_info, mod_folder)

if __name__ == "__main__":
    main()
