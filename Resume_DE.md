# Lebenslauf — AI Automation Engineer

**Mykyta (Nikita) Rozumnyi**

Nordrhein-Westfalen, Deutschland · nikita.rozumniy77@gmail.com · +49 160 96290325
GitHub: [github.com/nikita-automation](https://github.com/nikita-automation) · LinkedIn: [linkedin.com/in/nikita-rozumniy](https://www.linkedin.com/in/nikita-rozumniy)

---

## Profil

AI Automation Engineer mit Schwerpunkt auf Business Workflow Automation, KI-Integrationen und API-gestützten Automatisierungssystemen. Ich entwickle modulare, produktionsreife Workflows, die manuelle Prozesse reduzieren, verschiedene Systeme zuverlässig verbinden und KI sinnvoll in bestehende Geschäftsabläufe integrieren — betrieben auf selbst administrierter Linux-Infrastruktur.

Aktuell im Produktiveinsatz: ein Dokumenten-Automatisierungssystem für einen Lieferdienst, das rund 70 Buchhaltungsbelege pro Tag automatisch erstellt, zustellt und in einem täglichen Register erfasst — und damit mehrere Stunden manuelle Arbeit pro Tag ersetzt.

---

## Zielpositionen

- AI Automation Engineer
- Automatisierungsentwickler
- Integration Engineer
- Workflow Engineer

---

## Kernkompetenzen

- Workflow-Automatisierung mit n8n (self-hosted, inkl. Verwaltung über REST API) und Make.com
- Event-getriebene Architekturen mit Webhooks, REST APIs und OAuth2
- Python für Automatisierungsservices, Datenparsing und PDF-Generierung (ReportLab)
- Idempotentes Pipeline-Design, Fehlerbehandlung und Zuverlässigkeit
- Airtable und Google Sheets als Automatisierungsdatenbanken
- OpenAI-, Whisper-, ElevenLabs- und HeyGen-Integrationen · Prompt Engineering
- WordPress REST API · Telegram Bot API
- Linux-Server-Administration, Docker, Cron, Git & GitHub
- Testing, Debugging und technische Dokumentation

---

## Technologien

n8n · Make.com · Python · ReportLab · SQLite · REST APIs · Webhooks · OAuth2 · JSON · OpenAI API · Whisper · ElevenLabs · HeyGen API · Airtable · Google Workspace (Drive, Sheets, Docs, Gmail/SMTP) · Google Sheets API · WordPress REST API · Telegram Bot API · Apify · Docker · Linux (VPS) · Cron · Git · GitHub · Markdown

---

## Praxisprojekt (Produktivbetrieb)

### Rechnungs- und Register-Automatisierung für einen Lieferdienst (Kyjiw)
[github.com/nikita-automation/choice-invoice-automation](https://github.com/nikita-automation/choice-invoice-automation)

Vollständig automatisiertes System, das jede angenommene Bestellung in einen druckfertigen Buchhaltungsbeleg („видаткова накладна") verwandelt — im Produktiveinsatz bei einem realen Lieferdienst.

- **~70 Belege pro Tag** automatisch erstellt; ersetzt mehrere Stunden manuelle Excel-Arbeit täglich
- **Event-getriebene Architektur:** ChoiceQR-Webhook → n8n → Anreicherung über ChoiceQR Open API → Python/ReportLab-PDF-Generator → Zustellung per E-Mail + Google-Drive-Archiv
- **Korrekte Buchhaltung:** berücksichtigt Rabatte (Promo-Codes), Zuschläge (Besteck, Verpackung, Lieferung) und datiert den Beleg nach dem Liefertermin; Summen stimmen mit dem Kundenbeleg überein
- **Tägliches Register in Google Sheets:** jede Bestellung erzeugt automatisch eine Zeile (Nr., Adresse, Summe) auf dem Tagesblatt — in Echtzeit, mit Tagessumme; ersetzt manuelles Kopieren von Adressen aus den PDFs
- **Idempotenz (SQLite):** Webhook-Wiederholungen und manuelle Läufe sind sicher; das Register wird bei jedem Lauf vollständig aus der Datenbank neu aufgebaut
- **Data-Retention-as-Code:** Cron + geplanter n8n-Workflow löschen Belege nach 3 Jahren — konform mit der aktualisierten Datenschutzerklärung des Kunden
- OAuth2-Integrationen mit drei Anbietern (ChoiceQR, Google Drive, Google Sheets/Gmail); alle Secrets im verschlüsselten Credential-Store von n8n

---

## Weitere Portfolio-Projekte

- **AI Reels Analysis** — automatisierte Analyse von Short-Form-Videos: Sammlung via Apify, Whisper-Transkription, KI-Auswertung, strukturierte Speicherung in Airtable
- **AI Telegram Assistant** — KI-gestützter Telegram-Assistent (OpenAI) mit Gesprächskontext und Routing für wiederkehrende Kommunikation
- **AI WordPress Publisher** — automatisierte Erstellung und Veröffentlichung von WordPress-Beiträgen über die REST API inkl. Entwurfs-Workflow
- **AI Call Analysis System** — Transkription und KI-Analyse von Gesprächen mit strukturierten Zusammenfassungen, Aufgabenlisten und Follow-ups
- **AI Voice Generator** — Sprachaufnahmen mit ElevenLabs aus freigegebenen Skripten, mit Statusverwaltung in Airtable
- **AI Avatar Generator** — HeyGen-Avatarvideos aus Airtable mit Render-Überwachung und automatischer Rückspeicherung

---

## Ausbildung

**Bachelor of Management** — abgeschlossenes Hochschulstudium, Ukraine

---

## Sprachen

- Deutsch — C1 (Deutsch Prime Zertifikat, 2026)
- Englisch — A2
- Ukrainisch — Muttersprache
- Russisch — Muttersprache

---

## Weiterbildung

PostgreSQL · Docker · Python · Advanced n8n · AI Agents

---

## Zertifikate

**Deutsch Prime — Deutsch als Zweitsprache: Fortgeschritten (C1)**
Abschlusszeugnis, März 2026 · 95 % Abschlussergebnis · 70 akademische Stunden
