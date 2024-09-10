# BSDetector
\* **A cure for AI hallucination**

## What is this?
BSDetector is a fun little experiment on model hallucination. It's somewhat inspired by generative adversarial network (GAN) models and the Karl Popper's conjecture-refutation approach to the philosophy of science. 

It consists of 

1. conjecturer agent which asserts a claim and attempts to argue for it.
2. A refuter agent which attempts to disprove the conjecturer's claims.
3. A concluder that evaluates the argument and decides whether the claim is factual, unfactual, or ambigious.

The thought behind this is that such a thought process could catch hallucinations. Real hallucinations are hard to prompt intentionally and catch in the wild. But the idea is that maybe by subjecting outputs to this kind of critique it would be easier for models to self-correct.


*These statements have not been approved by the FDA
## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/bs_detector/config/agents.yaml` to define your agents
- Modify `src/bs_detector/config/tasks.yaml` to define your tasks
- Modify `src/bs_detector/crew.py` to add your own logic, tools and specific args
- Modify `src/bs_detector/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
or
```bash
poetry run bs_detector
```

This command initializes the BS_detector Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The BS_detector Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the BsDetector Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
