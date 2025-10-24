---
layout: post
title: "Big News: Amazon apologises to customers impacted by huge AWS outage"
date: 2025-10-23T12:08:51
author: "badely"
categories: [Technology]
tags: []
excerpt: "A 'faulty automation' was at the core of the issues that caused knock-on effects for more than one thousand sites on Monday, an expert told the BBC."
image: assets/images/ce0a97e01398c2a5b76bf0ba6e7e6111.jpg
---

Let's dive into the details: Amazon Web Services (AWS) has apologised to customers impacted by Monday's massive outage, after it knocked some of the world's largest platforms offline.

Snapchat, Reddit and Lloyds Bank were among more than 1,000 sites and services reported to have gone down as a result of issues at the heart of the cloud computing giant's operations in North Virginia, US on 20 October.

In a detailed summary of what caused the outage, Amazon said it occurred as a result of errors which meant its internal systems could not connect websites with the IP addresses computers use to find them.

"We apologise for the impact this event caused our customers," the company said.

"We know how critical our services are to our customers, their applications and end users, and their businesses.

"We know this event impacted many customers in significant ways."

While many platforms such as the online games Roblox and Fortnite were back up and running within a few hours of the outage, some services experienced prolonged downtime.

This included Lloyds Bank, with some customers experiencing issues until mid-afternoon, as well as US payments app Venmo and social media site Reddit.

The outage had a far-reaching impact - even reportedly disrupting the sleep of some smart bed owners.

Eight Sleep, which makes sleep "pods" with temperature and elevation options requiring an internet connection, said it would work to "outage-proof" its mattresses after some overheated and even got stuck in an inclined position.

Many experts said the outage showed how reliant tech is on Amazon's dominance in the cloud computing sector, as a market largely cornered by AWS and Microsoft Azure.

The company said it would also "do everything we can" to learn from the event and improve its availability.

In its lengthy summary of Monday's outage, Amazon said it came down to an issue in US-EAST-1 - its largest cluster of data centres which power much of the internet.

Critical processes in the region's database which stores and manages the Domain Name System (DNS) records, allowing website URLs to be understood by computers, effectively fell out of sync.

According to Amazon, this triggered a "latent race condition" - or in other words unearthed a dormant bug that could occur in an unlikely sequence of events.

The delay in one process, which Amazon said occurred in the early hours of Monday morning, had a knock-on effect which caused its systems to stop working properly.

Much of this process is automated, meaning it is done without human involvement.

Dr Junade Ali, a software engineer and fellow at the Institute for Engineering and Technology, told the BBC "faulty automation" had been at the core of Amazon's problems.

"The specific technical reason is a faulty automation broke the internal 'address book' systems in that region rely upon," he said.

"So they couldn't find one of the other key systems."

Like others, Dr Ali believes it highlights the need for companies to be more resilient and diversify their cloud service providers "so they can fail over to other data centres and providers when one isn't available". 

"In this instance, those who had a single point of failure in this Amazon region were susceptible to being taken offline," he said.

Sign up for our Tech Decoded newsletter to follow the world's top tech stories and trends. Outside the UK? Sign up here.

