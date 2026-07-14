# API Reliability Monitor — SLA Report

> Last updated: **2026-07-14 15:10 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.18% | 2081.0 | 10206.7 | 1000ms | 267/1419 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 122.3 | 4595.4 | 1500ms | 4/1419 |
| ❌ | `ipapi_check` | 74.42% | 99.93% | 153.7 | 4507.0 | 2500ms | 1/1419 |
| ❌ | `nasa_apod` | 75.48% | 51.23% | 3238.7 | 11152.5 | 2000ms | 692/1419 |
| ❌ | `dog_ceo_random` | 94.86% | 96.62% | 543.6 | 10244.1 | 2500ms | 48/1419 |
| ⚠️ | `open_meteo_weather` | 98.66% | 97.11% | 723.1 | 14877.1 | 2000ms | 41/1419 |
| ⚠️ | `rest_countries` | 98.94% | 98.66% | 310.0 | 10221.5 | 2500ms | 19/1419 |
| ✅ | `useless_fact` | 99.65% | 99.72% | 634.2 | 10229.6 | 2500ms | 4/1419 |
| ✅ | `catfact_random` | 99.79% | 99.37% | 256.2 | 10080.2 | 3000ms | 9/1419 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.93% | 97.5 | 4328.4 | 1500ms | 1/1419 |
| ✅ | `agify_name` | 99.93% | 99.72% | 385.4 | 16112.2 | 2000ms | 4/1419 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 208.5 | 3882.8 | 2000ms | 2/1419 |

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
| `nasa_apod` | 11:00 | 3539.3 | 51.9% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
