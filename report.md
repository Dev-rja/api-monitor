# API Reliability Monitor — SLA Report

> Last updated: **2026-04-24 03:25 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 60.18% | 4198.7 | 10206.7 | 1000ms | 182/457 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 128.9 | 4088.9 | 1500ms | 2/457 |
| ❌ | `nasa_apod` | 61.71% | 36.54% | 4416.4 | 10549.1 | 2000ms | 290/457 |
| ❌ | `ipapi_check` | 93.65% | 100.0% | 158.2 | 353.0 | 2500ms | 0/457 |
| ⚠️ | `open_meteo_weather` | 98.25% | 96.94% | 738.7 | 14877.1 | 2000ms | 14/457 |
| ⚠️ | `rest_countries` | 98.47% | 98.03% | 361.0 | 10221.5 | 2500ms | 9/457 |
| ⚠️ | `dog_ceo_random` | 99.34% | 90.81% | 833.7 | 10244.1 | 2500ms | 42/457 |
| ✅ | `catfact_random` | 99.34% | 99.34% | 268.2 | 10080.2 | 3000ms | 3/457 |
| ✅ | `useless_fact` | 99.56% | 99.12% | 582.9 | 10229.6 | 2500ms | 4/457 |
| ✅ | `agify_name` | 100.0% | 99.78% | 374.6 | 3237.1 | 2000ms | 1/457 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 232.8 | 2314.9 | 2000ms | 1/457 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/457 |

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
