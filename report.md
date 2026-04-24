# API Reliability Monitor — SLA Report

> Last updated: **2026-04-24 22:59 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 58.26% | 4385.7 | 10206.7 | 1000ms | 197/472 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 128.5 | 4088.9 | 1500ms | 2/472 |
| ❌ | `nasa_apod` | 61.86% | 36.86% | 4409.0 | 10549.1 | 2000ms | 298/472 |
| ❌ | `ipapi_check` | 92.8% | 100.0% | 158.5 | 353.0 | 2500ms | 0/472 |
| ⚠️ | `open_meteo_weather` | 98.31% | 97.03% | 732.1 | 14877.1 | 2000ms | 14/472 |
| ⚠️ | `rest_countries` | 98.52% | 98.09% | 356.0 | 10221.5 | 2500ms | 9/472 |
| ⚠️ | `dog_ceo_random` | 99.36% | 91.1% | 819.1 | 10244.1 | 2500ms | 42/472 |
| ✅ | `catfact_random` | 99.36% | 99.36% | 265.4 | 10080.2 | 3000ms | 3/472 |
| ✅ | `useless_fact` | 99.58% | 99.15% | 583.6 | 10229.6 | 2500ms | 4/472 |
| ✅ | `agify_name` | 100.0% | 99.79% | 372.7 | 3237.1 | 2000ms | 1/472 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 235.5 | 2314.9 | 2000ms | 1/472 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/472 |

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
