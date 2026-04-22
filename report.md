# API Reliability Monitor — SLA Report

> Last updated: **2026-04-22 21:08 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.79% | 3943.4 | 10206.7 | 1000ms | 163/438 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 129.5 | 4088.9 | 1500ms | 2/438 |
| ❌ | `nasa_apod` | 61.19% | 36.76% | 4417.4 | 10549.1 | 2000ms | 277/438 |
| ❌ | `ipapi_check` | 93.61% | 100.0% | 158.0 | 353.0 | 2500ms | 0/438 |
| ⚠️ | `open_meteo_weather` | 98.17% | 96.8% | 746.3 | 14877.1 | 2000ms | 14/438 |
| ✅ | `rest_countries` | 99.09% | 98.4% | 325.4 | 10221.5 | 2500ms | 7/438 |
| ⚠️ | `dog_ceo_random` | 99.32% | 90.41% | 853.1 | 10244.1 | 2500ms | 42/438 |
| ✅ | `catfact_random` | 99.32% | 99.32% | 271.1 | 10080.2 | 3000ms | 3/438 |
| ✅ | `useless_fact` | 99.54% | 99.09% | 585.3 | 10229.6 | 2500ms | 4/438 |
| ✅ | `agify_name` | 100.0% | 99.77% | 373.6 | 3237.1 | 2000ms | 1/438 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 230.7 | 2314.9 | 2000ms | 1/438 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.2 | 252.0 | 1500ms | 0/438 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 03:00 | 6314.9 | 91.67% |
| `nasa_apod` | 17:00 | 6132.0 | 73.08% |
| `nasa_apod` | 18:00 | 5700.0 | 84.21% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 4979.2 | 61.54% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `numbers_trivia` | 12:00 | 4944.8 | 47.37% |
| `nasa_apod` | 21:00 | 4923.2 | 56.0% |
| `nasa_apod` | 19:00 | 4739.6 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
