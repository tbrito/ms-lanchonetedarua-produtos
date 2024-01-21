from typing import Type

# apenas para pull request
class ContainerDI:
    dependencies = {}

    @classmethod
    def register(cls, dependency_class, dependency_instance):
        cls.dependencies[dependency_class] = dependency_instance

    @classmethod
    def get(cls, dependency_class):
        return cls.dependencies.get(dependency_class)