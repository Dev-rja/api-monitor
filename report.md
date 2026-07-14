# API Reliability Monitor — SLA Report

> Last updated: **2026-07-14 01:01 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.09% | 2090.2 | 10206.7 | 1000ms | 267/1412 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 122.2 | 4595.4 | 1500ms | 4/1412 |
| ❌ | `ipapi_check` | 74.58% | 99.93% | 153.9 | 4507.0 | 2500ms | 1/1412 |
| ❌ | `nasa_apod` | 75.42% | 51.27% | 3241.2 | 11152.5 | 2000ms | 688/1412 |
| ❌ | `dog_ceo_random` | 94.83% | 96.6% | 545.3 | 10244.1 | 2500ms | 48/1412 |
| ⚠️ | `open_meteo_weather` | 98.65% | 97.1% | 724.0 | 14877.1 | 2000ms | 41/1412 |
| ⚠️ | `rest_countries` | 98.94% | 98.65% | 310.9 | 10221.5 | 2500ms | 19/1412 |
| ✅ | `useless_fact` | 99.65% | 99.72% | 634.4 | 10229.6 | 2500ms | 4/1412 |
| ✅ | `catfact_random` | 99.79% | 99.36% | 256.2 | 10080.2 | 3000ms | 9/1412 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.93% | 97.6 | 4328.4 | 1500ms | 1/1412 |
| ✅ | `agify_name` | 99.93% | 99.72% | 385.5 | 16112.2 | 2000ms | 4/1412 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 209.0 | 3882.8 | 2000ms | 2/1412 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4597.2 | 77.27% |
| `nasa_apod` | 09:00 | 4062.5 | 53.33% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `nasa_apod` | 17:00 | 4055.0 | 54.79% |
| `numbers_trivia` | 03:00 | 3835.9 | 36.36% |
| `nasa_apod` | 01:00 | 3752.8 | 54.55% |
| `nasa_apod` | 18:00 | 3619.6 | 50.67% |
| `nasa_apod` | 12:00 | 3605.8 | 53.23% |
| `nasa_apod` | 11:00 | 3453.8 | 51.28% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
