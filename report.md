# API Reliability Monitor — SLA Report

> Last updated: **2026-08-26 14:05 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **7/12** &nbsp;|&nbsp; Avg uptime: **77.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.67% | 3165.3 | 10420.1 | 1000ms | 728/2400 |
| ❌ | `public_apis_list` | 0.0% | 99.46% | 139.5 | 5075.4 | 1500ms | 13/2400 |
| ❌ | `ipapi_check` | 49.96% | 99.96% | 144.5 | 4507.0 | 2500ms | 1/2400 |
| ❌ | `nasa_apod` | 80.38% | 58.21% | 2734.3 | 11152.5 | 2000ms | 1003/2400 |
| ⚠️ | `dog_ceo_random` | 96.83% | 97.54% | 484.2 | 10244.1 | 2500ms | 59/2400 |
| ✅ | `open_meteo_weather` | 99.0% | 98.21% | 674.4 | 14877.1 | 2000ms | 43/2400 |
| ✅ | `rest_countries` | 99.38% | 99.13% | 266.1 | 10221.5 | 2500ms | 21/2400 |
| ✅ | `useless_fact` | 99.79% | 99.71% | 655.3 | 10229.6 | 2500ms | 7/2400 |
| ✅ | `catfact_random` | 99.79% | 99.46% | 261.3 | 10080.2 | 3000ms | 13/2400 |
| ✅ | `coingecko_bitcoin` | 99.83% | 99.92% | 96.3 | 4328.4 | 1500ms | 2/2400 |
| ✅ | `agify_name` | 99.92% | 99.5% | 402.9 | 16112.2 | 2000ms | 12/2400 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.92% | 184.6 | 3882.8 | 2000ms | 2/2400 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 4740.2 | 47.06% |
| `numbers_trivia` | 10:00 | 3758.2 | 35.79% |
| `numbers_trivia` | 00:00 | 3645.0 | 34.92% |
| `numbers_trivia` | 14:00 | 3543.4 | 34.26% |
| `numbers_trivia` | 02:00 | 3519.9 | 33.33% |
| `numbers_trivia` | 09:00 | 3427.7 | 33.01% |
| `numbers_trivia` | 17:00 | 3401.9 | 33.87% |
| `nasa_apod` | 03:00 | 3359.4 | 49.02% |
| `nasa_apod` | 05:00 | 3356.1 | 48.53% |
| `numbers_trivia` | 05:00 | 3301.6 | 32.35% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
