# MPSC Daily Update — setup

## काय आहे?
ही स्वतंत्र HTML interface आहे:
- Daily 50 MCQs
- Current Affairs feed
- PYQ search/filter
- Static GK
- Score/progress
- Last Updated

## महत्त्वाची मर्यादा
फक्त local `.html` file स्वतःहून रोज background मध्ये internet वरून update होत नाही.
Auto-update साठी ती GitHub Pages/Netlify सारख्या hosting वर ठेवून scheduled updater चालवावा.

## Recommended architecture
1. `mpsc_daily_update.html` = interface
2. `daily_update.json` = प्रश्न + news data
3. `.github/workflows/daily-update.yml` = रोज updater
4. `update.py` = RSS/API वरून news आणून data update करण्याची जागा

## 2500 Previous-Year Questions
या template मध्ये 2500 चे target आहे. वास्तविक MPSC PYQs बनावटपणे तयार न करता verified question papers/answer keys मधून import करावेत.
मी सध्या demo records ठेवले आहेत. तुम्ही तुमचे PDF/PYQ files दिल्यास त्यावरून bank तयार करता येईल.

## Daily 50 questions कसे auto-generate करायचे?
Verified news sources -> updater -> current affairs summary -> MCQ generation service -> `daily_update.json` -> website.
यासाठी API key/hosting secret लागतो. API शिवाय updater फक्त headlines/news जमा करू शकतो; दर्जेदार 50 MCQs स्वयंचलित बनवण्यासाठी question-generation service आवश्यक आहे.

## Current source examples
- MPSC official site: https://www.mpsc.gov.in/
- PIB: https://www.pib.gov.in/
