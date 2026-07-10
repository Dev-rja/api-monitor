# API Reliability Monitor — SLA Report

> Last updated: **2026-07-10 11:34 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.32% | 2165.0 | 10206.7 | 1000ms | 267/1357 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 122.5 | 4595.4 | 1500ms | 4/1357 |
| ❌ | `nasa_apod` | 74.72% | 50.26% | 3317.0 | 11152.5 | 2000ms | 675/1357 |
| ❌ | `ipapi_check` | 75.9% | 99.93% | 154.6 | 4507.0 | 2500ms | 1/1357 |
| ❌ | `dog_ceo_random` | 94.84% | 96.9% | 526.5 | 10244.1 | 2500ms | 42/1357 |
| ⚠️ | `open_meteo_weather` | 98.6% | 96.98% | 730.4 | 14877.1 | 2000ms | 41/1357 |
| ⚠️ | `rest_countries` | 98.89% | 98.6% | 316.0 | 10221.5 | 2500ms | 19/1357 |
| ✅ | `useless_fact` | 99.63% | 99.71% | 633.3 | 10229.6 | 2500ms | 4/1357 |
| ✅ | `catfact_random` | 99.78% | 99.34% | 255.5 | 10080.2 | 3000ms | 9/1357 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 97.9 | 4328.4 | 1500ms | 1/1357 |
| ✅ | `agify_name` | 99.93% | 99.71% | 384.4 | 16112.2 | 2000ms | 4/1357 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 211.4 | 3882.8 | 2000ms | 2/1357 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4792.7 | 80.95% |
| `nasa_apod` | 09:00 | 4153.2 | 53.45% |
| `nasa_apod` | 17:00 | 4069.4 | 55.71% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `numbers_trivia` | 03:00 | 4003.6 | 38.1% |
| `nasa_apod` | 01:00 | 3943.4 | 56.1% |
| `nasa_apod` | 18:00 | 3749.8 | 52.78% |
| `nasa_apod` | 11:00 | 3574.2 | 53.33% |
| `nasa_apod` | 20:00 | 3560.1 | 51.16% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
