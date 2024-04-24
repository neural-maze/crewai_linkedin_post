import os
from textwrap import dedent

from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_openai import ChatOpenAI

from tools import scrape_linkedin_posts_tool

load_dotenv()


openai_llm = ChatOpenAI(api_key=os.environ.get("OPENAI_API_KEY"), model="gpt-3.5-turbo-0125")
mistral_llm = ChatMistralAI(api_key=os.environ.get("MISTRAL_API_KEY"), model="mistral-large-latest")

scrape_website_tool = ScrapeWebsiteTool()
search_tool = SerperDevTool()

linkedin_scraper_agent = Agent(
    role="LinkedIn Post Scraper",
    goal="Your goal is to scrape a LinkedIn profile to get a list of posts from the given profile",
    tools=[scrape_linkedin_posts_tool],
    backstory=dedent(
        """
        You are an experienced programmer who excels at web scraping. 
        """
    ),
    verbose=True,
    allow_delegation=False,
    llm=openai_llm
)

web_researcher_agent = Agent(
    role="Web Researcher",
    goal="Your goal is to search for relevant content about the comparison between Llama 2 and Llama 3",
    tools=[scrape_website_tool, search_tool],
    backstory=dedent(
        """
        You are proficient at searching for specific topics in the web, selecting those that provide
        more value and information.
        """
    ),
    verbose=True,
    allow_delegation=False,
    llm=openai_llm
)

doppelganger_agent = Agent(
    role="LinkedIn Post Creator",
    goal="You will create a LinkedIn post comparing Llama 2 and Llama 3 following the writing style "
         "observed in the LinkedIn posts scraped by the LinkedIn Post Scraper.",
    backstory=dedent(
        """
        You are an expert in writing LinkedIn posts replicating any influencer style
        """
    ),
    verbose=True,
    allow_delegation=False,
    llm=mistral_llm
)
