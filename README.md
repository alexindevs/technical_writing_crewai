# Technical Writing Workflow Crew

Hey there! 👋 I'm Alexin, a backend engineer and aspiring technical writer who got tired of the manual process of researching, outlining, and drafting articles. So, I decided to build my own AI-powered writing workflow using CrewAI to make my life easier.

## What is This?

This is my personal technical writing assistant – a CrewAI-powered workflow that helps me go from article idea to first draft with minimal manual intervention. It's basically my writing buddy that does the heavy lifting of research, outlining, and initial drafting.

## Prerequisites

- Python 3.10-3.13
- UV (for dependency management)
- OpenAI API Key

## Setup and Installation

1. Install UV:

    ```bash
        pip install uv
    ```

2. Install dependencies:

```bash
crewai install
```

## Configuration Files You'll Need to Customize

### 1. OpenAI API Key

Add your `OPENAI_API_KEY` to the `.env` file.

### 2. Writing Sample

Create a `writing_sample.txt` in the project root. This helps the editor agent understand your personal writing style. Include:

- A few of your technical articles
- Blog posts
- Writing examples that showcase your tone and technical depth

### 3. Outline Template

Modify `outline_template.txt` with your preferred article outline structure. I've included a default template, but you might want to customize it to fit your specific writing needs.

### 4. Article Queue

Create `article_queue.json` to define your writing pipeline:

```json
[
    {
        "title": "Your Article Title",
        "subtitle": "Descriptive Subtitle",
        "description": "Longer description of what you want the article to be about",
        "status": "backlog"
    }
]
```

### Customization Paths

- `config/agents.yaml`: Define agent roles and capabilities
- `config/tasks.yaml`: Set up task configurations
- `crew.py`: Add custom logic, tools, and specific arguments
- `main.py`: Add custom inputs for agents and tasks

## Running the Workflow

From the project root:

```bash
crewai run
```

This will:

1. Find the next article in the backlog
2. Research the topic
3. Create an outline
4. Write a first draft
5. Edit the draft to match your style

## My Journey

As a backend engineer diving into technical writing, I wanted a tool that could help me be more consistent and efficient. This CrewAI workflow is my experiment in building a personal writing assistant. It's a work in progress, and I'm learning so much about AI agents and workflow automation!

## Support and Feedback

- Having issues? Open a GitHub issue
- Want to collaborate? Send a PR
- Just want to chat about AI Agents? I'm all ears!

Enjoy the workflow, and happy writing! 🚀✍️
