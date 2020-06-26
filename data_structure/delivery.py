from typing import List, Text


class NoAgentFoundException(Exception):
    def __init__(self, message):
        self.message = message


class Agent(object):
    def __str__(self):
        return "<Agent: {}>".format(self._name)
        
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load


class Ticket(object):
    def __init__(self, id, restrictions):
        self.tId = id
        self.restrictions = restrictions
        

class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        filtered = filter(lambda x: x.load <= 3, agents)
        if not filtered:
            raise NoAgentFoundException('No Agent')
        return filtered

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        return min(self._filter_loaded_agents(agents), key=lambda x: x.load)

class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        return min(self._filter_loaded_agents(agents), key=lambda x: (len(x.skills), x.load))
        
if __name__ == "__main__":
    pass