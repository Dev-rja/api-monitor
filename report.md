# API Reliability Monitor — SLA Report

> Last updated: **2026-06-01 13:06 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 72.61% | 2929.5 | 10206.7 | 1000ms | 266/971 |
| ❌ | `public_apis_list` | 0.0% | 99.59% | 126.3 | 4595.4 | 1500ms | 4/971 |
| ❌ | `ipapi_check` | 76.21% | 100.0% | 152.6 | 431.8 | 2500ms | 0/971 |
| ❌ | `nasa_apod` | 78.58% | 58.08% | 2832.4 | 10549.1 | 2000ms | 407/971 |
| ⚠️ | `rest_countries` | 98.46% | 98.15% | 362.1 | 10221.5 | 2500ms | 18/971 |
| ⚠️ | `open_meteo_weather` | 98.97% | 96.91% | 706.4 | 14877.1 | 2000ms | 30/971 |
| ✅ | `dog_ceo_random` | 99.49% | 95.67% | 587.3 | 10244.1 | 2500ms | 42/971 |
| ✅ | `catfact_random` | 99.69% | 99.18% | 267.4 | 10080.2 | 3000ms | 8/971 |
| ✅ | `coingecko_bitcoin` | 99.69% | 100.0% | 97.1 | 253.3 | 1500ms | 0/971 |
| ✅ | `useless_fact` | 99.79% | 99.59% | 620.3 | 10229.6 | 2500ms | 4/971 |
| ✅ | `agify_name` | 99.9% | 99.69% | 382.5 | 16112.2 | 2000ms | 3/971 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.79% | 224.3 | 3882.8 | 2000ms | 2/971 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 02:00 | 4028.8 | 50.0% |
| `nasa_apod` | 17:00 | 3845.3 | 50.0% |
| `nasa_apod` | 11:00 | 3729.1 | 47.27% |
| `numbers_trivia` | 05:00 | 3674.1 | 34.62% |
| `numbers_trivia` | 07:00 | 3552.2 | 33.33% |
| `nasa_apod` | 09:00 | 3526.1 | 47.73% |
| `nasa_apod` | 05:00 | 3511.6 | 61.54% |
| `numbers_trivia` | 10:00 | 3454.8 | 32.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
