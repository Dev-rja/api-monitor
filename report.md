# API Reliability Monitor — SLA Report

> Last updated: **2026-07-11 06:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.47% | 2150.8 | 10206.7 | 1000ms | 267/1367 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 122.4 | 4595.4 | 1500ms | 4/1367 |
| ❌ | `nasa_apod` | 74.76% | 50.48% | 3304.7 | 11152.5 | 2000ms | 677/1367 |
| ❌ | `ipapi_check` | 75.64% | 99.93% | 154.5 | 4507.0 | 2500ms | 1/1367 |
| ❌ | `dog_ceo_random` | 94.88% | 96.85% | 526.6 | 10244.1 | 2500ms | 43/1367 |
| ⚠️ | `open_meteo_weather` | 98.61% | 97.0% | 729.2 | 14877.1 | 2000ms | 41/1367 |
| ⚠️ | `rest_countries` | 98.9% | 98.61% | 315.0 | 10221.5 | 2500ms | 19/1367 |
| ✅ | `useless_fact` | 99.63% | 99.71% | 633.6 | 10229.6 | 2500ms | 4/1367 |
| ✅ | `catfact_random` | 99.78% | 99.34% | 255.6 | 10080.2 | 3000ms | 9/1367 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 98.0 | 4328.4 | 1500ms | 1/1367 |
| ✅ | `agify_name` | 99.93% | 99.71% | 384.5 | 16112.2 | 2000ms | 4/1367 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 211.2 | 3882.8 | 2000ms | 2/1367 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4597.2 | 77.27% |
| `nasa_apod` | 09:00 | 4153.2 | 53.45% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `nasa_apod` | 17:00 | 4018.9 | 54.93% |
| `nasa_apod` | 01:00 | 3943.4 | 56.1% |
| `numbers_trivia` | 03:00 | 3835.9 | 36.36% |
| `nasa_apod` | 18:00 | 3749.8 | 52.78% |
| `nasa_apod` | 11:00 | 3574.2 | 53.33% |
| `nasa_apod` | 12:00 | 3546.1 | 53.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
