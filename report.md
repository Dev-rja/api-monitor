# API Reliability Monitor — SLA Report

> Last updated: **2026-06-23 20:38 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 77.26% | 2467.7 | 10206.7 | 1000ms | 266/1170 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 124.9 | 4595.4 | 1500ms | 4/1170 |
| ❌ | `nasa_apod` | 74.44% | 51.2% | 3307.0 | 11152.5 | 2000ms | 571/1170 |
| ❌ | `ipapi_check` | 76.41% | 99.91% | 155.7 | 4507.0 | 2500ms | 1/1170 |
| ⚠️ | `rest_countries` | 98.72% | 98.38% | 336.9 | 10221.5 | 2500ms | 19/1170 |
| ⚠️ | `open_meteo_weather` | 98.97% | 96.92% | 712.6 | 14877.1 | 2000ms | 36/1170 |
| ✅ | `useless_fact` | 99.57% | 99.66% | 631.1 | 10229.6 | 2500ms | 4/1170 |
| ✅ | `dog_ceo_random` | 99.57% | 96.41% | 549.3 | 10244.1 | 2500ms | 42/1170 |
| ✅ | `catfact_random` | 99.74% | 99.23% | 261.9 | 10080.2 | 3000ms | 9/1170 |
| ✅ | `coingecko_bitcoin` | 99.74% | 100.0% | 96.0 | 253.3 | 1500ms | 0/1170 |
| ✅ | `agify_name` | 99.91% | 99.74% | 376.4 | 16112.2 | 2000ms | 3/1170 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.83% | 217.7 | 3882.8 | 2000ms | 2/1170 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4788.8 | 68.75% |
| `nasa_apod` | 17:00 | 4293.2 | 56.25% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 01:00 | 4165.7 | 58.62% |
| `nasa_apod` | 09:00 | 4114.4 | 54.0% |
| `nasa_apod` | 11:00 | 3791.8 | 53.13% |
| `nasa_apod` | 18:00 | 3605.5 | 52.54% |
| `nasa_apod` | 20:00 | 3451.4 | 48.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
