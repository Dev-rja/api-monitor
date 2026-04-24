# API Reliability Monitor — SLA Report

> Last updated: **2026-04-24 19:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 58.76% | 4337.1 | 10206.7 | 1000ms | 193/468 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 128.2 | 4088.9 | 1500ms | 2/468 |
| ❌ | `nasa_apod` | 61.54% | 36.32% | 4442.3 | 10549.1 | 2000ms | 298/468 |
| ❌ | `ipapi_check` | 93.16% | 100.0% | 158.4 | 353.0 | 2500ms | 0/468 |
| ⚠️ | `open_meteo_weather` | 98.29% | 97.01% | 734.1 | 14877.1 | 2000ms | 14/468 |
| ⚠️ | `rest_countries` | 98.5% | 98.08% | 357.6 | 10221.5 | 2500ms | 9/468 |
| ⚠️ | `dog_ceo_random` | 99.36% | 91.03% | 823.5 | 10244.1 | 2500ms | 42/468 |
| ✅ | `catfact_random` | 99.36% | 99.36% | 266.3 | 10080.2 | 3000ms | 3/468 |
| ✅ | `useless_fact` | 99.57% | 99.15% | 582.8 | 10229.6 | 2500ms | 4/468 |
| ✅ | `agify_name` | 100.0% | 99.79% | 374.0 | 3237.1 | 2000ms | 1/468 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 236.0 | 2314.9 | 2000ms | 1/468 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/468 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 17:00 | 5806.4 | 71.43% |
| `nasa_apod` | 18:00 | 5779.3 | 85.71% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `nasa_apod` | 11:00 | 5359.7 | 64.29% |
| `numbers_trivia` | 12:00 | 5201.9 | 50.0% |
| `numbers_trivia` | 03:00 | 5200.2 | 50.0% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `numbers_trivia` | 18:00 | 4987.3 | 47.62% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
