from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from bs_detector.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class BsDetectorCrew():
	"""BsDetector crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def conjecturer(self) -> Agent:
		return Agent(
			config=self.agents_config['conjecturer'],
			verbose=True
		)

	@agent
	def refuter(self) -> Agent:
		return Agent(
			config=self.agents_config['refuter'],
			verbose=True
		)
	
	@agent
	def concluder(self) -> Agent:
		return Agent(
			config=self.agents_config['concluder'],
			verbose=True
		)

	@task
	def assert_claim(self) -> Task:
		return Task(
			config=self.tasks_config['assert_claim'],
		)

	@task
	def refute_claim(self) -> Task:
		return Task(
			config=self.tasks_config['refute_claim'],
		)
	
	@task
	def conclude(self) -> Task:
		return Task(
			config=self.tasks_config['conclude_argument']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the BsDetector crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)