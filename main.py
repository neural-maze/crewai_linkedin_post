from crewai import Crew
from dotenv import load_dotenv

from agents import linkedin_scraper_agent, web_researcher_agent, doppelganger_agent
from tasks import scrape_linkedin_task, web_research_task, create_linkedin_post_task

load_dotenv()


crew = Crew(
    agents=[
        linkedin_scraper_agent,
        web_researcher_agent,
        doppelganger_agent
    ],
    tasks=[
        scrape_linkedin_task,
        web_research_task,
        create_linkedin_post_task
    ]
)

result = crew.kickoff()


print("Here is the result: ")
print(result)
