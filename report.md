# API Reliability Monitor — SLA Report

> Last updated: **2026-07-11 16:13 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.58% | 2139.9 | 10206.7 | 1000ms | 267/1375 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 122.5 | 4595.4 | 1500ms | 4/1375 |
| ❌ | `nasa_apod` | 74.84% | 50.47% | 3299.5 | 11152.5 | 2000ms | 681/1375 |
| ❌ | `ipapi_check` | 75.49% | 99.93% | 154.4 | 4507.0 | 2500ms | 1/1375 |
| ❌ | `dog_ceo_random` | 94.91% | 96.8% | 528.0 | 10244.1 | 2500ms | 44/1375 |
| ⚠️ | `open_meteo_weather` | 98.62% | 97.02% | 728.5 | 14877.1 | 2000ms | 41/1375 |
| ⚠️ | `rest_countries` | 98.91% | 98.62% | 314.1 | 10221.5 | 2500ms | 19/1375 |
| ✅ | `useless_fact` | 99.64% | 99.71% | 634.1 | 10229.6 | 2500ms | 4/1375 |
| ✅ | `catfact_random` | 99.78% | 99.35% | 255.7 | 10080.2 | 3000ms | 9/1375 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 97.9 | 4328.4 | 1500ms | 1/1375 |
| ✅ | `agify_name` | 99.93% | 99.71% | 385.1 | 16112.2 | 2000ms | 4/1375 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 210.7 | 3882.8 | 2000ms | 2/1375 |

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
