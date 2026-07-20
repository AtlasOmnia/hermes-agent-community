---
title: "My Hermes setup (w/ Notion knowledge base), crons, and use cases"
author: u/NeurosisByAnalysis
date: 2026-07-17
score: 176
comments: 30
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1uz77ew/my_hermes_setup_w_notion_knowledge_base_crons_and/
flair: "USE CASE - Real-world tasks, business uses, personal workflows"
---

# My Hermes setup (w/ Notion knowledge base), crons, and use cases

**Posted by u/NeurosisByAnalysis on 2026-07-17 · 176 points (98% upvoted) · 30 comments**

I've gotten more out of this subreddit than any other subreddit ever, so wanted to contribute. Few threshold points:

1. I have zero affiliation/connection to anything named here.
2. I don't name, identify, or promote my projects (likely all inapplicable to users here anyway)
3. This post is 100% hand-typed by me, with zero AI or other party input/revision/edits/suggestions.

**Quick relevant background**

I am US-based, an attorney (16 years), and my wife and I own a local brick-and-mortar business (a few locations in our city).  Our business is in a low-profit, high-regulation industry.  My legal work was in general civil litigation, but in the last few years, my experience as an attorney and business owner in this industry has pushed me into a growing side project basically providing part-time general counsel to other businesses in this industry. 

I am non-technical (can't code), but comfortable learning and trying, with guidance. When we opened our business 14 years ago, I learned enough to never have to hire an agency to do web stuff for us (e.g., Wordpress; domain, email marketing health, DNS stuff; SEO; some basic automations/integrations with things like web forms, Google Sheets, and software tools like Slack). 

As to AI, I've spent the last couple years using discreet AI tools. A main one actually became Remio (again, zero affiliation), which I got via AppSumo lifetime deal, and which I basically used as a super-powered local file search. I gave Remio access to my local folder where I keep all my "general counsel" documents (separate sub-folders for each client), and could say things like, "I know I wrote an administrative appeal for a client about \_\_\_, can you find it for me?" and Remio did a good job of always finding what I needed, legitimately saving me time.  I tried setting up some automations with Zapier over the years but could never get them to work perfectly and consistently. I also downloaded and tried OpenClaw, but just didn't get it and gave up quickly.

A few months ago, Reddit started suggesting posts from this subreddit, and as I read along, I got more interested.

**My setup**  
I initially downloaded Hermes to my laptop (M4 Macbook Pro), but the same day, I got a Raspberry Pi 5 and SSD for the Pi and asked Hermes to help me move itself to the Pi, which it did perfectly.  So my current hardware/model setup is:

* Hermes on Raspberry Pi 5, with 1TB SSD
* OpenAI/Codex subscription (model in use basically 99% of the time)
* DeepSeek API (barely used)
* A few local LLM models on the Pi (basically never used)
* Telegram gateway (free Telegram plan), with one folder for 8 different chat groups (each group having only myself and Hermes (via the Telegram bot))
* Notion as several things, including knowledge database, report/checklist repository, Kanban tracker
* Hermes has its own Gmail account.

**First automations**

The reason I got interested in Hermes was I felt it could finally automate a few repetitive tasks.  For example, in connection with our business, every month I get emails with the same form (exact same 1-page PDF, but with different info filled in).  I open the PDF in PDF Expert, affix my digital signature, flatten and send back.  I thought Hermes could use each app on my computer to do this for me. 

Once I got Hermes set up, I explained what I wanted done.  It told me it didn't have to use my desktop apps (like PDF Expert), but if I gave it a transparent version of my signature, it could do the job (check when the email arrived, sign the PDF, and send it back).  And it worked.

So I added a few more seemingly complex automations related to recording customer payments and reconciling those between our invoice platform (Zoho Billing) and the Google Sheet we use to track things by month.  Those also worked.

**Expanding its agentic portfolio**

I have been working on a SaaS project in our industry (think "OpenTable or Vagaro for Industry X"), and it is getting traction.  Wholly unrelated to Hermes, I was in the stage of gathering leads and starting outbound marketing.  One very effective but very manual growth hack I discovered was if a company's website had a button that looked like a booking button, but actually led to a contact form or page with contact info (e.g., "Call or email us to book"), I would set up my tool for them, and email them to say, "If you have your booking button point here, interested people can actually book their visit online, which will get you more visits and save you time.  We also have automated reminders set up, so you'll also get fewer no-shows.  If you want this, just give me an email address and I'll make you the admin."). 

Hermes was basically able to find and inspect thousands of website, obtain contact information, and give me a Google Sheet with a list of "hot leads" that met that exact criteria (website has booking button that only led to contact page, not a booking page). 

**Extraordinary idea and execution from Hermes, leading to completely new business**

As I mentioned, one side project I have developed has been becoming the go-to attorney in my business's industry (which is highly-regulated, but also very local (almost all small businesses, few large players), very low-margin/low-profit, so anything short of actually getting sued, most businesses never hire an attorney for anything).  Because I know the industry so well, and this is just a side project, I still bill at an attorney rate, but I can answer folks' questions and give them instructions in like 6, 12, or 18 minutes, so these businesses can get competent legal advice for a few hundred dollars, not thousands.  Still, this is just me using my time and getting paid by the hour (or fraction of an hour).   
  
I am condensing a lot of chats here, but a couple weeks ago, Hermes basically developed a new software/business for me by essentially saying, "A lot of your clients ask the same questions and you give the same answers.  How about we build a knowledge database in Notion and set up an AI chatbot, so when clients ask a question, the chatbot can do a first pass response, based on your knowledge database.  You can manually review the responses.  The chatbot can elevate questions it is not confident it can answer.  I (Hermes) can go through the last four years of your emails, search for threads where you get asked a question and you provided advice, and then convert that into an anonymized Q&A to add to the knowledge database.  We can set it up so the AI chatbot is web-based and SMS-based.  Clients will subscribe to your service to get access to the web portal where they can chat and add a phone number that is approved to chat with the bot by SMS.  This will allow you to take on more clients (now subscribers), and also free up your time."

Hermes has been building the entire thing for me, with very little input from me (mostly just asking me to approve commands in Telegram).  It's even helped me re-brand and build this out, so that over this weekend, I should go from having one website for my general counsel/consulting service to:

* Re-branded landing page for essentially everything I offer (continued personal consulting/representation, free resources (e.g., ebook guides I've been offering)
* Subscription-gated hub/dashboard for subscribers, where they get access to paid resources (templates I've been offering, plus a searchable version of the Q&A database), plus the web-based chatbot, and a profile page where they can add their phone number, to chat with my AI "associate" via text message.
* The backend for the AI chatbot, including all the SMS stuff (approved brand and campaign, webhooks, etc.)
* Backend for the subscription stuff (Stripe, magic login links)

**A word on Notion**

A lot of folks here talk about Obsidian.  I've tried Obsidian but was using Notion before I installed Hermes, so that's where I had Hermes set some things up:

* **Its own project tracker**
   * A Kanban board with columns for: Ideas for future; Tasks in progress; Ongoing/recurring tasks/crons (active); Ongoing/recurring tasks/crons (error); Done; Canceled
   * I tasked Hermes with keeping this updated twice daily (e.g., if we add a new cron, add it to the active cron column; if a random idea comes up that we don't have time for, add it to the future ideas column; etc.)
* **Checklists for me**
   * When we're working on something, and there are a lot of steps I need to do (e.g., get an API key from Porkbun so Hermes can make edits; decide on the name of a subdomain; etc.), I ask Hermes to create a subpage in our Hermes Notion page with a checklist of everything it needs me to do.  
   * It can check the list and execute when things get checked off, and send me reminders, but so far we've been working mostly in real-time, so I just do the checklist in the moment.
* **Knowledge database for my consulting work/new SaaS**
   * The consulting Q&A is set up as a database with a column for the question, a column for the answer, and a column where I can tag with categories.  
   * Hermes backfilled this database from my past email threads.
   * Hermes keeps it updated by checking my sent folder each night for any threads that day where a client asked a substantive question and I answered it. 
      * Hermes leaves the category column blank.  Once I review and revise the Q&A, I give it a tag.  Hermes has a separate cron where it checks this private database for any Q&A with a tag, and if there is one, Hermes sweeps that Q&A into the public-facing Q&A database, which will be subscriber-searchable and which the AI chatbot will pull from. 
* **Websites**
   * Because the subscriber-searchable database is in Notion, it seemed like a good idea to just build the subscriber dashboard in Notion and publish to a custom domain with something like Notion Sites, Sotion, or Super.  Hermes said it could do that for me (get the sites online as websites at a custom domain), without the subscription fee, via Cloudflare tunnel (which I gave Hermes access to). 

I'm not trying to trigger any "Notion vs. Obsidian" debate.  I'm just saying this is how I've got things set up.

**A word on Telegram**

Telegram was the first gateway I set up (huge thanks to some step-by-steps in this subreddit).  I tried a couple other apps/gateways discussed in this group, but I returned to Telegram just because it's easy and straightforward.  Putting all of my Hermes chats into one folder has basically eliminated the problem of having to cull spam Telegram chats, which I can now just ignore. 

**Memory, Soul, tokens, Hermes health monitoring**

My Hermes is basically still close to how it was out of the box.  Only one profile, no sub-agents (I keep asking Hermes if more profiles make sense or it needs sub-agents, but it tells me no).  I haven't touched any of the .md files.  It's been close to two months and in my opinion, my Hermes has only been getting better.

Once I got some message basically saying it got limited and I should check back.  (This was when I had it working a lot to backfill the Q&A and gather leads for the booking SaaS.)  In Codex, I was able to do a "reset" (it said I had four available), and that fixed it. 

Another time there were some weird messages about character limit.  I asked Hermes about it, and it explained the issue (something about a memory file), gave me a list of items it would do to fix the problem, and asked my permission to do them.  I gave it permission, and the issue was fixed.

I created a dedicated Telegram chat called "Hermes Doctor," and there, said I wanted this chat to be for Hermes to set up "ongoing health/fitness checks."  I said, "My goal is to have you monitor yourself from here, so we can identifies problems or bloat early. I'm thinking things like: 'I see the memory is getting close to the character limit' or 'I noticed that token burn has unexpectedly jumped, and when I looked into it, I saw that we were unnecessarily including \_\_ with every requests'.  What are some other checks, crons, reports, or alerts we can set up here?"

Hermes gave me 15 categories of checks, each with several specific tasks.  For example:

* Memory/profile budget (Daily) - Memory or user profile >90-95%, or stale/duplicative entries detected
* Prompt/token budget regression (Daily/weekly) - hermes prompt-size --platform telegram jumps unexpectedly; tool schemas/skills/memory grow
* Raspberry Pi system health (Hourly/daily) - High temp/throttling, high load, swap pressure, low memory, SSD not mounted
* Credential/OAth health (Daily) - Gmail/Google/Notion/Zoho tokens missing/expired; auth files unreadable

It also suggesting a reporting structure:

* Alerts that are quiet and only fire on actionable thresholds
* Daily digest (short table)
* Weekly audit with deeper recommendations

Then it listed which ones it recommended implementing immediately.  It also said it would set up most as "script-only no\_agent jobs so monitoring itself stays cheap."  

**Final word of appreciation**

I've been wanting to expand my use and understanding of AI for a few years now.  Hermes and this group has helped me fully accomplish that goal.  

But what I did not expect was actually how much my *imagination* of what *I* can do with AI has expanded exponentially.  I know from just reading the news and staying informed that AI has been doing insane things (protein folding, intelligence and targeting work in wars, app development, etc.).  But for me, given the work *I* do and the capabilities and time *I* have, my mindset a few months ago was, "I really need to figure out how I can automate social media and content marketing with AI," or "Maybe AI can help me automate this invoice tracking," or "Maybe I can find a lifetime deal for an AI that just keeps our Wordpress site up to date and healthy."

Now, though, it genuinely feels like I reached a crest and can see for myself, this extraordinary landscape laid out before me, which I've read about and been told about,  but honestly could not visualize until seeing it for myself.

That's it.  No promotion, no asks, just information on how I'm using Hermes, and a big "Thank You!" to this group and to Nous Research!

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1uz77ew/my_hermes_setup_w_notion_knowledge_base_crons_and/)

