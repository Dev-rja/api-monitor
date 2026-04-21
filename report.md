# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 22:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.17% | 3710.3 | 10206.7 | 1000ms | 147/422 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 129.2 | 4088.9 | 1500ms | 2/422 |
| ❌ | `nasa_apod` | 61.14% | 37.44% | 4392.0 | 10549.1 | 2000ms | 264/422 |
| ❌ | `ipapi_check` | 93.6% | 100.0% | 158.6 | 353.0 | 2500ms | 0/422 |
| ⚠️ | `open_meteo_weather` | 98.1% | 96.92% | 745.2 | 14877.1 | 2000ms | 13/422 |
| ⚠️ | `dog_ceo_random` | 99.29% | 90.05% | 869.3 | 10244.1 | 2500ms | 42/422 |
| ✅ | `catfact_random` | 99.29% | 99.29% | 275.6 | 10080.2 | 3000ms | 3/422 |
| ✅ | `useless_fact` | 99.53% | 99.05% | 585.5 | 10229.6 | 2500ms | 4/422 |
| ✅ | `agify_name` | 100.0% | 99.76% | 373.4 | 3237.1 | 2000ms | 1/422 |
| ✅ | `rest_countries` | 100.0% | 99.05% | 259.2 | 7269.1 | 2500ms | 4/422 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 232.3 | 2314.9 | 2000ms | 1/422 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/422 |

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
