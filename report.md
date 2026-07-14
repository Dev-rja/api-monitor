# API Reliability Monitor — SLA Report

> Last updated: **2026-07-14 17:47 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 81.21% | 2078.4 | 10206.7 | 1000ms | 267/1421 |
| ❌ | `public_apis_list` | 0.0% | 99.72% | 122.4 | 4595.4 | 1500ms | 4/1421 |
| ❌ | `ipapi_check` | 74.31% | 99.93% | 153.6 | 4507.0 | 2500ms | 1/1421 |
| ❌ | `nasa_apod` | 75.51% | 51.3% | 3234.7 | 11152.5 | 2000ms | 692/1421 |
| ❌ | `dog_ceo_random` | 94.86% | 96.55% | 545.5 | 10244.1 | 2500ms | 49/1421 |
| ⚠️ | `open_meteo_weather` | 98.66% | 97.11% | 722.8 | 14877.1 | 2000ms | 41/1421 |
| ⚠️ | `rest_countries` | 98.94% | 98.66% | 309.8 | 10221.5 | 2500ms | 19/1421 |
| ✅ | `useless_fact` | 99.65% | 99.72% | 634.2 | 10229.6 | 2500ms | 4/1421 |
| ✅ | `catfact_random` | 99.79% | 99.37% | 256.2 | 10080.2 | 3000ms | 9/1421 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.93% | 97.6 | 4328.4 | 1500ms | 1/1421 |
| ✅ | `agify_name` | 99.93% | 99.72% | 385.4 | 16112.2 | 2000ms | 4/1421 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 208.5 | 3882.8 | 2000ms | 2/1421 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4597.2 | 77.27% |
| `nasa_apod` | 09:00 | 4062.5 | 53.33% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `nasa_apod` | 17:00 | 4003.6 | 54.05% |
| `numbers_trivia` | 03:00 | 3835.9 | 36.36% |
| `nasa_apod` | 01:00 | 3752.8 | 54.55% |
| `nasa_apod` | 18:00 | 3619.6 | 50.67% |
| `nasa_apod` | 12:00 | 3605.8 | 53.23% |
| `nasa_apod` | 11:00 | 3539.3 | 51.9% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
