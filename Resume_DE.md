# Nikita Rozumniy

**AI Automation Engineer**

Deutschland · nikita.rozumniy77@gmail.com · GitHub: [github.com/nikita-automation](https://github.com/nikita-automation) · LinkedIn: [TODO]

---

## Profil

AI Automation Engineer mit Fokus auf produktive Automatisierungssysteme für reale Unternehmen — keine Demos. Ich entwerfe End-to-End-Pipelines, die Bestellplattformen, Dokumente und Kommunikationskanäle mit n8n, Python und modernen KI-APIs verbinden — auf selbst administrierter Linux-Infrastruktur.

Aktuelles Projekt: ein Dokumenten-Automatisierungssystem für einen Lieferdienst, das ca. 4 Stunden tägliche manuelle Arbeit eliminiert — jede eingehende Bestellung wird innerhalb von Sekunden zu einem druckfertigen Buchhaltungsdokument, per E-Mail zugestellt und in Google Drive archiviert, mit gesetzeskonformer 3-Jahres-Aufbewahrungsrichtlinie.

---

## Berufserfahrung

### Freelance AI Automation Engineer — selbstständig
*2025 — heute · remote (Kunden in der Ukraine / EU)*

**Rechnungsautomatisierung für einen Lieferdienst (Kyjiw)** — [github.com/nikita-automation/choice-invoice-automation](https://github.com/nikita-automation/choice-invoice-automation)

- Automatisierte Erstellung von ca. 70 Buchhaltungsdokumenten pro Tag; ersetzt ca. 4 Stunden tägliche manuelle Excel-Arbeit
- Event-getriebene Architektur: ChoiceQR-Webhook → n8n → Anreicherung über ChoiceQR Open API → Python/ReportLab-PDF-Generator → doppelte Zustellung (SMTP-E-Mail + Google-Drive-Backup)
- PDF-Ausgabe repliziert die Excel-Vorlage der Buchhaltung im A5-Format: kyrillische Schriften, einzeilige Positionszeilen mit Auto-Verkleinerung, Beträge in Worten (Ukrainisch)
- Idempotente Verarbeitung (SQLite-Dedup-Guard): Webhook-Retries und manuelle Wiederholungen sind sicher; 46 echte Bestellungen am ersten Produktivtag
- OAuth2-Integrationen mit drei Anbietern (ChoiceQR, Google Drive, Gmail); alle Secrets im verschlüsselten Credential-Store von n8n
- Data-Retention-as-Code: Cron + geplanter n8n-Workflow löschen Dokumente automatisch nach 3 Jahren — konform mit der Datenschutzerklärung des Kunden (an deren Aktualisierung ich mitgewirkt habe)

**KI-Content- und Kommunikations-Automatisierungen (ausgewählte Projekte)**

- **AI Reels Analysis Platform** — Pipeline: Instagram-Reels-Sammlung via Apify, Whisper-Transkription, GPT-Analyse, strukturierte Content-Briefings
- **AI Telegram Assistant** — self-hosted Assistent (n8n + OpenAI + Telegram Bot API) mit Konversationsgedächtnis und Routing-Logik
- **AI WordPress Publishing Pipeline** — RSS-Feeds → KI-generierte Artikel mit Bildern → automatische WordPress-Veröffentlichung
- **AI Call Analysis System** — Audioaufnahmen → Whisper-Transkription → strukturierte Business-Insights mit ChatGPT
- **AI Voice & Avatar Generation** — ElevenLabs-/HeyGen-Pipelines, orchestriert über Airtable und Google Drive

---

## Technische Kenntnisse

**Automatisierung & Integration:** n8n (self-hosted, inkl. Verwaltung über REST API), Make.com, Webhook-Architekturen, REST APIs, OAuth2-Flows, JSON-Mapping, idempotentes Pipeline-Design, Fehlerbehandlung & Retries

**Programmierung:** Python (Automatisierungsservices, PDF-Generierung mit ReportLab, Datenparsing), JavaScript (n8n Code Nodes), SQL (SQLite, PostgreSQL-Grundlagen), Bash

**KI-Dienste:** OpenAI API (GPT, Whisper), Prompt Engineering, ElevenLabs, HeyGen, DeepSeek

**Infrastruktur:** Linux (Ubuntu VPS) Administration, Docker, Nginx Reverse Proxy, PM2, SSH, Cron, Git/GitHub, Backup- & Aufbewahrungs-Automatisierung

**Plattformen:** Telegram Bot API, WordPress REST API, Google Workspace (Drive, Sheets, Docs, Gmail/SMTP), Airtable, Apify, ChoiceQR Open API

---

## Sprachen

- Ukrainisch — Muttersprache
- Russisch — Muttersprache
- Deutsch — gute Kenntnisse (B2)
- Englisch — technische Arbeitskenntnisse (Dokumentation, Code, schriftliche Kommunikation)

---

## Berufliches Ziel

Teil eines Teams werden, das Automatisierung als Engineering versteht: zuverlässige Integrationen, messbarer Business-Impact und KI dort, wo sie tatsächlich manuelle Arbeit eliminiert.
