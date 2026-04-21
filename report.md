# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 19:40 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.63% | 3664.8 | 10206.7 | 1000ms | 144/419 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 129.9 | 4088.9 | 1500ms | 2/419 |
| ❌ | `nasa_apod` | 61.34% | 37.47% | 4380.1 | 10549.1 | 2000ms | 262/419 |
| ❌ | `ipapi_check` | 93.56% | 100.0% | 159.1 | 353.0 | 2500ms | 0/419 |
| ⚠️ | `open_meteo_weather` | 98.09% | 96.9% | 745.8 | 14877.1 | 2000ms | 13/419 |
| ⚠️ | `dog_ceo_random` | 99.28% | 89.98% | 872.4 | 10244.1 | 2500ms | 42/419 |
| ✅ | `catfact_random` | 99.28% | 99.28% | 276.6 | 10080.2 | 3000ms | 3/419 |
| ✅ | `useless_fact` | 99.52% | 99.05% | 585.5 | 10229.6 | 2500ms | 4/419 |
| ✅ | `agify_name` | 100.0% | 99.76% | 372.6 | 3237.1 | 2000ms | 1/419 |
| ✅ | `rest_countries` | 100.0% | 99.05% | 259.0 | 7269.1 | 2500ms | 4/419 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 232.8 | 2314.9 | 2000ms | 1/419 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.1 | 252.0 | 1500ms | 0/419 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 03:00 | 6314.9 | 91.67% |
| `nasa_apod` | 17:00 | 5959.2 | 72.0% |
| `nasa_apod` | 18:00 | 5870.5 | 83.33% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 5164.2 | 64.0% |
| `nasa_apod` | 19:00 | 4739.6 | 62.5% |
| `numbers_trivia` | 10:00 | 4692.0 | 45.0% |
| `numbers_trivia` | 12:00 | 4658.8 | 44.44% |
| `nasa_apod` | 12:00 | 4598.1 | 66.67% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
