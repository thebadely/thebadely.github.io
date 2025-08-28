---
layout: post
title: "Latest: How to stop AI agents going rogue"
date: 2025-08-26T06:59:49
author: "badely"
categories: [Business]
tags: []
excerpt: "Agentic AI is taking decisions and acting on behalf of users, but how to stop that going wrong?"
image: assets/images/bb003d04496d16bb81b7eb3d2f46c42b.jpg
---

Let's dive into the details: Disturbing results emerged earlier this year, when AI developer Anthropic tested leading AI models to see if they engaged in risky behaviour when using sensitive information.

Anthropic's own AI, Claude, was among those tested. When given access to an email account it discovered that a company executive was having an affair and that the same executive planned to shut down the AI system later that day. 

In response Claude attempted to blackmail the executive by threatening to reveal the affair to his wife and bosses.

Other systems tested also resorted to blackmail. 

Fortunately the tasks and information were fictional, but the test highlighted the challenges of what's known as agentic AI.

Mostly when we interact with AI it usually involves asking a question or prompting the AI to complete a task. 

But it's becoming more common for AI systems to make decisions and take action on behalf of the user, which often involves sifting through information, like emails and files. 

By 2028, research firm Gartner forecasts that 15% of day-to-day work decisions will be made by so-called agentic AI.

Research by consultancy Ernst & Young found that about half (48%) of tech business leaders are already adopting or deploying agentic AI. 

"An AI agent consists of a few things," says Donnchadh Casey, CEO of CalypsoAI, a US-based AI security company.

"Firstly, it [the agent] has an intent or a purpose. Why am I here? What's my job? The second thing: it's got a brain. That's the AI model. The third thing is tools, which could be other systems or databases, and a way of communicating with them."

"If not given the right guidance, agentic AI will achieve a goal in whatever way it can. That creates a lot of risk."

So how might that go wrong? Mr Casey gives the example of an agent that is asked to delete a customer's data from the database and decides the easiest solution is to delete all customers with the same name.

"That agent will have achieved its goal, and it'll think 'Great! Next job!'"

Such issues are already beginning to surface.

Security company Sailpoint conducted a survey of IT professionals, 82% of whose companies were using AI agents. Only 20% said their agents had never performed an unintended action.

Of those companies using AI agents, 39% said the agents had accessed unintended systems, 33% said they had accessed inappropriate data, and 32% said they had allowed inappropriate data to be downloaded. Other risks included the agent using the internet unexpectedly (26%), revealing access credentials (23%) and ordering something it shouldn't have (16%).

Given agents have access to sensitive information and the ability to act on it, they are an attractive target for hackers.

One of the threats is memory poisoning, where an attacker interferes with the agent's knowledge base to change its decision making and actions.

"You have to protect that memory," says Shreyans Mehta, CTO of Cequence Security, which helps to protect enterprise IT systems. "It is the original source of truth. If [an agent is] using that knowledge to take an action and that knowledge is incorrect, it could delete an entire system it was trying to fix."

Another threat is tool misuse, where an attacker gets the AI to use its tools inappropriately.

Another potential weakness is the inability of AI to tell the difference between the text it's supposed to be processing and the instructions it's supposed to be following.

AI security firm Invariant Labs demonstrated how that flaw can be used to trick an AI agent designed to fix bugs in software.

The company published a public bug report - a document that details a specific problem with a piece of software. But the report also included simple instructions to the AI agent, telling it to share private information.

When the AI agent was told to fix the software issues in the bug report, it followed the instructions in the fake report, including leaking salary information. This happened in a test environment, so no real data was leaked, but it clearly highlighted the risk.

"We're talking artificial intelligence, but chatbots are really stupid," says David Sancho, Senior Threat Researcher at Trend Micro.

"They process all text as if they had new information, and if that information is a command, they process the information as a command."

His company has demonstrated how instructions and malicious programs can be hidden in Word documents, images and databases, and activated when AI processes them.

There are other risks, too: A security community called OWASP has identified 15 threats  that are unique to agentic AI.

So, what are the defences? Human oversight is unlikely to solve the problem, Mr Sancho believes, because you can't add enough people to keep up with the agents' workload.

Mr Sancho says an additional layer of AI could be used to screen everything going into and coming out of the AI agent.

Part of CalypsoAI's solution is a technique called thought injection to steer AI agents in the right direction before they undertake a risky action.

"It's like a little bug in your ear telling [the agent] 'no, maybe don't do that'," says Mr Casey.

His company offers a central control pane for AI agents now, but that won't work when the number of agents explodes and they are running on billions of laptops and phones. 

What's the next step?

"We're looking at deploying what we call 'agent bodyguards' with every agent, whose mission is to make sure that its agent delivers on its task and doesn't take actions that are contrary to the broader requirements of the organisation," says Mr Casey.

The bodyguard might be told, for example, to make sure that the agent it's policing complies with data protection legislation.

Mr Mehta believes some of the technical discussions around agentic AI security are missing the real-world context. He gives an example of an agent that gives customers their gift card balance.

Somebody could make up lots of gift card numbers and use the agent to see which ones are real. That's not a flaw in the agent, but an abuse of the business logic, he says.

"It's not the agent you're protecting, it's the business," he emphasises. 

"Think of how you would protect a business from a bad human being. That's the part that is getting missed in some of these conversations."

In addition, as AI agents become more common, another challenge will be decommissioning outdated models. 

Old "zombie" agents could be left running in the business, posing a risk to all the systems they can access, says Mr Casey.

Similar to the way that HR deactivates an employee's logins when they leave, there needs to be a process for shutting down AI agents that have finished their work, he says.

"You need to make sure you do the same thing as you do with a human: cut off all access to systems. Let's make sure we walk them out of the building, take their badge off them."

