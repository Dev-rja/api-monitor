# API Reliability Monitor — SLA Report

> Last updated: **2026-04-22 20:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 62.93% | 3929.3 | 10206.7 | 1000ms | 162/437 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 129.8 | 4088.9 | 1500ms | 2/437 |
| ❌ | `nasa_apod` | 61.33% | 36.84% | 4404.3 | 10549.1 | 2000ms | 276/437 |
| ❌ | `ipapi_check` | 93.59% | 100.0% | 158.2 | 353.0 | 2500ms | 0/437 |
| ⚠️ | `open_meteo_weather` | 98.17% | 96.8% | 746.5 | 14877.1 | 2000ms | 14/437 |
| ⚠️ | `dog_ceo_random` | 99.31% | 90.39% | 853.8 | 10244.1 | 2500ms | 42/437 |
| ✅ | `rest_countries` | 99.31% | 98.63% | 302.8 | 10221.5 | 2500ms | 6/437 |
| ✅ | `catfact_random` | 99.31% | 99.31% | 271.4 | 10080.2 | 3000ms | 3/437 |
| ✅ | `useless_fact` | 99.54% | 99.08% | 584.7 | 10229.6 | 2500ms | 4/437 |
| ✅ | `agify_name` | 100.0% | 99.77% | 373.3 | 3237.1 | 2000ms | 1/437 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.77% | 230.8 | 2314.9 | 2000ms | 1/437 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.2 | 252.0 | 1500ms | 0/437 |

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
| `nasa_apod` | 19:00 | 4739.6 | 62.5% |
| `nasa_apod` | 21:00 | 4705.1 | 54.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
