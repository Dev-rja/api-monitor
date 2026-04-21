# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 23:48 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 64.86% | 3740.6 | 10206.7 | 1000ms | 149/424 |
| ❌ | `public_apis_list` | 0.0% | 99.53% | 129.5 | 4088.9 | 1500ms | 2/424 |
| ❌ | `nasa_apod` | 61.32% | 37.26% | 4383.9 | 10549.1 | 2000ms | 266/424 |
| ❌ | `ipapi_check` | 93.63% | 100.0% | 158.6 | 353.0 | 2500ms | 0/424 |
| ⚠️ | `open_meteo_weather` | 98.11% | 96.7% | 752.9 | 14877.1 | 2000ms | 14/424 |
| ⚠️ | `dog_ceo_random` | 99.29% | 90.09% | 867.6 | 10244.1 | 2500ms | 42/424 |
| ✅ | `catfact_random` | 99.29% | 99.29% | 274.8 | 10080.2 | 3000ms | 3/424 |
| ✅ | `useless_fact` | 99.53% | 99.06% | 585.4 | 10229.6 | 2500ms | 4/424 |
| ✅ | `agify_name` | 100.0% | 99.76% | 372.8 | 3237.1 | 2000ms | 1/424 |
| ✅ | `rest_countries` | 100.0% | 99.06% | 258.4 | 7269.1 | 2500ms | 4/424 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 231.8 | 2314.9 | 2000ms | 1/424 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.6 | 252.0 | 1500ms | 0/424 |

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
| `nasa_apod` | 21:00 | 4705.1 | 54.17% |
| `numbers_trivia` | 10:00 | 4692.0 | 45.0% |
| `numbers_trivia` | 12:00 | 4658.8 | 44.44% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
