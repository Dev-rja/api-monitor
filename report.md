# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 23:00 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.01% | 3725.5 | 10206.7 | 1000ms | 148/423 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 129.4 | 4088.9 | 1500ms | 2/423 |
| ❌ | `nasa_apod` | 61.23% | 37.35% | 4388.0 | 10549.1 | 2000ms | 265/423 |
| ❌ | `ipapi_check` | 93.62% | 100.0% | 158.6 | 353.0 | 2500ms | 0/423 |
| ⚠️ | `open_meteo_weather` | 98.11% | 96.69% | 753.5 | 14877.1 | 2000ms | 14/423 |
| ⚠️ | `dog_ceo_random` | 99.29% | 90.07% | 868.4 | 10244.1 | 2500ms | 42/423 |
| ✅ | `catfact_random` | 99.29% | 99.29% | 275.2 | 10080.2 | 3000ms | 3/423 |
| ✅ | `useless_fact` | 99.53% | 99.05% | 585.1 | 10229.6 | 2500ms | 4/423 |
| ✅ | `agify_name` | 100.0% | 99.76% | 372.9 | 3237.1 | 2000ms | 1/423 |
| ✅ | `rest_countries` | 100.0% | 99.05% | 258.8 | 7269.1 | 2500ms | 4/423 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 232.0 | 2314.9 | 2000ms | 1/423 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/423 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 03:00 | 6314.9 | 91.67% |
| `nasa_apod` | 17:00 | 5959.2 | 72.0% |
| `nasa_apod` | 18:00 | 5870.5 | 83.33% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 5164.2 | 64.0% |
| `nasa_apod` | 19:00 | 4739.6 | 62.5% |
| `nasa_apod` | 21:00 | 4705.1 | 54.17% |
| `numbers_trivia` | 10:00 | 4692.0 | 45.0% |
| `numbers_trivia` | 12:00 | 4658.8 | 44.44% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
