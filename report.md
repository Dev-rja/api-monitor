# API Reliability Monitor — SLA Report

> Last updated: **2026-04-24 05:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 60.04% | 4211.6 | 10206.7 | 1000ms | 183/458 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 128.7 | 4088.9 | 1500ms | 2/458 |
| ❌ | `nasa_apod` | 61.57% | 36.46% | 4429.5 | 10549.1 | 2000ms | 291/458 |
| ❌ | `ipapi_check` | 93.67% | 100.0% | 158.2 | 353.0 | 2500ms | 0/458 |
| ⚠️ | `open_meteo_weather` | 98.25% | 96.94% | 737.9 | 14877.1 | 2000ms | 14/458 |
| ⚠️ | `rest_countries` | 98.47% | 98.03% | 360.4 | 10221.5 | 2500ms | 9/458 |
| ⚠️ | `dog_ceo_random` | 99.34% | 90.83% | 832.3 | 10244.1 | 2500ms | 42/458 |
| ✅ | `catfact_random` | 99.34% | 99.34% | 267.8 | 10080.2 | 3000ms | 3/458 |
| ✅ | `useless_fact` | 99.56% | 99.13% | 583.0 | 10229.6 | 2500ms | 4/458 |
| ✅ | `agify_name` | 100.0% | 99.78% | 374.4 | 3237.1 | 2000ms | 1/458 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 234.8 | 2314.9 | 2000ms | 1/458 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.9 | 252.0 | 1500ms | 0/458 |

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
