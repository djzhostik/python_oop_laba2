class Store:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        keys = key.split('.')
        current_data = self.data

        for i in range(len(keys) - 1):
            if keys[i] not in current_data:
                current_data[keys[i]] = {}
            current_data = current_data[keys[i]]

        current_data[keys[-1]] = value

    def get(self, key):
        keys = key.split('.')
        current_data = self.data

        for k in keys:
            if k in current_data:
                current_data = current_data[k]
            else:
                return None

        return current_data

    def update(self, key, value):
        self.set(key, value)

    def delete(self, key):
        keys = key.split('.')
        current_data = self.data

        for i in range(len(keys) - 1):
            if keys[i] in current_data:
                current_data = current_data[keys[i]]
            else:
                return

        del current_data[keys[-1]]