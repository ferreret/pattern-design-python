import json


class ConfigSingleton:
    _instance = None

    def __new__(cls, filename="config.json"):
        if not cls._instance:
            cls._instance = super(ConfigSingleton, cls).__new__(cls)
            cls._instance.__load(filename)
        return cls._instance

    def __load(self, filename):
        try:
            with open(filename, "r") as file:
                self.config = json.load(file)
        except FileNotFoundError:
            self.config = None
            print(f"Configuration file {filename} not found.")
        except json.JSONDecodeError:
            self.config = None
            print(f"Error decoding JSON from {filename}.")

    def get(self, key, default=None):
        return self.config.get(key, default) if self.config else default


config1 = ConfigSingleton("02-singleton/config.json")

print(config1.get("version"))  # Should print the version from config.json
print(config1.get("name"))  # Should print the name from config.json

