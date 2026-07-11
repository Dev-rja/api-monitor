# API Reliability Monitor — SLA Report

> Last updated: **2026-07-11 15:16 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.57% | 2141.3 | 10206.7 | 1000ms | 267/1374 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 122.4 | 4595.4 | 1500ms | 4/1374 |
| ❌ | `nasa_apod` | 74.82% | 50.44% | 3301.7 | 11152.5 | 2000ms | 681/1374 |
| ❌ | `ipapi_check` | 75.55% | 99.93% | 154.5 | 4507.0 | 2500ms | 1/1374 |
| ❌ | `dog_ceo_random` | 94.91% | 96.8% | 527.4 | 10244.1 | 2500ms | 44/1374 |
| ⚠️ | `open_meteo_weather` | 98.62% | 97.02% | 728.6 | 14877.1 | 2000ms | 41/1374 |
| ⚠️ | `rest_countries` | 98.91% | 98.62% | 314.3 | 10221.5 | 2500ms | 19/1374 |
| ✅ | `useless_fact` | 99.64% | 99.71% | 634.1 | 10229.6 | 2500ms | 4/1374 |
| ✅ | `catfact_random` | 99.78% | 99.34% | 255.8 | 10080.2 | 3000ms | 9/1374 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 97.9 | 4328.4 | 1500ms | 1/1374 |
| ✅ | `agify_name` | 99.93% | 99.71% | 385.0 | 16112.2 | 2000ms | 4/1374 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 210.8 | 3882.8 | 2000ms | 2/1374 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4597.2 | 77.27% |
| `nasa_apod` | 09:00 | 4088.2 | 52.54% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `nasa_apod` | 17:00 | 4018.9 | 54.93% |
| `nasa_apod` | 01:00 | 3943.4 | 56.1% |
| `numbers_trivia` | 03:00 | 3835.9 | 36.36% |
| `nasa_apod` | 18:00 | 3749.8 | 52.78% |
| `nasa_apod` | 12:00 | 3657.9 | 54.1% |
| `nasa_apod` | 11:00 | 3530.4 | 52.63% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
