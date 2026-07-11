# API Reliability Monitor — SLA Report

> Last updated: **2026-07-11 19:33 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.62% | 2135.7 | 10206.7 | 1000ms | 267/1378 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 122.5 | 4595.4 | 1500ms | 4/1378 |
| ❌ | `nasa_apod` | 74.82% | 50.44% | 3302.1 | 11152.5 | 2000ms | 683/1378 |
| ❌ | `ipapi_check` | 75.33% | 99.93% | 154.4 | 4507.0 | 2500ms | 1/1378 |
| ❌ | `dog_ceo_random` | 94.92% | 96.81% | 527.2 | 10244.1 | 2500ms | 44/1378 |
| ⚠️ | `open_meteo_weather` | 98.62% | 97.02% | 728.0 | 14877.1 | 2000ms | 41/1378 |
| ⚠️ | `rest_countries` | 98.91% | 98.62% | 313.8 | 10221.5 | 2500ms | 19/1378 |
| ✅ | `useless_fact` | 99.64% | 99.71% | 634.4 | 10229.6 | 2500ms | 4/1378 |
| ✅ | `catfact_random` | 99.78% | 99.35% | 255.8 | 10080.2 | 3000ms | 9/1378 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 97.9 | 4328.4 | 1500ms | 1/1378 |
| ✅ | `agify_name` | 99.93% | 99.71% | 385.1 | 16112.2 | 2000ms | 4/1378 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 210.5 | 3882.8 | 2000ms | 2/1378 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4597.2 | 77.27% |
| `nasa_apod` | 17:00 | 4104.7 | 55.56% |
| `nasa_apod` | 09:00 | 4088.2 | 52.54% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `nasa_apod` | 01:00 | 3943.4 | 56.1% |
| `numbers_trivia` | 03:00 | 3835.9 | 36.36% |
| `nasa_apod` | 18:00 | 3707.6 | 52.05% |
| `nasa_apod` | 12:00 | 3657.9 | 54.1% |
| `nasa_apod` | 11:00 | 3530.4 | 52.63% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
