# API Reliability Monitor — SLA Report

> Last updated: **2026-04-24 14:05 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 59.4% | 4275.1 | 10206.7 | 1000ms | 188/463 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 128.9 | 4088.9 | 1500ms | 2/463 |
| ❌ | `nasa_apod` | 61.12% | 36.07% | 4476.5 | 10549.1 | 2000ms | 296/463 |
| ❌ | `ipapi_check` | 93.3% | 100.0% | 158.0 | 353.0 | 2500ms | 0/463 |
| ⚠️ | `open_meteo_weather` | 98.27% | 96.98% | 735.7 | 14877.1 | 2000ms | 14/463 |
| ⚠️ | `rest_countries` | 98.49% | 98.06% | 359.1 | 10221.5 | 2500ms | 9/463 |
| ⚠️ | `dog_ceo_random` | 99.35% | 90.93% | 828.4 | 10244.1 | 2500ms | 42/463 |
| ✅ | `catfact_random` | 99.35% | 99.35% | 267.4 | 10080.2 | 3000ms | 3/463 |
| ✅ | `useless_fact` | 99.57% | 99.14% | 582.0 | 10229.6 | 2500ms | 4/463 |
| ✅ | `agify_name` | 100.0% | 99.78% | 373.8 | 3237.1 | 2000ms | 1/463 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 235.7 | 2314.9 | 2000ms | 1/463 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/463 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 17:00 | 6006.5 | 74.07% |
| `nasa_apod` | 18:00 | 5937.8 | 85.0% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `nasa_apod` | 11:00 | 5359.7 | 64.29% |
| `numbers_trivia` | 12:00 | 5201.9 | 50.0% |
| `numbers_trivia` | 03:00 | 5200.2 | 50.0% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `numbers_trivia` | 10:00 | 4947.7 | 47.62% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
