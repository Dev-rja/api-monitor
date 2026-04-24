# API Reliability Monitor — SLA Report

> Last updated: **2026-04-24 08:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 59.91% | 4224.4 | 10206.7 | 1000ms | 184/459 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 128.5 | 4088.9 | 1500ms | 2/459 |
| ❌ | `nasa_apod` | 61.44% | 36.38% | 4442.2 | 10549.1 | 2000ms | 292/459 |
| ❌ | `ipapi_check` | 93.68% | 100.0% | 158.2 | 353.0 | 2500ms | 0/459 |
| ⚠️ | `open_meteo_weather` | 98.26% | 96.95% | 737.7 | 14877.1 | 2000ms | 14/459 |
| ⚠️ | `rest_countries` | 98.47% | 98.04% | 360.2 | 10221.5 | 2500ms | 9/459 |
| ⚠️ | `dog_ceo_random` | 99.35% | 90.85% | 831.5 | 10244.1 | 2500ms | 42/459 |
| ✅ | `catfact_random` | 99.35% | 99.35% | 268.4 | 10080.2 | 3000ms | 3/459 |
| ✅ | `useless_fact` | 99.56% | 99.13% | 583.0 | 10229.6 | 2500ms | 4/459 |
| ✅ | `agify_name` | 100.0% | 99.78% | 374.6 | 3237.1 | 2000ms | 1/459 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 234.8 | 2314.9 | 2000ms | 1/459 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/459 |

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
