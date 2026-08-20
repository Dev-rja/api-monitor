# API Reliability Monitor — SLA Report

> Last updated: **2026-08-20 14:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.45% | 3484.3 | 10420.1 | 1000ms | 728/2170 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 137.1 | 5075.4 | 1500ms | 10/2170 |
| ❌ | `ipapi_check` | 54.79% | 99.95% | 145.1 | 4507.0 | 2500ms | 1/2170 |
| ❌ | `nasa_apod` | 79.08% | 55.85% | 2888.2 | 11152.5 | 2000ms | 958/2170 |
| ⚠️ | `dog_ceo_random` | 96.5% | 97.33% | 495.8 | 10244.1 | 2500ms | 58/2170 |
| ⚠️ | `open_meteo_weather` | 98.99% | 98.02% | 684.4 | 14877.1 | 2000ms | 43/2170 |
| ✅ | `rest_countries` | 99.31% | 99.03% | 273.7 | 10221.5 | 2500ms | 21/2170 |
| ✅ | `useless_fact` | 99.77% | 99.68% | 652.3 | 10229.6 | 2500ms | 7/2170 |
| ✅ | `catfact_random` | 99.77% | 99.4% | 263.7 | 10080.2 | 3000ms | 13/2170 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.91% | 96.4 | 4328.4 | 1500ms | 2/2170 |
| ✅ | `agify_name` | 99.91% | 99.72% | 394.8 | 16112.2 | 2000ms | 6/2170 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.91% | 188.3 | 3882.8 | 2000ms | 2/2170 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5237.4 | 52.17% |
| `numbers_trivia` | 02:00 | 4653.3 | 44.44% |
| `numbers_trivia` | 10:00 | 4275.8 | 40.96% |
| `numbers_trivia` | 14:00 | 3926.9 | 38.14% |
| `numbers_trivia` | 00:00 | 3818.8 | 36.67% |
| `numbers_trivia` | 05:00 | 3783.9 | 37.29% |
| `numbers_trivia` | 17:00 | 3781.4 | 37.84% |
| `numbers_trivia` | 09:00 | 3780.7 | 36.56% |
| `nasa_apod` | 05:00 | 3759.6 | 54.24% |
| `nasa_apod` | 09:00 | 3582.8 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
