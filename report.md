# API Reliability Monitor — SLA Report

> Last updated: **2026-04-08 03:30 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **81.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 307.4 | 588.9 | 1000ms | 0/145 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 114.2 | 234.1 | 1500ms | 0/145 |
| ❌ | `nasa_apod` | 91.72% | 70.34% | 1697.2 | 10538.0 | 2000ms | 43/145 |
| ❌ | `ipapi_check` | 93.1% | 100.0% | 156.2 | 252.2 | 2500ms | 0/145 |
| ❌ | `open_meteo_weather` | 94.48% | 95.17% | 1004.9 | 14877.1 | 2000ms | 7/145 |
| ❌ | `dog_ceo_random` | 98.62% | 72.41% | 1730.1 | 5586.8 | 2500ms | 40/145 |
| ⚠️ | `useless_fact` | 98.62% | 99.31% | 625.2 | 10229.6 | 2500ms | 1/145 |
| ⚠️ | `catfact_random` | 98.62% | 99.31% | 304.5 | 10070.5 | 3000ms | 1/145 |
| ✅ | `agify_name` | 100.0% | 99.31% | 407.3 | 3237.1 | 2000ms | 1/145 |
| ✅ | `rest_countries` | 100.0% | 98.62% | 301.4 | 7269.1 | 2500ms | 2/145 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.31% | 251.3 | 2314.9 | 2000ms | 1/145 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 102.2 | 252.0 | 1500ms | 0/145 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `open_meteo_weather` | 05:00 | 4216.1 | 25.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 11:00 | 3203.4 | 50.0% |
| `open_meteo_weather` | 06:00 | 3112.1 | 20.0% |
| `dog_ceo_random` | 12:00 | 3057.6 | 50.0% |
| `nasa_apod` | 20:00 | 2829.3 | 40.0% |
| `nasa_apod` | 22:00 | 2715.0 | 30.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
