# API Reliability Monitor — SLA Report

> Last updated: **2026-04-22 23:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.5% | 3971.5 | 10206.7 | 1000ms | 165/440 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 129.2 | 4088.9 | 1500ms | 2/440 |
| ❌ | `nasa_apod` | 61.14% | 36.82% | 4421.5 | 10549.1 | 2000ms | 278/440 |
| ❌ | `ipapi_check` | 93.64% | 100.0% | 158.1 | 353.0 | 2500ms | 0/440 |
| ⚠️ | `open_meteo_weather` | 98.18% | 96.82% | 745.8 | 14877.1 | 2000ms | 14/440 |
| ⚠️ | `rest_countries` | 98.86% | 98.18% | 347.7 | 10221.5 | 2500ms | 8/440 |
| ⚠️ | `dog_ceo_random` | 99.32% | 90.45% | 851.1 | 10244.1 | 2500ms | 42/440 |
| ✅ | `catfact_random` | 99.32% | 99.32% | 271.0 | 10080.2 | 3000ms | 3/440 |
| ✅ | `useless_fact` | 99.55% | 99.09% | 585.5 | 10229.6 | 2500ms | 4/440 |
| ✅ | `agify_name` | 100.0% | 99.77% | 374.3 | 3237.1 | 2000ms | 1/440 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 231.7 | 2314.9 | 2000ms | 1/440 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.3 | 252.0 | 1500ms | 0/440 |

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
