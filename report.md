# API Reliability Monitor — SLA Report

> Last updated: **2026-06-14 14:36 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.6% | 2632.6 | 10206.7 | 1000ms | 266/1090 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 125.7 | 4595.4 | 1500ms | 4/1090 |
| ❌ | `nasa_apod` | 75.69% | 53.76% | 3155.1 | 10565.8 | 2000ms | 504/1090 |
| ❌ | `ipapi_check` | 76.33% | 99.91% | 156.4 | 4507.0 | 2500ms | 1/1090 |
| ⚠️ | `rest_countries` | 98.62% | 98.35% | 342.9 | 10221.5 | 2500ms | 18/1090 |
| ⚠️ | `open_meteo_weather` | 98.9% | 96.7% | 720.2 | 14877.1 | 2000ms | 36/1090 |
| ✅ | `dog_ceo_random` | 99.54% | 96.15% | 564.2 | 10244.1 | 2500ms | 42/1090 |
| ✅ | `catfact_random` | 99.72% | 99.17% | 264.4 | 10080.2 | 3000ms | 9/1090 |
| ✅ | `coingecko_bitcoin` | 99.72% | 100.0% | 96.4 | 253.3 | 1500ms | 0/1090 |
| ✅ | `useless_fact` | 99.82% | 99.63% | 626.7 | 10229.6 | 2500ms | 4/1090 |
| ✅ | `agify_name` | 99.91% | 99.72% | 378.4 | 16112.2 | 2000ms | 3/1090 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.82% | 219.6 | 3882.8 | 2000ms | 2/1090 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 05:00 | 4214.9 | 65.52% |
| `nasa_apod` | 09:00 | 4014.2 | 52.08% |
| `nasa_apod` | 17:00 | 4014.1 | 53.33% |
| `nasa_apod` | 11:00 | 3861.7 | 50.0% |
| `nasa_apod` | 01:00 | 3797.2 | 52.0% |
| `nasa_apod` | 18:00 | 3491.9 | 51.85% |
| `nasa_apod` | 14:00 | 3469.5 | 47.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
