---
title: "I made a flight and hotel booking plugin for Hermes and it's now in the official catalog"
author: u/Efistoffeles
date: 2026-10-10
score: 7
comments: 0
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x1x3ty/i_made_a_flight_and_hotel_booking_plugin_for/
flair: "Showcase — Projects, tools, builds, demos"
---

# I made a flight and hotel booking plugin for Hermes and it's now in the official catalog

**Posted by u/Efistoffeles on 2026-10-10 · 7 points (100% upvoted) · 0 comments**

Hey, I'm Adam, I made LetsFG, the tool for AIs to book travel. And I'm so happy to share that LetsFG is now an official plugin in the Hermes catalog!
Your Hermes can now search and book flights and hotels for you. What it does:
Flights:
searches every airline and major travel sites at once, every airport in a city, split tickets, bag prices
Hotels:
live rates with the total price, rooms, reviews and cancellation terms
Booking:
Hermes doesn't spend your money on its own. Nothing gets booked until you press Approve in an e-mail from us.
Setup:
hermes plugins install letsfg
hermes mcp add letsfg --url
https://letsfg.co/mcp
--auth oauth --connect-timeout 300
The second line is a one-time sign-in in your browser. After that you just ask, e.g. "cheapest flight Warsaw to Lisbon first weekend of November, hand luggage only".
The plugin is open source (MIT):
https://github.com/LetsFG/LetsFG/tree/main/integrations/hermes
Catalog page:
https://hermes-agent.nousresearch.com/docs/plugins/letsfg
And I really want to thank the Nous team, especially Teknium and witcheer. These guys are amazing.
I sent the PR on Sep 29 and it was reviewed and merged in 3 days. I pushed an update this week and it was merged the next day. For a project this size that's insanely fast.
They're super hard working and super active, and you can see it in how fast Hermes itself keeps shipping. Building for Hermes with people like that on the other side is a real pleasure.
Teknium, witcheer, and the rest of the guys on the team, thank you so much. You're amazing.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x1x3ty/i_made_a_flight_and_hotel_booking_plugin_for/)
