# API Reliability Monitor — SLA Report

> Last updated: **2026-04-23 05:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.08% | 4012.9 | 10206.7 | 1000ms | 168/443 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 129.1 | 4088.9 | 1500ms | 2/443 |
| ❌ | `nasa_apod` | 61.4% | 37.02% | 4399.0 | 10549.1 | 2000ms | 279/443 |
| ❌ | `ipapi_check` | 93.68% | 100.0% | 158.1 | 353.0 | 2500ms | 0/443 |
| ⚠️ | `open_meteo_weather` | 98.19% | 96.84% | 744.9 | 14877.1 | 2000ms | 14/443 |
| ⚠️ | `rest_countries` | 98.42% | 98.19% | 347.0 | 10221.5 | 2500ms | 8/443 |
| ⚠️ | `dog_ceo_random` | 99.32% | 90.52% | 848.5 | 10244.1 | 2500ms | 42/443 |
| ✅ | `catfact_random` | 99.32% | 99.32% | 270.6 | 10080.2 | 3000ms | 3/443 |
| ✅ | `useless_fact` | 99.55% | 99.1% | 585.5 | 10229.6 | 2500ms | 4/443 |
| ✅ | `agify_name` | 100.0% | 99.77% | 375.2 | 3237.1 | 2000ms | 1/443 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 231.6 | 2314.9 | 2000ms | 1/443 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.4 | 252.0 | 1500ms | 0/443 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 17:00 | 6132.0 | 73.08% |
| `nasa_apod` | 03:00 | 5851.5 | 84.62% |
| `nasa_apod` | 18:00 | 5700.0 | 84.21% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 4979.2 | 61.54% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `numbers_trivia` | 12:00 | 4944.8 | 47.37% |
| `nasa_apod` | 21:00 | 4923.2 | 56.0% |
| `numbers_trivia` | 03:00 | 4828.3 | 46.15% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
