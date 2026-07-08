# API Reliability Monitor — SLA Report

> Last updated: **2026-07-08 22:28 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.1% | 2186.3 | 10206.7 | 1000ms | 267/1342 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 122.5 | 4595.4 | 1500ms | 4/1342 |
| ❌ | `nasa_apod` | 74.59% | 50.07% | 3335.6 | 11152.5 | 2000ms | 670/1342 |
| ❌ | `ipapi_check` | 76.23% | 99.93% | 154.8 | 4507.0 | 2500ms | 1/1342 |
| ❌ | `dog_ceo_random` | 94.78% | 96.87% | 528.1 | 10244.1 | 2500ms | 42/1342 |
| ⚠️ | `open_meteo_weather` | 98.58% | 96.94% | 731.9 | 14877.1 | 2000ms | 41/1342 |
| ⚠️ | `rest_countries` | 98.88% | 98.58% | 317.3 | 10221.5 | 2500ms | 19/1342 |
| ✅ | `useless_fact` | 99.63% | 99.7% | 633.1 | 10229.6 | 2500ms | 4/1342 |
| ✅ | `catfact_random` | 99.78% | 99.33% | 255.6 | 10080.2 | 3000ms | 9/1342 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 98.0 | 4328.4 | 1500ms | 1/1342 |
| ✅ | `agify_name` | 99.93% | 99.7% | 383.8 | 16112.2 | 2000ms | 4/1342 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 212.1 | 3882.8 | 2000ms | 2/1342 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4792.7 | 80.95% |
| `nasa_apod` | 05:00 | 4266.1 | 62.16% |
| `nasa_apod` | 09:00 | 4153.2 | 53.45% |
| `nasa_apod` | 01:00 | 4125.5 | 58.97% |
| `nasa_apod` | 17:00 | 4069.4 | 55.71% |
| `numbers_trivia` | 03:00 | 4003.6 | 38.1% |
| `nasa_apod` | 18:00 | 3795.9 | 53.52% |
| `nasa_apod` | 11:00 | 3627.0 | 53.42% |
| `nasa_apod` | 20:00 | 3574.9 | 50.59% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
