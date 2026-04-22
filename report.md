# API Reliability Monitor — SLA Report

> Last updated: **2026-04-22 11:05 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 63.95% | 3829.0 | 10206.7 | 1000ms | 155/430 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 129.9 | 4088.9 | 1500ms | 2/430 |
| ❌ | `nasa_apod` | 61.16% | 37.44% | 4398.0 | 10549.1 | 2000ms | 269/430 |
| ❌ | `ipapi_check` | 93.72% | 100.0% | 158.4 | 353.0 | 2500ms | 0/430 |
| ⚠️ | `open_meteo_weather` | 98.14% | 96.74% | 749.9 | 14877.1 | 2000ms | 14/430 |
| ⚠️ | `dog_ceo_random` | 99.3% | 90.23% | 860.2 | 10244.1 | 2500ms | 42/430 |
| ✅ | `catfact_random` | 99.3% | 99.3% | 273.3 | 10080.2 | 3000ms | 3/430 |
| ✅ | `useless_fact` | 99.53% | 99.07% | 585.1 | 10229.6 | 2500ms | 4/430 |
| ✅ | `agify_name` | 100.0% | 99.77% | 372.9 | 3237.1 | 2000ms | 1/430 |
| ✅ | `rest_countries` | 100.0% | 99.07% | 257.9 | 7269.1 | 2500ms | 4/430 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 231.1 | 2314.9 | 2000ms | 1/430 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.4 | 252.0 | 1500ms | 0/430 |

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
| `nasa_apod` | 19:00 | 4739.6 | 62.5% |
| `nasa_apod` | 21:00 | 4705.1 | 54.17% |
| `numbers_trivia` | 10:00 | 4692.0 | 45.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
