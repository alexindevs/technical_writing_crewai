from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import WebsiteSearchTool, JSONSearchTool, FileReadTool, FileWriterTool, ScrapeWebsiteTool
from crewai_tools import SerperDevTool

@CrewBase
class AiWritingWorkflowCrew:
    """AI-powered Technical Writing Workflow Crew"""

    def __init__(self):
        super().__init__()
        # Initialize tools
        self.website_search = WebsiteSearchTool()
        self.json_search = JSONSearchTool()
        self.file_read = FileReadTool()
        self.serper = SerperDevTool()
        self.file_write = FileWriterTool()
        self.scraper = ScrapeWebsiteTool()

    @agent
    def research_agent(self) -> Agent:
        config = self.agents_config['research_agent']
        config['tools'] = [self.website_search, self.serper, self.scraper]
        return Agent(**config)

    @agent
    def outline_writer(self) -> Agent:
        config = self.agents_config['outline_writer']
        config['tools'] = [self.file_read, self.file_write]
        return Agent(**config)

    @agent
    def draft_writer(self) -> Agent:
        config = self.agents_config['draft_writer']
        config['tools'] = [self.file_read, self.file_write]
        return Agent(**config)

    @agent
    def editor_agent(self) -> Agent:
        config = self.agents_config['editor_agent']
        config['tools'] = [self.file_read, self.file_write]
        return Agent(**config)

    @task
    def find_next_undrafted_article(self) -> Task:
        return Task(
            config=self.tasks_config['find_next_undrafted_article'],
            tools=[],
        )

    @task
    def gather_research_data(self) -> Task:
        return Task(
            config=self.tasks_config['gather_research_data'],
            tools=[self.website_search, self.serper, self.scraper],
        )

    @task
    def create_article_outline(self) -> Task:
        return Task(
            config=self.tasks_config['create_article_outline'],
            tools=[self.file_read, self.file_write],
        )

    @task
    def write_first_draft(self) -> Task:
        return Task(
            config=self.tasks_config['write_first_draft'],
            tools=[self.file_read, self.file_write],
        )

    @task
    def edit_draft(self) -> Task:
        return Task(
            config=self.tasks_config['edit_draft'],
            tools=[self.file_read, self.file_write],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AI Writing Workflow Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            planning=True,
        )