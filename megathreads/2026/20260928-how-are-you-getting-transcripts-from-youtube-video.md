---
title: "How are you getting transcripts from YouTube videos?"
author: u/CeleryVids-4075
date: 2026-09-28
score: 12
comments: 32
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wrium6/how_are_you_getting_transcripts_from_youtube/
flair: "INTEGRATIONS — App connections, webhooks, API workflows"
---

# How are you getting transcripts from YouTube videos?

**Posted by u/CeleryVids-4075 on 2026-09-28 · 12 points (100% upvoted) · 32 comments**

I’ve asked Hermes several times to get transcripts from YouTube videos, but we keep failing.
I know people often say, “Just ask Hermes how to do it,” but I’ve tried that repeatedly, and I’ve had more failures than successes. So now I’m turning to the Reddit community.
How are you guys pulling transcripts from YouTube videos?
In my specific case, I sometimes want to give Hermes a YouTube video and ask something like:
"How can I apply some of the lessons from this video to our own situation?"
That workflow sounds useful, but it keeps failing when Hermes tries to retrieve the transcript, so it has not really worked out for me.
What tools or methods are you using successfully?
Thanks, and sorry if this is a noob question.
EDIT: For anyone experiencing the same problem and searching this thread in the future, the YouTube content skill that ships with Hermes does work for videos that have transcripts. My problem was my IP address due to a VPN causing YouTube to block me and I had to set up an exception so that YouTube traffic just went through a normal IP and then it worked.
I'm currently exploring Faster Whisper (
https://github.com/Mugen0815/faster-whisper
) as a local option for the videos that don't have transcripts. So I'll download the audio and try to do it that way. I'm not sure whether my hardware can handle it, but I'm asking Hermes to investigate that right now.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wrium6/how_are_you_getting_transcripts_from_youtube/)
