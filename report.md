# API Reliability Monitor — SLA Report

> Last updated: **2026-07-10 23:08 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.43% | 2154.8 | 10206.7 | 1000ms | 267/1364 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 122.3 | 4595.4 | 1500ms | 4/1364 |
| ❌ | `nasa_apod` | 74.71% | 50.44% | 3309.5 | 11152.5 | 2000ms | 676/1364 |
| ❌ | `ipapi_check` | 75.73% | 99.93% | 154.5 | 4507.0 | 2500ms | 1/1364 |
| ❌ | `dog_ceo_random` | 94.87% | 96.85% | 527.1 | 10244.1 | 2500ms | 43/1364 |
| ⚠️ | `open_meteo_weather` | 98.61% | 96.99% | 729.3 | 14877.1 | 2000ms | 41/1364 |
| ⚠️ | `rest_countries` | 98.9% | 98.61% | 315.2 | 10221.5 | 2500ms | 19/1364 |
| ✅ | `useless_fact` | 99.63% | 99.71% | 633.1 | 10229.6 | 2500ms | 4/1364 |
| ✅ | `catfact_random` | 99.78% | 99.34% | 255.3 | 10080.2 | 3000ms | 9/1364 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 97.8 | 4328.4 | 1500ms | 1/1364 |
| ✅ | `agify_name` | 99.93% | 99.71% | 384.3 | 16112.2 | 2000ms | 4/1364 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 211.2 | 3882.8 | 2000ms | 2/1364 |

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
