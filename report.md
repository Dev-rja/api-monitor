# API Reliability Monitor — SLA Report

> Last updated: **2026-04-25 11:23 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 57.17% | 4491.8 | 10206.7 | 1000ms | 206/481 |
| ❌ | `public_apis_list` | 0.0% | 99.58% | 127.7 | 4088.9 | 1500ms | 2/481 |
| ❌ | `nasa_apod` | 62.37% | 37.42% | 4363.6 | 10549.1 | 2000ms | 301/481 |
| ❌ | `ipapi_check` | 92.1% | 100.0% | 158.1 | 353.0 | 2500ms | 0/481 |
| ⚠️ | `open_meteo_weather` | 98.34% | 97.09% | 728.9 | 14877.1 | 2000ms | 14/481 |
| ⚠️ | `rest_countries` | 98.54% | 98.13% | 353.8 | 10221.5 | 2500ms | 9/481 |
| ⚠️ | `dog_ceo_random` | 99.38% | 91.27% | 812.3 | 10244.1 | 2500ms | 42/481 |
| ✅ | `catfact_random` | 99.38% | 99.38% | 263.6 | 10080.2 | 3000ms | 3/481 |
| ✅ | `useless_fact` | 99.58% | 99.17% | 582.8 | 10229.6 | 2500ms | 4/481 |
| ✅ | `agify_name` | 100.0% | 99.79% | 373.2 | 3237.1 | 2000ms | 1/481 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 235.4 | 2314.9 | 2000ms | 1/481 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/481 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 01:00 | 5838.7 | 66.67% |
| `nasa_apod` | 17:00 | 5806.4 | 71.43% |
| `nasa_apod` | 18:00 | 5779.3 | 85.71% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `numbers_trivia` | 07:00 | 5211.4 | 50.0% |
| `numbers_trivia` | 12:00 | 5201.9 | 50.0% |
| `numbers_trivia` | 03:00 | 5200.2 | 50.0% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 5182.1 | 62.07% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
