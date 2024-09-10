from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class BsDetectorCrew():
	"""BsDetector crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def conjecturer(self) -> Agent:
		return Agent(
			config=self.agents_config['conjecturer'],
			verbose=True,
			allow_delegation=True
		)

	@agent
	def refuter(self) -> Agent:
		return Agent(
			config=self.agents_config['refuter'],
			verbose=True,
			allow_delegation=True,
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
			config=self.tasks_config['conclude_argument'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the BsDetector crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)