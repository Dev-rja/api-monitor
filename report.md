# API Reliability Monitor — SLA Report

> Last updated: **2026-08-26 06:22 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.54% | 3177.9 | 10420.1 | 1000ms | 728/2390 |
| ❌ | `public_apis_list` | 0.0% | 99.46% | 139.6 | 5075.4 | 1500ms | 13/2390 |
| ❌ | `ipapi_check` | 50.13% | 99.96% | 144.5 | 4507.0 | 2500ms | 1/2390 |
| ❌ | `nasa_apod` | 80.29% | 58.12% | 2742.4 | 11152.5 | 2000ms | 1001/2390 |
| ⚠️ | `dog_ceo_random` | 96.82% | 97.53% | 484.7 | 10244.1 | 2500ms | 59/2390 |
| ✅ | `open_meteo_weather` | 99.0% | 98.2% | 674.9 | 14877.1 | 2000ms | 43/2390 |
| ✅ | `rest_countries` | 99.37% | 99.12% | 266.5 | 10221.5 | 2500ms | 21/2390 |
| ✅ | `useless_fact` | 99.79% | 99.71% | 654.9 | 10229.6 | 2500ms | 7/2390 |
| ✅ | `catfact_random` | 99.79% | 99.46% | 261.6 | 10080.2 | 3000ms | 13/2390 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.92% | 96.4 | 4328.4 | 1500ms | 2/2390 |
| ✅ | `agify_name` | 99.92% | 99.5% | 402.8 | 16112.2 | 2000ms | 12/2390 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 184.8 | 3882.8 | 2000ms | 2/2390 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4740.2 | 47.06% |
| `numbers_trivia` | 10:00 | 3795.8 | 36.17% |
| `numbers_trivia` | 00:00 | 3645.0 | 34.92% |
| `numbers_trivia` | 14:00 | 3575.5 | 34.58% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 09:00 | 3491.9 | 33.66% |
| `numbers_trivia` | 17:00 | 3401.9 | 33.87% |
| `nasa_apod` | 03:00 | 3359.4 | 49.02% |
| `nasa_apod` | 05:00 | 3356.1 | 48.53% |
| `nasa_apod` | 09:00 | 3331.2 | 46.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
