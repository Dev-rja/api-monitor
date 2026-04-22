# API Reliability Monitor — SLA Report

> Last updated: **2026-04-22 06:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 64.4% | 3785.2 | 10206.7 | 1000ms | 152/427 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 130.1 | 4088.9 | 1500ms | 2/427 |
| ❌ | `nasa_apod` | 61.12% | 37.24% | 4403.2 | 10549.1 | 2000ms | 268/427 |
| ❌ | `ipapi_check` | 93.68% | 100.0% | 158.6 | 353.0 | 2500ms | 0/427 |
| ⚠️ | `open_meteo_weather` | 98.13% | 96.72% | 750.7 | 14877.1 | 2000ms | 14/427 |
| ⚠️ | `dog_ceo_random` | 99.3% | 90.16% | 862.9 | 10244.1 | 2500ms | 42/427 |
| ✅ | `catfact_random` | 99.3% | 99.3% | 273.5 | 10080.2 | 3000ms | 3/427 |
| ✅ | `useless_fact` | 99.53% | 99.06% | 584.8 | 10229.6 | 2500ms | 4/427 |
| ✅ | `agify_name` | 100.0% | 99.77% | 372.1 | 3237.1 | 2000ms | 1/427 |
| ✅ | `rest_countries` | 100.0% | 99.06% | 257.9 | 7269.1 | 2500ms | 4/427 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 231.3 | 2314.9 | 2000ms | 1/427 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.5 | 252.0 | 1500ms | 0/427 |

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
