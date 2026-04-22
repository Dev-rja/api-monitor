# API Reliability Monitor — SLA Report

> Last updated: **2026-04-22 23:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.36% | 3985.3 | 10206.7 | 1000ms | 166/441 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 129.4 | 4088.9 | 1500ms | 2/441 |
| ❌ | `nasa_apod` | 61.22% | 36.96% | 4412.5 | 10549.1 | 2000ms | 278/441 |
| ❌ | `ipapi_check` | 93.65% | 100.0% | 158.1 | 353.0 | 2500ms | 0/441 |
| ⚠️ | `open_meteo_weather` | 98.19% | 96.83% | 745.1 | 14877.1 | 2000ms | 14/441 |
| ⚠️ | `rest_countries` | 98.87% | 98.19% | 347.4 | 10221.5 | 2500ms | 8/441 |
| ⚠️ | `dog_ceo_random` | 99.32% | 90.48% | 849.8 | 10244.1 | 2500ms | 42/441 |
| ✅ | `catfact_random` | 99.32% | 99.32% | 270.6 | 10080.2 | 3000ms | 3/441 |
| ✅ | `useless_fact` | 99.55% | 99.09% | 585.4 | 10229.6 | 2500ms | 4/441 |
| ✅ | `agify_name` | 100.0% | 99.77% | 374.1 | 3237.1 | 2000ms | 1/441 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 231.5 | 2314.9 | 2000ms | 1/441 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.2 | 252.0 | 1500ms | 0/441 |

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
