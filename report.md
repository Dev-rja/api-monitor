# API Reliability Monitor — SLA Report

> Last updated: **2026-04-24 18:27 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 58.89% | 4324.9 | 10206.7 | 1000ms | 192/467 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 128.4 | 4088.9 | 1500ms | 2/467 |
| ❌ | `nasa_apod` | 61.46% | 36.4% | 4446.1 | 10549.1 | 2000ms | 297/467 |
| ❌ | `ipapi_check` | 93.15% | 100.0% | 158.4 | 353.0 | 2500ms | 0/467 |
| ⚠️ | `open_meteo_weather` | 98.29% | 97.0% | 734.6 | 14877.1 | 2000ms | 14/467 |
| ⚠️ | `rest_countries` | 98.5% | 98.07% | 358.1 | 10221.5 | 2500ms | 9/467 |
| ⚠️ | `dog_ceo_random` | 99.36% | 91.01% | 824.9 | 10244.1 | 2500ms | 42/467 |
| ✅ | `catfact_random` | 99.36% | 99.36% | 266.7 | 10080.2 | 3000ms | 3/467 |
| ✅ | `useless_fact` | 99.57% | 99.14% | 582.6 | 10229.6 | 2500ms | 4/467 |
| ✅ | `agify_name` | 100.0% | 99.79% | 374.3 | 3237.1 | 2000ms | 1/467 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 236.3 | 2314.9 | 2000ms | 1/467 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/467 |

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
