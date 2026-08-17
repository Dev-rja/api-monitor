# API Reliability Monitor — SLA Report

> Last updated: **2026-08-17 03:26 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 65.57% | 3577.0 | 10420.1 | 1000ms | 701/2036 |
| ❌ | `public_apis_list` | 0.0% | 99.56% | 136.4 | 5075.4 | 1500ms | 9/2036 |
| ❌ | `ipapi_check` | 58.1% | 99.95% | 145.6 | 4507.0 | 2500ms | 1/2036 |
| ❌ | `nasa_apod` | 78.19% | 54.32% | 2979.8 | 11152.5 | 2000ms | 930/2036 |
| ⚠️ | `dog_ceo_random` | 96.27% | 97.15% | 507.8 | 10244.1 | 2500ms | 58/2036 |
| ⚠️ | `open_meteo_weather` | 98.92% | 97.89% | 691.6 | 14877.1 | 2000ms | 43/2036 |
| ✅ | `rest_countries` | 99.26% | 98.97% | 279.2 | 10221.5 | 2500ms | 21/2036 |
| ✅ | `useless_fact` | 99.75% | 99.66% | 650.7 | 10229.6 | 2500ms | 7/2036 |
| ✅ | `catfact_random` | 99.75% | 99.41% | 263.5 | 10080.2 | 3000ms | 12/2036 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.9% | 96.8 | 4328.4 | 1500ms | 2/2036 |
| ✅ | `agify_name` | 99.9% | 99.75% | 392.0 | 16112.2 | 2000ms | 5/2036 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 191.2 | 3882.8 | 2000ms | 2/2036 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5376.8 | 53.66% |
| `numbers_trivia` | 02:00 | 4898.3 | 46.67% |
| `numbers_trivia` | 10:00 | 4472.8 | 42.86% |
| `nasa_apod` | 05:00 | 4196.2 | 58.82% |
| `numbers_trivia` | 14:00 | 4176.1 | 40.66% |
| `numbers_trivia` | 05:00 | 4102.4 | 39.22% |
| `numbers_trivia` | 09:00 | 3846.3 | 37.21% |
| `numbers_trivia` | 17:00 | 3801.2 | 38.1% |
| `numbers_trivia` | 00:00 | 3774.1 | 36.21% |
| `nasa_apod` | 03:00 | 3758.3 | 56.1% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
