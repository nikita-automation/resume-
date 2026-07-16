# Nikita Rozumniy

**AI Automation Engineer**

Germany · nikita.rozumniy77@gmail.com · GitHub: [github.com/nikita-automation](https://github.com/nikita-automation) · LinkedIn: [linkedin.com/in/nikita-rozumniy](https://www.linkedin.com/in/nikita-rozumniy)

---

## Professional Profile

AI Automation Engineer who builds production automation systems for real businesses — not demos. I design end-to-end pipelines that connect ordering platforms, payment data, documents, and communication channels using n8n, Python, and modern AI APIs, running on self-hosted Linux infrastructure that I administer myself.

Recent work: a document automation system for a food-delivery business that eliminated ~4 hours of daily manual work by turning every incoming order into a print-ready accounting document within seconds — delivered by e-mail and archived to Google Drive, with a legally compliant 3-year retention policy.

---

## Experience

### Freelance AI Automation Engineer — self-employed
*2025 — present · remote (clients in Ukraine / EU)*

**Invoice automation for a food-delivery business (Kyiv)** — [github.com/nikita-automation/choice-invoice-automation](https://github.com/nikita-automation/choice-invoice-automation)

- Automated the creation of ~70 accounting documents ("видаткова накладна") per day, replacing ~4 hours of daily manual Excel work
- Event-driven architecture: ChoiceQR webhook → n8n → ChoiceQR Open API enrichment → Python/ReportLab PDF generator → dual delivery (SMTP e-mail + Google Drive backup)
- PDF output replicates the accountant's legacy Excel template on A5: Cyrillic fonts, one-line item rows with auto-shrink, totals spelled out in Ukrainian words
- Idempotent processing (SQLite dedup guard) makes webhook retries and manual replays safe; 46 real orders processed on launch day
- OAuth2 integrations with three providers (ChoiceQR, Google Drive, Gmail); all secrets in n8n's encrypted credential store
- Data-retention-as-code: cron + scheduled n8n workflow auto-delete documents after 3 years, matching the client's published privacy policy (which I helped update)

**AI content and communication automations (selected client and production projects)**

- **AI Reels Analysis Platform** — pipeline that collects Instagram Reels via Apify, transcribes with Whisper, analyses content with GPT and produces structured content briefs
- **AI Telegram Assistant** — self-hosted assistant (n8n + OpenAI + Telegram Bot API) with conversation memory and routing logic
- **AI WordPress Publishing Pipeline** — RSS feeds → AI-written articles with generated images → automatic WordPress publishing
- **AI Call Analysis System** — audio recordings → Whisper transcription → ChatGPT extraction of structured business insights
- **AI Voice & Avatar Generation** — ElevenLabs / HeyGen pipelines orchestrated through Airtable and Google Drive

---

## Technical Skills

**Automation & Integration:** n8n (self-hosted, incl. management via REST API), Make.com, webhook architectures, REST APIs, OAuth2 flows, JSON mapping, idempotent pipeline design, error handling & retries

**Programming:** Python (automation services, PDF generation with ReportLab, data parsing), JavaScript (n8n code nodes), SQL (SQLite, PostgreSQL fundamentals), Bash

**AI Services:** OpenAI API (GPT, Whisper), prompt engineering, ElevenLabs, HeyGen, DeepSeek

**Infrastructure:** Linux (Ubuntu VPS) administration, Docker, Nginx reverse proxy, PM2, SSH, cron, Git/GitHub, backup & data-retention automation

**Platforms:** Telegram Bot API, WordPress REST API, Google Workspace (Drive, Sheets, Docs, Gmail/SMTP), Airtable, Apify, ChoiceQR Open API

---

## Languages

- Ukrainian — native
- Russian — native
- German — C1
- English — technical working proficiency (documentation, code, written communication)

---

## Professional Goal

Join a team where automation is treated as engineering: reliable integrations, measurable business impact, and AI applied where it actually removes manual work.
