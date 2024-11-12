# Agents.py

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def perform_task(self):
        return f"{self.name} yang berperan sebagai {self.role} sedang mengerjakan tugas."

class Agents:
    def Agent1(self):
        return Agent(name="Agent 1", role="Programmer Handal")

    def Agent2(self):
        return Agent(name="Agent 2", role="Programmer Handal")
