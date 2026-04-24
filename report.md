# API Reliability Monitor — SLA Report

> Last updated: **2026-04-24 09:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 59.78% | 4237.2 | 10206.7 | 1000ms | 185/460 |
| ❌ | `public_apis_list` | 0.0% | 99.57% | 128.7 | 4088.9 | 1500ms | 2/460 |
| ❌ | `nasa_apod` | 61.3% | 36.3% | 4455.2 | 10549.1 | 2000ms | 293/460 |
| ❌ | `ipapi_check` | 93.7% | 100.0% | 158.2 | 353.0 | 2500ms | 0/460 |
| ⚠️ | `open_meteo_weather` | 98.26% | 96.96% | 737.0 | 14877.1 | 2000ms | 14/460 |
| ⚠️ | `rest_countries` | 98.48% | 98.04% | 359.7 | 10221.5 | 2500ms | 9/460 |
| ⚠️ | `dog_ceo_random` | 99.35% | 90.87% | 830.9 | 10244.1 | 2500ms | 42/460 |
| ✅ | `catfact_random` | 99.35% | 99.35% | 268.0 | 10080.2 | 3000ms | 3/460 |
| ✅ | `useless_fact` | 99.57% | 99.13% | 582.6 | 10229.6 | 2500ms | 4/460 |
| ✅ | `agify_name` | 100.0% | 99.78% | 374.2 | 3237.1 | 2000ms | 1/460 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 234.7 | 2314.9 | 2000ms | 1/460 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/460 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 17:00 | 6006.5 | 74.07% |
| `nasa_apod` | 18:00 | 5937.8 | 85.0% |
| `nasa_apod` | 03:00 | 5600.9 | 85.71% |
| `numbers_trivia` | 03:00 | 5200.2 | 50.0% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 5177.6 | 62.96% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `numbers_trivia` | 10:00 | 4947.7 | 47.62% |
| `numbers_trivia` | 12:00 | 4944.8 | 47.37% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
