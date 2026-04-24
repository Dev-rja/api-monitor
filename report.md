# API Reliability Monitor — SLA Report

> Last updated: **2026-04-24 16:32 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 59.14% | 4300.2 | 10206.7 | 1000ms | 190/465 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 128.6 | 4088.9 | 1500ms | 2/465 |
| ❌ | `nasa_apod` | 61.29% | 36.34% | 4458.8 | 10549.1 | 2000ms | 296/465 |
| ❌ | `ipapi_check` | 93.12% | 100.0% | 158.1 | 353.0 | 2500ms | 0/465 |
| ⚠️ | `open_meteo_weather` | 98.28% | 96.99% | 735.1 | 14877.1 | 2000ms | 14/465 |
| ⚠️ | `rest_countries` | 98.49% | 98.06% | 358.7 | 10221.5 | 2500ms | 9/465 |
| ⚠️ | `dog_ceo_random` | 99.35% | 90.97% | 826.4 | 10244.1 | 2500ms | 42/465 |
| ✅ | `catfact_random` | 99.35% | 99.35% | 267.1 | 10080.2 | 3000ms | 3/465 |
| ✅ | `useless_fact` | 99.57% | 99.14% | 582.3 | 10229.6 | 2500ms | 4/465 |
| ✅ | `agify_name` | 100.0% | 99.78% | 374.1 | 3237.1 | 2000ms | 1/465 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 236.1 | 2314.9 | 2000ms | 1/465 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/465 |

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
