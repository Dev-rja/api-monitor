# API Reliability Monitor — SLA Report

> Last updated: **2026-04-22 14:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.66% | 3858.1 | 10206.7 | 1000ms | 157/432 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 129.9 | 4088.9 | 1500ms | 2/432 |
| ❌ | `nasa_apod` | 61.11% | 37.27% | 4407.6 | 10549.1 | 2000ms | 271/432 |
| ❌ | `ipapi_check` | 93.75% | 100.0% | 158.3 | 353.0 | 2500ms | 0/432 |
| ⚠️ | `open_meteo_weather` | 98.15% | 96.76% | 749.0 | 14877.1 | 2000ms | 14/432 |
| ⚠️ | `dog_ceo_random` | 99.31% | 90.28% | 858.2 | 10244.1 | 2500ms | 42/432 |
| ✅ | `catfact_random` | 99.31% | 99.31% | 272.6 | 10080.2 | 3000ms | 3/432 |
| ✅ | `useless_fact` | 99.54% | 99.07% | 584.9 | 10229.6 | 2500ms | 4/432 |
| ✅ | `agify_name` | 100.0% | 99.77% | 372.8 | 3237.1 | 2000ms | 1/432 |
| ✅ | `rest_countries` | 100.0% | 99.07% | 257.8 | 7269.1 | 2500ms | 4/432 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 231.0 | 2314.9 | 2000ms | 1/432 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/432 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 03:00 | 6314.9 | 91.67% |
| `nasa_apod` | 17:00 | 5959.2 | 72.0% |
| `nasa_apod` | 18:00 | 5870.5 | 83.33% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 4979.2 | 61.54% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `numbers_trivia` | 12:00 | 4944.8 | 47.37% |
| `nasa_apod` | 19:00 | 4739.6 | 62.5% |
| `nasa_apod` | 21:00 | 4705.1 | 54.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
