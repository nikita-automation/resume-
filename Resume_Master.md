# Mykyta (Nikita) Rozumnyi

**AI Automation Engineer**

North Rhine-Westphalia, Germany · nikita.rozumniy77@gmail.com · +49 160 96290325
GitHub: [github.com/nikita-automation](https://github.com/nikita-automation) · LinkedIn: [linkedin.com/in/nikita-rozumniy](https://www.linkedin.com/in/nikita-rozumniy)

---

## Professional Profile

AI Automation Engineer who builds production automation systems for real businesses — not demos. I design end-to-end pipelines that connect ordering platforms, documents, AI models and communication channels using n8n, Python and modern AI APIs, running on self-hosted Linux infrastructure I administer myself.

Currently in production: a document automation system for a food-delivery business that turns every order into a print-ready accounting document, delivers it, and records it in a daily register — replacing several hours of manual work per day.

---

## Practical Project (in production)

### Invoice & registry automation for a food-delivery business (Kyiv)
[github.com/nikita-automation/choice-invoice-automation](https://github.com/nikita-automation/choice-invoice-automation)

- **~70 accounting documents per day** generated automatically, replacing hours of manual Excel work
- **Event-driven architecture:** ChoiceQR webhook → n8n → ChoiceQR Open API enrichment → Python/ReportLab PDF generator → delivery via e-mail + Google Drive archive
- **Correct accounting:** applies discounts (promo codes) and surcharges (cutlery, packaging, delivery); dates the document by the delivery date; totals match the customer receipt
- **Real-time daily register in Google Sheets:** each order appends a row (no., address, amount) to that day's tab with a running total — replacing manual copying of addresses out of the PDFs
- **Idempotency (SQLite):** webhook retries and manual replays are safe; the register is rebuilt in full from the database on every run
- **Data-retention-as-code:** cron + scheduled n8n workflow delete documents after 3 years, matching the client's updated privacy policy
- OAuth2 integrations with three providers (ChoiceQR, Google Drive, Google Sheets/Gmail); all secrets in n8n's encrypted credential store

---

## Other Portfolio Projects

- **AI Reels Analysis** — collects short-form videos via Apify, transcribes with Whisper, analyses with AI, stores structured results in Airtable
- **AI Telegram Assistant** — self-hosted assistant (OpenAI) with conversation context and routing
- **AI WordPress Publisher** — automated creation and publishing of WordPress posts via the REST API, with a draft workflow
- **AI Call Analysis System** — transcription and AI analysis of calls into summaries, action items and follow-ups
- **AI Voice Generator** — ElevenLabs voice generation from approved scripts, state-managed in Airtable
- **AI Avatar Generator** — HeyGen avatar videos from Airtable with render monitoring and automatic write-back

---

## Technical Skills

**Automation & Integration:** n8n (self-hosted, incl. management via REST API), Make.com, webhook architectures, REST APIs, OAuth2 flows, JSON mapping, idempotent pipeline design, error handling & retries

**Programming:** Python (automation services, PDF generation with ReportLab, data parsing), JavaScript (n8n code nodes), SQL (SQLite, PostgreSQL fundamentals), Bash

**AI Services:** OpenAI API (GPT, Whisper), prompt engineering, ElevenLabs, HeyGen

**Infrastructure:** Linux (Ubuntu VPS) administration, Docker, cron, Git/GitHub, backup & data-retention automation

**Platforms:** Telegram Bot API, WordPress REST API, Google Workspace (Drive, Sheets, Docs, Gmail/SMTP), Airtable, Apify, ChoiceQR Open API

---

## Education

**Bachelor of Management** — completed university degree, Ukraine

---

## Languages

- Ukrainian — native
- Russian — native
- German — C1 (Deutsch Prime certificate, 2026)
- English — A2

---

## Continuing Education

PostgreSQL · Docker · Python · Advanced n8n · AI Agents
