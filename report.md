# API Reliability Monitor — SLA Report

> Last updated: **2026-04-22 01:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 64.71% | 3755.5 | 10206.7 | 1000ms | 150/425 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 129.7 | 4088.9 | 1500ms | 2/425 |
| ❌ | `nasa_apod` | 61.18% | 37.18% | 4398.3 | 10549.1 | 2000ms | 267/425 |
| ❌ | `ipapi_check` | 93.65% | 100.0% | 158.7 | 353.0 | 2500ms | 0/425 |
| ⚠️ | `open_meteo_weather` | 98.12% | 96.71% | 752.1 | 14877.1 | 2000ms | 14/425 |
| ⚠️ | `dog_ceo_random` | 99.29% | 90.12% | 866.0 | 10244.1 | 2500ms | 42/425 |
| ✅ | `catfact_random` | 99.29% | 99.29% | 274.4 | 10080.2 | 3000ms | 3/425 |
| ✅ | `useless_fact` | 99.53% | 99.06% | 585.0 | 10229.6 | 2500ms | 4/425 |
| ✅ | `agify_name` | 100.0% | 99.76% | 372.9 | 3237.1 | 2000ms | 1/425 |
| ✅ | `rest_countries` | 100.0% | 99.06% | 258.3 | 7269.1 | 2500ms | 4/425 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 231.6 | 2314.9 | 2000ms | 1/425 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/425 |

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
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `nasa_apod` | 19:00 | 4739.6 | 62.5% |
| `nasa_apod` | 21:00 | 4705.1 | 54.17% |
| `numbers_trivia` | 10:00 | 4692.0 | 45.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
