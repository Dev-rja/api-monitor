# API Reliability Monitor — SLA Report

> Last updated: **2026-06-02 02:03 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.72% | 2918.1 | 10206.7 | 1000ms | 266/975 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 125.9 | 4595.4 | 1500ms | 4/975 |
| ❌ | `ipapi_check` | 76.1% | 100.0% | 152.6 | 431.8 | 2500ms | 0/975 |
| ❌ | `nasa_apod` | 78.46% | 57.95% | 2844.9 | 10549.1 | 2000ms | 410/975 |
| ⚠️ | `rest_countries` | 98.46% | 98.15% | 361.3 | 10221.5 | 2500ms | 18/975 |
| ⚠️ | `open_meteo_weather` | 98.97% | 96.92% | 705.6 | 14877.1 | 2000ms | 30/975 |
| ✅ | `dog_ceo_random` | 99.49% | 95.69% | 586.5 | 10244.1 | 2500ms | 42/975 |
| ✅ | `catfact_random` | 99.69% | 99.18% | 267.2 | 10080.2 | 3000ms | 8/975 |
| ✅ | `coingecko_bitcoin` | 99.69% | 100.0% | 97.0 | 253.3 | 1500ms | 0/975 |
| ✅ | `useless_fact` | 99.79% | 99.59% | 620.0 | 10229.6 | 2500ms | 4/975 |
| ✅ | `agify_name` | 99.9% | 99.69% | 382.4 | 16112.2 | 2000ms | 3/975 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 224.1 | 3882.8 | 2000ms | 2/975 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 3845.3 | 50.0% |
| `nasa_apod` | 02:00 | 3796.6 | 57.14% |
| `nasa_apod` | 11:00 | 3729.1 | 47.27% |
| `numbers_trivia` | 05:00 | 3674.1 | 34.62% |
| `numbers_trivia` | 07:00 | 3552.2 | 33.33% |
| `nasa_apod` | 09:00 | 3526.1 | 47.73% |
| `nasa_apod` | 05:00 | 3511.6 | 61.54% |
| `numbers_trivia` | 10:00 | 3454.8 | 32.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
