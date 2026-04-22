# API Reliability Monitor — SLA Report

> Last updated: **2026-04-22 08:11 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 64.25% | 3799.9 | 10206.7 | 1000ms | 153/428 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 130.2 | 4088.9 | 1500ms | 2/428 |
| ❌ | `nasa_apod` | 60.98% | 37.15% | 4417.1 | 10549.1 | 2000ms | 269/428 |
| ❌ | `ipapi_check` | 93.69% | 100.0% | 158.6 | 353.0 | 2500ms | 0/428 |
| ⚠️ | `open_meteo_weather` | 98.13% | 96.73% | 750.1 | 14877.1 | 2000ms | 14/428 |
| ⚠️ | `dog_ceo_random` | 99.3% | 90.19% | 862.2 | 10244.1 | 2500ms | 42/428 |
| ✅ | `catfact_random` | 99.3% | 99.3% | 273.9 | 10080.2 | 3000ms | 3/428 |
| ✅ | `useless_fact` | 99.53% | 99.07% | 584.6 | 10229.6 | 2500ms | 4/428 |
| ✅ | `agify_name` | 100.0% | 99.77% | 371.8 | 3237.1 | 2000ms | 1/428 |
| ✅ | `rest_countries` | 100.0% | 99.07% | 257.7 | 7269.1 | 2500ms | 4/428 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 231.1 | 2314.9 | 2000ms | 1/428 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/428 |

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
