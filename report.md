# API Reliability Monitor — SLA Report

> Last updated: **2026-07-11 00:08 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.44% | 2153.5 | 10206.7 | 1000ms | 267/1365 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 122.4 | 4595.4 | 1500ms | 4/1365 |
| ❌ | `nasa_apod` | 74.73% | 50.48% | 3307.4 | 11152.5 | 2000ms | 676/1365 |
| ❌ | `ipapi_check` | 75.68% | 99.93% | 154.5 | 4507.0 | 2500ms | 1/1365 |
| ❌ | `dog_ceo_random` | 94.87% | 96.85% | 526.9 | 10244.1 | 2500ms | 43/1365 |
| ⚠️ | `open_meteo_weather` | 98.61% | 97.0% | 729.3 | 14877.1 | 2000ms | 41/1365 |
| ⚠️ | `rest_countries` | 98.9% | 98.61% | 315.1 | 10221.5 | 2500ms | 19/1365 |
| ✅ | `useless_fact` | 99.63% | 99.71% | 633.4 | 10229.6 | 2500ms | 4/1365 |
| ✅ | `catfact_random` | 99.78% | 99.34% | 255.6 | 10080.2 | 3000ms | 9/1365 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 97.9 | 4328.4 | 1500ms | 1/1365 |
| ✅ | `agify_name` | 99.93% | 99.71% | 384.5 | 16112.2 | 2000ms | 4/1365 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 211.1 | 3882.8 | 2000ms | 2/1365 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4792.7 | 80.95% |
| `nasa_apod` | 09:00 | 4153.2 | 53.45% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `nasa_apod` | 17:00 | 4018.9 | 54.93% |
| `numbers_trivia` | 03:00 | 4003.6 | 38.1% |
| `nasa_apod` | 01:00 | 3943.4 | 56.1% |
| `nasa_apod` | 18:00 | 3749.8 | 52.78% |
| `nasa_apod` | 11:00 | 3574.2 | 53.33% |
| `nasa_apod` | 12:00 | 3546.1 | 53.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
