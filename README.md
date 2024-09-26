# Minecraft Mod Converter

# Overview
This Python script is designed to assist mod developers in updating their Minecraft mods to newer versions. It automates the process of updating the necessary configuration files and applying API changes based on the selected Minecraft version.

# Features
Updates gradle.properties and fabric.mod.json files with the specified Minecraft version and its associated dependencies.
Applies specific API changes based on the Minecraft version selected, ensuring compatibility with new updates.
Supports multiple versions of Minecraft, allowing users to easily choose their target version.

# Supported Versions
The following Minecraft versions are supported, along with their associated mappings:

1.21

Yarn Mappings: 1.21+build.9
Loader Version: 0.16.5
Fabric Version: 0.102.0+1.21
API Changes: entity_api, rendering_api, item_group_registration

1.20.6

Yarn Mappings: 1.20.6+build.3
Loader Version: 0.16.5
Fabric Version: 0.100.8+1.20.6
API Changes: None

1.20.5

Yarn Mappings: 1.20.5+build.1
Loader Version: 0.16.5
Fabric Version: 0.97.8+1.20.5
API Changes: None
1.20.4

Yarn Mappings: 1.20.4+build.3
Loader Version: 0.16.5
Fabric Version: 0.97.2+1.20.4
API Changes: loot_api, gradle_tooling

1.20.3

Yarn Mappings: 1.20.3+build.1
Loader Version: 0.16.5
Fabric Version: 0.91.1+1.20.3
API Changes: transfer_api, block_codecs

1.20.2

Yarn Mappings: 1.20.2+build.4
Loader Version: 0.16.5
Fabric Version: 0.91.6+1.20.2
API Changes: networking_overhaul, block_wood_registry

1.20.1

Yarn Mappings: 1.20.1+build.10
Loader Version: 0.16.5
Fabric Version: 0.92.2+1.20.1
API Changes: None

# Installation
To use this script, ensure you have Python installed on your machine. You can download Python from the Microsoft Store.

Steps to Run the Script
Clone or download this repository.
Open the folder where the script is located.
You can drag your mod's source folder onto the script after running the run.bat file. (You can rename .bat to .txt to see what .bat is doing)
Follow the on-screen prompts to select the desired Minecraft version.

# Safety and Privacy

Your privacy is important. This script does not log any information about the mods being updated. You can rest assured that your private mod source code will not be leaked or recorded during the update process.

Additionally, for your convenience, I have left #Notes in the code for every new section, explaining what each part does. This should help you understand the functionality of the script better.

# Usage
When prompted, provide the path to the folder containing your mod's source code (or drag and drop the folder onto the script).
Select the version of Minecraft you want to update your mod to from the list provided.
The script will update the gradle.properties and fabric.mod.json files and apply any necessary API changes.

# Important Notes
Ensure you back up your mod files before running the script, as it will overwrite existing configuration files.
The script may require modification for specific use cases or additional versions not covered in the default mappings.
